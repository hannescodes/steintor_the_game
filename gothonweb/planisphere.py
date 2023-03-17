from sys import exit
import random

Silver = False
Olle = False
Money = 0
Dose = False
Chemtrails = False
Haller = False
Pommes = False
pommes_talk = False
grafitti_talk = False
bellini_fight = False


class Room(object):
    def __init__(self, name, description, image=None):
        self.name = name
        self.description = description
        self.paths = {}
        self.image = image

    def go(self, direction):
        room = self.paths.get(direction, None)
        if room:
            room.on_enter()
        return room

    def add_paths(self, paths):
        self.paths.update(paths)

    def on_enter(self):
        pass



sentences = [
    'DU BIST TOD. Vielleicht besser so. Warst eh ein Assi',
    'DU BIST TOD Die Welt ist jetzt ein klein wenig besser ohne dich.',
    'DU BIST TOD. take the L.',
    'DU BIST TOD. Zurecht.',
    'DU BIST TOD. Sorry.',
    'DU BIST TOD. Da hilft dir auch kein Heiltrank Hexenmeister.'
]

tot = Room("Game  Over", 

random.choice(sentences),

"game_over.png"

)


start = Room("Start",
"""
Willkommen bei "STEINTOR - the Game" 

Drücke "1" um das Spiel zu starten.

""",

"start.png")

 
silberwasser = Room("Silberwasser",
"""
Vor ein paar Jahren waren die Echsenmenschen schon einmal soweit, dass Steintor zu übernehmen. 

Allerdings konnte ich mir von Power-Sven das magische Silberwasser besorgen.
Damit konnte ich die Echsenmenschen erkennen und mit meinen Superkräften besiegen. 

Allerdings kann ein Mensch das Silberwasser nur einmal in seinem Leben benutzen...daher bin ich jetzt raus.

Aber weisst du was, du warst immer korrekt Kusenq. Ich gebe dir einfach meine Ampulle mit Silberwasser. 
Mach damit was du willst. Eventuell schaffst du es ja, die Echsenmenschen zu besieggen. Bol Sans."

Du bedankst dich für das Silberwasser und gehst mit gemischten Gefühlen zurück zum Eck.

Drücke '1' um fortzufahren...
""", 
"silberwasser.png")

def enter_silberwasser():
    global Silver
    Silver = True
    update_eck2_paths()
    update_eck2_paths_2()
    update_kein_drink_paths()
    update_bellini_paths()
    update_olle_direkt_paths()
    update_eck2_paths_4()
    
silberwasser.on_enter = enter_silberwasser

lu_dicht = Room("Lu", 
"""

Das Lu hat jetzt dicht.

Drücke '1' um fortzufahren...

""",

"lu_dicht.png"
)


lu = Room("Im  Lu", 
"""

Im Lu ist nicht viel los. Nur eine Person sitzt alleine an der Bar am Tresen. Nach näherem Hinsehen erkennst du, dass es Heyduck ist.

Er sieht ehrlich gesagt etwas von der Rolle aus. Eventuell hat er keinen Bock mit dir zu labern. 

Willst du trotzdem mit ihm reden, kurz 'Hi' sagen, oder 

gehst du wieder raus?
                            
1 = Mit Heyduck reden
2 = Wieder raus

""",

"lu.png"
)

deeptalk_heyduck = Room("Deeptalk  mit  Heyduck", 
"""
Heyduck ist echt depri. Du sagtst kurz 'Hi' und er guckt hoch. Er erkennt dich und lächelt dich an. Gleich darauf guck er aber wieder runter und sagt:

"Alles ist vorbei. Sie haben gewonnen...."
                            
"Wer hat gewonnen?" fragst du...

Heyduck : "Die Echsenmenschen haben uns. Diesmal kann ich die die Welt nicht mehr retten. Die letzen zwei Male hatte ich alle Artefakte dabei..."

Du: "Macht Sinn...aber welche Artefakte meinst du?"

Heyduck: "Bei ersten Mal hatte ich die Chemtrails. Beim zweiten Mal hatte ich das Silberwasser...."

Du: "Hmmmmm....Das ist schlecht....aber ich meine, was ist passiert mit...."

1 = Den Chemtrails,
2 = Dem Silberwasser
                            
?
""",
"deeptalk_heyduck.png"
)

