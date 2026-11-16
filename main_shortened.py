import random 
'''
1 for Snake
-1 for Water
0 for gun 

'''
computer = random.choice([1,0,-1])
youstr =  input("Enter your choice(s/w/g): ").strip().lower()
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

if youstr not in youDict:
    print("Invalid input! Please enter s, w, or g.")
    exit()
you = youDict[youstr]

# By now we have two numbers (variables) , you and computer

print(f"You choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")

if (computer == you):
    print("It's a Draw!")

else:
    # Determine winner using the difference
    if (computer - you) in [-1, 2]:
       print("You Lose!")
    else:
       print("You Win!")