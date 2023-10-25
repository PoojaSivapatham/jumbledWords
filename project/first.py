import random
print("\n-----------------GUESS THE JUMBLED WORDS-------------------\n")
print("select the category\n")
print("1.colours\n2.animals\n3.fruits\n4.vegetables\n5.body parts")
c=input("enter your choice:")
colours=["red","blue","green","black","white","yellow","violet","brown"]
animals=["dog","cat","monkey","bear","cow","lion","tiger","zebra"]
fruits=["apple","banana","mango","watermelon","pomegranate","strawberry","grapes","pineapple"]
vegetables=["carrot","beatroot","potato","onion","brinjal","cucumber","mushroom","tomato"]
bodyParts=["eyes","nose","teeth","lips","ears","leg","hand","hair"]
if(c==1):
    word=random.choice(colours)
elif(c==2):
    word=random.choice(animals)
elif(c==3):
    word=random.choice(fruits)
elif(c==4):
    word=random.choice(vegetables)
elif(c==5):
    word=random.choice(bodyParts)
letters=list(word)
random.shuffle(letters)
jumbled_word="".join(letters)
while True:
    guess=input("guess:")
    if guess.lower() != word.lower():
        print("Try again")
    else:
        break
print("congratulations!!")