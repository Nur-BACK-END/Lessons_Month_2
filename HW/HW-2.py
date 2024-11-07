from main import Hero

class Archer(Hero):
    def __init__(self, name, health, arrows=20):
        super().__init__(name, health)
        self.arrows = arrows

    def arrow(self):
        if self.arrows > 0:
            self.arrows -= 1
            return f"{self.name} выпускает стрелу! Осталось стрел: {self.arrows}"
        else:
            return f"{self.name} закончились стрелы!"

    def action(self):
        action_message = super().action()
        arrow_message = self.arrow()
        return f"{action_message}\n{arrow_message}"

def hero_action(hero):
    print(hero.introduce())
    print(hero.rest())
    print(hero.action())

archer = Archer("Купидон", 100)

hero_action(archer)
