

define e = Character('Эйлин', color="#021b02")
define v = Character('Василий', color="#d11e78")
define vi = Character('Василина', color="#da27a4")


label start:

    scene bg class

    show leo normal
    v "Привет!"
    hide leo

    show saki curious
    vi "Привет, что ты тут забыл?"

    scene bg corridor
    with fade

    show leo angry
    v "Как тут грязно! Пошли к тебе домой!"
    
    scene bg room
    with fade 
    show agustina smile

    "Creator" "Ive been waiting for you so long time!"

    
  
    return