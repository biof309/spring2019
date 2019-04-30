class Creature():
    
    #the equals I am putting here represent what the default will be if nothing is passed
    def __init__(self, name, health=10, level=1):
        self.name = name
        self.health = health
        self.level = level
        
    def receive_damage(self,damage):     #we'll talk about why I am writing this this way in a second.
        self.health = self.health - damage
    
    #let's test: if you import it later, it won't run
    if __name__ == '__main__':
        a_hero = Creature("Jordyn")
        print(a_hero.name)
