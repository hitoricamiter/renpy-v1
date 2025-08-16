define e = Character('Эйлин', color="#021b02")
define v = Character('Василий', color="#f70202", image='leo')
define vi = Character('[viname]', color="#a8e600", image='saki')
define n = Character(None, kind=nvl)


define cash = 150

# Оскорбление мужа
define husbandInsult = False
define familyMoneySold = False 



init:
    $ right2 = Position(xalign=0.85,yalign=1.0)
    $ left2 = Position(xalign=0.55,yalign=1.0)