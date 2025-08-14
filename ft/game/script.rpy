

define e = Character('Эйлин', color="#021b02")
define v = Character('Василий', color="#f70202", image='leo')
define vi = Character('Василина', color="#a8e600", image='saki')

init:
    $ right2 = Position(xalign=0.85,yalign=1.0)
    $ left2 = Position(xalign=0.55,yalign=1.0)


label start:

    scene bg class with fade
    show leo smiling at right2 with dissolve 
    show saki curious at left2 with moveinleft

    "Василина студентка с любовником"
    "ходит на пары а после проводит время с любовником"
    "муж узнает об измене"

    menu: 
        "Что делать?"

        "Расстаться с мужем":
            jump breakup
        
        "Не расставаться с мужем":
            jump dontbreakup

    return

label breakup:

    "Василина решает расстаться с мужем"

    return

label dontbreakup:
    "василиса решает все исправить"

    return