# Oyetunde Oyewo
# 1881782

print("Birthday Calculator")
print("Current Day")
current_month = int(input("Enter Current Month: "))
current_day = int(input("Enter Current Day: "))
current_year = int(input("Enter Current Year: "))
print("The current day is", current_month, "/", current_day, "/", current_year)
print("Birthday")
birth_month = int(input("Enter Birthday Month: "))
birth_day = int(input("Enter Birthday Day: "))
birth_year = int(input("Enter Birthday Year: "))
print("Your birthday is on", birth_month, "/", birth_day, "/", birth_year)

#  to fix cases of birthday = 2/10/2001 and current day = 2/9/2021
if current_month >= birth_month:
    if current_day >= birth_day:
        print("You are", current_year - birth_year, "years old")
    else:
        print("You are", current_year - birth_year - 1, "years old")
if current_month == birth_month:
    if current_day == birth_day:
        print("Happy Birthday!")
