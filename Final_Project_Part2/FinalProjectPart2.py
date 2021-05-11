# Oyetunde Oyewo
# 1881782

import csv
from dateutil.parser import parse
import datetime

inventory = {}
# to incorporate the ManufacturerList file
with open("ManufacturerList.csv", 'r') as man_file:  # to open manufacturerList file
    lines = csv.reader(man_file, delimiter=',')
    #  to input ManufacturerList content into dictionary
    for rows in lines:
        inventory[rows[0]] = []
        for col in rows[1:]:  # Skips ID in first Column and checks from 1
            inventory[rows[0]].append(col)
        # print(inventory[rows[0]])

# to incorporate PriceList file
with open("PriceList.csv", 'r') as price_file:  # to open PriceList file
    lines = csv.reader(price_file, delimiter=',')
    # to input content into dict
    for rows in lines:
        for col in rows[1:]:  # Skips ID in First Column and checks from 1
            inventory[rows[0]].insert(2, col)  # puts price in proper column

# to incorporate ServiceDateList file
with open("ServiceDatesList.csv", 'r') as date_file:  # to open and read
    lines = csv.reader(date_file, delimiter=',')  # ServiceDatesList file
    # to input content into dict
    for rows in lines:
        for col in rows[1:]:  # skips ID in the first column and checks from 1
            inventory[rows[0]].insert(3, col)  # replace w/o taking away initial element at index

# this is to see what the full inventory is
sorted_manufacturer = sorted(inventory.items(), key=lambda x: x[1])  # sort the dictionary based on manufacturer name
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

# to create item type inventories with different manufacturers to pick from
sorted_ID = sorted(inventory.items(), key=lambda x: x[1][2])  # sort by the items price from least to most expensive
laptop_inventory = open('LaptopInventory.csv', 'w')
phone_inventory = open('PhoneInventory.csv', 'w')
tower_inventory = open('TowerInventory.csv', 'w')

for line in sorted_ID:
    if (str(line[1][1]).strip()).lower() == 'laptop':
        laptop_inventory.write(str(line[0]))
        laptop_inventory.write(',')
        laptop_inventory.write(str(line[1][0]))
        laptop_inventory.write(',')
        laptop_inventory.write(str(line[1][1]))
        laptop_inventory.write(',')
        laptop_inventory.write(str(line[1][2]))
        laptop_inventory.write(',')
        laptop_inventory.write(str(line[1][3]))
        laptop_inventory.write(',')
        laptop_inventory.write(str(line[1][4]))
        laptop_inventory.write('\n')
    elif (str(line[1][1]).strip()).lower() == 'phone':
        phone_inventory.write(str(line[0]))
        phone_inventory.write(',')
        phone_inventory.write(str(line[1][0]))
        phone_inventory.write(',')
        phone_inventory.write(str(line[1][1]))
        phone_inventory.write(',')
        phone_inventory.write(str(line[1][2]))
        phone_inventory.write(',')
        phone_inventory.write(str(line[1][3]))
        phone_inventory.write(',')
        phone_inventory.write(str(line[1][4]))
        phone_inventory.write('\n')
    elif (str(line[1][1]).strip()).lower() == 'tower':
        tower_inventory.write(str(line[0]))
        tower_inventory.write(',')
        tower_inventory.write(str(line[1][0]))
        tower_inventory.write(',')
        tower_inventory.write(str(line[1][1]))
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

today = datetime.datetime.now()  # get the current date and time

query = str(input("What is the manufacturer and item type you want to see? \n"))
query_list = query.split(' ')

sorted_inventory = sorted(inventory.items(), key=lambda x: parse(x[1][2]), reverse=True)
# sort based on price from most expensive to least expensive
# in the script only the 1st item is printed
# and this ensure that the most expensive item comes first


