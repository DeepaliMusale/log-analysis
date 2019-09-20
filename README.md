# PROJECT - LOG-ANALYSIS

## Task:

 To create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

## Reporting Questions:
 1) What are most popular three articles of all time?
 2) Who are the most popular article authors of all time?
 3) On which days did more than 1% of requests lead to errors? 

## Requirements:
To start on this project, you'll need database software (provided by a Linux virtual machine) and the data to analyze.

[Vagrant](https://www.vagrantup.com/downloads.html) - Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem.

[Virtual Box](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) - VirtualBox is the software that actually runs the virtual machine.

[FSND-Virtual-Machine](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip) - Download the VM configuration file
 
[Git](https://git-scm.com/downloads) - We need to use Git Bash terminal

**Skills** - Python3,PostgreSQL

 #### Download the Data
 Download the [database data here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). You will need to unzip this file after downloading it. The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine.

 ## Procedure:
 1) Install Git using the link provided in the requirements section.
 2) Install Vagrant using the link provided in the requirements section.
 3) Install Virtual Machine using the link provided in the requirements section.
 4) Download and unzip the VM configuration file 'FSND-Virtual-Machine' using the link which is provided in the requirements section.
 5) Open Git Bash Terminal and start the virtual machine by running the command ```vagrant up```. When ```vagrant up``` is finished running and you get shell prompt back, run command ```vagrant ssh``` to log in to your newly installed VM
 6) To load the data, cd into the vagrant directory and use the command ***psql -d news -f newsdata.sql***.
 Here's what this command does:

 **psql** — the PostgreSQL command line program
 
 **-d news** — connect to the database named news which has been set up for you
 
 **-f newsdata.sql** — run the SQL statements in the file newsdata.sql
 
 Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.
 
 7) To run the database type, ***psql -d news***
 
 8) #### Explore the Data
 
 Once you have the data loaded into your database, connect to your database using **psql -d news** and explore the tables using the **\dt** and **\d table** commands and select statements.

 **\dt** — display tables — lists the tables that are available in the database.
 **\d table** — (replace table with the name of a table) — shows the database schema for that particular table.
 Get a sense for what sort of information is in each column of these tables.

 The database includes three tables:
 
 The ***authors table*** includes information about the authors of articles.
 
 The ***articles table*** includes the articles themselves.
 
 The ***log table*** includes one entry for each time a user has accessed the site.

 9) #### Connecting from your code
 The database that you're working with in this project is running PostgreSQL. So in your code, you'll want to use the ```psycopg2``` Python module to connect to it, for instance:
              ```db = psycopg2.connect("dbname=news")```
 
 10) Run the commands from the **list of views** below to run the python program successfully.
 
 11) Run command ```python newsdatadb_solution.py;``` to get the queries output

              ##List of Views

**-------------------- First Query-------------------**

**1) num_of_views**

create view num_views as 
select title, count(*) as views
from articles, log where substring(log.path,10)=articles.slug 
group by title
order by views desc;

***select * from num_of_views limit 3;***
```
              title               | views
----------------------------------+--------
 Candidate is jerk, alleges rival | 338647
 Bears love berries, alleges bear | 253801
 Bad things gone, say good people | 170098
(3 rows)
```

**----------------Second Query---------------------**

**2) popular_articles** 

create view popular_articles as select author,num_of_views.title,views from ((articles join authors on articles.author = authors.id) join num_of_views on articles.title=num_of_views.title) order by views desc;

*** select * from popular_articles ***

```
 author |               title                | views
--------+------------------------------------+--------
      2 | Candidate is jerk, alleges rival   | 338647
      1 | Bears love berries, alleges bear   | 253801
      3 | Bad things gone, say good people   | 170098
      1 | Goats eat Google's lawn            |  84906
      2 | Trouble for troubled troublemakers |  84810
      4 | Balloon goons doomed               |  84557
      1 | There are a lot of bears           |  84504
      1 | Media obsessed with bears          |  84383
```

**3) popular_authors** 

create view popular_authors as 
select name, author, popular_articles.title, cast(views as int) from popular_articles join authors on authors.id=popular_articles.author 
order by views desc;

***select name, views from popular_authors order by views desc;***

```
          name          | views
------------------------+--------
 Rudolf von Treppenwitz | 338647
 Ursula La Multa        | 253801
 Anonymous Contributor  | 170098
 Ursula La Multa        |  84906
 Rudolf von Treppenwitz |  84810
(5 rows)

```

**----------------------Third Query --------------------**

**4) num_of_errors**

create view num_of_errors as 
select date(time) as date, count(*) as errors 
from log where status='404 NOT FOUND' 
group by date order by date;

***select * from num_of_errors order by errors desc limit 5;**
```
     date    | errors
------------+--------
 2016-07-17 |   1265
 2016-07-19 |    433
 2016-07-24 |    431
 2016-07-05 |    423
 2016-07-06 |    420
(5 rows)
```

**5) num_of_reqs**

create view num_of_reqs as 
select date(time) as date, count(*) as reqs 
from log group by date, order by date;

***select * from num_of_reqs order by reqs desc limit 5;***
```
    date    | reqs
------------+-------
 2016-07-17 | 55907
 2016-07-18 | 55589
 2016-07-19 | 55341
 2016-07-21 | 55241
 2016-07-09 | 55236
(5 rows)
```

**6) percentage**

create view percentage as 
select cast(num_of_reqs.date as text), cast(round((100.0*num_of_errors.errors/num_of_reqs.reqs), 3) as float(2)) as percent from num_of_reqs, num_of_errors where num_of_reqs.date=num_of_errors.date 
order by num_of_reqs.date;

***select * from percentage order by percent desc limit 1;***
```
    date    | percent
------------+---------
 2016-07-17 |   2.263
(1 row)
```

 _ _This project belongs to Deepali Musale. &copy; 2019, [github](https://github.com/DeepaliMusale/log-analysis)_ _
