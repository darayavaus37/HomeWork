#hdfgbjfdjvbdfjh
#fghhjhvhjfjh
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


      
