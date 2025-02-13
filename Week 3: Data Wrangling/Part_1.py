import numpy as np
import pandas as pd
import seaborn as sns

import matplotlib
matplotlib.use('TkAgg') #Had issues with the weyland backend for matplotlib
import matplotlib.pyplot as plt

import duckdb

# Connecting to the DuckDB database
con = duckdb.connect('/home/lethal365/AIStudent/Week 3: Data Wrangling/BingeBlitz.db')

"""
# Listing all tables
tables = con.execute("SHOW TABLES").fetchdf()
print("Tables in BingeBlitz:", tables)
"""

df_stream = con.execute("""
    SELECT title_id, bandwidth 
    FROM streaming_data 
    LIMIT 20
    """).fetchdf()
#print(df_stream.head())


    ### MAX BANDWIDTH TITLE ###

max_band_title_2 = con.execute("""
    WITH MaxBandwidth AS (
    SELECT title_id, bandwidth
    FROM streaming_data
    WHERE bandwidth = (SELECT MAX(bandwidth) FROM streaming_data)
    )
    SELECT t.title, m.title_id, m.bandwidth
    FROM MaxBandwidth m
    JOIN title_data t ON m.title_id = t.title_id;
""").fetchdf()


print(f"The movie with most bandwidth is {max_band_title_2.iloc[0,0]}")

#print(f"The title of the film with highest bandwith globally is '{max_band_title}' with a bandwidth of {max_band} \n")


    ### PEAK USAGE TIME PER REGION ###

"""
regions = con.execute("SELECT DISTINCT region FROM streaming_data").fetchdf()
print(regions)
"""

df_peak_bandwidth = con.execute("""
    SELECT s1.region, s1.time_measured, s1.bandwidth
    FROM streaming_data s1
    WHERE s1.bandwidth = (
        SELECT MAX(s2.bandwidth)
        FROM streaming_data s2
        WHERE s1.region = s2.region
    )
    ORDER BY region ASC
    """).fetchdf()

print(f"{df_peak_bandwidth} \n")
#THIS IS A WEIRD FUCKING OUTPUT BUT IT IS OK MAYBE. CHECK IF DATABASE IS FOR ONE DAY IN 2021 ONlY ALSO WEIRD UK HAS 3 PEAKS
#IDK BRO EVERYONE WAS BORED ON THE FIRST OF JANUARY AND WANTED TO WATCH FUCKING SURFS UP I GUESS?


    ### MOST COMMON RESOLUTION AND DEVICES ###

df_most_common_resolution = con.execute("""
    SELECT resolution
    FROM streaming_data
    WHERE resolution IN (
        SELECT resolution
        FROM streaming_data
        GROUP BY resolution
        ORDER BY COUNT(*) DESC
        LIMIT 1
    )
    LIMIT 1
""").fetchdf().iloc[0,0]

print(f"most common resolution is: {df_most_common_resolution}")


df_most_common_device = con.execute("""
    SELECT device
    FROM streaming_data
    WHERE device IN (
        SELECT device
        FROM streaming_data
        GROUP BY device
        ORDER BY COUNT(*) DESC
        LIMIT 1
    )
    LIMIT 1
""").fetchdf().iloc[0,0]

print(f"most common device is {df_most_common_device}")


    ### TASK 2 JOINS

"""
genres = con.execute("SELECT DISTINCT genre from title_data").fetchdf()

print(genres)
"""

df_genre_views = con.execute("""
    WITH TopGenres AS (
        SELECT t.genre, v.time_day, SUM(v.viewership) AS total_views
        FROM title_data t
        INNER JOIN viewership_data v ON t.title_id = v.title_id
        GROUP BY t.genre, v.time_day
        ORDER BY total_views DESC
        LIMIT 5
    )
    SELECT * FROM TopGenres;
""").fetchdf()

print(df_genre_views)
# WEIRD NA OUTPUT CHECK IF QURYING RIGHT

"""
dates = con.execute("SELECT DISTINCT time_day from viewership_data").fetchdf()

print(dates)
""" #DATA SEEMS TO ONLY BE FOR JANUARY 2021


    ### TASK 3 WINDOW FUNCTIONS

df_fastest_growth = con.execute("""
    SELECT title_id, viewership, time_day,
                                FROM viewership_data
                                LIMIT 10

""").fetchdf()

print(df_fastest_growth)

con.close()