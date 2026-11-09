USE ai_keylogger_system;

INSERT INTO sessions (session_id, start_time, end_time, status)
VALUES ('test_session', NOW(), NOW(), 'active');

INSERT INTO segments (session_id, segment_id, total_keys, duration)
VALUES ('test_session', 1, 100, 12.5);

SET @last_segment_id = LAST_INSERT_ID();

INSERT INTO features (
    segment_id,
    total_keys,
    duration,
    keys_per_second,
    dwell_mean,
    dwell_std,
    flight_mean,
    flight_std,
    special_key_ratio,
    backspace_ratio,
    pause_ratio,
    uniform_timing_score
) VALUES (
    @last_segment_id,
    100,
    12.5,
    8.0,
    0.10,
    0.02,
    0.20,
    0.04,
    0.25,
    0.05,
    0.10,
    15
);

INSERT INTO risk_predictions (segment_id, risk_level, probability)
VALUES (@last_segment_id, 'High', 0.92);

INSERT INTO alerts (segment_id, risk_level, probability, reason)
VALUES (@last_segment_id, 'High', 0.92, 'Test high-risk pattern');

INSERT INTO logs (action, description)
VALUES ('TEST_DATA', 'Test data inserted successfully');