chemtrails = Room("Chemtrails",

"""
Als die Echsenmenschen zu ersten Mal versucht haben, das Steintor zu inflitrieren, habe ich zu einer List gegriffen. 

Die Echsenmenschen essen am liebsten McRib. Daher habe ich hundert Sparmenüs gekauft und am Henschenbusch hingelegt. 
Da sind die Echsenmensch dann alle hin.

Ich wusste aber von meinen Informanten, dass ein Chemtrail-Flugzeug zu einer bestimmten Uhrzeit über den Henschenbusch fliegt. Die Chemtrails sind nur
dazu da, die Echsenmenschen zu töten. Als alle Echsenmenschen gerade ganz gechillt ihre McRibs gegessen haben, ist das Flugzeug gekommen und ZACK...

alle Echsenmenschen haben sich in Luft aufgelöst...."

Heyduck guckt dich stolz an. 'Bester Mann!' Sagst du und gibst ihm einen Handshake. 
"Allerdings sollten wir nicht zulange über solche Themen reden. Die Wände haben Ohren!' fügst du hinzu.

Er nickt nickt und guckt sich kurz um. Du nutzt die Zeit und gehst ein bisschen verdutzt zurück zum Eck.

Drücke '1' um fortzufahren...

""",

"chemtrails.png"

)

def enter_chemtrails():
    global Chemtrails
    Chemtrails = True
    update_eck2_paths_2()
 
chemtrails.on_enter = enter_chemtrails


heyduck_again = Room("Wie  war  das  nochmal...",

"""
Du gehtst direkt zu Heyduck am Tresen....

"Heyduck....wie war das nochmal mit:

1 Den Chemtrails
2 Dem Silberwasser


""",

"lu.png"

)


dobben = Room("Am  Dobben", 
"""
Du willst gerade zum Dobben gehen, da siehst du auf einmal einen Macker ein Streetbombing am Edeka machen.

Er sieht dich und will erst wegrennen. Du sagst im aber, er soll weitermachen. Du feierst halt Grafitti zu derbe. 
    
Er feiert es auch und fragt dich, ob du nicht kurz Schmiere willst, weil er die Outlines noch fertigziehen will. 

Machst du oder hast du Schiss..?
                        
1 = Schmiere stehen
2 = Schiss
3 = Später wiederkommen
                        
""",

"dobben.png"

)

grafitti = Room("Grafitti", 
"""
Der Junge ist gerade fertig, als du die Bullen von Richtung Weser aus kommen siehst.

Du sagst kurz 'Meckel' und er haut ab. Dabei fällt ihm allerdings seine Dose runter. Ihm ist egal, er haut einfach nur ab.
                                    
Die Bullen fahren einfach weiter und checken nichts. 

Du wartest noch kurz ob der Macker wiederkommt, tut er aber nicht. Du gehst wieder zurück.

Allerdings nimmst du noch die Dose mit. Man weiss ja nie.

Drücke '1' um fortzufahren...
                       
""",

"grafitti.png"

)

def enter_dose():
    global Dose
    Dose = True
    update_eck2_paths()
    update_olle_direkt_3_paths()
    update_habe_pommes_paths()
    
grafitti.on_enter = enter_dose

schiss = Room("Schiss", 
"""
Ganz ehrlich. Wie kann man so ein ekliger Typ sein. 

Aber egal.....Du gehst einfach weiter und gehst bei der Sparkasse über die Strasse.

Gerade als du artig über den Zebrastreifen gehst, kommt ein Bullenwagen mit leisem Blaulicht um die Ecke. 

Anscheinend hat wohl jemand die Bullen wegen dem Jungen und dem Streetbombing gerufen.

Pech für dich, dass die Bullen viel zu schnell um die Ecke gefahren kommen und dich voll erwischen. 

Du fliegst ein paar Meter durch die Luft und denkst noch. 'Fuck!
warum habe ich nicht die Eier und Nerven gehabt, Schmiere zu stehen.
                                    
Du bist gestorben bevor du aufschlägst. Wallahe zurecht.

Drücke '1' um fortzufahren...
                       
""",
"schiss.png"

)


