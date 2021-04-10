# Oyetunde Oyewo
# 1881782

import csv
from dateutil.parser import parse
import datetime

inventory = {}

# Part A

# to incorporate the ManufacturerList file
with open("ManufacturerList.csv", 'r') as man_file:  # to open manufacturerList file
    lines = csv.reader(man_file, delimiter=',')
    #  to input ManufacturerList content into dictionary
    for rows in lines:
        inventory[rows[0]] = []
        for col in rows[1:]:  # Skips ID in first Column
            inventory[rows[0]].append(col)
        # print(inventory[rows[0]])

# to incorporate PriceList file
with open("PriceList.csv", 'r') as price_file:  # to open PriceList file
    lines = csv.reader(price_file, delimiter=',')
    # to input content into dict
    for rows in lines:
        for col in rows[1:]:  # Skips ID in First Column
            inventory[rows[0]].insert(2, col)  # puts price in proper column

# to incorporate ServiceDateList file
with open("ServiceDatesList.csv", 'r') as date_file:  # to open and read
    lines = csv.reader(date_file, delimiter=',')  # ServiceDatesList file
    # to input content into dict
    for rows in lines:
        for col in rows[1:]:  # skips ID in the first column
            inventory[rows[0]].insert(3, col)  # replace w/o taking away initial element at index

sorted_manufacturer = sorted(inventory.items(), key=lambda x: x[1])  # sort the dictionary based on elements
full_inventory = open('FullInventory.csv', 'w')  # at index 1
for line in sorted_manufacturer:
    full_inventory.write(str(line[0]))
    full_inventory.write(',')
    full_inventory.write(str(line[1][0]))
    full_inventory.write(',')
    full_inventory.write(str(line[1][1]))
    full_inventory.write(',')
    full_inventory.write(str(line[1][2]))
    full_inventory.write(',')
    full_inventory.write(str(line[1][3]))
    full_inventory.write(',')
    full_inventory.write(str(line[1][4]))
    full_inventory.write('\n')
full_inventory.close()

# Part B

sorted_ID = sorted(inventory.items(), key=lambda x: x[0])  # sort by the items ID

laptop_inventory = open('LaptopInventory.csv', 'w')
phone_inventory = open('PhoneInventory.csv', 'w')
tower_inventory = open('TowerInventory.csv', 'w')

for line in sorted_ID:
    if str(line[1][1]).lower() == 'laptop':
        laptop_inventory.write(str(line[0]))
        laptop_inventory.write(',')
        laptop_inventory.write(str(line[1][0]))
        laptop_inventory.write(',')
        laptop_inventory.write(str(line[1][2]))
        laptop_inventory.write(',')
        laptop_inventory.write(str(line[1][3]))
        laptop_inventory.write(',')
        laptop_inventory.write(str(line[1][4]))
        laptop_inventory.write('\n')
    elif str(line[1][1]).lower() == 'phone':
        phone_inventory.write(str(line[0]))
        phone_inventory.write(',')
        phone_inventory.write(str(line[1][0]))
        phone_inventory.write(',')
        phone_inventory.write(str(line[1][2]))
        phone_inventory.write(',')
        phone_inventory.write(str(line[1][3]))
        phone_inventory.write(',')
        phone_inventory.write(str(line[1][4]))
        phone_inventory.write('\n')
    elif str(line[1][1]).lower() == 'tower':
        tower_inventory.write(str(line[0]))
        tower_inventory.write(',')
        tower_inventory.write(str(line[1][0]))
        tower_inventory.write(',')
        tower_inventory.write(str(line[1][2]))
        tower_inventory.write(',')
        tower_inventory.write(str(line[1][3]))
        tower_inventory.write(',')
        tower_inventory.write(str(line[1][4]))
        tower_inventory.write('\n')
    else:
        print("Why did you not tell us about this?")

phone_inventory.close()
laptop_inventory.close()
tower_inventory.close()

# Part C
today = datetime.datetime.now()  # get the current date and time

sorted_past = sorted(inventory.items(), key=lambda x: parse(x[1][3]))
# sorts the dictionary based on the date using the parse to ensure they are in proper format

past_date_inventory = open('PastServiceDateInventory.csv', 'w')
for line in sorted_past:
    date_split = line[1][3].split('/')  # make a list of date sep into month,day,year (year=2 , month=0, day=1)
    format_date = str(date_split[1]) + '/' + date_split[0] + '/' + date_split[2]  # puts date in format datetime() uses
    compare_date = datetime.datetime.strptime(format_date, "%d/%m/%Y")  # puts date into the imported datetime()
    if compare_date < today:  # compares the dates using the same format so there's no error
        past_date_inventory.write(str(line[0]))
        past_date_inventory.write(',')
        past_date_inventory.write(str(line[1][0]))
        past_date_inventory.write(',')
        past_date_inventory.write(str(line[1][1]))
        past_date_inventory.write(',')
        past_date_inventory.write(str(line[1][2]))
        past_date_inventory.write(',')
        past_date_inventory.write(str(line[1][3]))
        past_date_inventory.write(',')
        past_date_inventory.write(str(line[1][4]))
        past_date_inventory.write('\n')

past_date_inventory.close()

# Part D

sorted_damaged = sorted(inventory.items(), key=lambda x: parse(x[1][2]), reverse=True)
# sort based on price from most expensive to least expensive

damaged_inventory = open('DamagedInventory.csv', 'w')
for line in sorted_damaged:
    if str(line[1][4]).lower() == 'damaged':
        damaged_inventory.write(str(line[0]))
        damaged_inventory.write(',')
        damaged_inventory.write(str(line[1][0]))
        damaged_inventory.write(',')
        damaged_inventory.write(str(line[1][1]))
        damaged_inventory.write(',')
        damaged_inventory.write(str(line[1][2]))
        damaged_inventory.write(',')
        damaged_inventory.write(str(line[1][3]))
        damaged_inventory.write('\n')

damaged_inventory.close()

