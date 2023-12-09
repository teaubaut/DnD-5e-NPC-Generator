import random
import csv
import sys

# File paths for race and class data
race_file_path = "./data/races.csv"
class_file_path = "./data/classes.csv"

# Maximum level for a non-player character
max_level = 20

# Alignment options on ethical and moral axes
ethical_axis = ["Lawful", "Neutral", "Chaotic"]
moral_axis = ["Good", "Neutral", "Evil"]


# Class representing the race of a non-player character
class NpcRace:
    def __init__(self, npc_race, **kwargs):
        super().__init__(**kwargs)
        # Initialize with a specific race or "random"
        self.npc_race = npc_race
        self.races = load_from_csv(race_file_path)
        self.race_post()

    def race_post(self):
        try:
            # Check if the npc_race attribute of the instance is set to "random"
            if self.npc_race == "random":
                # If so, assign a random race to npc_race using the get_random_race method
                self.npc_race = self.get_random_race()

            # Check if the npc_race is not in the predefined list of races (self.races)
            if self.npc_race not in self.races:
                # If the race is not in the list, raise a ValueError
                raise ValueError

        except ValueError:
            # If a ValueError is caught (due to invalid race), terminate the program with an error message
            sys.exit("Invalid race")

    def get_random_race(self):
        # Return a random race from race data
        return random.choice(self.races) if self.races else None


# Class representing the class of a non-player character
class NpcClass:
    def __init__(self, npc_class, **kwargs):
        super().__init__(**kwargs)
        # Initialize with a specific class or "random"
        self.npc_class = npc_class
        self.classes = load_from_csv(class_file_path)
        self.class_post()

    def class_post(self):
        try:
            # Check if the npc_class attribute of the instance is set to "random"
            if self.npc_class == "random":
                # If so, assign a random class to npc_class using the get_random_class method
                self.npc_class = self.get_random_class()

            # Check if the npc_class is not in the predefined list of classes (self.classes)
            if self.npc_class not in self.classes:
                # If the class is not in the list, raise a ValueError
                raise ValueError

        except ValueError:
            # If a ValueError is caught (due to invalid class), terminate the program with an error message
            sys.exit("Invalid class")

    def get_random_class(self):
        # Return a random class from class data
        return random.choice(self.classes) if self.classes else None


# Class representing a non-player character, inheriting npc_race
class NonPlayerCharacter(NpcRace, NpcClass):
    def __init__(self, npc_class, npc_level, npc_alignment, npc_race):
        # Initialize the base class (npc_race)
        super().__init__(npc_race=npc_race, npc_class=npc_class)
        # Initialize additional NPC attributes
        # self.npc_class = npc_class
        self.npc_level = npc_level
        self.npc_alignment = npc_alignment

    def __str__(self) -> str:
        # String representation of the NPC
        return f"Race: {self.npc_race} Class: {self.npc_class} Level: {self.npc_level} Alignment: {self.npc_alignment}"


def main():
    # Main function to create and display a non-player character
    non_player_character = NonPlayerCharacter(
        npc_race="random",  # Set the race as "random" or a specific race
        npc_class="random",  # Set the class as "random" or a specific class
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


def get_random_level(range):
    return random.randrange(range) + 1


def get_random_alignments():
    ethics = random.choice(ethical_axis)
    morals = random.choice(moral_axis)
    return f"{ethics}-{morals}"


if __name__ == "__main__":
    main()
