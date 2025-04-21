#!/usr/bin/env python3
from idlelib.debugobj_r import WrappedObjectTreeItem

# display a welcome message
print("The Area and Perimeter Program")
print()
print("Enter the Length and Width")
print("======================")

# get inputs from the user
Length      = int(input("Enter Length: "))
Width      = int(input("Enter Width: "))

# Calculate Area by multiplying input for Length by input for Width
Area = round(Length * Width)

# calculate Perimeter by combining 2 Length inputs and 2 Width Inputs from user
Perimeter = (Length + Length + Width + Width)

# format and display the result
print("======================")

#inlcude "Your Length and Width:" text to user
print("Your Length and Width:", Length, "and", Width)
print("Area:  ", Area,
      "\nPerimeter:", Perimeter)

#print thank you message
print("Thanks for using this program!")


