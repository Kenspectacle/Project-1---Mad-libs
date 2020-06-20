import sys
from time import sleep

if __name__ == "__main__":

    Adjective = ""
    Noun1 = ""
    Noun2 = ""
    Adverb = ""
    Animation = "almost there"
    print("Hello, welcome to your(mine?) first Python Project! :)\nIn this project we will be doing madlib. Have fun! :D")
    Adjective = input("Please Input an adjective: ")
    Noun1 = input("Please Input the first noun: ")
    Noun2 = input("Please Input the second noun: ")
    for i in range(3):
        print(f"{Animation}{'.'*i}", end="\r")
        sleep(1)
    print(f"{Animation}{'.'*(i+1)}")
    Adverb = input("Please Input an Adverb: ")
    print(f"You have found a {Noun1} in the {Adjective} Valhalla!!\nCongratulation, but it is hardly {Adverb} better compared to {Noun2}. Keep going!")

    