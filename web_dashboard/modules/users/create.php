<?php
$page_title = "Add User";
require_once "../../includes/header.php";
require_once "../../includes/sidebar.php";

$error = "";
$success = "";

if (isset($_POST['save'])) {
    $full_name = mysqli_real_escape_string($conn, $_POST['full_name']);
    $email = mysqli_real_escape_string($conn, $_POST['email']);
    $role = mysqli_real_escape_string($conn, $_POST['role']);
    $password = password_hash($_POST['password'], PASSWORD_DEFAULT);

    $check = mysqli_query($conn, "SELECT id FROM users WHERE email='$email'");

    if (mysqli_num_rows($check) > 0) {
        $error = "Email already exists.";
    } else {
        mysqli_query($conn, "
            INSERT INTO users (full_name, email, password, role)
            VALUES ('$full_name', '$email', '$password', '$role')
        ");

        mysqli_query($conn, "
            INSERT INTO logs (action, description)
            VALUES ('CREATE_USER', 'New user created: $email')
        ");

        $success = "User created successfully.";
    }
}
?>

<div class="table-box">
    <h3>Add New User</h3>

    <?php if ($error != "") { ?>
        <div class="error-box"><?php echo $error; ?></div>
    <?php } ?>

    <?php if ($success != "") { ?>
        <div style="background:#dcfce7;color:#166534;padding:10px;border-radius:8px;margin-bottom:15px;">
            <?php echo $success; ?>
        </div>
    <?php } ?>

    <form method="POST">
        <label>Full Name</label>
        <input type="text" name="full_name" required class="form-control">

        <label>Email</label>
        <input type="email" name="email" required class="form-control">

        <label>Password</label>
        <input type="password" name="password" required class="form-control">

        <label>Role</label>
        <select name="role" required class="form-control">
            <option value="admin">Admin</option>
        </select>

        <br>
        <button type="submit" name="save" class="btn">Save User</button>
        <a href="index.php" class="btn btn-danger">Back</a>
    </form>
</div>

<?php require_once "../../includes/footer.php"; ?>
