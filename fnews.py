import random
# ////////////////////////////////////////////////////////////////////////////////////////////
# ---------------------------random subjects-----------------------------------
subjects = [
    "A lazy cat",
    "A school boy",
    "My funny uncle",
    "A crying baby",
    "A crazy goat",
    "My best friend",
    "A dancing dog",
    "A sleepy teacher",
    "A talking fish",
    "A smart monkey",
    "My neighbour",
    "A silly robot",
    "A flying cow",
    "My little sister",
    "A chicken with shoes"
]
# -------------------------------random actions----------------------------------
actions = [
    "ate all the ice cream",
    "danced on the roof",
    "started crying in the exam",
    "slept during a fight",
    "ran away with the TV remote",
    "sang a funny song",
    "became the school principal",
    "forgot how to walk",
    "made tea with Pepsi",
    "got scared of a balloon",
    "wrote a love letter to a pizza",
    "fought with a mirror",
    "opened a shop on the moon",
    "got stuck in the fridge",
    "talked to a shoe"
]
# -------------------------------------random objects------------------------------
objects = [
    "in the school canteen",
    "inside the bathroom",
    "on live TV",
    "at 3AM last night",
    "during the wedding",
    "inside a shopping bag",
    "on the principal’s chair",
    "in front of 100 people",
    "while cooking noodles",
    "under the bed",
    "during morning assembly",
    "on the school bus",
    "at the zoo",
    "inside the washing machine",
    "in a dream"
]
def breaking():
    sub=random.choice(subjects)
    act=random.choice(actions)
    obj=random.choice(objects)
    headlines=f"{sub} {act} {obj}!"
    return headlines

def onenews():
    while True:
        print(f"HEADLINE:{breaking()}.")
        choice=input("YOU WANT ANOTHER   NEWS(Y/N):- ").lower()
        if choice =="n":
            break
# ////////////////////////////////////////////////////////////////////////////////////////////
def savefile():
    with open("HEADLINES FILE.txt", "w") as f:
        start=0
        user=int(input("HOW MANY NEWS YOU WANT IN TEXT FILE:- "))
        for news in range(user):
            start=start+1
            f.writelines(f"{start}. {breaking()}\n")
    print(f"{start} NEWS SAVED TO THE HEADLINES FILE IN TEXT FORM.")

# ////////////////////////////////////////////////////////////////////////////////////////////
print("Welcome to the Funny Fake News Generator!")
print("1.NEW HEADLINES")
print("2.SAVE IN TEXT FILE")
print("3.EXIT")
choice=int(input("WHICH SERVICE DO YOU WANT(1-3):- "))
match choice:
    case 1:
        onenews()
    case 2:
        savefile()
    case 3:
        exit()
    case _:
        print("!!INVALID CHOICE!!")

