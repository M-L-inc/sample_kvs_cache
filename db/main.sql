CREATE DATABASE myflaskapp;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE USER 'benchmark_user'@'localhost' IDENTIFIED BY 'benchmark_test';
CREATE USER 'benchmark_user'@'127.0.0.1' IDENTIFIED BY 'benchmark_test';

-- Grant privileges for both user specifications
GRANT ALL PRIVILEGES ON myflaskapp.* TO 'benchmark_user'@'localhost';
GRANT ALL PRIVILEGES ON myflaskapp.* TO 'benchmark_user'@'127.0.0.1';

FLUSH PRIVILEGES;