import random

# dependence factors
startingPopulation = 50
growthFactor = 1.00005
infantMortality = 5
agricultural_production = 5 # 5 unit of food and one person use 1 unit per year
disaster_chance = 10  #means 10% 1 after 10 years
fertility_start = 18  # these are age a women can become pregrant ranging from m18 to 35 
fertility_end = 35
food = 0
totalPopulation = []

class Person:
    def __init__(self, age):
        self.gender = random.randint(0,1)
        self.age = age
        self.pregnant = 0

# a person of age of 8+ is capable of producing food

def harvest(food, agricultural_production):
    able_people = 0
    for person in totalPopulation:
        if person.age > 8:
            able_people += 1
    food += able_people + agricultural_production

    if food < len(totalPopulation):
        del totalPopulation[0:int(len(totalPopulation)-food)]
        food = 0
    else:
        food -= len(totalPopulation)

def reproduce(fertility_start, fertility_end):
    for person in totalPopulation:
        if person.gender == 1:
            if person.age > fertility_start:
                if person.age < fertility_end:
                    if random.randint(0,5) == 1:
                        if random.randint(0,100) > infantMortality:
                            totalPopulation.append(Person(0))



def start_simulation():
    for person in range(startingPopulation):
        totalPopulation.append(Person(random.randint(18,50)))



def run_year(food, agricultural_production, fertility_start, fertility_end,infantMortality,disaster_chance):
    harvest(food, agricultural_production)
    reproduce(fertility_start, fertility_end)
    for person in totalPopulation:
        if person.age > 80:
            totalPopulation.remove(person)
        else:
            person.age += 1
    if random.randint(0,100) < disaster_chance:
        del totalPopulation[0:int(random.uniform(0.05, 0.2) * len(totalPopulation))]
    persons_age = []
    for person in totalPopulation:
        persons_age.append(person.age)
    print(persons_age)

    infantMortality *= 0.985
    return [infantMortality, persons_age]

def run_simulation():
    start_simulation()
    infantMortality = 5
    populations = []
    while len(totalPopulation) < 100000 and len(totalPopulation) > 1:
        data = run_year(food,agricultural_production,fertility_start, fertility_end,infantMortality,disaster_chance)
        infantMortality = data[0]
        populations.append(data[1])
    return populations