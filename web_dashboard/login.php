<?php
require_once "config/config.php";
require_once "config/db.php";

$error = "";

if (isset($_POST['login'])) {
    $email = mysqli_real_escape_string($conn, $_POST['email']);
    $password = $_POST['password'];

    $query = "SELECT * FROM users WHERE email='$email' LIMIT 1";
    $result = mysqli_query($conn, $query);

    if (mysqli_num_rows($result) == 1) {
        $user = mysqli_fetch_assoc($result);

        if (password_verify($password, $user['password'])) {
            $_SESSION['user_id'] = $user['id'];
            $_SESSION['full_name'] = $user['full_name'];
            $_SESSION['role'] = $user['role'];

            header("Location: modules/dashboard/index.php");
            exit();
        } else {
            $error = "Access denied. Invalid credentials.";
        }
    } else {
        $error = "Access denied. Invalid credentials.";
    }
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Login - KeyGuard AI</title>
    <link rel="stylesheet" href="assets/css/style.css">
    <link rel="icon" type="image/png" href="assets/img/logo.png">
    <link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Orbitron:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        body.login-body {
            min-height: 100vh;
            background: #000000;
            display: flex;
            align-items: center;
            justify-content: center;
            background-image:
                linear-gradient(rgba(0, 255, 65, 0.03) 1px, transparent 1px),
                linear-gradient(90deg, rgba(0, 255, 65, 0.03) 1px, transparent 1px);
            background-size: 30px 30px;
            font-family: 'Share Tech Mono', monospace;
        }

        .login-box {
            width: 440px;
            background: #050505;
            padding: 40px;
            border: 1px solid #00ff41;
            box-shadow:
                0 0 30px rgba(0, 255, 65, 0.2),
                0 0 80px rgba(0, 255, 65, 0.05),
                inset 0 0 30px rgba(0, 255, 65, 0.02);
            text-align: center;
            position: relative;
        }

        .login-box::before {
            content: '> KEYGUARD_AI // SECURE ACCESS TERMINAL';
            position: absolute;
            top: -12px;
            left: 20px;
            background: #000000;
            color: #00ff41;
            font-size: 11px;
            padding: 0 8px;
            letter-spacing: 2px;
            font-family: 'Share Tech Mono', monospace;
        }

        .login-box::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 2px;
            background: linear-gradient(90deg, transparent, #00ff41, transparent);
            animation: scan 3s linear infinite;
        }

        @keyframes scan {
            0% { opacity: 0.3; }
            50% { opacity: 1; }
            100% { opacity: 0.3; }
        }

        /* Terminal ASCII Logo */
        .terminal-login-logo {
            margin-bottom: 20px;
        }

        .ascii-logo {
            font-family: 'Share Tech Mono', monospace;
            font-size: 12px;
            color: #00ff41;
            line-height: 1.3;
            white-space: pre;
            text-shadow: 0 0 8px rgba(0, 255, 65, 0.6);
            display: inline-block;
            text-align: left;
        }

        .login-title {
            font-family: 'Orbitron', monospace;
            font-size: 18px;
            color: #00ff41;
            letter-spacing: 4px;
            text-shadow: 0 0 15px rgba(0, 255, 65, 0.6);
            margin: 10px 0 5px;
            animation: glow 2s ease-in-out infinite;
        }

        @keyframes glow {
            0%, 100% { text-shadow: 0 0 5px rgba(0, 255, 65, 0.5); }
            50% { text-shadow: 0 0 20px rgba(0, 255, 65, 0.9), 0 0 40px rgba(0, 255, 65, 0.3); }
        }

        .login-sub {
            color: #005510;
            font-size: 11px;
            letter-spacing: 2px;
            margin-bottom: 30px;
        }

        .login-box label {
            display: block;
            text-align: left;
            margin: 15px 0 6px;
            font-size: 11px;
            color: #00aa2a;
            letter-spacing: 3px;
            text-transform: uppercase;
            font-family: 'Share Tech Mono', monospace;
        }

        .login-box label::before {
            content: '> ';
            color: #005510;
        }

        .login-box input {
            width: 100%;
            padding: 12px;
            background: #000000;
            border: 1px solid #00330d;
            color: #00ff41;
            font-family: 'Share Tech Mono', monospace;
            font-size: 14px;
            outline: none;
            transition: 0.3s;
            letter-spacing: 1px;
        }

        .login-box input:focus {
            border-color: #00ff41;
            box-shadow: 0 0 10px rgba(0, 255, 65, 0.3);
        }

        .login-box input::placeholder {
            color: #003308;
        }

        .login-box button {
            margin-top: 25px;
            width: 100%;
            padding: 14px;
            border: 1px solid #00ff41;
            background: transparent;
            color: #00ff41;
            font-family: 'Orbitron', monospace;
            font-size: 13px;
            letter-spacing: 4px;
            cursor: pointer;
            transition: 0.3s;
            text-transform: uppercase;
        }

        .login-box button:hover {
            background: #00ff41;
            color: #000000;
            box-shadow: 0 0 25px rgba(0, 255, 65, 0.5);
        }

        .error-box {
            background: rgba(255, 0, 0, 0.05);
            color: #ff4444;
            padding: 10px;
            border: 1px solid #ff0000;
            margin-bottom: 15px;
            font-size: 12px;
            letter-spacing: 1px;
            text-align: left;
        }

        .error-box::before {
            content: '[ERROR] ';
            color: #ff0000;
        }

        .login-footer {
            margin-top: 20px;
            font-size: 10px;
            color: #003308;
            letter-spacing: 2px;
            border-top: 1px solid #001a07;
            padding-top: 15px;
        }

        /* Scanline effect */
        body.login-body::after {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: repeating-linear-gradient(
                0deg,
                transparent,
                transparent 2px,
                rgba(0, 0, 0, 0.03) 2px,
                rgba(0, 0, 0, 0.03) 4px
            );
            pointer-events: none;
            z-index: 9999;
        }
    </style>
</head>
<body class="login-body">

<div class="login-box">

    <div class="terminal-login-logo">
        <div class="ascii-logo">
 ██╗  ██╗ ██████╗
 ██║ ██╔╝██╔════╝
 █████╔╝ ██║  ███╗
 ██╔═██╗ ██║   ██║
 ██║  ██╗╚██████╔╝
 ╚═╝  ╚═╝ ╚═════╝</div>
    </div>

    <div class="login-title">KEYGUARD_AI</div>
    <p class="login-sub">> AI-BASED BEHAVIORAL DETECTION SYSTEM</p>

    <?php if ($error != "") { ?>
        <div class="error-box"><?php echo $error; ?></div>
    <?php } ?>

    <form method="POST">
        <label>Email</label>
        <input type="email" name="email" placeholder="user@system.com" required>

        <label>Password</label>
        <input type="password" name="password" placeholder="••••••••" required>

        <button type="submit" name="login">[ AUTHENTICATE ]</button>
    </form>

    <div class="login-footer">
        // AUTHORIZED PERSONNEL ONLY // KEYGUARD AI v1.0
    </div>

</div>

</body>
</html>
