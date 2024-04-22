-- Script to create MySQL users 'holberton_user'
--	Replicates the database 'tyrell_corp' from web-01 to web-02

SHOW VARIABLES LIKE 'validate_password%';
SET GLOBAL validate_password_policy=LOW;
CREATE USER 'holberton_user'@'localhost'
IDENTIFIED BY 'projectcorrection280hbtn';

-- Grant permission to the holberton_user to create databases
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
SET GLOBAL validate_password_policy=MEDIUM;

CREATE DATABASE IF NOT EXISTS tyrell_corp;

CHANGE MASTER TO
MASTER_HOST = '18.204.8.46',
MASTER_USER = 'replica_user',
MASTER_PASSWORD = 'replica_user_passwd',
MASTER_LOG_FILE = 'mysql-bin.000001',
MASTER_LOG_POS = 154;

START SLAVE;

SHOW SLAVE STATUS\G;
FLUSH PRIVILEGES;
EXIT;
