<?php
$page_title = "Edit User";
require_once "../../includes/header.php";
require_once "../../includes/sidebar.php";

$id = (int)$_GET['id'];

$user_result = mysqli_query($conn, "SELECT * FROM users WHERE id='$id'");
$user = mysqli_fetch_assoc($user_result);

if (!$user) {
    echo "<div class='table-box'>User not found.</div>";
    require_once "../../includes/footer.php";
    exit();
}

$success = "";

if (isset($_POST['update'])) {
    $full_name = mysqli_real_escape_string($conn, $_POST['full_name']);
    $email = mysqli_real_escape_string($conn, $_POST['email']);
    $role = mysqli_real_escape_string($conn, $_POST['role']);

    if (!empty($_POST['password'])) {
        $password = password_hash($_POST['password'], PASSWORD_DEFAULT);

        mysqli_query($conn, "
            UPDATE users 
            SET full_name='$full_name', email='$email', role='$role', password='$password'
            WHERE id='$id'
        ");
    } else {
        mysqli_query($conn, "
            UPDATE users 
            SET full_name='$full_name', email='$email', role='$role'
            WHERE id='$id'
        ");
    }

    mysqli_query($conn, "
        INSERT INTO logs (action, description)
        VALUES ('UPDATE_USER', 'User updated: $email')
    ");

    $success = "User updated successfully.";

    $user_result = mysqli_query($conn, "SELECT * FROM users WHERE id='$id'");
    $user = mysqli_fetch_assoc($user_result);
}
?>

<div class="table-box">
    <h3>Edit User</h3>

    <?php if ($success != "") { ?>
        <div style="background:#dcfce7;color:#166534;padding:10px;border-radius:8px;margin-bottom:15px;">
            <?php echo $success; ?>
        </div>
    <?php } ?>

    <form method="POST">
        <label>Full Name</label>
        <input type="text" name="full_name" value="<?php echo $user['full_name']; ?>" required class="form-control">

        <label>Email</label>
        <input type="email" name="email" value="<?php echo $user['email']; ?>" required class="form-control">

        <label>New Password</label>
        <input type="password" name="password" class="form-control">
        <small>Leave empty if you do not want to change password.</small>

        <br><br>

        <label>Role</label>
        <select name="role" required class="form-control">
            <option value="admin" <?php if ($user['role'] == "admin") echo "selected"; ?>>Admin</option>
        </select>

        <br>
        <button type="submit" name="update" class="btn">Update User</button>
        <a href="index.php" class="btn btn-danger">Back</a>
    </form>
</div>

<?php require_once "../../includes/footer.php"; ?>
