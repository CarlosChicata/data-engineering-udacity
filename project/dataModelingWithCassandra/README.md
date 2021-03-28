## Project summary
Startup Sparkify have collections of songs and user activities by music streaming app. They want to understand what songs user are listening to. They don't have a easy way to query their data and to need a analitycs database to query and solve those doubts.

This project implements a database schema and use a ETL pipeline to read data from CSV file and store this data in wide column database using python and Apache Cassandra.

## How the project works?
Since the analytics team need a analytics database but the database need to create query first to matching this queries to answer. 
We create schemes to answer those question:
1) Give me the artist, song title and song's length in the music app history that was heard during sessionId = 338, and itemInSession = 4
2) Give me only the following: name of artist, song (sorted by itemInSession) and user (first and last name) for userid = 10, sessionid = 182
3) Give me every user name (first and last) in my music app history who listened to the song 'All Hands Against His Own'

## How do run this project
Upload this jupiter notebook and run each cell in sequential order.
