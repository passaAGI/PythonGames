import random
import os
import time
import sys

def drawer(errorcounter):
    ec = errorcounter
    if(ec == 0):
        print("_______")
        print("|      |")
        print("|")
        print("|")
        print("|")
        print("-")
    elif(ec == 1):
        print("_______")
        print("|      |")
        print("|      O")
        print("|")
        print("|")
        print("-")
    elif(ec == 2):
        print("_______")
        print("|      |")
        print("|      O")
        print("|      |")
        print("|")
        print("-")     
    elif(ec == 3):
        print("_______")
        print("|      |")
        print("|     \O")
        print("|      |")
        print("|")
        print("-")
    elif(ec == 4):
        print("_______")
        print("|      |")
        print("|     \O/")
        print("|      |")
        print("|")
        print("-")
    elif(ec == 5):
        print("_______")
        print("|      |")
        print("|     \O/")
        print("|      |")
        print("|     /")
        print("-")
    elif(ec == 6):
        print("_______")
        print("|      |")
        print("|     \O/")
        print("|      |")
        print("|     / \\")
        print("-")

def wordSelector():
        if not os.path.exists('words.txt'):
            print("File words.txt does not exist in working directory!")
            time.sleep(3)
            os.system('exit')
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        file = open(os.path.join(__location__, 'words.txt'))
        words = file.readlines()
        myword = random.choice(words)
        myword.strip()
        return(myword)

def hideAns(ans, lista):
    lista2 = []
    lista2.append(lista[0])
    for i in lista[1:-1]:
            i = "-"
            lista2.append(i)
    lista2.append(lista[-1])
    return(lista2)

def showLetter(lista, hiddenans, letter):
    lista3 = []
    lista3.append(lista[0])
    for i in lista[1:-1]:
        if(i == letter) or (i in hiddenans):
            lista3.append(i)
        else:
            i = "-"
            lista3.append(i)
    lista3.append(lista[-1])
    return(lista3)

def main():
        flag = True
        errorcounter = 0
        attempt = ""
        letter = ""
        lista = []
        misses = []
        print("*********")
        print("*Hangman*")
        print("*********\n")
        time.sleep(3)
        ans = wordSelector()
        ans = ans[:-1] #delete line if unnecessary (based on input .txt file)
        
        for i in ans:
            lista.append(i)
        
        hiddenans = hideAns(ans, lista)
        
        while flag:
            os.system('cls')
            drawer(errorcounter)
            print(hiddenans)
            misses.sort()
            print("Misses:", misses)
            a_or_l = input("Attempt or letter? [A][L] ")
            a_or_l = a_or_l.upper()
            if(a_or_l == "A"):
                attempt = input("Attempt: ")
                if attempt == ans:
                    print("RIGHT!")
                    print("You won!")
                    time.sleep(3)
                    flag = False
                elif attempt != ans:
                    print("Wrong")
                    errorcounter += 1
            elif(a_or_l == "L"):
                letter = input("Letter: ")
                if(((letter == lista[0]) and (letter in lista[:1])) or ((letter == lista[-1]) and (letter in lista[:-1])) or (letter in misses)):
                    print("This letter is already shown!")
                elif(letter not in lista):
                    print("Wrong")
                    errorcounter += 1
                    misses.append(letter)
                elif(letter in lista):
                    print("Right!")
                    hiddenans = showLetter(lista, hiddenans, letter)
            check = "".join(hiddenans)
            if(ans == check):
                print("RIGHT!")
                print("You won!")
                time.sleep(3)
                flag = False
            if(errorcounter == 6):
                print("Maximum number of errors is 6!")
                print("You died!")
                print("The correct answer is", ans)
                time.sleep(4)
                flag = False

main()
