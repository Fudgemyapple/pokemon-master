import random


class Pokemon():
    def __init__(self, name, species, level, max_hp, current_hp, poki_type, consious, ap, owner):
        self.name = name
        self.species = species
        self.level = level
        self.max_hp = max_hp 
        self.type = type 
        self.current_hp = current_hp
        self.consious = consious
        self.ap = ap
        self.owner = owner
    
    def __repr__(self):
        return "This Pokimon is a level {level} {species} called {name}. It belongs to {owner}".format(level = self.level, species = self.species, name = self.name, owner = self.owner)

    

class Trainer():
    def __init__(self, name,):
        self.name = name
        self.owned_pokimon = []

    def __repr__(self):
        return self.name    
   
    def pokemon_generator(self, name, species, level):
        max_hp = random.randint(80, 120)
        current_hp = max_hp
        ap = random.randint(15, 40)
        pokemon_types = {"charmander": "fire", "squirtle": "water", "bulbasaur": "grass"}
        poki_type = pokemon_types[species]
        name = Pokemon(name, species, level, max_hp, current_hp, poki_type , True, ap, self)
        self.owned_pokimon.append(name)

    def training_battle(pokimon_1, pokemon_2)
    


ash = Trainer("Ash")

ash.pokemon_generator("poki1", "charmander", 10)
ash.pokemon_generator("poki2", "squirtle", 10)