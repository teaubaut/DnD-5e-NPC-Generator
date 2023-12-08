import random
import csv

# File paths for race and class data
race_file_path = "./data/races.csv"
class_file_path = "./data/classes.csv"

# Maximum level for a non-player character
max_level = 20

# Alignment options on ethical and moral axes
ethical_axis = ["Lawful", "Neutral", "Chaotic"]
moral_axis = ["Good", "Neutral", "Evil"]


# Class representing the race of a non-player character
class npc_race:
    def __init__(self, npc_race) -> None:
        # Initialize with a specific race or "random"
        self.npc_race = npc_race
        self.__post_init__()

    def __post_init__(self):
        # If race is set to "random", pick a random race
        if self.npc_race == "random":
            self.npc_race = self.get_random_race()

    def get_random_race(self):
        # Load race data and return a random race
        races = load_from_csv(race_file_path)
        return random.choice(races) if races else None


# Class representing a non-player character, inheriting npc_race
class NonPlayerCharacter(npc_race):
    def __init__(self, npc_class, npc_level, npc_alignment, npc_race="random"):
        # Initialize the base class (npc_race)
        super().__init__(npc_race)
        # Initialize additional NPC attributes
        self.npc_class = npc_class
        self.npc_level = npc_level
        self.npc_alignment = npc_alignment

    def __str__(self) -> str:
        # String representation of the NPC
        return f"Race: {self.npc_race} Class: {self.npc_class} Level: {self.npc_level} Alignment: {self.npc_alignment}"


def main():
    # Main function to create and display a non-player character
    non_player_character = NonPlayerCharacter(
        npc_race="random",  # Set the race as "random" or a specific race
        npc_class=get_random_class(),  # Randomly select a class
        npc_level=get_random_level(max_level),  # Randomly select a level
        npc_alignment=get_random_alignments(),  # Randomly select an alignment
    )
    print(non_player_character)  # Print the NPC's detail


def load_from_csv(file):
    try:
        with open(file, newline="") as csvfile:
            reader = csv.reader(csvfile)
            return [row[0] for row in reader if row]
    except FileNotFoundError:
        print(f"File not found: {file}")
        return []


# def get_random_race():
#     races = load_from_csv(race_file_path)
#     return random.choice(races) if races else None


def get_random_class():
    classes = load_from_csv(class_file_path)
    return random.choice(classes) if classes else None


def get_random_level(range):
    return random.randrange(range) + 1


def get_random_alignments():
    ethics = random.choice(ethical_axis)
    morals = random.choice(moral_axis)
    return f"{ethics}-{morals}"


if __name__ == "__main__":
    main()
