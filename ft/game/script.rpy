

define e = Character('Эйлин', color="#021b02")
define v = Character('Василий', color="#f70202", image='leo')
define vi = Character('Василина', color="#a8e600", image='saki')

init:
    $ right2 = Position(xalign=0.85,yalign=1.0)
    $ left2 = Position(xalign=0.55,yalign=1.0)


label start:

    scene bg class
    with fade

    show leo smiling at right2
    with dissolve
    
    show saki curious at left2
    with moveinleft

    v "Привет, давай знакомиться"
    vi @ worried "Я не ем морковку, спасибо"
    v blush"Это у меня только шапка морковная, внизу — {w=2} угольная шахта"
    vi angry "Катись к чёрту"
    show saki surprised
    extend " витамин D на ножках"

    vi '''
    Производим длинный

    Бабский монолог

    Проверка сплочения блоков
    
    Внутри тройных кавычек
    '''

    v sad "ёбаный вагинокапитализм"  


    hide leo with dissolve
    hide saki with moveoutleft

    #scene bg room with pushleft
    #scene bg school with wipeleft
    #with blinds

    "Creator" "Pause"
    return