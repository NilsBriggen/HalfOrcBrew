# Import base data
from baseData import *

# Try to import additional data
try:
    from additionalData import *

    extended = True
except ImportError:
    extended = False


# Creator class to create the character
class Creator:
    def __init__(self):
        self.stats = {"STR": 0, "DEX": 0, "CON": 0, "INT": 0, "WIS": 0, "CHA": 0}
        self.requiredChoices = [
            "race",
            "class",
            "level",
            "stats",
            "feats",
            "background",
            "alignment",
            "proficiencies",
            "equipment",
        ]
        self.modifiers = {
            "STR": [],
            "DEX": [],
            "CON": [],
            "INT": [],
            "WIS": [],
            "CHA": [],
        }

    def getRace(self):
        temp = [race["name"] for race in base["races"]]
        if extended:
            for book in extension.keys():
                if "races" in extension[book].keys():
                    temp.extend(iter(extension[book]["races"]))
        for i in range(len(temp)):
            temp[i] = temp[i].capitalize().replace("-", " ")
        temp.sort()
        return temp

    def getRaceStats(self, race):
        for i in range(len(base["races"])):
            if base["races"][i]["name"] == race:
                race = i
                continue

        if type(race) != int and extended:
            race = str(race).lower()
            for book in extension:
                if "races" in extension[book]:
                    if race in extension[book]["races"]:
                        buffs = extension[book]["races"][race]["abilities"]
                        for buff in buffs.keys():
                            self.modifiers[buff].append(buffs[buff])
                        break

        elif type(race) == int:
            temp = base["races"][race]["asi"]
            for i in range(len(temp)):
                self.modifiers[temp[i]["attributes"]].append(temp[i]["value"])

        else:
            return "error"

        print(self.modifiers)


creator = Creator()
print(creator.getRace())
race = input().replace(" ", "-")
creator.getRaceStats(race)