after_grafitti = Room("Nach  dem  Malen", 
"""
Das Bild am Dobben sieht ok aus, der Style ist aber eher kacke und das Bild hat wirklich schlechte Outlines. Aber immerhin hat er sich Mühe gegeben. 

Du wartest noch kurz bei dem Bild, hast aber auch keinen Bock dafür jetzt gebustet zu werden. Du gehst wieder zum Eck.

Drücke '1' um fortzufahren...

""",
"after_grafitti.png"

)

                           
etwas_fehlt_dobben = Room("Irgendetwas  fehlt", 
"""
Du gehst Richtung Dobben....aber du hast das Gefühl, irgendwas fehlt noch.

Drücke '1' um fortzufahren...
"""
,
"etwas_fehlt_dobben.png"

)

etwas_fehlt_bellini = Room("Irgendetwas  fehlt", 
"""
Du gehst Richting Belini....aber du hast das Gefühl, irgendwas fehlt noch.

Drücke '1' um fortzufahren...

""",
"etwas_fehlt_bellini.png"
)

eck = Room("Am  Eck", 
"""
Du bist so am späten Abend am Eck. Wie immer alles irgendwie langweilig aber nachhause ist auch irgendwie kacke. Du denkst wie
immer, dass noch irgendwas gehen muss.  Du entscheidest dich dafür, noch kurz irgendwo hin zu gehen. Nur das Lu oder das ChinChilla haben noch auf. Worauf hast du Bock?
                
1 = Ins Lu
2 = Richtung Dobben
3 = Richtung Bellini
4 = Ins Chinchilla,
""", 

"eck.png"

)

eck2 = Room("Wieder  am  Eck", 
"""
Du bist wieder am Eck. Alles ziemlich ruhig...Wo willst du hin?

1 = Ins Lu
2 = Richtung Dobben
3 = Richtung Bellini
4 = Ins Chinchilla
""",

"eck.png"

)

bellini = Room("Bellini", 

"""

Du willst gerade ins Bellini reingehen, da hörst du einen Schrei. Hinter die scheint eine Schlägerei loszugehen.

Zwei Gruppen von Leuten die du nicht genau zuordnen kannst, rangeln sich irgendwie komisch vor der Tür rum. 

Auf einmal geht alles ganz schnell und du bist mittindrin. Du kannst mitfighten, einen auf Friedensrichter
machen oder abhauen in Richtung Insel oder Eck.

1 = Fight
2 = Friedensrichter
3 = zurück zum Eck abhauen
4 = Richtung Insel abhauen?

""",

"bellini.png"

)

fight = Room("Round  One:  Fight",

"""
Du kriegst auf einmal ein oder zwei Dinger von der Seite ab. Du gehst zu Boden. Auf einmal fällt die wie durch ein Wunder Heyduck wieder ein.

Du hörst seine Stimme in deinem Kopf:
                                        
"Bro...nimm das Silberwasser...nimm es....nimm es."  
                                    
Du nimmst einen Schluck von dem Silberwasser und stehst wieder auf. Beide Partein gucken dich komisch an.

Erst passiert garnichts. Aber auf einmal wirst du zum Ultimate Warrior und machst auch die gleiche Show. Arme hoch, Gorilla Press, alles dabei...

5 Dropkicks, 4 Flying Elbows und 3 Gorilla Presses später steht keiner mehr von den Assis. Egal von welcher Seite. 

Auf dem Boden liegt noch 1 Euro, den wahrscheinlich einer der Jungs verloren hat. 

Du hebst den Euro auf, reibst dir wie Bruce Lee die Nase und haust in Richtung Insel ab. Keiner kommt dir hinterher.

Drücke '1' um fortzufahren...

""",

"fight.png"
)

def on_enter_fight():
    global Money, bellini_fight
    Money += 1
    bellini_fight = True
    update_werderimbiss_paths()
    update_eck2_paths_5()

fight.on_enter = on_enter_fight

no_fight = Room("No Fighting...",

"""
Du bist richtig im Handgemenge mit dabei. Du hast allerdings keine Chance. 

Du kannst aber mit einer gekonnten Judo Rollen der Schlägerei entkommen. 

Ganz Ehrlich, Schlägerei ist das letzte was du jetzt brauchst. Du gehst zurück zum Eck.

Drücke '1' um fortzufahren...'

"""
)

