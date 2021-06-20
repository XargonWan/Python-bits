import random

# TODO: add food availability: normal, scarse, starvation
# TODO: add casualties (humans, predators, weather)

id = 0 # ant's ID starts from 0 and goes on
colony = [] # list of ants in the colony
tot_queens = 0
tot_workers = 0
tot_soldiers = 0
tot_males = 0
tot_females = 0
deadcounts = 0
actual_queen = ""

# "Actual" counters
act_workers = 0
act_soldiers = 0
act_queens = 0 # this is more for debug purposes
act_males = 0
act_females = 0

# OPTIONS
food = 10 # starting food
max_eggs = 100 # max eggs layable per day
season = 'spring' # starting season


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
                self.starving = 0
        else:
                self.starving += 1

class queen(ant):
        def __init__(self):
                global tot_queens
                global act_queens
                global tot_females
                global act_females
                global actual_queen
                super().__init__()
                self.life = random.randint(1095,1460) # quenn's lifespan is longer
                self.gender = 'f' # queens are only female
                self.type = 'queen'
                tot_females += 1
                act_females += 1
                tot_queens += 1
                act_queens += 1
                actual_queen = self
                self.ate_today = False

        def eat(self):  # for the queen we need a special eat function as she eats more times in a day
                global food
                if food >= 1:
                        food -= 1
                        self.starving = 0
                        self.ate_today = True
                elif self.ate_today == False:
                        self.starving += 1
                        

        def die(self):
                global colony
                global act_queens
                global actual_queen
                global deadcounts
                deadcounts += 1
                actual_queen = ""
                act_queens -= 1
                colony.remove(self)
                #print(f'The queen is dead today, long live the new queen!') #DEBUG
                

class soldier(ant):
        def __init__(self):
                global tot_soldiers
                global tot_males
                global tot_females
                global act_soldiers
                global act_females
                global act_males
                super().__init__()
                self.type = 'soldier'
                tot_soldiers += 1
                act_soldiers += 1
                if self.gender == 'm':
                        tot_males += 1
                        act_males += 1
                else:
                        tot_females += 1
                        act_females += 1
        def die(self):
                global act_soldiers
                global colony
                global act_females
                global act_males
                global deadcounts
                deadcounts += 1
                colony.remove(self)
                act_soldiers -= 1
                if self.gender == 'm':
                        act_males += 1
                else:
                        act_females += 1               

class worker(ant):
        def __init__(self):
                super().__init__()
                global tot_workers
                global tot_females
                global act_workers
                global act_females
                self.gender = 'f' # tot_workers are only female
                self.type = 'worker'
                tot_workers += 1
                act_workers += 1
                tot_females += 1
                act_females += 1
        def die(self):
                global act_workers
                global colony
                global act_females
                global deadcounts
                deadcounts += 1
                colony.remove(self)
                act_workers -= 1
                act_females -= 1


def reproduce():
        global food
        global actual_queen
        global colony
        global max_eggs
        if not any(isinstance(ant, queen) for ant in colony):
                # if the queen is dead and we have enough food we grow a new queen and we feed her
                if food >= 1:
                        colony.append(queen())
                        #for ant in colony:
                        #        if ant.type == 'queen':
                        #                actual_queen = ant
                        actual_queen.eat()
        elif season != 'winter' and food >= len(colony)-1: #if it's not winter and we got enough food, reproduce!
                i = 1
                #print(f'DEBUG: Giorno {day}, non è inverno e abbiamo {food} cibo, i={i}')
                while i <= (max_eggs - len(colony)-1):    # we want to make sure that we don't consume tomorrow's food
                        if random.randint(1,100) <= 70 or not any(isinstance(ant, worker) for ant in colony): # let's cast a percentage and see which type of ant is to be born
                                colony.append(worker())
                                actual_queen.eat()
                                #print(f'Creo worker, cibo {food}, max eggs {max_eggs}, i={i}')
                        else:
                                colony.append(soldier())
                                actual_queen.eat()
                                #print(f'Creo soldier, cibo {food}, max eggs {max_eggs}, i={i}')
                        i += 1


print ("Welcome to your ant colony.")
total_days = int(input('For how many days you want to run the simulation? '))
day = 1 # we start from the day number 1
daycount = 0 # initializing counter fos seasons
colony.append(queen())

# DEBUG Lines
#print (f'\nDEBUG: Simulation started')
#print (f'You have {len(colony)} ants:')
#print (f'{act_workers} workers.')
#print (f'{act_soldiers} soldiers.')
#print (f'You have {food} food units.')
#print (f'{deadcounts} ants died since the first day.')
# END DEBUG Lines

while day <= total_days:

        # it's a new day
        daycount += 1

        print (f'\nDEBUG: Day {day} resume:')

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

                #DEBUG
                #if this_ant.type == 'queen':
                #        print(f'Queen starving: {this_ant.starving}, life: {this_ant.life} HP')
                #DEBUG
                
                # check if this ant is still alive
                if this_ant.starving >= 15 or this_ant.life == 0:
                        this_ant.die()

                # tot_workers will be working, ecept in winter                
                if this_ant.type == "worker" and season != 'winter':
                        food += random.randint(0,3)

                # daily meal        
                this_ant.eat()

                # new day, one less to live
                this_ant.life -= 1

        reproduce()

        if total_days <= 20:
                print (f'You have a queen and {len(colony)} ants:')
                print (f'{act_workers} workers.')
                print (f'{act_soldiers} soldiers.')
                print (f'You have stored {food} food units.')
                print (f'{deadcounts} ants died since the first day.')

        day += 1



if len(colony) != 0:
        print ('\n***Colony summary***')
        print (f'Your colony successfully survived for {day-1} days.')
        print (f'{tot_queens} queens succeeded.')
        print (f'You have a queen and {len(colony)} ants:')
        print (f'{tot_workers} workers.')
        print (f'{tot_soldiers} soldiers.')
        print (f'{tot_males} are males and {tot_females} are female.')
        print (f'You have stored {food} food units.')
        print (f'\n{deadcounts} ants died since the first day.')
print (f'You got a total of {id} ants since the beginning.')        