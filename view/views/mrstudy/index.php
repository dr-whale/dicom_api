<?php
use yii\helpers\Html;
use yii\widgets\LinkPager;
?>

<h1>MR Study</h1>
<ul>
<?php foreach ($dicom as $value): ?>
    <li>
        ID: <?= $value->ID ?><br>
        InstanceUID: <?= $value->InstanceUID ?><br>
        SeriesUID: <?= $value->SeriesUID ?><br>
        StudyUID: <?= $value->StudyUID ?><br>
        Patient: <?= $value->Patient ?><br>
        Rows: <?= $value->Rows ?><br>
        Columns: <?= $value->Columns ?>
    </li>
<?php endforeach; ?>
</ul>

<?= LinkPager::widget(['pagination' => $pagination]) ?>