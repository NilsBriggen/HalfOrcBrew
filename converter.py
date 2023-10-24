import json


def convert_to_python():
    with open("all-content.json", "r", encoding="utf-8-sig") as f:
        content = json.load(
            f,
        )
    return content


content = convert_to_python()

with open("all-content.py", "w") as f:
    f.write("data = " + str(content))
