import random


def checkscore(yourscore, computerscore):
    if yourscore == 10:
        print("\nYou win!")
        exit()
    elif computerscore == 10:
        print("\nComputer wins!")
        exit()
    else:
        pass

def userinput():
    print("ROCK PAPER SCISSORS")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("\nYou chose Rock")
    elif choice == "2":
        print("\nYou chose Paper")
    elif choice == "3":
        print("\nYou chose Scissors")
    return choice

def computerchoice():
    random_number = random.randint(1, 3)
    if random_number == 1:
        print("Computer chose Rock")
    elif random_number == 2:
        print("Computer chose Paper")
    elif random_number == 3:
        print("Computer chose Scissors")
    return random_number

def main():
    Your_score = 0
    Computer_score = 0
    print("\nRemember. First to 10 wins.")
    while True:
       
        print("\nYour score: ", Your_score)
        print("Computer score: ", Computer_score)
        print("\n")
        choice = userinput()
        computerschoice = computerchoice()
        if choice == "1" and computerschoice == 1:
            print("It's a tie!")
        elif choice == "1" and computerschoice == 2:
            print("You lose!")
            Computer_score += 1
        elif choice == "1" and computerschoice == 3:
            print("You win!")
            Your_score += 1
        elif choice == "2" and computerschoice == 1:
            print("You win!")
            Your_score += 1
        elif choice == "2" and computerschoice == 2:
            print("It's a tie!")
        elif choice == "2" and computerschoice == 3:
            print("You lose!")
            Computer_score += 1
        elif choice == "3" and computerschoice == 1:
            print("You lose!")
            Computer_score += 1
        elif choice == "3" and computerschoice == 2:
            print("You win!")
            Your_score += 1
        elif choice == "3" and computerschoice == 3:
            print("It's a tie!")
        elif choice == "4":
            break
        else:
            print("Invalid choice")
        checkscore(Your_score, Computer_score)
        input("\nPress Enter key to continue")

if __name__ == "__main__":
    main()
