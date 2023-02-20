from pydicom.dataset import Dataset
from pynetdicom import AE
from .class_description import Singleton
from lib import Log

class LocalAE(metaclass=Singleton):
    def __init__(self):
        self.ae = AE(ae_title = 'LocalSCU')
        self.code = '1.2.840.10008.5.1.4.1.2.1.2'
        self.ae.add_requested_context(self.code)
        self.assoc = self.ae.associate("orthanchost", 4242, ae_title="OrthancGeneral")
        self.ds = Dataset()

    def move(self, patient_id):
        self.ds.QueryRetrieveLevel = 'PATIENT'
        self.ds.PatientID = patient_id
        if self.assoc.is_established:
            responses = self.assoc.send_c_move(self.ds, 'OrthancSecond', self.code)
            for (status, identifier) in responses:
                if status:
                    Log().info('C-MOVE query status: 0x{0:04x}'.format(status.Status))
                else:
                    Log().warning('Connection timed out, was aborted or received invalid response')
            self.assoc.release()
        else:
            Log().error('Association rejected, aborted or never connected')