\c auth_db;

INSERT INTO login_users
    (username, password_hash, status)
VALUES
    ('admin', 'admin', 'ACTIVE'),
    ('user1', 'password123', 'ACTIVE'),
    ('inactive_user', 'password123', 'INACTIVE')
ON CONFLICT (username) DO NOTHING;