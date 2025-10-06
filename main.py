import savehandler



# luo tallenteet kansio jos sitä ei ole.

    
def printMainMenu():
    print("1. Start a new game")
    print("2. Continue saved game")
    print("3. Show highscores")
    print("0. Exit")


def main():
    savehandler.initSaves()

main()