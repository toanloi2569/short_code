# Some shell scrip for postgresql

**Start server postgre**  
`sudo service posgresql start`

**Query database**  
`sudo -u postgres psql -c "$query;"`  
ex : `sudo -u postgres psql -c "DROP DATABASE test;"`

**Create databse**  
`sudo -u postgres psql -c "CREATE DATABASE $dbname;"`  
ex : `sudo -u postgres psql -c "CREATE DATABASE test;"`

**Drop database**  
`sudo -u postgres psql -c "DROP DATABASE $dbname;"`  
ex : `sudo -u postgres psql -c "DROP DATABASE test;"`

**Set password**  
`sudo -u postgres psql -c "ALTER USER $user PASSWORD '$password';"`  
ex : `sudo -u postgres psql -c "ALTER USER postgres PASSWORD 'password';"`

# Access to terminal-based front-end to PostgreSQL
`sudo -i -u postgres`  
`psql`	: access to terminal-based front-end to PostgreSQL  
`\l`  	:  list databases  
`\c dbname` :  access a database

# Dump and load database
**Dump database with password**  
`PGPASSWORD="$password" pg_dump -U $user -h localhost $dbname > $filename.pgsql`  
ex : `PGPASSWORD="password" pg_dump -U postgres -h localhost test > db.pgsql`  

**Load database with password**  
`PGPASSWORD="$password" psql -U $user -h localhost $dbname < $filename.pgsql`  
ex : `PGPASSWORD="password" psql -U postgres -h localhost test < db.pgsql`  

**Dump database**  
`pg_dump -u $user -h localhost $dbname > $filename.pgsql`  
ex : `pg_dump -u postgres -h localhost test > db.pgsql`  
