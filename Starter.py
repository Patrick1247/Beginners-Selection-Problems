print("Welcome to the Rollercoaster!\n\nIn order to ride the rollercoaster, there is a height requirement of 120cm")
height = input("Please enter your height in cm: ")
cm = int(height)
if cm >=120:
    confirm = input("Are you lying?👀 y/n ")
    if confirm == "y":
        print("Sorry, you can't ride this rollercoaster. But atleast you are honest.")
    elif confirm == "n":
        print ("Welcome aboard!")
    else:
        print("Invalid response. Go to the back of the line. Please answer 'y' or 'n' to confirm next time.")
elif cm<120:
     print(" Sorry, little babies can't ride this rollercoaster. Come back when you are ready")