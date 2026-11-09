<?php
require_once "../../config/config.php";
require_once "../../config/db.php";
require_once "../../includes/auth.php";

$where = "WHERE 1=1";

if (!empty($_GET['risk_level'])) {
    $risk_level = mysqli_real_escape_string($conn, $_GET['risk_level']);
    $where .= " AND risk_level='$risk_level'";
}

header("Content-Type: text/csv; charset=utf-8");
header("Content-Disposition: attachment; filename=keyguard_ai_report.csv");

$output = fopen("php://output", "w");

fputcsv($output, [
    "ID",
    "Risk Level",
    "Probability",
    "Created At"
]);

$result = mysqli_query($conn, "
    SELECT *
    FROM risk_predictions
    $where
    ORDER BY created_at DESC
");

while ($row = mysqli_fetch_assoc($result)) {
    fputcsv($output, [
        $row['id'],
        $row['risk_level'],
        round($row['probability'] * 100, 2) . "%",
        $row['created_at']
    ]);
}

fclose($output);
exit();
?>
