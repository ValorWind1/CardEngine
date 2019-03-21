import pickle



def saveData(obj):

    save_file = open("saveData.dat","wb")
    pickle.dump(obj,save_file)
    save_file.close()

def loadData():
    load_file = open ("saveData.dat", "rb")
    loaded_game_data = pickle.load(load_file)
    return loaded_game_data



def usInput():
    global nameCard, labelCard, attackCard, defenseCard
    nameCard = input (" Name of the card :")
    labelCard = input (" Name of the label of the card :")
    attackCard = input (" attack of the card : ")
    defenseCard = input (" defense of the card :")

def usResult():

    print ("Name of card is : " + nameCard)
    print ("Name of the label: "+ labelCard)
    print (" Attack of: " + nameCard + " is : " + attackCard)
    print (" Defense of: " + nameCard + " is : " + defenseCard)




if __name__ == "__main__":
    usInput()
    usResult()
    loadData()
    saveData(object)

