# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Dog:
    def __init__(self, name, lvl):
        self.name = name
        self.lvl = lvl
        self.attack = 1
        self.defense = 1
        self.max_health = 1
        self.curr_health = 1

    def __str__(self):
        return f"{self.name} is at level {self.lvl}"

    def show_stats(self):
        return f"{self.name} is at level {self.lvl}\n{self.name}s stats are:\n\tAttack: {self.attack}\n\tDefense: {self.defense}\n\tHealth: {self.curr_health}/{self.max_health}\n"

    def speak(self, sound):
        return f"{self.name} says {sound}"

    def deal_dmg(self, target, damage):
        target.take_dmg(damage)
        return f"{self.name} deals {damage} damage to {target.name}.\n"

    def take_dmg(self, damage):
        self.curr_health -= damage
        if self.curr_health <= 0:
            self.curr_health = 0
            return f"{self.name} takes {damage} and is defeated.\n"
        return f"{self.name} takes {damage} damage.\n"

    def bite(self, target):
        return self.deal_dmg(target, self.attack)

    def special_attack(self, target):
        return f"{self.name} has no special attack. Nothing happens.\n"


class Bulldog(Dog):

        def __init__(self, name, lvl):
            unit = Dog
            self.name = name
            self.lvl = lvl
            self.attack = 5
            self.defense = 3
            self.max_health = 35
            self.curr_health = self.max_health

        def special_attack(self, target):
            self.deal_dmg(target, self.attack * 4)
            return f"{self.name} tries to bite {target.name}s head off and deals {self.attack * 4} damage.\n"


class Bernadina(Dog):

    def __init__(self, name, lvl):
        unit = Dog
        self.name = name
        self.lvl = lvl
        self.attack = 4
        self.defense = 8
        self.max_health = 42
        self.curr_health = self.max_health

    def special_attack(self, target):
        self.deal_dmg(target, self.defense * 2)
        return f"{self.name} tackles {target.name} with his hardnened fur and deals {self.defense * 2} damage.\n"


class Laprador(Dog):

    def __init__(self, name, lvl):
        unit = Dog
        self.name = name
        self.lvl = lvl
        self.attack = 3
        self.defense = 5
        self.max_health = 50
        self.curr_health = self.max_health

    def special_attack(self, target):
        target.curr_health += round(self.max_health * 0.6)
        if target.curr_health > target.max_health:
            target.curr_health = target.max_health
        return f"{self.name} is caring {target.name}s wounds and restores {round(self.max_health * 0.6)} health.\n"


def main():
    player = Bulldog("Hasan", 1)
    enemy = Bernadina("Spüli", 1)
    print(player.show_stats())
    print(enemy.show_stats())
    print(player.bite(enemy))
    print(enemy.show_stats())
    print(enemy.bite(player))
    print(player.show_stats())
    print(player.special_attack(enemy))
    print(enemy.show_stats())
    print(enemy.special_attack(player))
    print(player.show_stats())
    print(player.special_attack(enemy))
    print(enemy.show_stats())


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