after_fight = Room("Nach  der  Schlägerei",

"""
Alter der Laden sieht echt nicht gut aus. Scheiben eingschlagen, Stühle kaputt....die Schlägerei ist echt ausgeartet.

Vor dem Laden stehen die Bullen und nehmen Adressen auf....du haust schnell ab zur Insel. Sicher ist sicher.

Drücke '1' um fortzufahren...

""",
"after_fight.png"
)
                 

friedensrichter = Room("Friedensrichter",

"""
Du entscheidest dich den grossen Boss Abu Salam Friedensrichter sein Vater zu machen. 

Du drückst einen der Jungs an die Wand und sagst mit lauter Stimme:

" Was zum Herrgottsnamen geht hier vor! Ihr wisst wohl nicht wer ich bin. 
Ich bin ein sehr guter Freund von Maimi Gianni und Carsten Stahl!!"
                                        
Deine eigene Stimme ist leider das Letzte was du noch auf dieser Welt hörst. 

Du kriegst einfach Mal von Allen auf die Fresse und stehst nie wieder auf....

Drücke '1' um fortzufahren...
                                    
""",
"friedensrichter.png"
)


chinchilla = Room("Chinchilla", 
"""

Das ChinChilla ist ziemlich voll. Alle haben gute Laune und der Vibe stimmt. 

Du findest erst keinen Platz und stehst dum rum.

Dann wird allerdings ein Platz neben einer derben Ollen frei....du hast erst Schiss aber dann gehst du trotzdem hin und setzt sich neben sie.

Du überlegst einen auf cool zu machen und ihr einen Drink zu spendieren.
                        
1 = Drink ausgeben
2 = Keinen Drink ausgeben

""",
"chinchilla.png"
)


drink = Room("Drink", 
"""

Du machst einen auf James Bond, checkst aber nicht das du in Wahrheit leider ein ziemlicher Assi bist. 

Allerdings checkt sie das, nimmt den Drink und haut ab. Du bist frustriert und holst dir selber noch einen Drink nach dem anderen und tippst auf deinem Telefon rum.

Als du irgendwann pissen musst und zur Toilette gehst, fällst du die Treppen runter und brichst dir das Genick....Sorry.
                    
Drücke '1' um fortzufahren...

""",
"drink.png"
)


kein_drink = Room("Kein  Drink",

"""
Ihr kommt locker ins Gespräch und die Alte scheint nicht nur gut auszusehen, sondern auch cool
zu sein.

Ihr labert so lange und merkt gar nicht wie die Zeit vergeht. Aber irgendwie erzählt sie komisches Zeug. Irgenwann sagt sie:

"Also manche Sachen sind wirklich komisch heutzutage. Ich hätte schwören können der Kerl da vorne hat gerade seine Zunge in seinen Drink gehalten.
Noch dazu sah die Zunge aus wie die von einer Echse. Irgendwie strange, dabei nehme ich gar kein Fentanyl. Aber ehrlich gesagt ist ja auch scheissegal,
mich wundert eh nichts mehr."

Drücke '1' um fortzufahren...

""",
"kein_drink.png"
)

def enter_kein_drink():
    global Olle
    Olle = True
    update_eck2_paths_3()
    update_eck2_paths_4()
    
kein_drink.on_enter = enter_kein_drink

kein_bock = Room("Gar  keinen  Bock",

"""
Ehrlich gesagt hast du gerade voll keinen Bock auf so ein Gelaber und stehst einfach auf und gehst. Ist bisschen unhöflich aber egal. Einen mit so was vollzulabern ist auch
nicht cool.

Eventuell ist die Olle ja später noch da.

Drücke '1' um fortzufahren...

""",

"olle_sad.png")


olle_direkt = Room("direkt  zur  Ollen",

"""

Du gehst direkt zu der Ollen. Sie sitzt immernoch gelangweilt am Tresen. Mega das Wunder, dass die noch kein Anderer angesprochen hat. 

"WAS??" fragt sie schon sichtlich abgenervt. Wahrscheinlich ist sie sauer weil direkt du abgehauen bist, als sie angefangen hat von Echsenmenschen zu labern.

Drücke '1' um fortzufahren...

""",

"olle_what.png"

)


