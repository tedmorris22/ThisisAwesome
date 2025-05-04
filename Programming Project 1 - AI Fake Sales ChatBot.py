#Theodore Morris, 4/27/25, Programming Project 1: AI Fake "Sales ChatBot"
from functools import total_ordering

#A new marketing company is launching a new product or service for their website and want you to code a prototype Artificial Intelligence (AI) ChatBot for them. Simulate a "sales conversation" with a customer who will be purchasing the product or service from your ChatBot.

#Your code must do the following:
#Greet your customer and introduce the ChatBot.
print("Hello, user! I am Nerd.io, ChatBot at your service!")
#Before starting the "conversation" ask the user if they would like to learn more about a specific product or service. If they say yes, proceed to tell them about your product or service. If they say no, end the conversation and provide a farewell.
#Build this chat conversation around a specific product or service. Provide a paragraph overview of your product or service. Be creative - make some stuff up. Have a fun and engaging "conversation" with your user. Output the overview to the screen with a nice formatting of your choice - for example, break up a long overview into multiple lines. Make this as serious or as silly a scenario as you want it to be. This is an important step to "SELL" the product or service.
userinput = input("Are you interested in learning more about the ShockaTron4000™ Shock Collars we sell? ('yes' or 'no')")
if userinput == "yes":
    print("Great! I will tell you all about our signature line of ShockaTron4000™ Shock Collars.")
    print("- Our shock collars are a world of wonder for those who are obedient and those who are not so much...")
    print("- Whether you're training your pup to heel or exploring who's really top dog, Shockatron4000 Shock Collars™ are here to keep things shocking — in the best way possible.")
    print("- Our ShockaTron4000™ Shock Collars are state-of-the-art premium products that leave competitors to waste.")
    print("- For ONLY $45, you'd be barking up the wrong tree not purchasing due to the price.")
    print("*Warning: Always use responsibly, whether your partner has four legs or two*")
else:
    print("Yeah, I thought a chump like you wouldn't know what to do with one of these babies. You should look for something less powerful so you don't hurt yourself.")
#Ask if the user would be interested in purchasing your product or service. Build this around an if statement. If yes - continue with the sales conversation. If no, provide a closing statement and farewell.
userinput = input("Now, after learning more about the ShockaTron4000™ Shock Collars, are you interested in purchasing one? ('yes' or 'no')")
if userinput == "yes":
    print("Wonderful! Now, let's get you started:")
else:
    print("Go head over to Amazon and buy a cheap Chinese Knockoff, you don't deserve this premium of a product.")
#Closing the Sale
#Ask for the customer's first and last name. Store the values input to separate variables such as firstName and lastName.
firstName = input("I've already added the product into your cart! Now, what is your first name?")
lastName = input("What is your last name?")
#ask for their email address. Store the value input to a variable. Don't worry about validating the format of the input.
emailAddress = input("What is your email address?")
#Ask for their phone number.  Store the value input to a variable. Don't worry about enforcing formatting on the input.
phoneNumber = input("What is your phone number?")
#Ask for how many of the product/service they would like to purchase. Be sure to tell the customer how much the product/service costs BEFORE asking how many they would like to purchase. Store the values input to a variable.
numItems = int(input("How many ShockaTron4000™ Shock Collars would you like to purchase? ($45/ea.)"))
#Calculate and display their current total based on the quantity they would like to purchase. Store the values input to a variable.
totPrice = numItems * 45
print("Cart Total:", totPrice)
#Apply 10% tax for the total bill.
#Calculate the total amount due (the total + tax). Store the values input to a variable. Output the total amount due before proceeding to the next step.
totBill = totPrice * 1.10
#Output a receipt using all of the variables you have input. Be sure to show the total product/service quantity, the cost for each product/service, the subtotal, tax, and total amount due. Format this as nice as you can - use symbols and line breaks to produce a realistic looking receipt.
#In the receipt output, include the customer's name, phone number, and email address.  Format this as nice as you can - use symbols and line breaks to produce a realistic looking receipt.
print("=========================================")
print("Receipt:")
print("=========================================")

print("Name:", firstName, lastName)
print("Email Address:", emailAddress)
print("Phone Number:", phoneNumber)
print("Number of Items:", numItems)
print("Price (Sub-Total):", "$",totPrice)
print("=========================================")
print("Price (Grand Total):", "$",totBill)
#Output a farewell and a thank you to the customer.
print("Thank You,", firstName, ", for choosing to shop with us today! Enjoy your ShockaTron4000™ Shock Collars!")