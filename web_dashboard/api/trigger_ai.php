<?php
require_once "../config/db.php";

$python = "python";
$script = "../../ai_engine/src/run_pipeline.py";

$command = $python . " " . escapeshellarg($script);

$output = shell_exec($command . " 2>&1");

echo "<pre>";
echo htmlspecialchars($output);
echo "</pre>";

echo "<hr>";
echo "<a href='import_ai_results.php'>Import AI Results to Database</a>";
?>
