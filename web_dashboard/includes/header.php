<?php
require_once dirname(__DIR__) . "/config/config.php";
require_once dirname(__DIR__) . "/config/db.php";
require_once dirname(__DIR__) . "/includes/auth.php";
?>

<!DOCTYPE html>
<html>
<head>
    <title><?php echo PROJECT_NAME; ?></title>

    <link rel="stylesheet" href="<?php echo BASE_URL; ?>assets/css/style.css">

    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
			<link rel="icon" type="image/png" href="<?php echo BASE_URL; ?>assets/img/logo.png">

</head>
<body>

<div class="layout">
