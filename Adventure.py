print("You are exploring a on a island in hopes of finding treasure\n")
print("You are currently on the shore")

option1 = input("Do you wish to: explore/wait? ")
if option1 == "explore":
    print("\nYou travel deep into the island and find an ancient temple")
    option2 = input("Do you wish to: go in/look around? ")
    if option2 == "go in":
            print("\nYou have entered the temple and find yourself inside a mysterious labrinth")
            option2_1 = input("Do you wish to go: straight/left/right? ")
            if option2_1 == "straight":
                print ("\nYou decide to go straight and are met with a hoarde of zombies")
                option2_1_1 = input("Do you wish to: fight/run? ")
                if option2_1_1 == "fight":
                    print("\nYou easily shredded all the zombies to pieces with your bare hands but you were so tired afterwards, you fell asleep and never woke up.")
                if option2_1_1 == "run":
                    print("\nYou immediately slam the gate shut and return to the first room. Phew!")
                    option2_2 = input("Do you wish to go: left/right? ")
                    if option2_3 == "left":
                        print("\nYou decide to turn left and find a statue of a dog with a button on its nose.")
                        option2_2_1 = input("Do you push the button, yes/no? ")
                        if option2_2_1 == "yes":
                            print("\nThe floor beneath you collapses and you fall onto a pit of spikes that penetrates your skull. Ouch!")
                        if option2_2_1 == "no":
                            print("\nYou decide not to push the button, although it may have contained some juicy rewards, you turn back and return to the first room.")
            elif option2_1 =="left":
                print("\nYou decide to turn left and find a statue of a dog with a button on its nose.")
                option2_2_1 = input("Do you push the button, yes/no? ")
                if option2_2_1 == "yes":
                    print("\nThe floor beneath you collapses and you fall onto a pit of spikes that penetrates your skull. Ouch!")
                if option2_2_1 == "no":
                    print("\nYou decide not to push the button, although it may have contained some juicy rewards, you turn back and return to the first room.")
    if option2 == "look around":
        print("You scan the perimeter but found nothing of interest")
        option2_2input("Do you wish to: go in/look further")
elif option1 == "wait":
    print("You sat down to wait but ended up falling asleep and never woke up.")