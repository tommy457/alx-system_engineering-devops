# 0x14. MySQL #



# Task 1:

CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';

GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';

# Task 2:

CREATE DATABASE tyrell_corp;

USE tyrell_corp;

CREATE TABLE nexus6 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(24));

INSERT INTO nexus6 (name) VALUES ("Mohamed");

GRANT SELECT ON tyrell_corp.* TO 'holberton_user'@'localhost';

# Task 3:

CREATE USER 'replica_user'@'%' IDENTIFIED BY 'projectcorrection280hbtn';

GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';

GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
