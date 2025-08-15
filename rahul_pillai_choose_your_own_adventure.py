
#Rahul Pillai
print("Welcome to the Uncharted 6: Nathan's Odyssey!")

name = input("Before we embark on this journey, what shall I call you? ")
print(f"Ah, greetings {name}! As the mist clears, you find yourself standing at a crossroads, the whispers of adventure beckoning from each direction. Which path shall you choose?")

print("1. Venture left into the unknown depths")
print("2. Brave the path to the right, where danger may lurk")

choice1 = input("Choose your destiny wisely. Shall it be left (1) or right (2)? ")

if choice1 == "1":
    print("A brave soul you are, opting for the path less trodden.")
    print("The leftward journey leads you to a darkened mouth of stone, a cave.")
    choice2 = input("Do you dare enter this ominous cavern? Yes or no? ")

    if choice2.lower() == "yes":
        print("You step into the cool, musty embrace of the cave, your heart pounding with anticipation.")
        print("To your astonishment, a gleam catches your eye amidst the shadows - a treasure chest!")
        print(f"Congratulations, {name}! You've uncovered the long-forgotten riches within.")
        print("With newfound wealth, you carve your legend into the annals of history.")

    elif choice2.lower() == "no":
        print("Cautious you remain, opting to continue along the path.")
        print("Beyond the cave's yawning entrance lies a hidden sanctuary, a secret garden where magical beings dwell.")
        print("You choose to linger here, amidst the enchanting flora and fauna, finding peace in their company.")
        print("Here, you shall dwell, forevermore.")

elif choice1 == "2":
    print("Ah, the path to the right, where many a daring adventurer has tread.")
    print("Before you stretches a rickety bridge, its timbers weathered by time and peril.")
    choice3 = input("Do you possess the courage to cross this perilous span? Yes or no? ")

    if choice3.lower() == "yes":
        print("With each cautious step, the bridge creaks and groans beneath your weight.")
        print("You reach the other side, heart pounding, only to find yourself in the midst of a hidden chamber.")
        print("Here, amidst ancient relics, you uncover the secrets of civilizations long past.")
        print("Your name shall echo through the ages as a renowned archaeologist, unraveling mysteries lost to time.")

    elif choice3.lower() == "no":
        print("Prudent you are, choosing caution over recklessness.")
        print("Retracing your steps, you seek another path.")
        choice4 = input("Shall you delve deeper into the woods (1) or seek an alternate route (2)? ")

        if choice4 == "1":
            print("Into the depths of the forest you wander, the trees whispering secrets untold.")
            print("Amidst the shadows, you encounter a creature of myth and legend, offering you a quest of unimaginable importance.")
            print("You accept the challenge, embarking on an odyssey that shall etch your name into the annals of heroism.")

        elif choice4 == "2":
            print("Venturing along a different path, you stumble upon a hidden village.")
            print("Here, amidst the tranquility of rural life, you find solace and contentment.")
            print("In this village, you shall find a new beginning, leaving behind the trials of the past.")

print(f"Thank you for embarking on this adventure, {name}. Your journey in Uncharted 6: Nathan's Odyssey has come to an end.")

