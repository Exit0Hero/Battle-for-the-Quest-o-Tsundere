import os

SAVE_FILE = "highscore.txt"


def load_highscore():

    if not os.path.exists(SAVE_FILE):

        with open(SAVE_FILE, "w") as f:
            f.write("0")

        return 0

    try:

        with open(SAVE_FILE, "r") as f:
            return int(f.read())

    except:

        return 0


def save_highscore(score):

    current = load_highscore()

    if score > current:

        with open(SAVE_FILE, "w") as f:
            f.write(str(score))

        return score

    return current


def reset_highscore():

    with open(SAVE_FILE, "w") as f:
        f.write("0")