olle_direkt_2 = Room("direkt  zur  Ollen",

"""

"Hast du meine Pommes?" fragt die Alte.

Drücke '1' um fortzufahren...

""",

"olle_direkt2.png"

)


olle_direkt_3 = Room("direkt  zur  Ollen",

"""

"Ok Big Hero.....malst du jetzt ein Bild für mich oder was?"

Die Olle lehnt sich zurück und bläst den Rauch Ihrer Kippe schräg nach oben in die Luft.


Drücke '1' um fortzufahren...
""",

"olle_direkt3.png"

)

direkt_keine_dose = Room("direkt  zur  Ollen",

"""

"F*** ing Loser....ich wusste es..."

Sie dreht sich um und spielt am Ihrem Handy. Du gehst frustriert wieder raus..

Drücke '1' um fortzufahren...


""",

"kein_bock.png"

)


olle_silberwasser = Room("Deeptalk  mit  der  Ollen",

"""
Also die Alte hat safe derbe einen an der Waffel soviel ist klar ist aber auch cool.

Dir fällt auf einmal ein, dass du ja das Silberwasser von Heyduck hast.

Du atmest einmal kurz durch und sagst: "Baby mach dir keine Sorgen wegen den Echsenmenschen. 
Lass uns sofort hier abhauen. Wenn Sie uns aufhalten wollen habe ich die Kräfte des magischen Silberwassers" und hälst die Flasche hoch. 

Die Olle sollte dir eigentlich ne Backpfeife geben, weil du einfach mehr als behindert bist. 
Allerdings macht sie das nicht und shrugged nur kurz. Ihr nehmt eure Sachen und wollt gerade gehen da sagt die Olle:

"Ich weiss nicht irgendwie habe ich noch voll Hunger. Ich hab voll Bock auf ne Pommes, am besten mit Mayo.
Kriegst du dass hin, mir eine Pommes zu besorgen?"

Drücke '1' um fortzufahren...

""",

"olle_direkt2.png"

)   

keine_pommes = Room("Keine  Pommes",
"""
Scheisse wie kommt die Alte den rein zufällig darauf, dass du jetzt eine Pommes dabei hast.

Hast du natürlich nicht.

Du bietest ihr an, dass ihr zusammen noch eine holen könnt aber irgendwie hat sie keinen Bock darauf. Warum auch immmer.

Naja egal. Du verabschiedest dich höflich und gehst wieder zum Eck. Die Olle bleibt sitzen.

Eventuell kriegst du ja echt irgendwo noch ne Pommes her.

Drücke '1' um fortzufahren...

""",
"olle_sad.png"
)

def enter_pommes_talk():
    global pommes_talk
    pommes_talk = True
    update_eck2_paths_4()
    
    
keine_pommes.on_enter = enter_pommes_talk


direkt_keine_pommes = Room("Keine  Pommes",
"""

Die Alte dreht sich um und rollt heftig mit den Augen.

Du drehst dich auch um und gehst raus aus dem Chinchilla..

Drücke '1' um fortzufahren...

""",

"olle_sad.png"

)


habe_pommes = Room ("Pommes!",

'''

Du die alte, eklige Pommes vom Werderimbiss dabei. Stolz präsentierst 
du Ihr diese. (wie auch immer du sie transportiert hast).

Die Olle guckt dich ziemlich weird an, feiert es dann aber mega, dass du Ihr Ihren Wunsch im Handumdrehen erfüllt hast. Sie sagt. "Alter! Mega treuer Macker. 
Noch nie war jemand so ein Mongo und hat ne Pommes einfach so für mich auf Tasche aber...hat aber auch irgendwas!"

"Ich denke ich kann dir helfen die Echsenmenschen zu besiegen. Allerdings habe ich dafür noch eine Bedingung. 
Ich komme gerade aus einer Beziehung und mein Ex hat viel Grafitti gemacht.Allerdings war er voll der Toy. 
Wenn du meinen Namen hier irgend ransprühen kannst und es besser als sein Scheiss aussieht, wäre das echt mega nice.....


Drücke '1' um fortzufahren...

''',

"olle_direkt3.png"

)

