import pickle

class UserInputs:
    def __init__(self, dmg, hp,nm,lbl):
        self.hp = hp
        self.dmg = dmg
        self.hp= hp
        self.nm = nm
        self.lbl=lbl

def save(obj):
    save_file = open('save.dat', 'wb')
    pickle.dump(obj, save_file)
    save_file.close()

def load():
    load_file = open('save.dat', 'rb')
    loaded_game_data = pickle.load(load_file)
    return loaded_game_data

def start():
    UserInputs.nm= input('Card Name: ')
    UserInputs.lbl = input('Card Label: ')
    UserInputs.dmg = input('Card Dmg: ')
    UserInputs.hp = input('Card Hp: ')

def main ():
    player = UserInputs(0,0,0,0)
    start()
    save(UserInputs)
    loaded_player = load()
    print (loaded_player.hp, loaded_player.dmg,loaded_player.lbl,loaded_player.nm)

if __name__ == '__main__':
    main()