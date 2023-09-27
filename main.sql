-- CREATE DATABASE big_data_db;
-- USE big_data_db Name;

CREATE TABLE data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    payload JSON,
    created_at DATETIME
);
