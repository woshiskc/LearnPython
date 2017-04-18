print """
You met Rivergod in the river. He said you lost an axe:
which axe you lost?
1.gold axe
2.iron axe
"""
axe = raw_input("> ")

if axe == "1":
    print "The gold axe is in front of your hand, what do you do?"
    print "1. Say you lost the axe and take the gold axe!"
    print "2. Tell the truth that you had not lost gold axe"

    answer1 == raw_input("> ")

    if answer1 == "1":
        print "You tell a lie , Rivergod gave you a shit!"
    elif answer1 == "2":
        print "Good boy , you tell the truth .Rivergod took the axe away."
    else:
        print "Rivergod don't know what you think, he went away!"

elif axe == "2":
    print "The iron axe is in front of your hand, what do you do?"
    print "1. Say you lost the axe and take the iron axe!"
    print "2. Tell the truth that you had not lost  axe"

    answer2 == raw_input("> ")

    if answer2 == "1":
        print "Rivergod was angry because you lie. He throw the iron axe away"
    elif answer2 == "2":
        print "Rivergod was happy and give the gold axe to you as prise"
    else:
        print "Rivergod don't know what you said. Could you speak English?"
