# Average Liveliness with Energy Criteria:
#
# Find the average value of liveliness for tracks where energy is greater than 0.5.
import csv

from analyze_spotify import genre, GENRES

rows = []

with open('top_50_2023.csv', 'r') as top_file:
    csv_reader = csv.reader(top_file, delimiter=',')
    header = next(csv_reader)
    for row in csv_reader:
        rows.append(row)
print(rows)
ENERGY = header.index('energy')
LIVELINESS = header.index('liveness')
liveliness_counter = 0
counter_energy = 0
for row in rows:
    if float(row[ENERGY]) >= 0.5:
        liveliness_counter += float(row[LIVELINESS])
        counter_energy += 1
print(f'Average: {liveliness_counter/counter_energy}')

#The most popular artist:

#Identify artists whose tracks appear the most in the list.

NAME = 0
name_dict = {}
for row in rows:
    if row[NAME] in name_dict:
        name_dict[row[NAME]] += 1
    else:
        name_dict[row[NAME]] = 1
top_artist = sorted(name_dict.items(), key = lambda x: x[1], reverse=True)
print(top_artist)

# The most popular year
#
# Find the year when the most songs were released

YEAR = header.index('album_release_date')
year_dict = {}
for row in rows:
    if row[YEAR][:4] in year_dict:
        year_dict[row[YEAR][:4]] += 1
    else:
        year_dict[row[YEAR][:4]] = 1
top_year = sorted(year_dict.items(), key = lambda x: x[1], reverse=True)
print(top_year)