def enter_grafitti_talk():
    global grafitti_talk
    grafitti_talk = True
    update_eck2_paths_4()
    
habe_pommes.on_enter = enter_grafitti_talk

olle_dose= Room ("Dose?",

'''
Ihr Ernst?

Woher denn jetzt noch ne Dose nehmen und irgendein Bild für die Olle malen. Auf gar keinen Fall!

Allerdings ist die Olle aber schon heftig geil und du hast das Gefühl, dass Sie dir bei deiner Mission nützlich sein kann

Vielleicht findest du ja echt noch irgendwo ne Dose. Den Versuch wäre es auf jeden Fall wert.

Du gehst wieder raus, die Olle bleibt sitzen.

Drücke '1' um fortzufahren...

''',

"kein_bock.png"

)


insel = Room("Insel",

"""
Du bist an der Werderinsel. Ist nicht viel los hier. Du kannst zum Werderimbiss gehen, oder wieder zurück zum Eck.
(du gehst besser durch die kleinen Strassen und nicht am Bellini vorbei)

An der Haltestelle entdeckst du auch noch Maik Haller, der gerade auf die Bahn wartet. 

du kannst du auch ne Runde mit ihn reden.

1 = Maik Haller ansprechen
2 = zum Werderimbiss gehen
3 = Zurück zum Eck

""",
"insel.png")  


insel_2 = Room("Insel",

"""
Du bist wieder an der Insel. Der Werderimbiss hat schon zu und Haller ist auch abgehauen.

Du gehst durch die kleinen Strassen zurück zum Eck.

Drücke '1' um fortzufahren...


""",
"insel_2.png")  


haller = Room("Haller",

"""
"Moin wie gehts?"....dann fällt dir ein, dass ihr ihn in der Grundschule derbe gemobbt habt und er eventuell
nen kleinen Addi auf dich haben könnte.
                                    
Aber er ist mega cool und ihr redet ein bisschen über alte Zeiten, dies das. Obwohl er Bahn fährt, sieht er irgendwie nach Kohle aus.

Wenn du gerade nicht genug hast, könntest du ihn danach fragen... ist aber derbe peinlich. 
                                    
1 = Haller nach Money fragen
2 = "Ach nichts...."

""",
"haller.png")  

haller_money = Room("Schnorren",

"""
Es fühlt sich an wie die größte Schande aller Zeiten. Er denkt jetzt auf jeden Fall, du bist der letzte Junkie und dass er im Leben gewonnen hat.

Aber du fragst trotzdem...

Er guckt kurz komisch, ist aber mega korrekt und gibt dir 1.50 EUR. Auch ohne dummen Spruch oder irgendwas. 
Du hast auf jeden Fall nicht das Gefühl,dich blamiert zu haben. 

Allerdings jetzt nochmal nach mehr Money zu fragen, wäre richtig maskharrah...Auf gar keinen Fall!

Drücke '1' um fortzufahren...

""",
"haller_money.png") 

def enter_haller_money():
    global Money, Haller
    Money += 1.5
    Haller = True
    update_werderimbiss_paths()
    update_insel_paths()
   
haller_money.on_enter = enter_haller_money

haller_nix = Room("Ach  nix...",

"""
Gerade als du Fragen willst, überlegst du dir es anders und sagst besser nichts.
                               
Du hast zwar keine Money aber Ehre gesichert.....geiler Macker.
                                            
Genau als du dich umdrehen willst, checkst du dass der Kerl doch irgendwie ein Psycho ist.
Er guckt voll komisch und irgendwie ist seine ganze Erscheinung ziemlich cringe...
                                            
Gerade als die Bah kommt, fängt er auf einmal an zu lachen und schubst dich mit aller Kraft vor die Bahn.

Die Bahn ist trotz Haltestelle immernoch derbe schnell...das heisst du bist Hackfleisch.... Mies.

Drücke '1' um fortzufahren...

""",
"ach_nix.png") 


