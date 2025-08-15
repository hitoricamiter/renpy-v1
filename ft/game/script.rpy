

define e = Character('Эйлин', color="#021b02")
define v = Character('Василий', color="#f70202", image='leo')
define vi = Character('[viname]', color="#a8e600", image='saki')

# Оскорбление мужа
define husbandInsult = False
define familyMoneySold = False 



init:
    $ right2 = Position(xalign=0.85,yalign=1.0)
    $ left2 = Position(xalign=0.55,yalign=1.0)


label start:

    scene bg class with fade

    menu:
        "какой логотип будет?"

        "{image=images/images.png}":
            "Пингквин"

        "{image=images/images.png}":
            "Идиот"

    $ viname = renpy.input("Введите имя персонажа: ", length = 12, allow="йцукенгшшАшшщзхххъфывапролджэячсмитьбю-ЙЦУКЕНГШЩЗХФЫВАПРОЛДЖЭЯЧСМаИТЬБЮ-", default = "Мухамед").strip()

    if viname.strip() == '':
        $ viname = 'Мухамед'

    show leo smiling at right2 with dissolve 
    show saki curious at left2 with moveinleft

    "{color=#26c218}текст{/color} {i}Тестим кавычки{/i} \"{b}Предохранитель{/b}\" {u}underlinetext{/u} {s} зачеркнутый текст {/s}"

    "[viname] {image=images/girl/girl blush.png} хочет сделать сеппуку"
    "ходит на пары а после проводит время с любовником"
    menu:
        "Оскорбить мужа?"

        "Назвать его ничтожеством?":
            "[viname] чмырит мужа по полной"
            $ husbandInsult = True

        "Уважительно о нем говорить?":
            "[viname] не хочет оскорблять мужа"

    menu:
        "Потратить деньги мужа?"

        "Да. Купить себе машину?":
            "[viname] покупает новенькую бентли"
            $ familyMoneySold = True

        "Не тратить деньги, воздержаться":
            "[viname] решила сохранить деньги мужа"



    "муж узнает об измене"

    menu: 
        "Что делать?"

        "Расстаться с мужем":
            jump breakup
        
        "Не расставаться с мужем":
            jump dontbreakup

        "Убить мужа" if husbandInsult and familyMoneySold:
            "Она убила и съела мужа."




    return

label breakup:

    if husbandInsult and familyMoneySold:
        "Василиса была засужена, потраченные деньги стали последней каплей он задушил её в гневе."
    elif husbandInsult or familyMoneySold:
        "Муж зол и не позволит ей развестись мирно"
    else:
        "Развод прошел достаточно спокойно"

    return

label dontbreakup:

    if husbandInsult:
        "Муж слышал оскорбления и не готов простить Василину"
        "Она решает повеситься"
    else: 
        "Василиса решает всё исправить"

    return