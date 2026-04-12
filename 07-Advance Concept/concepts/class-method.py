class Animal:
    species = 'mammal'

    @classmethod
    def set_name(cls, newname):
        cls.species = newname
    @classmethod
    def get_species(cls):
        return cls.species
    
Animal.set_name('dog')
print(Animal.get_species())