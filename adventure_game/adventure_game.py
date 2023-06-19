import time
import random

list_of_enemies = ["wicked pirate", "fairie", "dragon", "troll"]
random_enemy = random.choice(list_of_enemies)


def main():
    while (True):
        print_pause("You find yourself standing in an open field, ",
                    "filled with grass and yellow wildflowers.")
        print_pause(
            f"Rumor has it that a {random_enemy} is somewhere around here, ",
            "and has been terrifying the nearby village.")
        print_pause("In front of you is a house.")
        print_pause("To your right is a dark cave.")
        print_pause(
            "In your hand you hold your trusty ",
            "(but not very effective) dagger.")

        field()

        choice = input("Would you like to play again? (y/n)")
        if (choice.lower() == 'y'):
            print_pause("Excellent! Restarting the game ... ")
            pass
        elif (choice.lower() == 'n'):
            print_pause("Thanks for playing! See you next time.")
            break
        else:
            print_pause("Invalid input")


def print_pause(*message: str):
    print(message)
    time.sleep(2)


def field():
    print_pause("")
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    choice = input("What would you like to do?\n(Please enter 1 or 2.)\n")
    if (choice == 1):
        house()
    elif (choice == 2):
        cave()
    else:
        pass

    choice = input("Would you like to (1) fight or (2) run away?")
    if (choice == 1):
        fight()
    elif (choice == 2):
        run_away()
    else:
        pass


def cave():
    print_pause("You peer cautiously into the cave.")
    print_pause("It turns out to be only a very small cave.")
    print_pause("Your eye catches a glint of metal behind a rock.")
    print_pause("You have found the magical Sword of Ogoroth!")
    print_pause(
        "You discard your silly old dagger and take the sword with you.")
    print_pause("You walk back out to the field.")


def house():
    print_pause("You approach the door of the house.")
    print_pause(
        f"You are about to knock when the door opens and out, ",
        "steps a {random_enemy}.")
    print_pause(f"Eep! This is the {random_enemy}'s house!")
    print_pause(f"The {random_enemy} attacks you!")
    print_pause(
        f"You feel a bit under-prepared for this, what with ",
        "only having a tiny dagger.")


def fight():
    print_pause(
        f"As the {random_enemy} moves to attack, you unsheath ",
        "your new sword.")
    print_pause(
        "The Sword of Ogoroth shines brightly in your hand ",
        "as you brace yourself for the attack.")
    print_pause(
        f"But the {random_enemy} takes one look at your shiny ",
        "new toy and runs away!")
    print(f"You have rid the town of the {random_enemy}. ",
          "You are victorious!")


def run_away():
    print_pause(
        "You run back into the field. Luckily, ",
        "you don't seem to have been followed.")


if __name__ == "__main__":
    main()