werderimbiss = Room("Werderimbiss",

"""

Im Werderimbiss arbeiten heute komische Leute...Die Pommes sind eigentlich auch richtig scheisse.

Aber egal...wer es feiert, feiert es halt.

Eine Pommes kostet genau 2.5. Hast du? 
                                    
1 = Pommes 
2 = Zurück zur Insel


""",

"werderimbiss.png"

)  


pommes = Room("Pommes",

"""

Cool. Du hast dir gerade eine richtig eklige Pommes mit Mayo gegönnt...du gehst damit zurück zum Eck.

Drücke '1' um fortzufahren...

""", 
"pommes.png"
)  

def enter_pommes():
    global Pommes
    Pommes = True
    update_olle_silberwasser_paths()
    update_olle_direkt_paths()
    update_after_fight_paths()
    
   
pommes.on_enter = enter_pommes

no_money = Room("Broke",

"""

Ekliger Mensch! Noch nicht mal Geld für ne Pommes Warak. Hau ab.


Drücke '1' um fortzufahren...

""",

"no_money.png")  

not_enough = Room("Mach  richtig",

"""

Warum machst du so? mach richtig yau. Mit diese ganze Geld.


Drücke '1' um fortzufahren...

""",

"not_enough.png")  


finished = Room("Herzlichen  Glückwunsch!",

"""

Du bist auf jeden Fall ein heftiger Macker!

Du hast direkt ne Dose dabei. Du zeigst ihr die Dose und sagst, dass du ready für alles bist.

Sie findet es einfach nur geil und geht voll darauf ab

Allerdings hast du voll keinen Bock jetzt so den Hampelmann für die Olle zu machen. Deswegen schlägst du vor das du ihr ein viel geileres Bild malen kannst 
wenn ihr zu dir geht.

Passt perfekt! Als Ihr am Dobben vorbei geht, zeigt die Olle auf das Streetbombing und sagt dass es von Ihrem Ex ist.  

Ein Flugzeug fliegt noch kurz übers Steine und alle Echsenmenschen lösen sich in Luft auf. 

Herzlichen Glückwunsch. Du hast die derbste Olle mitgenommen, das Spiel durchgespielt und das Steintor gerettet.

THE END

""",

"finished.png")  

the_end  = Room("Congratulations",

"""
""",
"the_end.png")  




deeptalk_heyduck.add_paths({
    '1': chemtrails,
    '2': silberwasser
})


lu.add_paths({
    "1": deeptalk_heyduck, 
    "2": eck2
})

chemtrails.add_paths({
    "1":eck2
   
})

lu_dicht.add_paths({
    "1":eck2  
})

heyduck_again.add_paths({
    "1":chemtrails,
    "2":silberwasser 
})

dobben.add_paths({

    "1":grafitti,
    "2":schiss,
    "3":eck2
   
})

grafitti.add_paths({

    "1":eck2,
   
})



after_grafitti.add_paths({

    "1":eck2,
   
})

bellini.add_paths({
    '1': no_fight,
    '2': friedensrichter,
    '3': eck2,
    '4': insel
})

def update_bellini_paths():
    if Silver:
        bellini.paths['1'] = fight     
    else:
        bellini.paths['1'] = no_fight

no_fight.add_paths({
    "1": eck2 
})

fight.add_paths({
    "1": insel
})

after_fight.add_paths({
    "1": insel
})

def update_after_fight_paths():
    if Pommes:
        after_fight.paths['1'] = insel_2
    else:
        after_fight.paths['1'] = insel


insel.add_paths({
    '1': haller,
    '2': werderimbiss,
    '3': eck2,
})

def update_insel_paths():
    if not Haller:
        insel.paths['1'] = haller
    else:
        insel.paths['1'] = haller_nix


insel_2.add_paths({
    '1': eck2,
})

haller.add_paths({
    '1': haller_money,
    '2': haller_nix,
})

haller_money.add_paths({
    '1': insel,
})


werderimbiss.add_paths({
    '1': no_money,
    '2': insel
})

def update_werderimbiss_paths():
    global Money
    if Money >= 2.5:
        werderimbiss.paths['1'] = pommes
    elif Money > 0:
        werderimbiss.paths['1'] = not_enough
    else:
        werderimbiss.paths['1'] = no_money


pommes.add_paths({
    '1': eck2,
})

no_money.add_paths({
    '1': insel
})