while query != 'q':
    manufacturer_count = 0
    item_type_count = 0
    lowercase_query_list = [i.lower() for i in query_list]
    temporary_word_list = []

    # to first identify the number of manufacturers and item types the user input
    for item in sorted_inventory:
        for words in lowercase_query_list:
            # checks if any of the words is a manufacturer name in the inventory
            if ((item[1][0].strip()).lower() == (words.strip()).lower()) and (
                    (words.strip()).lower() not in temporary_word_list):  # ensures one word isn't counted >1 time
                manufacturer_count += lowercase_query_list.count((item[1][0].strip()).lower())
                temporary_word_list.append(words)
            # checks if any of the words is a item type in the inventory
            if ((item[1][1].strip()).lower() == (words.strip()).lower()) and (
                    (words.strip()).lower() not in temporary_word_list):
                item_type_count += lowercase_query_list.count((item[1][1].strip()).lower())
                temporary_word_list.append(words)

    #  to search for the item in the inventory
    for item in sorted_inventory:
        date_split = item[1][3].split('/')  # make a list of date sep into month,day,year (year=2 , month=0, day=1)
        format_date = str(date_split[1]) + '/' + date_split[0] + '/' + date_split[2]
        # puts date in format datetime() uses
        compare_date = datetime.datetime.strptime(format_date, "%d/%m/%Y")  # puts date into the imported datetime()

        #  to check if the user only input 1 manufacturer name and 1 item type
        if (manufacturer_count == 1) and (item_type_count == 1):
            # to ensure no repetition of item type and have the code run at the appropriate time
            if lowercase_query_list.count((item[1][1].strip()).lower()) == 1:
                # to ensure no repetition of manufacturer and have the code run at the appropriate time
                if lowercase_query_list.count((item[1][0].strip()).lower()) == 1:
                    # to ensure item is not past its service date
                    if compare_date >= today:  # compares the dates using the same format so there's no error
                        # to ensure item is not damaged
                        if str(item[1][4]).lower() != 'damaged':
                            print("Your item is: {item_id} {manufacturer_name} {item_type} ${item_price}"
                                  .format(item_id=item[0], manufacturer_name=item[1][0],
                                          item_type=item[1][1], item_price=item[1][2]))

                            # to give the customer an additional item to choose from within a $50 price range
                            # from another manufacturer (prioritizes giving less expensive options).

                            # This opens the cvs file of the item type in read format
                            with open((item[1][1].strip()).capitalize() + "Inventory.csv", 'r') as type_file:
                                lines = csv.reader(type_file, delimiter=',')
                                for rows in lines:
                                    # to put the date for the second item in proper format
                                    date_split2 = rows[4].split('/')
                                    format_date2 = str(date_split[1]) + '/' + date_split[0] + '/' + date_split[2]
                                    compare_date2 = datetime.datetime.strptime(format_date, "%d/%m/%Y")
                                    # check if the prices are close (<= 50)
                                    if abs(int(item[1][2]) - int(rows[3])) <= 50:
                                        # ensures that it is not by the same manufacturer
                                        if (item[1][0].strip()).lower() != (rows[1].strip()).lower():
                                            # checks if second option is past its service date or damaged
                                            if (compare_date2 > today) and (str(rows[5]).lower() != 'damaged'):
                                                print("You may, also, consider: {item_id} {manufacturer} {item_type} "
                                                      "${item_price}".format(item_id=rows[0], manufacturer=rows[1],
                                                                             item_type=rows[2], item_price=rows[3]))
                                                break  # to break the for-loop for the second item

                            break  # to break the for_loop for the first item
                        # if there's an item with same manufacturer name, item type,good service date, but its damaged
                        elif item == sorted_inventory[len(sorted_inventory)-1]:
                            print("No such item in inventory")
                            break
                    # if there's an item with same manufacturer name, item type, but bad service date
                    elif item == sorted_inventory[len(sorted_inventory)-1]:
                        print("No such item in inventory")
                        break
                # if there's an item with 1 item type, but greater than or less than 1 manufacturer name
                elif item == sorted_inventory[len(sorted_inventory)-1]:
                    print("No such item in inventory")
                    break
            # if user's input has greater than or less than 1 item type
            elif item == sorted_inventory[len(sorted_inventory)-1]:
                print("No such item in inventory")
                break
        else:
            # if (manufacturer_count and item_type_count > 1) or (manufacturer_count and item_type_count < 1):
            print("No such item in inventory")
            break  # to break the 1st for-loop if the first item when the item isn't found

    print()
    query = input("What is  the manufacturer and item type you want to see? \n")
    query_list = query.split(' ')
