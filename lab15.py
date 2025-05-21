class Character:
    def __init__(self, name, level, health, attack):
        self.name = name
        self.level = level
        self.health = health
        self.attack = attack

    def print_info(self):
        print(f"Ім'я: {self.name}")
        print(f"Рівень: {self.level}")
        print(f"Здоров'я: {self.health}")
        print(f"Атака: {self.attack}")

    def attack_enemy(self, enemy):
        print(f"{self.name} атакує {enemy.name} і завдає {self.attack} шкоди.")
        enemy.health -= self.attack
        if enemy.health <= 0:
            enemy.health = 0
            print(f"{enemy.name} загинув.")
        else:
            print(f"У {enemy.name} залишилось {enemy.health} здоров'я.")


class Warrior(Character):
    def __init__(self, name, level, health, attack, armor):
        super().__init__(name, level, health, attack)
        self.armor = armor

    def heal(self):
        self.health += 10
        print(f"{self.name} відновив здоров'я. Тепер: {self.health}")


class Mage(Character):
    def __init__(self, name, level, health, attack, mana):
        super().__init__(name, level, health, attack)
        self.mana = mana

    def heal(self):
        self.health += 15
        print(f"{self.name} відновив здоров'я за допомогою магії. Тепер: {self.health}")


class Archer(Character):
    def __init__(self, name, level, health, attack, arrows):
        super().__init__(name, level, health, attack)
        self.arrows = arrows

    def heal(self):
        self.health += 8
        print(f"{self.name} перев'язав рани. Здоров'я тепер: {self.health}")


# Демонстрація
if __name__ == "__main__":
    hero1 = Warrior("Богдан", 5, 100, 20, armor=15)
    hero2 = Mage("Мирослава", 4, 80, 25, mana=100)
    hero3 = Archer("Тарас", 3, 90, 18, arrows=30)

    print("=== ІНФОРМАЦІЯ ПРО ПЕРСОНАЖІВ ===")
    hero1.print_info()
    print("------")
    hero2.print_info()
    print("------")
    hero3.print_info()

    print("\n=== БІЙ ===")
    hero1.attack_enemy(hero2)
    hero2.attack_enemy(hero1)
    hero3.attack_enemy(hero1)

    print("\n=== ВІДНОВЛЕННЯ ЗДОРОВ'Я ===")
    hero1.heal()
    hero2.heal()
    hero3.heal()
