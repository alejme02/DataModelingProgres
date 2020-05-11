#DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""

CREATE TABLE songplays(
    songplay_id SERIAL NOT NULL, 
    start_time timestamp, 
    user_id varchar,
    song_id varchar, 
    artist_id varchar,
    session_id int, 
    level varchar, 
    location varchar, 
    user_agent varchar, 
    PRIMARY KEY(songplay_id));

""")

songplayfull_table_create = ("""

CREATE TABLE songplaysfull(
    songplay_id SERIAL NOT NULL, 
    start_time timestamp, 
    user_id varchar,
    song_id varchar, 
    artist_id varchar,
    session_id varchar, 
    level varchar, 
    location varchar, 
    user_agent varchar, 
    PRIMARY KEY(songplay_id),
    FOREIGN KEY(user_id) REFERENCES users(user_id),
    FOREIGN KEY(song_id) REFERENCES songs(song_id),
    FOREIGN KEY(artist_id) REFERENCES artists(artist_id));

""")

user_table_create = ("""

CREATE TABLE users(
    user_id varchar NOT NULL, 
    first_name varchar, 
    last_name varchar,
    gender char, 
    level varchar, 
    PRIMARY KEY(user_id));
""")

song_table_create = ("""

CREATE TABLE songs(
    song_id varchar NOT NULL, 
    title varchar, 
    artist_id varchar, 
    year int, 
    duration decimal,
    PRIMARY KEY(song_id));

""")

artist_table_create = ("""

CREATE TABLE artists(
    artist_id varchar NOT NULL, 
    name varchar, 
    location varchar,
    latitude varchar, 
    longitude varchar, 
    PRIMARY KEY(artist_id));

""")

time_table_create = ("""

CREATE TABLE time(
    start_time timestamp NOT NULL, 
    hour int, 
    day int, 
    week int,
    month int, 
    year int, 
    weekday int, 
    PRIMARY KEY(start_time));

""")


# INSERT RECORDS

songplay_table_insert = ("""

INSERT INTO songplays(start_time, user_id, song_id, artist_id, session_id, level, location, user_agent)
    VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
    ON CONFLICT DO NOTHING;
    
""")

user_table_insert = (

"""
INSERT INTO users(user_id, first_name, last_name, gender, level)
    VALUES(%s,%s,%s,%s,%s)
    ON CONFLICT DO NOTHING;
    
""")

song_table_insert = ("""

INSERT INTO songs(song_id, title, artist_id, year, duration) 
    VALUES (%s,%s,%s,%s,%s)
    ON CONFLICT DO NOTHING;
    
""")

artist_table_insert = ("""

INSERT INTO artists(artist_id, name, location, latitude, longitude) 
    VALUES(%s,%s,%s,%s,%s)
     ON CONFLICT DO NOTHING;

""")

time_table_insert = ("""

INSERT INTO time(start_time, hour, day, week, month, year, weekday)
    VALUES(%s,%s,%s,%s,%s,%s,%s)
    ON CONFLICT DO NOTHING;
""")

# FIND SONGS
song_select = ("""SELECT a.artist_id, s.song_id FROM songs s JOIN artists a ON s.artist_id = a.artist_id 
WHERE s.title = %s AND a.name = %s AND s.duration = %s""")

# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create, songplay_table_create]

drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]