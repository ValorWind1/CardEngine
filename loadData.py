import pickle

class UserInputs:
    def __init__(self, dmg, hp,nm,lbl,qt):
        self.hp = hp
        self.dmg = dmg
        self.hp= hp
        self.nm = nm
        self.lbl=lbl
        self.qt=qt

def save(obj):
    save_file = open('save.dat', 'wb')
    pickle.dump(obj, save_file)
    save_file.close()

def load():
    load_file = open('save.dat', 'rb')
    loaded_game_data = pickle.load(load_file)
    return loaded_game_data

def start():
    while True:
        UserInputs.nm= input('Card Name: ')
        UserInputs.lbl = input('Card Label: ')
        UserInputs.dmg = input('Card Dmg: ')
        UserInputs.hp = input('Card Hp: ')

        with open("output.txt", "a") as file:
                file.write(UserInputs.nm + "\n")
                file.write(UserInputs.lbl + "\n")
                file.write(UserInputs.dmg + "\n")
                file.write(UserInputs.hp + "\n\n")
        file.close()
        UserInputs.qt = input("Do you want to create a new card ? y/n ")
        if UserInputs.qt =="n":
            break





def main ():
    player = UserInputs(0,0,0,0,0)
    start()
    save(UserInputs)
    loaded_player = load()
    print (loaded_player.hp, loaded_player.dmg,loaded_player.lbl,loaded_player.nm,loaded_player.qt)

if __name__ == '__main__':
    main()