# #Exercise 3-1: Enhance the Miles Per Gallon program
# print("The Miles Per Gallon program\n")
#
# # Create a loop to get user input for multiple trips
# while True:
#     # Get miles driven from the user
#     miles_driven = float(input("Enter miles driven: "))
#
#     # Get gallons of gas used from the user
#     gallons_used = float(input("Enter gallons of gas used: "))
#
#     # Get cost per gallon from the user
#     cost_per_gallon = float(input("Enter cost per gallon: "))
#
#     # Calculate the miles per gallon
#     print(f"Miles Per Gallon:", miles_driven/gallons_used)
#     milesGallon = miles_driven / gallons_used
# # Calculate the total gas cost
#     print(f"Total Gas Cost:", (gallons_used*cost_per_gallon))
#     totGas = gallons_used * cost_per_gallon
# #Calculate the cost per mile
#     costMile = cost_per_gallon/milesGallon
# # Print the result
#     print(f"Cost Per Mile:", (cost_per_gallon/milesGallon))
#     # Ask the user if they want to enter another trip
#     another_trip = input("\nGet entries for another trip (y/n)? ")
#     if another_trip.lower() != "y":
#         break
# Exercise 3-2: Enhance the Test Scores program
#enhance the Test Scores program so it lets the user input multiple sets of scores. To do that, use a nested while loop.
#Modify the program so that when the user enters "end" it ends the set of score entries and outputs the Total and Average Score for the set that was just finished.
# Then ask if there is another set of test scores to enter. Be sure to keep the validation for the number input to be between 0 and 100.

print("The Test Scores program\n")
print("Enter test scores")
print("Enter 'end' to end input")
print("===============================")

# Outer loop to manage multiple sets of scores
while True:
    total_score = 0
    count = 0

    # Inner loop to input scores for a single set
    while True:
        score_input = input("Enter test score: ")

        # Check if input is "end"
        if score_input.lower() == "end":
            # end the set of score entries and outputs the Total and Average Score for the set that was just finished.
            print(f"Your Total:", )
            print(f"Avg. Score:",)
            break
        # ---- Your code here ----------
        int(score_input)
    #     # Validate the input score
    #     if 0 <= score_input <= 100:
    #         #code here
    #     else:
    #             # ---- Your code here ----------
    #             # Calculate the average score
    #             # ---- Your code here ----------
    #
    # # Ask the user if they want to enter another set of scores
    # another_set = input("Enter another set of test scores (y/n)? ")
    # if another_set.lower() != "y":
    #     break
    # else:
    #     print("\nEnter test scores")
    #     print("Enter 'end' to end input")
    #     print("===============================")