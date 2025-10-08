import random

mapids = {
    "EASY_1":[
        [1, 0, 0, 4, 8, 9, 0, 0, 6],
        [7, 3, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 1, 2, 9, 5],
        [0, 0, 7, 1, 2, 0, 6, 0, 0],
        [5, 0, 0, 7, 0, 3, 0, 0, 8],
        [0, 0, 6, 0, 9, 5, 7, 0, 0],
        [9, 1, 4, 6, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 3, 7],
        [8, 0, 0, 5, 1, 2, 0, 0, 4]
    ],
    "MEDIUM_1": [
        [0, 0, 0, 5, 0, 7, 0, 0, 0],
        [0, 4, 0, 2, 6, 3, 0, 0, 0],
        [1, 0, 7, 4, 0, 0, 0, 0, 0],
        [3, 6, 0, 0, 0, 0, 0, 4, 5],
        [0, 0, 2, 0, 5, 0, 7, 0, 0],
        [7, 9, 0, 0, 0, 0, 0, 6, 2],
        [0, 0, 0, 0, 0, 9, 4, 0, 1],
        [0, 0, 0, 1, 3, 4, 0, 9, 0],
        [0, 0, 0, 6, 0, 5, 0, 0, 0]
    ],
    "HARD_1": [
        [2, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 9, 0, 5, 0, 0, 0, 6, 0],
        [8, 1, 5, 0, 7, 0, 9, 0, 0],
        [1, 0, 0, 0, 6, 7, 0, 9, 0],
        [9, 0, 0, 4, 5, 0, 0, 0, 2],
        [0, 3, 0, 0, 0, 0, 0, 0, 8],
        [0, 5, 0, 0, 0, 0, 8, 2, 0],
        [4, 0, 0, 0, 0, 0, 0, 1, 6],
        [3, 0, 0, 2, 0, 0, 0, 0, 7]
    ]
}


def generateHard():
    hardmaps = list(filter(lambda x : "HARD" in x, mapids.keys()))
    print(hardmaps)
    print(hardmaps[random.randint(0, len(hardmaps)-1)])
    return hardmaps[random.randint(0, len(hardmaps)-1)]

def generateEasy():
    hardmaps = list(filter(lambda x : "MEDIUM" in x, mapids.keys()))
    return hardmaps[random.randint(0, len(hardmaps)-1)]

def generateMedium():
    hardmaps = list(filter(lambda x : "HARD" in x, mapids.keys()))
    return hardmaps[random.randint(0, len(hardmaps)-1)]


if __name__ == "__main__":
    print(generateHard())