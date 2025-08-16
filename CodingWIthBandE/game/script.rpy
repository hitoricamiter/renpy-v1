define e = Character("Враг")
define p = Character("Игрок")

init python:
    # Классы
    class Skill:
        def __init__(self, name, damage, cost=0):
            self.name = name
            self.damage = damage
            self.cost = cost

    class CharacterStat:
        def __init__(self, name, hp, attack, skills):
            self.name = name
            self.max_hp = hp
            self.hp = hp
            self.attack = attack
            self.skills = skills

    # Скиллы
    slash = Skill("Удар", 15)
    fireball = Skill("Огненный шар", 30, cost=10)

    # Персонажи
    player = CharacterStat("Герой", 100, 10, [slash, fireball])
    enemy = CharacterStat("Гоблин", 50, 8, [])

    # Инвентарь
    inventory = {"Зелье": 3}

    # Функции боя
    def attack(attacker, target, skill=None):
        if skill:
            dmg = skill.damage
        else:
            dmg = attacker.attack
        target.hp -= dmg
        if target.hp < 0:
            target.hp = 0
        return dmg

    def use_item(item_name, target):
        if inventory.get(item_name, 0) > 0:
            if item_name == "Зелье":
                target.hp += 30
                if target.hp > target.max_hp:
                    target.hp = target.max_hp
            inventory[item_name] -= 1
            return True
        return False

label start:
    scene black

    jump battle

label battle:
    $ turn = "player"
    while player.hp > 0 and enemy.hp > 0:

        if turn == "player":
            menu:
                "Атаковать обычным ударом":
                    $ dmg = attack(player, enemy)
                    "Вы нанесли [dmg] урона [enemy.name]! У врага осталось HP: [enemy.hp]"
                    $ turn = "enemy"

                "Использовать навык":
                    menu:
                        "Удар":
                            $ dmg = attack(player, enemy, slash)
                            "Вы использовали Удар! Урон: [dmg]. У врага осталось HP: [enemy.hp]"
                            $ turn = "enemy"
                        "Огненный шар":
                            $ dmg = attack(player, enemy, fireball)
                            "Вы применили Огненный шар! Урон: [dmg]. У врага осталось HP: [enemy.hp]"
                            $ turn = "enemy"

                "Использовать предмет":
                    menu:
                        "Зелье ([inventory.get('Зелье',0)] осталось)":
                            $ used = use_item("Зелье", player)
                            if used:
                                "Вы использовали Зелье. Ваше HP: [player.hp]"
                            else:
                                "Зелий больше нет!"
                            $ turn = "enemy"

        else:
            # Враг атакует
            $ dmg = attack(enemy, player)
            "[enemy.name] атакует вас и наносит [dmg] урона! Ваше HP: [player.hp]"
            $ turn = "player"

    if player.hp <= 0:
        "Вы были повержены..."
        return
    else:
        "[enemy.name] побеждён!"
        return
