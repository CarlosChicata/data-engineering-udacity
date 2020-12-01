import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    """
    read a json file and insert in song and artist tables.
    
    Params:
    - cur : db connection instance
    - filepath: path of file
    
    Return:
    None
    """
    # open song file
    df = pd.read_json(filepath, lines=True)

    # insert song record
    # to more study about pandas
    song_data = df.loc[:,['song_id', 
                          'title', 
                          'artist_id', 
                          'year', 
                          'duration']].values[0].tolist()
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    # to more study about pandas
    artist_data = df.loc[:,['artist_id',
                            'artist_name',
                            'artist_location',
                            'artist_latitude',
                            'artist_longitude']].values[0].tolist()
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """
    read a json file and insert in user, time, songplays tables.
    
    Params:
    - cur : db connection instance
    - filepath: path of file contain the entities
    
    Return:
    None
    """
    # open log file
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    df = df[df['page']=='NextSong']

    # convert timestamp column to datetime
    t = pd.to_datetime(df['ts'], unit='ms')
    
    # insert time data records
    # to more study about pandas
    time_data = (df['ts'].tolist(),
                 t.dt.hour.values.tolist(), 
                 t.dt.day.values.tolist(), 
                 t.dt.week.values.tolist(),
                 t.dt.month.values.tolist(), 
                 t.dt.year.values.tolist(), 
                 t.dt.weekday.values.tolist())
    column_labels = ('timestamp', 
                     'hour',
                     'day',
                     'weekOfYear',
                     'month',
                     'year',
                     'weekday')
    time_df = pd.DataFrame(list(time_data), index = list(column_labels)).transpose()

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    # to more study about pandas
    # have more recent status of user.
    # and verification in github
    user_df = df.sort_values(
        by='ts', ascending=False).loc[:,['userId',
                                        'firstName', 
                                        'lastName', 
                                        'gender',
                                        'level']].drop_duplicates('userId')

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = (df.ts[index].item(),
                         int(df.userId[index]), 
                         df.level[index], 
                         songid,
                         artistid, 
                         df.sessionId[index].item(),
                         df.location[index], 
                         df.userAgent[index])
        cur.execute(songplay_table_insert, songplay_data+songplay_data)


def process_data(cur, conn, filepath, func):
    """
    interface method to read and insert entity from file.
    
    Params:
    - cur : db connection instance
    - conn : connection root
    - filepath: path of file contain the entities
    - func : methods to read and insert entities
    
    Return:
    None
    """
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main() 
