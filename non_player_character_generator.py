import random
import csv

from dataclasses import dataclass


race_file_path = "./data/races.csv"
class_file_path = "./data/classes.csv"

max_level = 20

ethical_axis = ["Lawful", "Neutral", "Chaotic"]
moral_axis = ["Good", "Neutral", "Evil"]


@dataclass(kw_only=True)
class NonPlayerCharacter:
    npc_race: str
    npc_class: str
    npc_level: int
    npc_alignment: str


def main():
    non_player_character = NonPlayerCharacter(
        npc_race=get_random_race(),
        npc_class=get_random_class(),
        npc_level=get_random_level(max_level),
        npc_alignment=get_random_alignments(),
    )
    print(non_player_character)


def load_from_csv(file):
    try:
        with open(file, newline="") as csvfile:
            reader = csv.reader(csvfile)
            return [row[0] for row in reader if row]
    except FileNotFoundError:
        print(f"File not found: {file}")
        return []


def get_random_race():
    races = load_from_csv(race_file_path)
    return random.choice(races) if races else None


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
