<?php
require_once "../config/db.php";

$csv_file = "../../ai_engine/data/predictions.csv";

if (!file_exists($csv_file)) {
    $status = "error";
    $message = "predictions.csv not found. Run the AI pipeline first.";
} else {
    $file = fopen($csv_file, "r");

    if (!$file) {
        $status = "error";
        $message = "Could not open predictions.csv.";
    } else {
        $header = fgetcsv($file);
        $imported = 0;
        $alerts_added = 0;

        mysqli_query($conn, "DELETE FROM alerts");
        mysqli_query($conn, "DELETE FROM risk_predictions");

        while (($row = fgetcsv($file)) !== false) {
            $data = array_combine($header, $row);
            if (!$data) continue;

            $segment_id     = mysqli_real_escape_string($conn, $data["segment_id"]);
            $session_id     = mysqli_real_escape_string($conn, $data["session_id"]);
            $user_id        = intval($data["user_id"]);
            $predicted_risk = mysqli_real_escape_string($conn, $data["predicted_risk"]);
            $risk_score     = intval($data["risk_score"]);
            $reason         = mysqli_real_escape_string($conn, $data["prediction_reason"]);
            $probability    = floatval($risk_score) / 100;

            mysqli_query($conn, "
                INSERT INTO risk_predictions (segment_id, risk_level, probability)
                VALUES (NULL, '$predicted_risk', '$probability')
            ");

            $imported++;

            if ($predicted_risk === "Medium" || $predicted_risk === "High") {
                mysqli_query($conn, "
                    INSERT INTO alerts (segment_id, risk_level, probability, reason, status, created_at)
                    VALUES (NULL, '$predicted_risk', '$probability', '$reason', 'Open', NOW())
                ");
                $alerts_added++;
            }
        }

        fclose($file);
        $status = "success";
        $message = "Import completed successfully.";
    }
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Import AI Results - KeyGuard AI</title>
    <link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Orbitron:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../assets/css/style.css">
</head>
<body class="import-body">

<div class="import-terminal-box">

    <div class="import-terminal-header">IMPORT AI RESULTS</div>

    <div class="import-log-line">Initializing import sequence...</div>
    <div class="import-log-line">Reading predictions.csv...</div>
    <div class="import-log-line">Clearing old records from database...</div>
    <div class="import-log-line">Writing new predictions and alerts...</div>

    <div class="import-progress-bar">
        <div class="import-progress-fill"></div>
    </div>

    <?php if ($status === "success") { ?>
        <div class="import-status-box import-status-success"><?php echo $message; ?></div>
        <div class="import-stats-grid">
            <div class="import-stat-item">
                <span class="import-stat-label">Rows Imported</span>
                <span class="import-stat-number"><?php echo $imported; ?></span>
            </div>
            <div class="import-stat-item import-stat-alerts">
                <span class="import-stat-label">Alerts Created</span>
                <span class="import-stat-number"><?php echo $alerts_added; ?></span>
            </div>
            <div class="import-stat-item">
                <span class="import-stat-label">Status</span>
                <span class="import-stat-number import-stat-done">DONE</span>
            </div>
        </div>
    <?php } else { ?>
        <div class="import-status-box import-status-error"><?php echo $message; ?></div>
    <?php } ?>

    <a class="import-btn-back" href="../modules/dashboard/index.php">
        RETURN TO DASHBOARD
    </a>

    <div class="import-footer-line">
        // KEYGUARD AI v1.0 // IMPORT SEQUENCE COMPLETE
    </div>

</div>

</body>
</html>
