-- Script to create MySQL users 'holberton_user' and 'replica_user'
--	Database: 'tyrell_corp' and Table: 'nexus6'

SHOW VARIABLES LIKE 'validate_password%';
SET GLOBAL validate_password_policy=LOW;
CREATE USER 'holberton_user'@'localhost'
IDENTIFIED BY 'projectcorrection280hbtn';

-- Grant permission to the holberton_user to create databases
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';

CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;

CREATE TABLE IF NOT EXISTS nexus6 (
	id INT,
	name VARCHAR(256)
);

INSERT INTO nexus6 (id, name) VALUES (1, 'Leon');
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';
CREATE USER 'replica_user'@'%' IDENTIFIED BY 'replica_user_passwd';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';

GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
CREATE USER 'web-02'@'34.203.77.40' IDENTIFIED BY 'web_02_passwd';
GRANT REPLICATION SLAVE ON *.* TO 'web-02'@'34.203.77.40';

SET GLOBAL validate_password_policy=MEDIUM;

FLUSH PRIVILEGES;
EXIT;
