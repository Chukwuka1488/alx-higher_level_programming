-- 12-utf8_conversion.sql

-- Select database
USE `hbtn_0c_0`;

-- Convert table
ALTER TABLE first_table 
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;