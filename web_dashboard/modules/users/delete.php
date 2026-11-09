<?php
require_once "../../config/config.php";
require_once "../../config/db.php";
require_once "../../includes/auth.php";

if (isset($_GET['id'])) {
    $id = (int)$_GET['id'];

    if ($id != $_SESSION['user_id']) {
        mysqli_query($conn, "DELETE FROM users WHERE id='$id'");

        mysqli_query($conn, "
            INSERT INTO logs (action, description)
            VALUES ('DELETE_USER', 'User deleted with ID: $id')
        ");
    }
}

header("Location: index.php");
exit();
?>
