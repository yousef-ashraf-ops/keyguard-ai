<?php
require_once "../../config/config.php";
require_once "../../config/db.php";
require_once "../../includes/auth.php";

if (isset($_GET['id'])) {
    $id = (int) $_GET['id'];

    mysqli_query($conn, "
        UPDATE alerts 
        SET status='Resolved' 
        WHERE id='$id'
    ");

    mysqli_query($conn, "
        INSERT INTO logs (action, description)
        VALUES ('RESOLVE_ALERT', 'Alert ID $id marked as resolved')
    ");
}

header("Location: index.php");
exit();
?>
