import random

# BUG: the ants are finishing the food in the first day, check needed

# TODO: add food availability: normal, scarse, starvation
# TODO: add casualties (humans, predators, weather)

id = 0 # ant's ID starts from 0 and goes on
colony = [] # list of ants in the colony
workers = 0
queens = 0
soldiers = 0
males = 0
females = 0
deadcounts = 0
queens = 0
# maleska = True # is there males? 'ka' is the question particle in japanese, in the beginning is true even if we got only the queen because we caount that the queen is layin the eggs

# OPTIONS
food = 10 # starting food
max_eggs = 100 # max eggs layable per day
season = 'spring' # starting season

# "Actual" counters
act_workers = 0
act_soldiers = 0


class ant: 
    def __init__(self):
        global id
        self.id = id
        id += 1
        self.life = random.randint(20,40)  # ant's lifespan in days
        self.gender = random.choice('m' 'f') # ant's gender, M = male, F = female
        self.starving = 0 # how many days without eating?              
    def eat(self):
        global food
        if food >= 1:
                food -= 1
        else:
                self.starving += 1


class queen(ant):
        def __init__(self):
                global queens
                super().__init__()
                self.life = random.randint(1095,1460) # quenn's lifespan is longer
                self.gender = 'f' # queens are only female
                self.type = 'queen'
                queens += 1

class soldier(ant):
        def __init__(self):
                super().__init__()
                self.type = 'soldier'

class worker(ant):
        def __init__(self):
                super().__init__()
                self.gender = 'f' # workers are only female
                self.type = 'worker'

def reproduce():
        global food
        global act_workers
        global act_soldiers
        if any(isinstance(ant, queen) for ant in colony): # if I got a queen in my colony
                if random.randint(1,100) <= 70: # let's cast a percentage and see which type of ant is to be born
                        colony.append(worker())
                        act_workers += 1
                        for ant in colony:
                                if ant.type == 'queen':
                                        actual_queen = ant
                        actual_queen.eat()
                else:
                        colony.append(soldier())
                        act_soldiers += 1
                        for ant in colony:
                                if ant.type == 'queen':
                                        actual_queen = ant
                        actual_queen.eat()


print ("Welcome to your ant colony.")
total_days = int(input('For how many days you want to run the simulation? '))
day = 1 # we start from the day number 1
daycount = 0 # initializing counter fos seasons
colony.append(queen())

while day <= total_days:

        # it's a new day
        daycount += 1

        # if there are no more ants the colony is over
        if len(colony) <= 0: 
                print (f'Your colony died after {day} days')
                break

        # let's check the season
        if daycount == 90:
                if season == 'spring':
                        season = 'summer'
                elif season == 'summer':
                        season = 'autumn'
                elif season == 'autumn':
                        season = 'winter'
                else:
                        season = 'spring'
                daycount = 0

        # now let's check the status of all the ants of the colony        
        for this_ant in colony:

                # death for starving
                if this_ant.starving >= 15:
                        colony.remove(this_ant) # if ant has was starving for 15 days or more will die
                        if this_ant.type == 'worker':
                                act_workers -= 1
                        elif this_ant.type == 'soldier':
                                act_soldiers -= 1
                
                # death for aging
                if this_ant.life == 0:
                        colony.remove(this_ant) # if ant has no more days to live, kill the ant, RIP
                        deadcounts += 1

                # workers will be working, ecept in winter                
                if this_ant.type == "worker" and season != 'winter':
                        food += 2

                # daily meal        
                this_ant.eat()

                # new day, one less to live
                this_ant.life -= 1

        # Is the queen dead?
        if not any(isinstance(ant, queen) for ant in colony):
                # if the queen is dead and we have enough food we grow a new queen and we feed her
                if food >= 1:
                        colony.append(queen())
                        for ant in colony:
                                if ant.type == 'queen':
                                        actual_queen = ant
                        actual_queen.eat()


        #if it's not winter and we got enough food, reproduce!
        if season != 'winter' and food > 0 and food >= len(colony):
                i = 1
                while i <= max_eggs:
                        reproduce()
                        i += 1
        
        #if food >= len(colony):
        #        food -= len(colony)  # each ant must eat, yeah it's true in the reproduction phase the queen already ate, but it's ok, she needs a lot of food
        #else:
        #        food = 0 # this check prevents the food goes negative
        day += 1
        #print (f'Day {day}, workers: {act_workers}, soldiers: {act_soldiers}, food: {food}.\n {colony}')

for this_ant in colony:
        if this_ant.type == 'worker':
                workers += 1
        elif this_ant.type == 'soldier':
                soldiers += 1
        elif this_ant.type == 'queen':
                queens += 1
        if this_ant.gender == 'm':
                males += 1
        elif this_ant.gender == 'f':
                females += 1

if len(colony) != 0:
        print ('Colony summary:')
        print (f'Your colony successfully survived for {day-1} days.')
        print (f'{queens} queens succeeded.')
        print (f'You got {workers} workers.')
        print (f'You got {soldiers} soldiers.')
        print (f'You got {males} males.')
        print (f'You got {females} females.')
        print (f'You got {food} food units.')
        print (f'{deadcounts} ants died since the first day.')
print (f'You got a total of {id} ants since the beginning.')


        