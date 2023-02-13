<?php

namespace app\controllers;

use yii\web\Controller;
use app\models\Dicom;

class DicomController extends Controller
{
    public function actionIndex()
    {
        $query = Dicom::find();

        $weather = $query->orderBy('forecast_date')->all();

        return $this->render('index', ['weather' => $weather]);
    }
}