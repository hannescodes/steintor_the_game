
# I want to built a small textgame in python. My goal is to make the item Silberwasser to be false in the beginnig.
#when entering the room called sliberwasser I want this to change to global True
# once Silberwasser =  True you can access the room dobben which was denied before.



from sys import exit

Silverwater = False
#so means i dont have the Silverwater at the beginning

class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)

lu = Room("Im Lu", 
"""
xxx
"""
)

deeptalk_heyduck = Room("Deeptalk mit Heyduck", 
"""
xxx
"""
)



silberwasser = Room("Silberwasser",
"""
Vor ein paar Jahren waren die Echsenmenschen schon einmal soweit, dass Steintor zu übernehmen. 
Allerdings konnte ich mir von Power-Sven das Silberwasser für 2 Gramm Bobel besorgen.
Damit konnte ich die Echsenmenschen erkennen und mit meinen Superkräften besiegen. 
Allerdings kann ein Mensch das Silberwasser nur einmal in seinem Leben benutzen...daher bin ich jetzt raus.

Aber weisst du was, du warst immer korrekt Kusenq. Ich gebe dir einfach meine Ampulle mit Silberwasser. 
Mach damit was du willst. Eventuell schaffst du es ja die Echsenmenschen zu besieggen. Bol Sans."

Du bedankst dich für das Silberwasser und gehst mit gemischten Gefühlen zurück zum Eck.

Drücke '1' um fortzufahren...

"""
# After visiting this room i want Silverwater changed to = True for the entire game.
global Silverwater
Silverwater = True
)



chemtrails = Room("Chemtrails",

"""
xxx
"""

)

dobben = Room("Am Dobben", 

"""

xxx
"""
)

etwas_fehlt_dobben = Room("Irgendetwas fehlt", 
"""
xxx.

"""
)

bellini = Room("Bellini", 

"""

xxx

"""
)

etwas_fehlt_bellini = Room("Irgendetwas fehlt", 
"""
xxx
"""
)

chinchilla = Room("Chinchilla", 
"""
xxx

"""
)




eck = Room("Am Eck", 
"""
xxx
"""
)

eck2 = Room("Wieder am Eck", 
"""
xxx

"""
)


chemtrails.add_paths({
    '1': eck2       
  })


deeptalk_heyduck.add_paths({
    '2': silberwasser,
    '1': chemtrails
    
})

generic_death = Room("death", "you died.")



lu.add_paths({
    "1": deeptalk_heyduck, 
    "2": eck2
})

dobben.add_paths({
   
})

eck.add_paths({
    '1': lu,
    '2': etwas_fehlt_dobben,
    '3': etwas_fehlt_bellini,
    '4': chinchilla
})

silberwasser.add_paths({
    '1': eck2        
  })

eck2.add_paths({
    '1': lu,
    '2': etwas_fehlt_dobben,
    '3': bellini,
    '4': chinchilla
})





etwas_fehlt_bellini.add_paths({
    '1':eck2
})


etwas_fehlt_dobben.add_paths({
    '1':eck2
})
START ='eck'

def load_room(name):
    """
   xxx
    """
    return globals().get(name)

def name_room(room):
    """
    xxx?
    """
    for key, value in globals().items():
        if value == room:
            return key

    
