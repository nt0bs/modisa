#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 23:52:07 2024

@author: Your name
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the movie csv file
df=pd.read_csv("movie_dataset.csv")

# Drop NAN rows in csv file
x = df['Revenue (Millions)'].mean()
y = df['Metascore'].mean()
df['Revenue (Millions)'].fillna(x, inplace = True)
df['Metascore'].fillna(y, inplace = True)



# Columns names
movie_name = df['Title']
genre = df['Genre']
director = df['Director']
actors = df['Actors']
year = df['Year']
rating = df['Rating']
revenue = df['Revenue (Millions)']



# Q1
high_rating = df[df["Rating"] == df["Rating"].max()]
print("Name of the movie with high rating is ", high_rating["Title"])


# Q2
average_revenue = revenue.mean()
print("Average revenue of all movies is", int(average_revenue), "Million")


# Q3
_2015 = df[df['Year'] == 2015]
_2016 = df[df['Year'] == 2016]

rev_2015 = _2015["Revenue (Millions)"].mean()
rev_2016 = _2016["Revenue (Millions)"].mean()

average_rev = round((rev_2015 + rev_2016)/2, 2)

print("Average revenue of movies done from 2015 to 2017", average_rev, "Millions")



# Q4
_2016 = len(df[df["Year"] == 2016])
print("The number of movies released in 2016 is", _2016)

# Q5
chris = df[df['Director'] == "Christopher Nolan"]
print("Number of movies directed by Christopher Nolan is", len(chris))    


# Q6
rating_over_8 = len(df[df["Rating"] > 7.9])     
print("Number of movies with rating at least 80.", rating_over_8)


# Q7
chris = df[df['Director'] == "Christopher Nolan"]
chris_rating = chris["Rating"]
print("Average Christopher Nolan rating is ", round(chris_rating.mean(),2))
 

# Q8

max_rating = df[df["Rating"] == df['Rating'].max()]
max_rat_year = max_rating['Year']
print("The year with maximun rating is", max_rat_year)



# Q9

_2006 = len(df[df['Year'] == 2006])        
perc_in = ((_2016 - _2006)/(_2006))*100
print("Percentage increase from 2006 to 2016 is", int(perc_in), "%")


# Q10



# Q11



# Q12

# copy 1

x = year
y = rating
plt.scatter(x, y)
plt.title('Yearly rating plot')
plt.xlabel('Year')
plt.ylabel('Rating')
plt.savefig("rating.png")
plt.show()

x = year
z = revenue
plt.scatter(x, z)
plt.title('Yearly revenue plot')
plt.xlabel('Year')
plt.ylabel('Revenue [Million]')
plt.savefig("revenue.png")
plt.show()

