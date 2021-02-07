# Introduction
A music streaming startup named Sparkify has gronw their user base and song database and want to move their proccess and data onto the cloud. 

Their data in S3 in format JSON, contain all logs of user activity on the app, and other directory with JSON metadata on the songs.

The Task is to build an ETL Pipeline to extract their data from S3, staging it in Redshift and then transforming data into a set of Dimensional and Fact Tables for ther analytics team of startup to continue finding insights to whats songs their users are listening.


## Schema for Song Play Analysis

A Star Schema would be required for optimized queries on song play queries


## Fact Table

+ **songplays** - records in event data associated with song plays i.e. records with page ```NextSong```
songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent


## Dimension Tables

+ **users** - users in the app
user_id, first_name, last_name, gender, level

+ **songs** - songs in music database
song_id, title, artist_id, year, duration

+ **artists** - artists in music database
artist_id, name, location, lattitude, longitude

+ **time** - timestamps of records in songplays broken down into specific units
start_time, hour, day, week, month, year, weekday


## Project Structure
+ ```create_tables.py``` - This script will drop old tables (if exist) and create new tables.
+ ```etl.py``` - This script executes the queries that extract ```JSON``` data from the ```S3 bucket``` and ingest them to ```Redshift```.
+ ```sql_queries.py``` - This file contains variables with SQL statement in String formats, partitioned by ```CREATE```, ```DROP```, `COPY` and ```INSERT``` statement.
+ ```dhw.cfg``` - Configuration file used that contains info about ```Redshift```, ```IAM``` and ```S3```.


## How to Run
+ Delete previous tables and create new tables by running ```python create_table.py```.
+ Extract data and transform using ETL process by running ```python etl.py```.