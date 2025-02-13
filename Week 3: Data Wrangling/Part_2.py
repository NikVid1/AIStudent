import numpy as np
import pandas as pd

import seaborn as sns
import matplotlib
matplotlib.use('TkAgg') #Had issues with the weyland backend for matplotlib
import matplotlib.pyplot as plt

import duckdb
import os

db_path = "/home/lethal365/AIStudent/Week 3: Data Wrangling/who.db" 

# Connect to the DuckDB database
con = duckdb.connect(db_path)

# -- Query: Showing the different tables in database
df_tables = con.execute("SHOW TABLES").fetchdf()
print(df_tables)

# ======================================================
# TASK 1: UGANDA AND USA COMPARISON OF DEATHRATES
# ======================================================

# -- Query: Getting format for tables
df_population = con.execute("""
    SELECT *
    FROM population
""").fetchdf()

df_copd = con.execute("""
    SELECT *
    FROM copd
""").fetchdf()

df_st_pop = con.execute("""
    SELECT *
    FROM standard_pop
""").fetchdf()

#print(df_population.head())
#print(df_copd.head())
#print(df_st_pop.head())
#print(df_copd.columns)

df_death_rate = con.execute("""
    SELECT age_group, UGA_death_rate, USA_death_rate
    FROM copd 
""").fetchdf()

#print(df_death_rate)

# -- Query: Getting population in 2019 from UGA and USA rows
df_ug_pop = con.execute("""
    SELECT PopTotal
    FROM population 
        WHERE Time = 2019
        AND ISO3_code = 'UGA'
""").fetchdf()

df_us_pop = con.execute("""
    SELECT PopTotal
    FROM population 
        WHERE Time = 2019
        AND ISO3_code = 'USA'
""").fetchdf()

# -- Math: Summing up population for all age groups in USA and UGA
UGA_pop_19 = df_ug_pop.sum() #assuming this is in 1k units so 42 milion checks out with google search
#print(UGA_pop_19)
USA_pop_19 = df_us_pop.sum() #assuming this is in 1k units so 330ish milion checks out with google search
#print(USA_pop_19.iloc)

# -- Math: Calculating total death rate for entire population (all age groups) in units deaths/100k for USA and UGA respectively
tot_deaths_UGA_19 = 0
for i in df_death_rate["UGA_death_rate"]:
    tot_deaths_UGA_19 = (i * UGA_pop_19.iloc[0]) / 100000 + tot_deaths_UGA_19

UGA_deaths_per_100k = (tot_deaths_UGA_19 / UGA_pop_19.iloc[0]) * 100000
print(UGA_deaths_per_100k.round(0))

tot_deaths_USA_19 = 0
for i in df_death_rate["USA_death_rate"]:
    tot_deaths_USA_19 = (i * USA_pop_19.iloc[0]) / 100000 + tot_deaths_USA_19

USA_deaths_per_100k = (tot_deaths_USA_19 / USA_pop_19.iloc[0]) * 100000
print(USA_deaths_per_100k.round(0))

# --- CONCLUSION 1: Similar total rates. Weird? Maybe not. 
# --- CONCLUSION 2: Factors at play could be: Difference in population size, average life length and differences in death rate over years. 


# ======================================================
# TASK 2: NAMIBIA ANALYSIS
# ======================================================

# -- Query: Inspecting dataframe without unnecessary columns
df_nam_cols = con.execute("""
        SELECT * 
        FROM population 
        WHERE ISO3_code = 'NAM'
""").fetchdf()

df_nam_cols.drop(['LocID','Notes','ISO3_code','SDMX_code','LocTypeName','LocTypeID','SortOrder','Location','ParentID','Variant'],axis=1,inplace=True)
print(df_nam_cols)
# -- Observation: Very low population numbers for higher age groups. Age group span -1 on index 7271? Weird formatting or error in data input?
# __ Observation 2: NAN IN ISO2_code

# -- Query: Looking at populations over time for Namibia. 
# --- HYPOTHESIS: Guessing I can extrapolate some historical context from the data. Maybe civil war, occupation by ZAF, epidemics or other
df_nam_pop = con.execute("""
    SELECT DISTINCT ON (Time) Time, PopTotal, PopFemale, PopMale, AgeGrp
    FROM population
    WHERE Time BETWEEN 1950 AND 2021
    AND ISO3_code = 'NAM'
    ORDER BY Time
""").fetchdf()

df_usa_pop = con.execute("""
    SELECT DISTINCT ON (Time) Time, PopTotal, PopFemale, PopMale, AgeGrp
    FROM population
    WHERE Time BETWEEN 1950 AND 2021
    AND ISO3_code = 'USA'
    ORDER BY Time
""").fetchdf()

print(df_nam_pop.to_string(index=False))  
# --- CONCLUSION 1: Note a slight drop in population during the 90s most likely due to AIDS/HIV epidemic


#Population growth per year from 1950 to 1990
pop_1950 = df_nam_pop[df_nam_pop["Time"] == 1950]["PopTotal"].values[0]
pop_1990 = df_nam_pop[df_nam_pop["Time"] == 1990]["PopTotal"].values[0]

avg_growth_pop = (pop_1990-pop_1950)/(1990-1950)
print(avg_growth_pop)

#Population growth per year during 90s 
pop_2000 = df_nam_pop[df_nam_pop["Time"] == 2000]["PopTotal"].values[0]

avg_growth_pop_aids = (pop_2000-pop_1990)/(2000-1990)
print(avg_growth_pop_aids)

# --- CONCLUSION: Population growth much lower during 90s than previous period of time. 0.8 vs 0.4 growth in population. Most likely due to AIDS epidemic