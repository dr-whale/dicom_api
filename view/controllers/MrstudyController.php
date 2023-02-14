<?php

namespace app\controllers;

use yii\web\Controller;
use yii\data\Pagination;
use app\models\Mr_table;

class MrstudyController extends Controller
{
    public function actionIndex()
    {
        $query = Mr_table::find();

        $pagination = new Pagination([
            'defaultPageSize' => 5,
            'totalCount' => $query->count(),
        ]);

        $dicom = $query->orderBy('ID')
            ->offset($pagination->offset)
            ->limit($pagination->limit)
            ->all();

        return $this->render('index', ['dicom' => $dicom, 'pagination' => $pagination]);
    }
}