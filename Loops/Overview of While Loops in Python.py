#nums = list(range(1,101))

#while len(nums) > 0:
#    print(nums.pop())


"""
def guessing_game():
    while True:
        print("What is your guess?")
        guess = input()

        if guess == "42":
            print("You guess the right number!")
            return False #sentinel value
        else:
            print(f"Nope, {guess} is incorrect, please try again.\n")

guessing_game()
"""



'''
def loop_using_while():
    dog_house = ["rosie", "zero", "skip", "sophie"]
    counter = 0
    while dog_house: #this does not call the right variable or set stoping point for the while loop.
        print(dog_house.pop(), counter) # called .pop() when I shouldn't have.
        counter += 1
        #always need a return []

#print(loop_using_while()) This was not needed because I already had a print() funtion
'''


def loop_using_while():
    dog_house = ["rosie", "zero", "skip", "sophie"]
    counter = 0

    while counter < 4:
        print(dog_house[counter]) #[] allow me to select both variables
        counter += 1
    return [dog_house, counter]

loop_using_while()