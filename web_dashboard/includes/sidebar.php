<div class="sidebar">

    <!-- LOGO + TITLE -->
    <div class="brand">
        <div class="terminal-logo">
            <div class="terminal-logo-top">
                <span class="tl-bracket">[</span>
                <span class="tl-text">KG</span>
                <span class="tl-bracket">]</span>
            </div>
            <div class="terminal-logo-art">
┌─────────────┐
│ ░▒▓ KG ▓▒░ │
│  AI SHIELD  │
│ ▄▀▄▀▄▀▄▀▄▀ │
└─────────────┘
            </div>
        </div>
        <h3>KEYGUARD_AI</h3>
        <p class="brand-sub">> BEHAVIOR_DETECTION_v1.0</p>
    </div>

    <!-- MAIN NAVIGATION -->
    <div class="menu-section">
        <span class="menu-title">// MAIN</span>

        <a href="<?php echo BASE_URL; ?>modules/dashboard/index.php">
            Dashboard
        </a>

        <a href="<?php echo BASE_URL; ?>modules/segments/index.php">
            Segments Analysis
        </a>

        <a href="<?php echo BASE_URL; ?>modules/alerts/index.php">
            Alerts
        </a>

        <a href="<?php echo BASE_URL; ?>modules/reports/index.php">
            Reports
        </a>
    </div>

    <!-- MANAGEMENT -->
    <div class="menu-section">
        <span class="menu-title">// MANAGEMENT</span>

        <a href="<?php echo BASE_URL; ?>modules/users/index.php">
            Users
        </a>

        <a href="<?php echo BASE_URL; ?>modules/settings/index.php">
            Settings
        </a>

        <a href="<?php echo BASE_URL; ?>modules/logs/index.php">
            System Logs
        </a>
    </div>

    <!-- AI CONTROL -->
    <div class="menu-section">
        <span class="menu-title">// AI ENGINE</span>

        <a href="<?php echo BASE_URL; ?>api/import_ai_results.php">
            Import AI Results
        </a>
    </div>

    <!-- USER INFO -->
    <div class="user-box">
        <strong><?php echo $_SESSION['full_name']; ?></strong>
        <small><?php echo ucfirst($_SESSION['role']); ?></small>
    </div>

    <!-- LOGOUT -->
    <a href="<?php echo BASE_URL; ?>logout.php" class="logout">
        Logout
    </a>

</div>

<div class="main-content">
    <div class="topbar">
        <h2><?php echo $page_title ?? "Dashboard"; ?></h2>
        <div class="topbar-right">
            <span class="status-dot"></span>
            <span class="status-text">SYSTEM ONLINE</span>
        </div>
    </div>
