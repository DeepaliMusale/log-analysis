## PROJECT - LOG-ANALYSIS

** Task:**
 Task is to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

### Reporting Questions:
 1) What are most popular three articles of all time?
 2) Who are the most popular article authors of all time?
 3) On which days did more than 1% of requests lead to errors? 

### Requirements:
#### The Virtual Machine
This project makes use of the same Linux-based virtual machine (VM) as the preceding lessons.

If you skipped those lessons and came right to this project, that's OK! However, you will need to go back to the instructions to install the virtual machine. Please see previous lessons to complete the installation process.

This will give you the PostgreSQL database and support software needed for this project. If you have used an older version of this VM, you may need to install it into a new directory.

If you need to bring the virtual machine back online (with vagrant up), do so now. Then log into it with vagrant ssh.

 #### Download the Data
 Next, download the data here. You will need to unzip this file after downloading it. The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine.

To build the reporting tool, you'll need to load the site's data into your local database. Review how to use the psql command in this lesson: (FSND version)

To load the data, cd into the vagrant directory and use the command psql -d news -f newsdata.sql.
Here's what this command does:

**psql** — the PostgreSQL command line program
**-d news** — connect to the database named news which has been set up for you
**-f newsdata.sql** — run the SQL statements in the file newsdata.sql
Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.

### Getting an error?
If this command gives an error message, such as —
psql: FATAL: database "news" does not exist
psql: could not connect to server: Connection refused
— this means the database server is not running or is not set up correctly. This can happen if you have an older version of the VM configuration from before this project was added. To continue, [download the virtual machine configuration](https://classroom.udacity.com/me) into a fresh new directory and start it from there.

### Explore the Data
Once you have the data loaded into your database, connect to your database using **psql -d news** and explore the tables using the **\dt** and **\d table** commands and select statements.

**\dt** — display tables — lists the tables that are available in the database.
**\d table** — (replace table with the name of a table) — shows the database schema for that particular table.
Get a sense for what sort of information is in each column of these tables.

The database includes three tables:
The ***authors table*** includes information about the authors of articles.
The ***articles table*** includes the articles themselves.
The ***log table*** includes one entry for each time a user has accessed the site.

### Connecting from your code
The database that you're working with in this project is running PostgreSQL, like the forum database that you worked with in the course. So in your code, you'll want to use the ```psycopg2``` Python module to connect to it, for instance:
As you explore the data, you may find it useful to take notes! Don't try to memorize all the columns. Instead, write down a description of the column names and what kind of values are found in those columns.
              ```db = psycopg2.connect("dbname=news")```