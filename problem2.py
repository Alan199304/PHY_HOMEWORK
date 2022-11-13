#If T-Rex is angry, hungry, and bored he will eat the Triceratops.
#Otherwise if T-Rex is tired and hungry, he will eat the Iguanadon.
#Otherwise if T-Rex is hungry and bored, he will eat the Stegasaurus.
#Otherwise if T-Rex is tired, he goes to sleep.
#Otherwise if T-Rex is angry and bored, he will fight with the Velociraptor.
#Otherwise if T-Rex is angry or bored, he roars.
#Otherwise T-Rex gives a toothy smile.
angry =  True
hungry = True
tired = False
bored = False


if tired:
    print("he will go to sleep")
    if hungry:
        print("T_rex will eat Iguanadon ")
elif angry   :
    print("T-rec will fight")
    if bored:
        print("he will fight with the Velociraptor")

    elif bored and hungry:
        print("he will eat the Triceratops")
    elif angry or bored:
        print("T-Rex roars! Rawr!")

elif hungry:
    print("T-rex eat!")
    if bored:
        print("he will eat the Stegasaurus")

else:
    print("T-Rex gives a toothy smile.")
