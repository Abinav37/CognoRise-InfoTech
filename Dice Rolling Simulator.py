import random

def roll_dice(num_sides, num_rolls):
    results = []
    for _ in range(num_rolls):
        roll = random.randint(1, num_sides)
        results.append(roll)
    return results

def main():
    print("Welcome to the Dice Rolling Simulator!")

    try:
        num_sides = int(input("Enter the number of sides on the dice: "))
        num_rolls = int(input("Enter the number of rolls: "))
    except ValueError:
        print("Invalid input! Please enter numerical values.")
        return

    results = roll_dice(num_sides, num_rolls)

    print(f"Rolling a {num_sides}-sided dice {num_rolls} times...")
    for i, result in enumerate(results, start=1):
        print(f"Roll {i}: {result}")

    print("Thanks for using the Dice Rolling Simulator!")

if __name__ == "__main__":
    main()
