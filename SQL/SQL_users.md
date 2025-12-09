#

mysql -u root -p (WSL)
sudo mysql
SHOW DATABASESSELECT user, host, plugin FROM mysql.user;
SELECT user, host, authentication_string FROM mysql.user;


CREATE USER 'username'@'host' IDENTIFIED WITH authentication_plugin BY 'password';
After CREATE USER, you specify a username. This is immediately followed by an @ sign and then the hostname from which this user will connect. If you only plan to access this user locally from your Ubuntu server, you can specify localhost. Wrapping both the username and host in single quotes isn’t always necessary, but doing so can help to prevent errors.

