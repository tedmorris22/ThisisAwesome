
#ask for user input (give me a year)
print("Enter a year")
#store user input as year variable
year = int(input())
#Check if the year is a leap year:
if(year/4==0) and (year/100 !=0 and year/400==0):
    print("It is a leap year!")
else:
    print("It is not a leap year.")

# ask for user's input of their birth year
print("Enter your birth year:")
#store user input as birth year variable
birthYear = int(input())
age = 2025-birthYear
print("You are", age,"Years old.")
if age <= 12:
    print("You are a child!")
elif age >=13 and age <=19:
    print("You are a teenager!")

elif age >=20 and age <=64:
    print("You are an adult!")

elif age >=65:
    print("You are a senior!")