not_enough .add_paths({
    '1': insel
})


chinchilla.add_paths({
    "1": drink,
    "2": kein_drink
})
  
olle_direkt.add_paths({
    "1" : olle_silberwasser
})

def update_olle_direkt_paths():
    if not Silver:
        olle_direkt.paths['1'] = kein_bock
    else:
        olle_direkt.paths['1'] = olle_silberwasser


olle_direkt_2.add_paths({
    "1" : direkt_keine_pommes 
})       

def update_olle_direkt_paths():
    if Pommes:
        olle_direkt_2.paths['1'] = habe_pommes
    else:
        olle_direkt_2.paths['1'] = direkt_keine_pommes 


direkt_keine_pommes.add_paths({
    '1': eck2
})


olle_direkt_3.add_paths({
    '1': direkt_keine_dose
})

def update_olle_direkt_3_paths():
    if Dose:
        olle_direkt_3.paths['1'] = finished
    else:
        olle_direkt.paths['1'] = direkt_keine_dose

direkt_keine_dose.add_paths({
    '1': eck2
})

kein_drink.add_paths({
    '1': kein_bock
})

def update_kein_drink_paths():
    if not Silver:
        kein_drink.paths['1'] = kein_bock  
    else:
        kein_drink.paths['1'] = olle_silberwasser 
        

olle_silberwasser.add_paths({
    '1': keine_pommes
    })

keine_pommes.add_paths({
    '1': eck2
    })

habe_pommes.add_paths({
    '1': olle_dose
    })
def update_habe_pommes_paths(): 
    if Dose:
        habe_pommes.paths['1'] = finished
    else:
        habe_pommes.paths['1'] = olle_dose

olle_dose.add_paths({
    '1': eck2
    })

def update_olle_silberwasser_paths():
    if Pommes:
        olle_silberwasser.paths['1'] = habe_pommes
    else:
        olle_silberwasser.paths['1'] = keine_pommes

kein_bock.add_paths({
    '1': eck2
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
    '3': etwas_fehlt_bellini,
    '4': chinchilla
})

def update_eck2_paths():
    if not Silver:
        eck2.paths['2'] = etwas_fehlt_dobben
    elif Dose:
        eck2.paths['2'] = after_grafitti
    else:
        eck2.paths['2'] = dobben

def update_eck2_paths_2():
    if Chemtrails and Silver:
        eck2.paths['1'] = lu_dicht
    elif Chemtrails and not Silver or Silver and not Chemtrails:
        eck2.paths['1'] = heyduck_again
    else:
        eck2.paths['1'] = lu
    
def update_eck2_paths_3():
    if not Olle:
        eck2.paths['3'] = etwas_fehlt_bellini
    elif bellini_fight:
        eck2.paths['3'] = after_fight
    else:
        eck2.paths['3'] = bellini

def update_eck2_paths_4():

    if pommes_talk and Silver and grafitti_talk:
        eck2.paths['4'] = olle_direkt_3

    elif pommes_talk and Silver and not grafitti_talk:
        eck2.paths['4'] = olle_direkt_2
    elif Olle and Silver:
        eck2.paths['4'] = olle_direkt
    elif Olle and not Silver and not grafitti_talk:
        eck2.paths['4'] = olle_direkt
    else:
        eck2.paths['4'] = chinchilla

def update_eck2_paths_5():
    if bellini_fight:
        eck2.paths['3'] = after_fight
    else: 
        eck2.paths['3'] = bellini


etwas_fehlt_dobben.add_paths({
    '1':eck2
})

etwas_fehlt_bellini.add_paths({
    '1':eck2
})


friedensrichter.add_paths({
    '1':tot
})

schiss.add_paths({
    '1':tot
})

haller_nix.add_paths({
    '1':tot
})

drink.add_paths({
    '1':tot
})

tot.add_paths({
    '1':start
})

start.add_paths({
    '1':eck
})

START = 'start'

def load_room(name):
    """
    There is a potential security problem here.
    Who gets to set name? Can that expose a variable?
    """
    return globals().get(name)

def name_room(room):
    """
    Same possible security problem. Can you trust room? What's a better solution than this global lookup?
    """
    for key, value in globals().items():
        if value == room:
            return key
