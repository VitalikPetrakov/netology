# Исправил вывод имени самого большого животного
class Animal:
    all_weight = 0
    weight_animal = 0
    name_weight_animal = ''

    def __init__(self, weight, name):
        self.weight = weight
        self.name = name
        Animal.all_weight += weight
        if weight > Animal.weight_animal:
            Animal.weight_animal = weight
            Animal.name_weight_animal = name

    def voise(self):
        print('голос животного')

    def eating(self):
        print('кормежка животного')


class Birds(Animal):
    def __init__(self, weight, name):
        super().__init__(weight, name)
        self.weight = weight
        self.name = name

    def voise(self):
        print('голос птицы')

    def eating(self):
        print('кормежка птицы')

    def egg_laying(self):
        print('птица несет яйца')


class Goose(Birds):
    def __init__(self, weight, name):
        super().__init__(weight, name)
        self.weight = weight
        self.name = name

    def voise(self):
        print('Га-га-га')

    def eating(self):
        print('Ем зерно')

    def egg_laying(self):
        print('Несу яйца')


class Chiken(Birds):
    def __init__(self, weight, name):
        super().__init__(weight, name)
        self.weight = weight
        self.name = name

    def voise(self):
        print('Ку-ка-ре-ку')

    def eating(self):
        print('Ем зерно')

    def egg_laying(self):
        print('Несу яйца')


class Duck(Birds):
    def __init__(self, weight, name):
        super().__init__(weight, name)
        self.weight = weight
        self.name = name

    def voise(self):
        print('Кряяяяя-Кряяяяя')

    def eating(self):
        print('Ем зерно')

    def egg_laying(self):
        print('Несу яйца')


class MilkAnimal(Animal):
    def __init__(self, weight, name):
        super().__init__(weight, name)
        self.weight = weight
        self.name = name

    def voise(self):
        print('голос парнокопытного с молоком')

    def eating(self):
        print('кормежка парнокопытного с молоком')

    def milking(self):
        print('дойка парнокопытного с молоком')


class Cow(MilkAnimal):
    def __init__(self, weight, name):
        super().__init__(weight, name)
        self.weight = weight
        self.name = name

    def voise(self):
        print('Му-му-му')

    def eating(self):
        print('Ем сено')

    def milking(self):
        print('Даю 2 литра вкусного коровьего молока')


class Goat(MilkAnimal):
    def __init__(self, weight, name):
        super().__init__(weight, name)
        self.weight = weight
        self.name = name

    def voise(self):
        print('Ме-ме-ме')

    def eating(self):
        print('Ем сено')

    def milking(self):
        print('Даю 0.5 литра вкусного козьего молока')


class Sheep(Animal):
    def __init__(self, weight, name):
        super().__init__(weight, name)
        self.weight = weight
        self.name = name

    def voise(self):
        print('Бе-бе-бе')

    def eating(self):
        print('ем траву')

    def shearing(self):
        print('стрижка овцы')


goose_2 = Goose(weight=11, name='Белый')
sheep_1 = Sheep(weight=50, name='Барашек')
chiken_1 = Chiken(weight=5, name='Ко-Ко')
chiken_2 = Chiken(weight=6, name='Кукареку')
goat_1 = Goat(weight=40, name='Рога')
goat_2 = Goat(weight=45, name='Копыта')
duck = Duck(weight=8, name='Кряква')
goose_1 = Goose(weight=10, name='Серый')
cow = Cow(weight=500, name='Манька')
sheep_2 = Sheep(weight=55, name='Кудрявый')
sheep_1.shearing()
cow.milking()
chiken_1.egg_laying()
goat_1.milking()

print(f'Общий вес животных на ферме: {Animal.all_weight}')
print(f'Имя самого тяжелого животного: {Animal.name_weight_animal}')
