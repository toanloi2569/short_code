# Some shell scrip for postgresql

### Start server postgre
sudo service posgresql start

### Query database
sudo -u postgres psql -c "$query;"

### Create databse
sudo -u postgres psql -c "CREATE DATABASE $dbname;"

### Drop database
sudo -u postgres psql -c "DROP DATABASE $dbname;"

### Set password 
sudo -u postgres psql -c "ALTER USER $user PASSWORD '$password';"

#---------------------------------------------------------------------------------#

# Access to terminal-based front-end to PostgreSQL
sudo -i -u postgres

psql		# access to terminal-based front-end to PostgreSQL
\l  		# list databases
\c dbname 	# access a database

#---------------------------------------------------------------------------------# 

# Dump database with password
PGPASSWORD="$password" pg_dump -U $user -h localhost $dbname > $filename.pgsql

# Load database with passworf
PGPASSWORD="$password" psql -U $user -h localhost $dbname < $filename.pgsql

# Dump database
pg_dump _u $user -h localhost $dbname > $filename.pgsql
