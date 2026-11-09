<?php
$page_title = "Users";
require_once "../../includes/header.php";
require_once "../../includes/sidebar.php";

$result = mysqli_query($conn, "SELECT * FROM users ORDER BY id DESC");
?>

<div class="table-box">
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:15px;">
        <h3>System Users</h3>
        <a class="btn" href="create.php">Add New User</a>
    </div>

    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Full Name</th>
                <th>Email</th>
                <th>Role</th>
                <th>Created At</th>
                <th>Action</th>
            </tr>
        </thead>

        <tbody>
            <?php while ($row = mysqli_fetch_assoc($result)) { ?>
                <tr>
                    <td><?php echo $row['id']; ?></td>
                    <td><?php echo $row['full_name']; ?></td>
                    <td><?php echo $row['email']; ?></td>
                    <td><?php echo ucfirst($row['role']); ?></td>
                    <td><?php echo $row['created_at']; ?></td>
                    <td>
                        <a class="btn" href="edit.php?id=<?php echo $row['id']; ?>">Edit</a>

                        <?php if ($row['id'] != $_SESSION['user_id']) { ?>
                            <a class="btn btn-danger" 
                               href="delete.php?id=<?php echo $row['id']; ?>"
                               onclick="return confirm('Are you sure you want to delete this user?');">
                               Delete
                            </a>
                        <?php } ?>
                    </td>
                </tr>
            <?php } ?>
        </tbody>
    </table>
</div>

<?php require_once "../../includes/footer.php"; ?>
