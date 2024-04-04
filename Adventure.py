print("You are exploring a on a island in hopes of finding treasure\n")
print("You are currently on the shore")

option1 = input("Do you want to: explore/wait? ")
if option1 == "explore":
    print("\nYou travel deep into the island and find an ancient temple")
    option2 = input("Do you want to: go in/look around? ")
    if option2 == "go in":
            print("\nYou have entered the temple and find yourself inside a mysterious labrinth")
            option2_1 = input("Do you want to go: straight/left/right? ")
            if option2_1 == "straight":
                print ("\nYou decide to go forwards is met with a hoarde of zombies")
                option2_2 = input("Do you want to: fight/run? ")
                if option2_2 == "fight":
                    print("\nYou easily shredded the zombies to pieces with your bare hands but you were so tired afterwards you ")
elif option1 == "wait":
    print("You sat down to wait but ended up falling asleep")