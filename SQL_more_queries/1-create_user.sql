-- script to create a sql user with id user_0d_1

-- makes user and checks that it doesn't already exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to new user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- makes sure the privileges is applied
FLUSH PRIVILEGES;
