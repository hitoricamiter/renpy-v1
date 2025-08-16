label start:

    scene bg class with fade

    n "Давным-давно в далекой далекой галактике"

    nvl hide

    $ viname = renpy.input("Введите имя персонажа: ", length = 12, allow="йцукенгшшАшшщзхххъфывапролджэячсмитьбю-ЙЦУКЕНГШЩЗХФЫВАПРОЛДЖЭЯЧСМаИТЬБЮ-", default = "Мухамед").strip()

    if viname.strip() == '':
        $ viname = 'Мухамед'

    show leo smiling at right2 with dissolve 
    show saki curious at left2 with moveinleft

    #"{color=#26c218}текст{/color} {i}Тестим кавычки{/i} \"{b}Предохранитель{/b}\" {u}underlinetext{/u} {s} зачеркнутый текст {/s}"

    vi "Тестим side картинку"
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
        "Потратить деньги мужа? У него на карте 150 тысяч"

        "Да. Купить себе машину?":
            call withdrawMoney
            "[viname] Снимает деньги с карты"

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

        "Сказать спасаибо что не потратила все деньги с карты" if cash > 100:
            "Спасибо тупая шлюха"
            jump dontbreakup




    return

label withdrawMoney:

    $ money = renpy.input("Сколько денег снять с карты?", length=3, allow="0123456789").strip() or "0"
    $ money = int(money)
    if money > 150:
        $ money = 150

    "Было [cash] на карте"
    "Было снято [money] тысяч с карты"
    $ cash = cash - money
    "Осталось [cash] рублей"

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