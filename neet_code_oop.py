class Pet:
    def __init__ (self, name:str, species:str):
        self.name = name
        self.species = species

# Do not modify below this line
my_pet = Pet("Fluffy", "cat")
print(f"My pet is a {my_pet.species} named {my_pet.name}")

class Pet:
    def __init__(self, name: str, species: str, hunger: int, energy: int):
        self.name = name
        self.species = species
        self.hunger = hunger
        self.energy = energy

# Don't modify the above code

# TODO: Create a pet named "Whiskers" that is a species of 'cat' with hunger level 6 and energy level 8
whiskers = Pet('Whiskers', 'cat', 6, 8)

# Don't modify the following code
print(f"{whiskers.name} ({whiskers.species}) - Hunger: {whiskers.hunger}, Energy: {whiskers.energy}") 

class Pet:
    def __init__(self, name: str, species: str, hunger: int, energy: int):
        self.name = name
        self.species = species
        self.hunger = hunger
        self.energy = energy

whiskers = Pet("Whiskers", "cat", 6, 8)

# TODO: Print Whiskers' initial attributes
print(f"Initial Attributes: {whiskers.name} ({whiskers.species}) - Hunger: {whiskers.hunger}, Energy: {whiskers.energy}")
# TODO: Modify Whiskers' attributes:
#  - Decrease hunger by 3
whiskers.hunger = 3
#  - Increase energy by 2
whiskers.energy = 10
# TODO: Print Whiskers' modified attributes
print(f"Modified Attributes: {whiskers.name} ({whiskers.species}) - Hunger: {whiskers.hunger}, Energy: {whiskers.energy}")

