import random

def main():
        choose = int(input("heads(1) or tails(2): "))

       
        ran = random.randint(1,2)



        if ran == 1:
            print("heads")
        elif ran == 2:
               print ("tails")

        if choose == ran:
            print("you win")
        elif choose != ran:
              print ("you lose")
        else:
              print("no option found it")




if __name__== "__main__":
    main()

