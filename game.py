import json

def set_charact(name):
    character = {
        "name": name,
        "items": ["주먹", "발차기", "겁주기"],
        "skill": ["방패", "순발력", "귀신"],
        "run": ["성공", "실패"]
    }
    with open("static/save.txt", "w", encoding="utf-8") as f:
        json.dump(character, f, ensure_ascii = False, indent=4)
    # print("{0}님의 모험을 시작합니다. (HP {1})".format(character['name'], character["hp"]))
    return character

def save_game(filename, charact):
    f = open("save.txt", "w", encoding="utf-8")
    for key in charact:
        print("%s:%s"  % (key, charact[key]))
        f.write("%s:%s\n" % (key, charact[key]))
    f.close()