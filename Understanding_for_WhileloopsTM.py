# #Gurveer Atwall,Theodore Morris, Sherreen Fan
# # In-Class Assignment - Understanding for and while Loops in Python
#
# # Part 1 -- for loops
# #Task 1: Print Numbers Using for Loop
# range(1,11)
# for i in range(1,11):
#     print(i)
# # Task 2  Sum of first n numbers
# #Write a program that asks the user for a number n and calculates the sum of numbers from 1 to n using a for loop.
# tot=0
# #n=user's input #
# n=(int(input("Give me a number.")))
# #sum of numbers from 1-n
# for i in range (1, n+1):
#     tot+=i
# print("The sum of numbers from 1 to", n, "is", tot)
#
#
# #Task 3: Multiplication Table Using for Loop
# # Write a program that prints the multiplication table of a number entered by the user.
# #ask for # from user
# n=(int(input("Give me a number:")))
# print("Enter A Number:", f"{n}")
# for i in range (0,10):
#     print(f"{n} * {i} = {n * i}")
# #Part 2: while Loops
# Task 4: Print Numbers Using while Loop
# Write a program that prints numbers from 1 to 10 using a while loop.
#enter initial value
startNum = 1
#enter while statement, set max # 10
while startNum <= 10:
#print values
    print(startNum)
#add initial + 1 until reach 10
    startNum += 1
# Task 5: Ask for User Input Until -1 is Entered
# Write a program that repeatedly asks the user to enter a number until they enter -1. After each input, add all the numbers together and print the result.

while True:
    # ask for user input
    n = int(input("Enter a number (-1 to stop):"))
    if n == -1:
        print("Loop Ended.")
        break
    else:
        print("Result is:", n)
#
# Task 6: Guess the Number Game (while Loop)
# Write a simple game where the user has to guess a secret number (e.g., 7).(Hint: make up the secret number)
# If they guess incorrectly, the program keeps asking them.
# If they guess correctly, the program congratulates them and ends.
secretNumber = 7
while True:
    # ask user to guess secret #
    n = int(input("Guess the secret number!"))
    if n == 7:
        print("You got it correct! Let's go to Vegas!")
        break
    else:
        print("Incorrect. Try again:")