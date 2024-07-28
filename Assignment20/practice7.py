import random


def main():
    options = [1,2]
    player_score = 0
    computer1_score = 0
    computer2_score = 0

    for _ in range(5):
        player_choice = input("Please Enter one of 1--->🤚 , \n2---> ✋ : ")
        computer1_choice = random.choice(options)
        computer2_choice = random.choice(options)

        print(f"user choice --->  {player_choice}, \ncomputer_2 choice ---> {computer2_choice}, \ncomputer_1 choice ---> {computer1_choice}")

        if (computer1_choice == computer2_choice) and (computer1_choice != player_choice):
            player_score += 1
            print("user win")
        elif (computer1_choice == player_choice) and (computer1_choice != computer2_choice):
            computer2_score += 1
            print("computer2 win")
        elif (computer2_choice == player_choice) and (computer2_choice != computer1_choice):
            computer1_score += 1
            print("computer1 win")
        elif computer1_choice == computer2_choice == player_choice:
            print("Equal")
    
        print(f"\nuser score ---> {player_score}, \ncomputer_2 score ---> {computer2_score}, \ncomputer_1 score ---> {computer1_score}")


if __name__ == "__main__":
    main()
