
def openCards():
    file = open ("output.txt","r")
    print(file.read())



def substractCards():

    output = []
    output1 = []


    with open("output.txt", encoding="utf-8") as f:
        for line in (f):
            result = 0
            result1 =0


            output.append(line.split()[2])
            output.append(line.split()[3])

            output1.append(line.split()[6])
            output1.append(line.split()[7])

            result += float((line.split()[2]))
            result += float((line.split()[3]))

            result1 += float((line.split()[6]))
            result1 += float((line.split()[7]))

            result1 -= result




    print(output)
    print(output1)

    print(result1)
    if result1>result:
        print("The winner is player 1 ! Congratulations " " by "+ str(result1)+"Value points")
    else :
        print ("The winner is player 2 ! Congratulations"" by "+ str(result1)+" Value points ")


def main ():
    openCards()
    substractCards()

if __name__ == '__main__':
    main()


