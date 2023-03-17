
hello I am creating a small textgame in python. I have two functions in a room.
I want both function called when entering the room i order to update later pathes in the game.
I want to avoid that one function elimiates the other...

is this code correct?

fight = Room("Round  One:  Fight",

"""
text

""",

"fight.png"

)


def enter_fight_money():
    global Money
    global bellini_fight
    Money += 1 and bellini_fight == True
    update_werderimbiss_paths()
    update_eck2_paths_5()

fight.on_enter = enter_fight_money






