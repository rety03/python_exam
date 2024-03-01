bday = input("When is your birthday (DD-MM-YYYY)? ")
year = bday[-4:]
#slice the strong

try:
    year = int(year)
    birth_year = 2023-year
    print("You are ",birth_year*365, "days old.")
#to get days in whole yers multiply by 365
except ValueError:
    print("Please enter a date")
except:
    print("Some other error I did not foresee")
else:
    print("No exceptions were raised")
finally:
    print("Thank you for the input")

