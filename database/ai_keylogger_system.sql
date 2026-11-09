-- phpMyAdmin SQL Dump
-- Database: `ai_keylogger_system`

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";
/*!40101 SET NAMES utf8mb4 */;

CREATE DATABASE IF NOT EXISTS `ai_keylogger_system`;
USE `ai_keylogger_system`;

CREATE TABLE `alerts` (
  `id` int(11) NOT NULL,
  `segment_id` int(11) DEFAULT NULL,
  `risk_level` enum('Low','Medium','High') DEFAULT NULL,
  `probability` float DEFAULT NULL,
  `reason` text DEFAULT NULL,
  `status` enum('Open','Resolved') DEFAULT 'Open',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `analyzed_segments` (
  `id` int(11) NOT NULL,
  `segment_id` varchar(150) DEFAULT NULL,
  `session_id` varchar(150) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `typing_speed` float DEFAULT NULL,
  `avg_dwell_time` float DEFAULT NULL,
  `avg_flight_time` float DEFAULT NULL,
  `pause_ratio` float DEFAULT NULL,
  `special_key_ratio` float DEFAULT NULL,
  `backspace_ratio` float DEFAULT NULL,
  `ctrl_alt_ratio` float DEFAULT NULL,
  `predicted_risk` varchar(50) DEFAULT NULL,
  `risk_score` int(11) DEFAULT NULL,
  `reason` text DEFAULT NULL,
  `created_at` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `analyzed_segments` (`id`, `segment_id`, `session_id`, `user_id`, `typing_speed`, `avg_dwell_time`, `avg_flight_time`, `pause_ratio`, `special_key_ratio`, `backspace_ratio`, `ctrl_alt_ratio`, `predicted_risk`, `risk_score`, `reason`, `created_at`) VALUES
(1, '3430cbaf-9afb-452e-90f3-217f73b8c034_0', '3430cbaf-9afb-452e-90f3-217f73b8c034', 2, 2.92381, 0.103263, 0.297834, 0, 0.290909, 0, 0.0545455, 'Low', 20, 'Normal behavioral pattern', '2026-05-18 06:31:22'),
(2, '3430cbaf-9afb-452e-90f3-217f73b8c034_1', '3430cbaf-9afb-452e-90f3-217f73b8c034', 2, 1.82891, 0.209389, 0.453481, 0.0555556, 0.263158, 0, 0.0526316, 'Low', 20, 'Normal behavioral pattern', '2026-05-18 06:31:22'),
(3, 'synthetic_low_0', 'synthetic', 2, 2.5, 0.12, 0.25, 0.05, 0.08, 0.03, 0, 'Low', 20, 'Normal behavioral pattern', '2026-05-18 06:31:22'),
(4, 'synthetic_low_1', 'synthetic', 2, 2.5, 0.12, 0.25, 0.05, 0.08, 0.03, 0, 'Low', 20, 'Normal behavioral pattern', '2026-05-18 06:31:22'),
(5, 'synthetic_low_2', 'synthetic', 2, 2.5, 0.12, 0.25, 0.05, 0.08, 0.03, 0, 'Low', 20, 'Normal behavioral pattern', '2026-05-18 06:31:22'),
(6, 'synthetic_low_3', 'synthetic', 2, 2.5, 0.12, 0.25, 0.05, 0.08, 0.03, 0, 'Low', 20, 'Normal behavioral pattern', '2026-05-18 06:31:22'),
(7, 'synthetic_low_4', 'synthetic', 2, 2.5, 0.12, 0.25, 0.05, 0.08, 0.03, 0, 'Low', 20, 'Normal behavioral pattern', '2026-05-18 06:31:22'),
(8, 'synthetic_low_5', 'synthetic', 2, 2.5, 0.12, 0.25, 0.05, 0.08, 0.03, 0, 'Low', 20, 'Normal behavioral pattern', '2026-05-18 06:31:22'),
(9, 'synthetic_low_6', 'synthetic', 2, 2.5, 0.12, 0.25, 0.05, 0.08, 0.03, 0, 'Low', 20, 'Normal behavioral pattern', '2026-05-18 06:31:22'),
(10, 'synthetic_low_7', 'synthetic', 2, 2.5, 0.12, 0.25, 0.05, 0.08, 0.03, 0, 'Low', 20, 'Normal behavioral pattern', '2026-05-18 06:31:22'),
(11, 'synthetic_low_8', 'synthetic', 2, 2.5, 0.12, 0.25, 0.05, 0.08, 0.03, 0, 'Low', 20, 'Normal behavioral pattern', '2026-05-18 06:31:22'),
(12, 'synthetic_low_9', 'synthetic', 2, 2.5, 0.12, 0.25, 0.05, 0.08, 0.03, 0, 'Low', 20, 'Normal behavioral pattern', '2026-05-18 06:31:22'),
(13, 'synthetic_medium_0', 'synthetic', 2, 3.2, 0.1, 0.18, 0.35, 0.28, 0.18, 0.05, 'Medium', 55, 'High backspace ratio; Unusual pause ratio', '2026-05-18 06:31:22'),
(27, 'synthetic_medium_1', 'synthetic', 2, 3.2, 0.1, 0.18, 0.35, 0.28, 0.18, 0.05, 'Medium', 55, 'High backspace ratio; Unusual pause ratio', '2026-05-18 06:32:03'),
(28, 'synthetic_medium_2', 'synthetic', 2, 3.2, 0.1, 0.18, 0.35, 0.28, 0.18, 0.05, 'Medium', 55, 'High backspace ratio; Unusual pause ratio', '2026-05-18 06:32:03'),
(29, 'synthetic_medium_3', 'synthetic', 2, 3.2, 0.1, 0.18, 0.35, 0.28, 0.18, 0.05, 'Medium', 55, 'High backspace ratio; Unusual pause ratio', '2026-05-18 06:32:03'),
(30, 'synthetic_medium_4', 'synthetic', 2, 3.2, 0.1, 0.18, 0.35, 0.28, 0.18, 0.05, 'Medium', 55, 'High backspace ratio; Unusual pause ratio', '2026-05-18 06:32:03'),
(31, 'synthetic_medium_5', 'synthetic', 2, 3.2, 0.1, 0.18, 0.35, 0.28, 0.18, 0.05, 'Medium', 55, 'High backspace ratio; Unusual pause ratio', '2026-05-18 06:32:03'),
(32, 'synthetic_medium_6', 'synthetic', 2, 3.2, 0.1, 0.18, 0.35, 0.28, 0.18, 0.05, 'Medium', 55, 'High backspace ratio; Unusual pause ratio', '2026-05-18 06:32:03'),
(33, 'synthetic_medium_7', 'synthetic', 2, 3.2, 0.1, 0.18, 0.35, 0.28, 0.18, 0.05, 'Medium', 55, 'High backspace ratio; Unusual pause ratio', '2026-05-18 06:32:03'),
(34, 'synthetic_medium_8', 'synthetic', 2, 3.2, 0.1, 0.18, 0.35, 0.28, 0.18, 0.05, 'Medium', 55, 'High backspace ratio; Unusual pause ratio', '2026-05-18 06:32:03'),
(35, 'synthetic_medium_9', 'synthetic', 2, 3.2, 0.1, 0.18, 0.35, 0.28, 0.18, 0.05, 'Medium', 55, 'High backspace ratio; Unusual pause ratio', '2026-05-18 06:32:03'),
(36, 'synthetic_high_0', 'synthetic', 2, 9.5, 0.04, 0.03, 0.02, 0.55, 0.04, 0.2, 'High', 85, 'Very high typing speed; High Ctrl/Alt usage; High special key usage', '2026-05-18 06:32:03'),
(37, 'synthetic_high_1', 'synthetic', 2, 9.5, 0.04, 0.03, 0.02, 0.55, 0.04, 0.2, 'High', 85, 'Very high typing speed; High Ctrl/Alt usage; High special key usage', '2026-05-18 06:32:03'),
(38, 'synthetic_high_2', 'synthetic', 2, 9.5, 0.04, 0.03, 0.02, 0.55, 0.04, 0.2, 'High', 85, 'Very high typing speed; High Ctrl/Alt usage; High special key usage', '2026-05-18 06:32:03'),
(39, 'synthetic_high_3', 'synthetic', 2, 9.5, 0.04, 0.03, 0.02, 0.55, 0.04, 0.2, 'High', 85, 'Very high typing speed; High Ctrl/Alt usage; High special key usage', '2026-05-18 06:32:03'),
(40, 'synthetic_high_4', 'synthetic', 2, 9.5, 0.04, 0.03, 0.02, 0.55, 0.04, 0.2, 'High', 85, 'Very high typing speed; High Ctrl/Alt usage; High special key usage', '2026-05-18 06:32:03'),
(41, 'synthetic_high_5', 'synthetic', 2, 9.5, 0.04, 0.03, 0.02, 0.55, 0.04, 0.2, 'High', 85, 'Very high typing speed; High Ctrl/Alt usage; High special key usage', '2026-05-18 06:32:03'),
(42, 'synthetic_high_6', 'synthetic', 2, 9.5, 0.04, 0.03, 0.02, 0.55, 0.04, 0.2, 'High', 85, 'Very high typing speed; High Ctrl/Alt usage; High special key usage', '2026-05-18 06:32:03'),
(43, 'synthetic_high_7', 'synthetic', 2, 9.5, 0.04, 0.03, 0.02, 0.55, 0.04, 0.2, 'High', 85, 'Very high typing speed; High Ctrl/Alt usage; High special key usage', '2026-05-18 06:32:03'),
(44, 'synthetic_high_8', 'synthetic', 2, 9.5, 0.04, 0.03, 0.02, 0.55, 0.04, 0.2, 'High', 85, 'Very high typing speed; High Ctrl/Alt usage; High special key usage', '2026-05-18 06:32:03'),
(45, 'synthetic_high_9', 'synthetic', 2, 9.5, 0.04, 0.03, 0.02, 0.55, 0.04, 0.2, 'High', 85, 'Very high typing speed; High Ctrl/Alt usage; High special key usage', '2026-05-18 06:32:03');

CREATE TABLE `features` (
  `id` int(11) NOT NULL,
  `segment_id` int(11) DEFAULT NULL,
  `total_keys` int(11) DEFAULT NULL,
  `duration` float DEFAULT NULL,
  `keys_per_second` float DEFAULT NULL,
  `dwell_mean` float DEFAULT NULL,
  `dwell_std` float DEFAULT NULL,
  `flight_mean` float DEFAULT NULL,
  `flight_std` float DEFAULT NULL,
  `special_key_ratio` float DEFAULT NULL,
  `backspace_ratio` float DEFAULT NULL,
  `pause_ratio` float DEFAULT NULL,
  `uniform_timing_score` float DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `features` (`id`, `segment_id`, `total_keys`, `duration`, `keys_per_second`, `dwell_mean`, `dwell_std`, `flight_mean`, `flight_std`, `special_key_ratio`, `backspace_ratio`, `pause_ratio`, `uniform_timing_score`, `created_at`) VALUES
(6, 6, 34, 7.25721, 4.685, 0.07999, 0.01593, 0.21629, 0.1996, 0.02941, 0, 0, 5.00742, '2026-05-06 18:01:02');

CREATE TABLE `logs` (
  `id` int(11) NOT NULL,
  `action` varchar(255) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `logs` (`id`, `action`, `description`, `created_at`) VALUES
(1, 'SYSTEM_START', 'System initialized successfully', '2026-05-02 03:32:17'),
(2, 'IMPORT_AI_RESULTS', 'AI CSV results imported successfully into MySQL', '2026-05-02 03:43:19'),
(3, 'IMPORT_AI_RESULTS', 'AI CSV results imported successfully into MySQL', '2026-05-02 03:53:56'),
(4, 'TEST_DATA', 'Test data inserted successfully', '2026-05-02 03:58:10'),
(5, 'IMPORT_AI_RESULTS', 'AI CSV results imported successfully into MySQL', '2026-05-06 18:01:02');

CREATE TABLE `risk_predictions` (
  `id` int(11) NOT NULL,
  `segment_id` int(11) DEFAULT NULL,
  `risk_level` enum('Low','Medium','High') DEFAULT NULL,
  `probability` float DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `risk_predictions` (`id`, `segment_id`, `risk_level`, `probability`, `created_at`) VALUES
(5, 6, 'Low', 1, '2026-05-06 18:01:02');

CREATE TABLE `segments` (
  `id` int(11) NOT NULL,
  `session_id` varchar(100) DEFAULT NULL,
  `segment_id` int(11) DEFAULT NULL,
  `total_keys` int(11) DEFAULT NULL,
  `duration` float DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `segments` (`id`, `session_id`, `segment_id`, `total_keys`, `duration`, `created_at`) VALUES
(6, 'session_9f71092c', 1, 34, 7.25721, '2026-05-06 18:01:02');

CREATE TABLE `sessions` (
  `id` int(11) NOT NULL,
  `session_id` varchar(100) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `start_time` datetime DEFAULT NULL,
  `end_time` datetime DEFAULT NULL,
  `status` enum('active','ended') DEFAULT 'active'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `sessions` (`id`, `session_id`, `user_id`, `start_time`, `end_time`, `status`) VALUES
(1, 'session_001', NULL, '2026-05-02 06:32:17', '2026-05-02 06:32:17', 'active'),
(2, 'test_session', NULL, '2026-05-02 06:57:37', '2026-05-02 06:57:37', 'active'),
(3, 'test_session', NULL, '2026-05-02 06:58:10', '2026-05-02 06:58:10', 'active');

CREATE TABLE `settings` (
  `id` int(11) NOT NULL,
  `setting_key` varchar(100) DEFAULT NULL,
  `setting_value` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `settings` (`id`, `setting_key`, `setting_value`) VALUES
(1, 'segment_duration_seconds', '10'),
(2, 'high_risk_threshold', '0.8'),
(3, 'medium_risk_threshold', '0.5');

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `full_name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `role` enum('admin','supervisor') DEFAULT 'supervisor',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `users` (`id`, `full_name`, `email`, `password`, `role`, `created_at`) VALUES
(1, 'System Admin', 'admin@system.com', '$2y$10$N8y5vcAq0sUbnhsGmzkoV.EVI7RkYqnEdH0.8gKAfyzC8AhMpWMQq', 'admin', '2026-05-02 03:32:17'),
(2, 'Test Admin', 'test@system.com', '$2y$10$N8y5vcAq0sUbnhsGmzkoV.EVI7RkYqnEdH0.8gKAfyzC8AhMpWMQq', 'admin', '2026-05-02 03:57:37');

ALTER TABLE `alerts` ADD PRIMARY KEY (`id`), ADD KEY `segment_id` (`segment_id`);
ALTER TABLE `analyzed_segments` ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `segment_id` (`segment_id`);
ALTER TABLE `features` ADD PRIMARY KEY (`id`), ADD KEY `segment_id` (`segment_id`);
ALTER TABLE `logs` ADD PRIMARY KEY (`id`);
ALTER TABLE `risk_predictions` ADD PRIMARY KEY (`id`), ADD KEY `segment_id` (`segment_id`);
ALTER TABLE `segments` ADD PRIMARY KEY (`id`);
ALTER TABLE `sessions` ADD PRIMARY KEY (`id`), ADD KEY `user_id` (`user_id`);
ALTER TABLE `settings` ADD PRIMARY KEY (`id`);
ALTER TABLE `users` ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `email` (`email`);

ALTER TABLE `alerts` MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
ALTER TABLE `analyzed_segments` MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=78;
ALTER TABLE `features` MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
ALTER TABLE `logs` MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
ALTER TABLE `risk_predictions` MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
ALTER TABLE `segments` MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
ALTER TABLE `sessions` MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
ALTER TABLE `settings` MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
ALTER TABLE `users` MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

ALTER TABLE `alerts` ADD CONSTRAINT `alerts_ibfk_1` FOREIGN KEY (`segment_id`) REFERENCES `segments` (`id`) ON DELETE CASCADE;
ALTER TABLE `features` ADD CONSTRAINT `features_ibfk_1` FOREIGN KEY (`segment_id`) REFERENCES `segments` (`id`) ON DELETE CASCADE;
ALTER TABLE `risk_predictions` ADD CONSTRAINT `risk_predictions_ibfk_1` FOREIGN KEY (`segment_id`) REFERENCES `segments` (`id`) ON DELETE CASCADE;
ALTER TABLE `sessions` ADD CONSTRAINT `sessions_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE SET NULL;
COMMIT;
