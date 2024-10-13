class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def get_name(self):
        return self.name

    def double_health(self):
        self.health_points *= 2

    def __str__(self):
        return f"{self.nickname}: {self.superpower}, Health: {self.health_points}"

    def catchphrase_length(self):
        return len(self.catchphrase)


hero = SuperHero("Clark Kent", "Superman", "Flying", 100, "I'm here to save the day!")


print(hero.get_name())
hero.double_health()
print(hero)
print(f"Length of catchphrase: {hero.catchphrase_length()}")

class Hulk(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, super_hit, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.super_hit = super_hit
        self.fly = fly

    def duble_health(self):
        self.health_points = self.health_points ** 2
        self.fly = True
        return self.health_points, self.fly

    def __str__(self):
        return (f'меня зовут {self.name}, но все меня знают как {self.nickname}\n'
                f'мои суперспособности как у {hero.nickname}но cлабее {self.superpower}\n'
                f' мое хп {self.health_points}\n'
                f'коронная фраза {self.catchphrase}')

    def flyy(self):
        return f'я не умею летать но могу прыгать'

    def phrase(self):
        return 'True in the True_phrase'


hulk = Hulk('Робет Брюс Беннер', 'Халк'
            , 'летать, бить, гнев', 6000,
            'Не зли меня а то убью', 2000)
print(hulk)
print(hulk.phrase())
print(hulk.flyy())
print(hulk.duble_health())

class Betmen(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, super_hit, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.super_hit = super_hit
        self.fly = fly

    def duble_health(self):
        self.health_points = self.health_points ** 2
        self.fly = True
        return self.health_points, self.fly

    def __str__(self):
        return (f'меня зовут {self.name}, но все меня знают как {self.nickname}\n'
                f'мои суперспособности это {self.superpower}\n'
                f' мое здоровье {self.health_points}\n'
                f'коронная фраза {self.catchphrase}')

    def flyy(self):
        return f'я летаю но только хлопками'

    def phrase(self):
        return 'True in the True_phrase'

bruse = Betmen('Брюс Уэйн', 'Бэтмен', 'тратить деньги и зашищать', 6000, 'Я работаю только один', None, '500 метров')

print(bruse)
class Villain(Hulk):
    people = 'monster'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, super_hit, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase, super_hit, fly)
        self.damage = damage

    def __str__(self):
        return (f'меня зовут {self.name}, но все меня знают как {self.nickname}\n'
                f'мои суперспособности это {self.superpower}\n'
                f' мое здоровье {self.health_points}\n'
                f'коронная фраза {self.catchphrase}\n'
                f'урон: {self.damage}')


    def gen_x(self):
        pass

    def crit(self):
        self.damage = self.damage ** 2
        return self.damage

kloun = Villain('James', 'Joker', 'обманывать и убивать',
             3000, 'xa-xa-xa-xa', 'punch', 4000)

print(kloun.crit())
print(kloun)
print(kloun.duble_health())