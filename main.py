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
        self.requiredChoices = ["race", "class", "level", "stats", "feats", "background", "alignment", "proficiencies", "equipment"]

    def getRace(self):
        temp = [race["name"] for race in base["races"]]
        if extended:
            for book in extension.keys():
                if "races" in extension[book].keys():
                    temp.extend(iter(extension[book]["races"]))
        temp.sort()
        for i in range(len(temp)):
            temp[i] = temp[i].replace("-", " ").capitalize()
        return temp

print(Creator().getRace())