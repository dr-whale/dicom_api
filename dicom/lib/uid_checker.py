from config import config
from config.enum_uid import StudiUID

def uid_checker(uid):
    if uid in config.class_uid[StudiUID.CT]:
        return StudiUID.CT
    elif uid  in config.class_uid[StudiUID.MR]:
        return StudiUID.MR
    else:
        return None