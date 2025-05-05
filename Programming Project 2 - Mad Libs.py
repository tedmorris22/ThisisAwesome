#Output a title for the game.
print("Hello, and welcome to my Learning to Fly Mad Libs Game!")
# Ask if the user would like to play a game.
while True:
    answer = input("Would you like to play? (y/n)")
    print()
    if answer == "y":
        print("Great! Let's begin.")
        break
    elif answer == "n":
        print("Goodbye!")
        exit()
# Ask for the players name. Greet the player.
print()
name = input("What is your name?")
print()
# Ask the player to choose from TWO story ideas you have created.
#Use an if statement here to separate the code for each choice.
print(f"Hello, {name}! Which story line would you like to play with? (a/b)")
print("a. Fly like an Eagle")
print("b. Pigs have Wings")
while True:
    userChoice = input()
    if userChoice == "a":
        # Ask the player to input between 6 to 10 names/words/numbers to fill in spots for your story. Please do not go over 10 inputs because it can get very long to run/test the programs!
        print("Now, let me get some information from you to make this a fun story.")
        print()
        food = input("What is a food you despise?")
        print()
        number = input("Give me a number from 5 to 10?")
        print()
        nameCeleb = input("What is the name of a movie character you admire?")
        print()
        adj = input("Give me an adjective:")
        print()
        verb = input("Give me a verb ending in -ing:")
        print()
        seaCreature = input("Give me a type of Sea Creature:")
        print()
        liquid = input("Give me a type of liquid:")
        print()
        noun = input("Give me a noun")
        # Create a short story to go along with the gameplay, substituting their inputted words into the story. Each story should be different and ask for different inputs. Do not reuse the same inputs for each story please. Your stories should be at a minimum of 4 sentences.
        print(f"{name}, here is your story:")
        print(f"One day, a group of overly ambitious {noun}s decided it was time to 'fly like an eagle', just like the Steve Miller Band {verb}ed about in their legendary {noun}.")
        print(f"Armed only with {food}s and an unsettling amount of {liquid}, they leapt from the nearest {noun}, fapping wildly as 'time kept on slippin', slippin', slippin' into the future.")
        print(f"After about {number} seconds of majestic plummeting, they realized they were less eagle and more sad {seaCreature}.")
        print(f"As they lay in a pile of {liquid} and broken dreams, one brave soul whispered, 'Next time... hang glider...'")
        break
    elif userChoice == "b":
        print("Now, let me get some information from you to make this a fun story.")
        print()
        food = input("What is a food you despise?")
        print()
        number = input("Give me a number from 5 to 10?")
        print()
        nameCeleb = input("What is the name of a movie character you admire?")
        print()
        adj = input("Give me an adjective:")
        print()
        verb = input("Give me a verb ending in -ing:")
        print()
        seaCreature = input("Give me a type of Sea Creature:")
        print()
        liquid = input("Give me a type of liquid:")
        print()
        noun = input("Give me a noun")
        # Create a short story to go along with the gameplay, substituting their inputted words into the story. Each story should be different and ask for different inputs. Do not reuse the same inputs for each story please. Your stories should be at a minimum of 4 sentences.
        print(f"One day, a group of {adj} pigs discovered a can of {seaCreature} lying in a {noun}. After slurping it up with their {food}-shaped snouts, they suddenly grew {noun}s on their backs!"
              f"With a loud {verb}, they soared into the sky, confusing the {seaCreature}s who were just trying to {verb}."
              f"Ever since, farmers have been installing {noun} on their barns to catch the turbocharged pigs before they crash into {nameCeleb}!")
# Ask if the user would like to play again (use a loop for this). Validate the user input as being y/n. If they input something that is NOT one of your options, ask the player to try again.
#Ask the user if they want to enter another Madlib Story
another = input("Another Mad Lib Story? (y/n)? ")
if another != "y":
    print("Goodbye!")
    exit()
# Validate the user input for the story selection. If they input something that is NOT one of your options, ask the player to try again.
# Create a counter to record how many stories they have created. Display the counter before asking if they would like to play again.
# Spend time formatting your output so that it looks nice.