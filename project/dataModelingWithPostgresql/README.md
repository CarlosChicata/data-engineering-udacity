## Project summary
Startup Sparkify have collections of songs and user activities by music streaming app. They want to understand what songs user are listening to. They don't have a easy way to query their data and to need a analitycs database to query and solve those doubts.

This project implements a database schema and use a ETL pipeline to read and store data from file in postgresql data base using python and pycopg2.

## How the project works?
Since the analytics team need a analytics database, the project implements a star schema in database with songplay table as fact table and their dimension table: song, time, user and artist tables.

this project contain those files to work:

**sql_table.py**: define a SQL to build, insert and query in tables: song, artist, time, user and songplay. this is a core of other files.

**create_table.py**: implement a process to drop old table and create new table in database. Use it to restart project.

**etl.py**: define a ETL to process the JSON files to read and insert in tables: song, artist, time, user and songplay.

**etl.ipynb**: implements a etl file to test methods in etl script.

**test.ipynb**: contain SQL query to test contents in all table after the ETL has been performed.

## How to use those files?
you will use a terminal to run those followed steps.

1. run in terminal this command to restar project.
```
python create_table.py
```
2. run in terminal this command to read and store data from collections by ETL.
```
python etl.py
```
3. open the test.ipynb and run all cell to test the content in database.

 
