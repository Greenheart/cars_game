#! python3

#cars_game.py
"""
author:  "Samuel Plumppu"
license: "MIT"
date:    "20 September 2015"
"""

import time
import random
import csv
import sys
gameversion= "b1.5"

#ERRORS

#TODO: Didn't get reward even if mission was completed successfully
"""
Working tires: 3/4
You have an extra tire with you. Use now?
'1': Use
'2': Save for later use
1

Replacing one of the broken tires...

Your car is fixed again and you completed the mission successfuly!
You earned 818 $!

Press Enter to continue...


-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-
                           Evening 3
-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-

             Cash: 1 $    Money in Bank: 1003 $
"""


#2

"""
You still have 1 broken tire(s).
You need to fix them in the Garage before the next mission!

Press Enter to continue...


-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-
                          Game Over!
-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-
You can't afford the tires you need to use your car!
Without a functional car, you will never be able to earn any
money and pay for new tires!

Press Enter to view the highscores!

Traceback (most recent call last):
  File "cars_game.py", line 1227, in <module>
  File "cars_game.py", line 1107, in endgame
    print("Creating 'hsdb.csv' in the same folder as this game.")
  File "cars_game.py", line 1132, in highscores
    session_entry = highscores[-1]
ValueError: Must have exactly one of create/read/write/append mode and at most one plus
"""
#TODO
#Test mission-events and fix bugs

#Compile game to .app, .exe etc. and upload to the webpage

#OPT
#Add a characther() - function for managing player skills and exp
#Add player experience --> Player gain exp for each mission played.
    #Add player.exp and player.next_level
    #Add exp-bounty to missions
        #(1.0 x exp for win, 0.2 for loss) * mission_risk
    #Every level up gives points for skills development
        #Level up driving skills, social skills
        #Exp needed for each level-up increases
    #Add characther- managing as an option to the evening()-loop

#Add some new cars
    #Add subclasses
    #Fix some game-logic for example upgrades (specific for each car.type)

class Car(object):
    def __init__(self):
        self.km_total= 0
        self.km_since_repair= 0
        self.tires= 4
        self.extra_tire= True
        self.color= "White"

    def car_stats(self):
        stats_title= "Stats for the {}".format(self.type)
        print("\n"+"-=-"*21)
        print("{:^63}".format(stats_title))
        print("-=-"*21+"\n")
        print(" "*7+"Max Speed: {} km/h".format(self.max_speed)+"   Fuel Consumption: {0:.1f} L/100 km".format(self.fuel_per_100km))
        print(" "*7+"Fuel in Tank: {:.0f} %".format((float(self.fuel_cur)/self.fuel_max)*100)+"   Total Distance: {} km".format(self.km_total))
        print(" "*7+"Car Safety: {:.1f}/5.0".format(self.safety)+"   Distance without repair: {} km".format(self.km_since_repair))

    @staticmethod
    def refuel(fuelprice):  #Let player buy fuel to the car
        print("\n\n"+"-=-"*21)
        print("{:^63}".format("Fuel Station"))
        print("-=-"*21+"\n")

        print("The current fuel price is {} $/L".format(fuelprice))
        fuel_missing= car.fuel_max-car.fuel_cur
        full_tank_cost = fuel_missing*fuelprice
        print("Your current amount of cash: {0:.0f} $".format(player.cash))

        print("""\nMake your choice!
'1': Pay {0:.0f} $ for a full tank. ({1:.1f} L of fuel)
'2': Buy a specific amount of fuel for {2} $/L
'3': Cancel Purchase""".format(full_tank_cost, fuel_missing, fuelprice))
        running = True
        while running:
            choice= input("")
            if choice == '1':   #Full tank
                if full_tank_cost > player.cash:
                    print("\nYou can\'t afford that much fuel!")
                    running= True
                else:
                    player.cash-= full_tank_cost
                    player.money_spent+= full_tank_cost
                    car.fuel_cur = car.fuel_max
                    running= False
                    print("\nCurrent fuel level: {0:.0f} %".format((float(car.fuel_cur)/car.fuel_max)*100))
            elif choice == '2': #Specific amount
                running= False

                value_loop= True
                int_loop= True
                while value_loop:
                    while int_loop:
                        try:
                            fuel_amount= int(input("\nAmount of fuel?\n"))
                            int_loop= False
                        except ValueError:
                            print("\nYou have to enter an integer! Example: '40'")
                            int_loop= True

                    if fuel_amount > (car.fuel_max-car.fuel_cur):
                        print("\nThe tank can\'t take that much fuel!")
                        value_loop= True
                        int_loop= True
                    elif fuel_amount <= 0:
                        print("\nYou have to buy at least 1 L of fuel!")
                        value_loop= True
                        int_loop= True
                    elif player.cash-(fuel_amount*fuelprice) <= 0:
                        print("\nYou can\'t afford that much fuel!")
                        value_loop= True
                        int_loop= True
                    else:
                        value_loop= False
                        int_loop= False
                        car.fuel_cur+=fuel_amount
                        player.cash-= (fuel_amount*fuelprice)
                        player.money_spent+= (fuel_amount*fuelprice)
                        print("\nCurrent fuel level: {0:.0f} %".format((float(car.fuel_cur)/car.fuel_max)*100))
            elif choice == '3': #Cancel Purchase
                running = False
            else:
                print("\nI don\'t understand. Try again!")
                running= True

class Ferrari(Car):
    def __init__(self):
        Car.__init__(self)
        self.max_speed= 360
        self.fuel_per_100km= 9.2
        self.fuel_max= 92
        self.fuel_cur= 92
        self.safety= 3.2
        self.type= "Ferrari"
        self.durability= 5

class MiniCooper(Car):
    def __init__(self):
        Car.__init__(self)
        self.max_speed= 145
        self.fuel_per_100km= 5.6
        self.fuel_max= 65
        self.fuel_cur= 65
        self.safety= 3.8
        self.type= "Mini Cooper"
        self.durability= 3

class car3(Car):    #Not yet implemented
    def __init__(self):
        Car.__init__(self)
        self.max_speed= 90
        self.fuel_per_100km= 3.4
        self.fuel_max= 58
        self.fuel_cur= 58
        self.safety= 3.4
        self.type= "Name of a small shitty car goes here"
        self.durability= 4

class Player(object):
    def __init__(self):
        self.username= None
        self.missions_total= 0
        self.succesful_missions= 0
        self.cash= 300
        self.money_spent= 0
        self.money_banked= 0
        self.driving_license= True
        self.social_skills= 3
        self.driving_skills= 0.8
        self.alive= True

    @staticmethod
    def mission():  #Mission Simulation
        mission_risk= random.randint(1,10)
        reward= (mission_risk*100)+random.randint(mission_risk,mission_risk*10) #V >= b1.3
        #reward= random.randint(10,100)*mission_risk    #Pre b1.3-formula
        mission_distance= (random.randint(20,40)*mission_risk)
        mission_time= (float(mission_distance)/car.max_speed)
        fuel_required= (mission_distance/100.0)*car.fuel_per_100km

        print("""\nNew mission available!
\nRisk Level: {0}
Reward: {1} $
Distance to drive: {2} km
Mission Time: {3:.1f} h
Fuel required: {4:.1f}/{5:.1f} L in your tank
""".format(mission_risk, reward, mission_distance, mission_time, fuel_required, car.fuel_cur))

        if fuel_required > car.fuel_cur:    #Check if enough fuel is available
            print("\nYou don't have enough fuel for this mission.\nWait until tomorrow to get a new one!")
            time.sleep(2)
        elif car.tires < 4: #Broken tires, car can't drive
            print("\nYour car still has {} broken tire(s) that needs to get fixed. \nDo this in the Garage.".format(4-car.tires))
            input("\nPress Enter to continue...")
        else:   #Let player accept or decline mission
            print("Make your choice!\n'1': Accept mission\n'2': Decline mission")
            player.missions_total+=1
            running= True
            while running:
                choice= input("")
                if choice == '1':   #If mission accepted
                    running= False

                    mission_title= "Mission {}".format(world.cur_day)
                    print("\n\n"+"-=-"*21)
                    print("{:^63}".format(mission_title))
                    print("-=-"*21+"\n")
                    car.fuel_cur-= fuel_required
                    car.km_total+= mission_distance
                    car.km_since_repair+=mission_distance
                    fail_risk= (mission_risk/((4.6*player.driving_skills)*car.safety))*100

                    #Balancing Code - To help in testing
                    #print "mission_risk: {}".format(mission_risk)
                    #print "player.driving_skills: {}".format(player.driving_skills)
                    #print "car.safety: {}".format(car.safety)
                    #print "fail_risk: {}\n\n".format(fail_risk)

                    print("Fail Risk: {0:.0f} %".format(fail_risk))

                    mission_outcome= random.randint(1, 100)   #Simulate mission using fail_risk
                    time.sleep(2)
                    input("\nPress Enter to see how the mission ended!\n")

                    if mission_outcome > (fail_risk):   #If mission successful
                        player.succesful_missions+=1
                        print("\nMission successful!")

                        speed_bonus= random.uniform(0.6, 1.1)
                        if mission_time <= speed_bonus and mission_time > 0.35:
                            reward+= 35*mission_risk
                            print("""\nThanks to your fast car you could complete the mission
in such a short time that you got a bonus of {0:.0f} $!""".format(35*mission_risk))
                        elif mission_time <= 0.35:
                            reward+= 50*mission_risk
                            print("""\nSuper Bonus!\nThanks to your fast car you could complete the mission
in such a short time that you got a bonus of {0:.0f} $!""".format(50*mission_risk))
                        else:
                            pass
                        print("\nYou earned {0:.0f} $!".format(reward))
                        player.cash+= reward

                    else:   #If mission not successful in the first try
                        Player.mission_event(reward, mission_risk) #Get random event

                elif choice == '2': #Mission declined
                    print("\nMision declined. Wait until tomorrow to get a new one.")
                    player.cash-= world.dayoff_cost
                    print("\nSince you declined the mission, you spend the day\ndoing something else. This costs you {0:.0f} $".format(world.dayoff_cost))
                    player.money_spent+=world.dayoff_cost
                    world.dayoff_cost*= 1.2
                    running= False
                else:
                    print("\nI don't understand. Try again!")
                    running= True
            time.sleep(2)

    @staticmethod
    def mission_event(reward, mission_risk): #Events for failed missions

        event_risk= random.randint(1, 100)
        if event_risk <= mission_risk*10 and player.missions_total >= 3:
            event_outcome= random.randint(1, 100) #Random number to decide event


            if event_outcome <= 30: #Speeding - 30%
                print("""\nYou drove too fast and got caught by the cops for speeding!\n
What do you do?\n'1': Try to talk yourself out of the situation
'2': Rely on the car and your driving-skills and try to escape!""")
                running= True
                while running:
                    choice= input("")

                    if choice== '1':    #Talk to cops
                        running= False
                        print("\nYou talk to the cops...")
                        time.sleep(2)
                        if player.driving_license:
                            if player.social_skills== 3:
                                print("\n...and they let you get away with just 4/5 of the cost, 200 $")
                                cost= 200
                            elif player.social_skills== 4:
                                print("\n...and they let you get away with just 1/5 of the cost, 50 $")
                                cost= 50
                            elif player.social_skills== 5:
                                print("\n...and talk yourself out of the situation")
                        else:
                            cost= 750
                            print("""\n...but they really don't like that you are driving without
your driving-license!""")
                        print("\nYou have to pay {} $!".format(cost))
                        player.cash-= cost
                        input("\nPress Enter to continue...")

                    elif choice== '2':  #Try to escape
                        running= False
                        print("""\nIn order to get away from the cops,
you drive up on the sidewalk destroying several benches and
trashbins...""")
                        time.sleep(2)
                        if car.max_speed >= 250:  # Maybe use driving_skills and car_handling too
                            print("\n...and get away thanks to your fast car and your driving-skills!\nThe cops had no chance!")
                            player.cash+= reward
                            player.succesful_missions+=1
                            print("\nYou earned {0:.0f} $!".format(reward))
                            input("\nPress Enter to continue...")

                        else:   #You try and fail, the cops get angry
                            if player.driving_license:
                                cost= 500
                                player.driving_license= False
                                print("\n...but your car is too slow and the cops catch you again!")
                                print("They also took your driving-license!")
                            else:
                                cost= 1500
                                print("\n...but your car is too slow and the cops catch you again! \nThis time you have to pay double cost, {} $!".format(cost))
                            player.cash-= cost
                            print("\n\nMission Failed!\nYou have to pay {}".format(cost))
                            input("\nPress Enter to continue...")
                    else:
                        running= True
                        print("\nI don't understand. Try again!\n")


            elif event_outcome > 30 and event_outcome <= 55:  #Flat Tires - 25%
                car.tires-= random.randint(1,2)
                print("""\nYou drove onto something sharp and destroyed {} of your tires!
\nYou will need 4 working tires before you can accept the next
mission.""".format(4-car.tires))
                time.sleep(2)

                if car.extra_tire:
                    print("\n\nWorking tires: {}/4\nYou have an extra tire with you. Use now?\n'1': Use\n'2': Save for later use".format(car.tires))
                    running= True
                    while running:
                        choice= input("")
                        if choice== '1':    #Use extra tire
                            running= False
                            print("\nReplacing one of the broken tires...")
                            car.extra_tire= False
                            car.tires+= 1
                        elif choice== '2':  #Cancel
                            running= False
                        else:
                            print("\nI don't understand. Try again!")

                if car.tires < 4:
                    running= True
                    while running:
                        print("""\nWorking tires: {}/4 \nYou need help to get home. What to do?
'1': Call for a recovery vehicle\n'2': Call a friend and try to convince him to help""".format(car.tires))
                        choice= input("")

                        if choice== '1':    #Recovery Vehicle
                            running= False
                            print("\nA recovery vehicle is soon there to help you back to your place")
                            time.sleep(2)
                            print("This costs 300 $")
                            player.cash-= 300

                        elif choice== '2':  #Friend
                            print("\nYou call one of your friends...")
                            time.sleep(2)

                            if player.social_skills== 3:
                                print("\n...who laughs at you!")
                                running= True
                                print("\nYou will still need help to get home")
                                input("\n\nPress Enter to continue...")

                            elif player.social_skills >= 4:
                                running= False
                                print("\n...that says he will be there as soon as possible!")
                                time.sleep(2)
                                print("\nYour friend helps you back to your place.")
                                time.sleep(2)

                        else:
                            print("\nI don't understand. Try again!\n")
                            running= True

                    if car.tires < 4:
                        print("\n\nYou still have {} broken tire(s).\nYou need to fix them in the Garage before the next mission!".format(4-car.tires))
                        input("\nPress Enter to continue...")

                else:
                    print("\nYour car is fixed again and you completed the mission successfuly!")
                    print("You earned {} $!".format(reward))
                    time.sleep(2)
                    input("\nPress Enter to continue...")


            elif event_outcome > 55 and event_outcome <= 80:  #Bad Car Crash - 25%
                print("\nYou drove into a car in front of you in the traffic light que.\nAn angry driver is now standing outside of your car.")
                print("\nWhat to do now?\n'1': Talk to the driver\n'2': Hit the driver with the your car's door \n'3': Try to escape by driving up on the sidewalk")
                running= True
                while running:
                    choice= input("")

                    if choice == '1':   #Talk
                        running= False
                        print("\nYou talk to the driver...")
                        if player.social_skills == 3:
                            print("\n...who says that you have to pay him 300 $.")
                            player.cash-= 300
                        else:
                            print("\n...who says that you have to pay him 200 $.")
                            player.cash-= 200
                        input("\nPress Enter to continue...")

                    elif choice == '2': #Hit driver with door
                        print("\nHow did you think that should help you in this situation?")
                        print("An even angrier driver is now standing outside of your car...")
                        time.sleep(2)
                        print("\nNah, just kidding! The driver is still laying on the ground.\nYou better get out of here before he gets on his feet again!")
                        running= False
                        print("You escape via the sidewalk.")
                        input("\nPress Enter to continue...")
                        print("\nMission successful!")
                        print("You earned {} $!".format(reward))
                        player.cash+=reward
                        player.succesful_missions+=1

                    elif choice == '3': #Escape
                        running= False
                        print("\nYou ignore the angry driver and escape via the sidewalk. \nLike a boss")
                        input("\nPress Enter to continue...")
                        print("\nMission successful!")
                        print("You earned {} $!".format(reward))
                        player.cash+=reward
                        player.succesful_missions+=1
                    else:
                        running= True
                        print("\nI don't understand. Try again!")


            elif event_outcome > 80 and event_outcome <= 90:  #Serious Car crash - 10%
                print("\nYour car got crushed by a big truck while you were delivering \na package. \nIt will cost 800 $ to repair your car since it's so demolished")
                player.cash-= 800
                input("\nPress Enter to continue...")

            else:  #Encounter stranger - 10%
                print("\nYou notice a car that seems to be following you.\nWhen you stop to deliver the mysterious package at an even more \nsuspicious house, a big man comes out from the other car.")
                input("\nPress Enter to continue...")
                print("\nHe walks up to you, looking at the package in your hands.\n- That package belongs to me.")
                input("\nPress Enter to continue...")
                print("\n- Ehm... What do you mean?, you respond a bit confused.")
                input("\nPress Enter to continue...")
                print("\n- That package is not like other packages you've seen, he says \n  while moving the hand inside of his coat. \n\nIt looks like if he's trying to grab something...")

                print("""\n\nHow do you react?\n'1': "...So this package is this special because is yours?" \n'2': Give the package to the man\n'3': Try to escape""")
                running= True
                while running:
                    choice= input("")

                    if choice == '1':   #Talk to stranger
                        running= False
                        print("\nThe man sighs and shakes his head while looking to the ground.\nHe's looking quite angry...")
                        input("\nPress Enter to continue...")
                        print("\n- I don't have time for your bad jokes!")
                        print("\nThe big man picks up a gun and shoots you twice in the stomach. \n\nIt kinda hurts... A lot.")
                        #player.alive = False

                    elif choice == '2': #Give package
                        running= False
                        print("\nThe man takes the package and starts walking back to his car")
                        input("\nPress Enter to continue...")
                        print("\nBut he don't take more than a couple of steps before suddently \nturning around. \n- Here, take this, the man says and gives you 400 $")
                        #player.cash+=400

                    elif choice == '3': #Run away
                        running= False
                        print("\nYou run to the car but accidently drop the package when you \nenter the car.")
                        print("\nPick up the package?\n'1': Pick it up. You can't just leave it to this strange man...\n'2': Leave it and drive away. Better get out of here fast...")
                        package_loop= True
                        while package_loop:
                            choice= input("")

                            if choice == '1':   #Pick up package
                                package_loop= False
                                print("\nYou pick up the package, but when you raise up again the man \nis holding a gun against your head.")
                                print("\n- How hard can it be to understand? the man says and shoots you \nin the head. \n\nIt kinda hurts... A lot.")
                                #player.alive= False
                            elif choice == '2': #Leave package
                                package_loop= False
                                print("\nYou drive away, start the radio and 'Leave The World Behind You'")
                            else:
                                print("\nI don't understand. Try again!")
                                package_loop= True

                    else:
                        print("\nI don't understand. Try again!")
                        running= True
                input("\nPress Enter to continue...")
        else:
            print("\n\nMission Failed!\n\nYou lost {:.0f} $!".format(world.fail_cost))
            player.cash-= world.fail_cost
            player.money_spent+=world.fail_cost
            world.fail_cost*= 1.2

    @staticmethod
    def save_money():   #Save money to bank
        print("\n\nCash: {0:.0f} $".format(player.cash)+"    Money in Bank: {0:.0f} $".format(player.money_banked))
        running = False
        value_loop= True
        while value_loop:
            try:
                save_amount= int(input("\nAmount to save?\n"))
            except ValueError:
                print("\nYou have to enter an integer! Example: '550'")
                continue

            if save_amount >= (player.cash-0.5):
                print("\nYou can\'t move all your cash to the bank!")
                value_loop= True
            elif save_amount <= 0:
                print("\nYou have to save something!")
                value_loop= True
            else:
                value_loop= False
                print("\nSaving {0:.0f} $ to your bank-account".format(save_amount))
                player.money_banked+=save_amount
                player.cash-=save_amount

class World(object):
    def __init__(self):
        self.fail_cost= 100
        self.dayoff_cost= 100
        self.cur_day= 1
        self.color_bonus= False
        self.is_active = True

    @staticmethod
    def new_day():  #Used every morning to display current stats.
        day= "Day {}".format(world.cur_day)
        print("\n\n"+"-=-"*21)
        print("{:^63}".format(day))
        print("-=-"*21+"\n")
        print(" "*16+"Cash: {0:.0f} $".format(player.cash)+"    Money Spent: {0:.0f} $".format(player.money_spent))
        print(" "*9+"Missions Completed: {}/{}".format(player.succesful_missions, player.missions_total)+"   Money in Bank: {0:.0f} $".format(player.money_banked))
        time.sleep(2)
        input("\nPress Enter to continue...")

    @staticmethod
    def evening():  #Used every night to display current stats
        evening= "Evening {}".format(world.cur_day)
        print("\n\n"+"-=-"*21)
        print("{:^63}".format(evening))
        print("-=-"*21+"\n")
        print(" "*13+"Cash: {0:.0f} $".format(player.cash)+"    Money in Bank: {0:.0f} $".format(player.money_banked)+"\n")
        time.sleep(2)
        car.car_stats()
        garage_visited= False
        input("\nPress Enter to continue...")
        fuelprice= random.randint(3,14)
        evening_loop= True
        while evening_loop:
            if garage_visited:
                print("\nCash: {0:.0f} $".format(player.cash)+"    Money in Bank: {0:.0f} $".format(player.money_banked))
            print("\n\nWhat do you want to do?\n'1': Upgrade & Repair your Car in the Garage\n'2': Buy Fuel - Current price: {} $/L\n'3': Save Money to the Bank (Improve Score)\n'4': View Stats for your Car\n'5': Continue to the Next Day".format(fuelprice))
            choice_loop= True
            while choice_loop:
                choice= input("")
                if choice== '1':    #Go to garage
                    choice_loop= False
                    garage_visited= True
                    Garage.garage_main()

                elif choice == '2': #Buy fuel
                    choice_loop= False
                    if car.fuel_cur == car.fuel_max:    #Player got full tank
                        print("\nYour tank is already full!")
                    elif player.cash-fuelprice <= 0:    #Player can\'t afford fuel
                        print("\nYou can\'t afford any fuel right now!")
                    else:   #The normal case, tank not full and player got cash
                        car.refuel(fuelprice)
                elif choice == '3':
                    choice_loop= False
                    if player.cash <= 1:
                        print("\nYou don\'t have any money to save!")
                    else:   #The normal case, player got cash to save
                        player.save_money()

                elif choice == '4': #View Stats
                    choice_loop= False
                    car.car_stats()
                    input("\nPress Enter to continue...")

                elif choice == '5':
                    evening_loop= False
                    choice_loop= False
                else:
                    print("\nI don\'t understand. Try again!")

class Garage(object):
    @staticmethod
    def garage_main():  #Upgrade and repair car
        garage_loop= True
        while garage_loop:
            print("\n"+"-=-"*21)
            print("{:^63}".format("Garage"))
            print("-=-"*21+"\n")

            print("""What do you want to do in the garage?\n'1': Upgrade your Car\n'2': Perform Service on your Car
'3': Replace Broken Tires\n'4': Enhance Car-Visuals\n'5': Leave the Garage""")
            running= True
            while running:
                choice= input("")
                if choice == '1':   #Upgrade car
                    running= False
                    Garage.upgrades()
                elif choice == '2': #Perform service
                    running= False
                    Garage.service()
                elif choice == '3': #Fix tires
                    running= False
                    Garage.replace_tires()
                elif choice == '4': #Visuals
                    running= False
                    Garage.styling()
                elif choice == '5': #Exit garage
                    running= False
                    garage_loop= False
                    print("\nLeaving the Garage...")
                    time.sleep(2)
                else:
                    running= True
                    print("\nI don\'t understand. Try again!")

    @staticmethod
    def upgrades(): #Upgrade car-stats, accessed from garage_main()
        error= "\nI don\'t understand. Try again!"
        upgrade_loop= True
        while upgrade_loop:
            print("\n"+"-=-"*21)
            print("{:^63}".format("Upgrades"))
            print("-=-"*21+"\n")
            upgrades_msg= "\nThese are the upgrades available for the moment:"
            choices_available= []   #Stores active menu-items (Currently possible choices)

            #Decide which upgrades that should be available
            if car.type == "Ferrari":
                if car.fuel_per_100km <= 7.6:
                    pass
                else:
                    choices_available.append(1)
                    upgrades_msg+= "\n'1': Fuel Efficiency --> from {} to {} L/100 km - 250 $".format(car.fuel_per_100km, (car.fuel_per_100km-0.4))

                if car.max_speed >= 440:
                    pass
                else:
                    choices_available.append(2)
                    upgrades_msg+="\n'2': Car Speed --> from {} to {} km/h - 200 $".format(car.max_speed, (car.max_speed+40))

            elif car.type == "Mini Cooper":
                if car.fuel_per_100km <= 4.8:
                    pass
                else:
                    choices_available.append(1)
                    upgrades_msg+= "\n'1': Fuel Efficiency --> from {} to {} L/100 km - 250 $".format(car.fuel_per_100km, (car.fuel_per_100km-0.4))

                if car.max_speed >= 260:
                    pass
                else:
                    choices_available.append(2)
                    upgrades_msg+="\n'2': Car Speed --> from {} to {} km/h - 200 $".format(car.max_speed, (car.max_speed+40))

            if car.safety > 4.9 and car.safety < 5.1:
                pass
            else:
                choices_available.append(3)
                upgrades_msg+="\n'3': Car Safety --> from {} to {}/5.0 - 200 $".format(car.safety, (car.safety+0.2))

            if len(upgrades_msg) <= 49: #Car can't be upgraded anymore
                print("\nYour car is fully upgraded!")
                time.sleep(2)
                print("\nGoing back to the Garage...")
                time.sleep(2)
                upgrade_loop= False
                continue
            else:   #Some upgrades are still available
                upgrades_msg+="\n'4': Go back to the garage"
                choices_available.append(4)
                print("Current amount of cash: {0:.0f} $".format(player.cash))
                print(upgrades_msg)

            running= True
            while running:
                choice= input("")
                if choice == '1':   #Upgrade Fuel Efficiency
                    if 1 in choices_available:  #Only check if any upgrades upgavailable
                        running= False
                        cost= 250
                        if (player.cash-cost) <= 0.5:
                            print("\nYou can't afford this upgrade!")
                        else:
                            print("\nImproving Fuel Efficiency...")
                            car.fuel_per_100km-=0.4
                            player.cash-=cost
                            player.money_spent+=cost
                    else:
                        print(error)
                        running= True
                elif choice == '2': #Upgrade Car Speed
                    if 2 in choices_available:
                        cost= 200
                        if (player.cash-cost) <= 0.5:
                            print("\nYou can't afford this upgrade!")
                        else:
                            print("\nImproving Max-Speed...")
                            car.max_speed+=40
                            player.cash-=cost
                            player.money_spent+=cost
                            running= False
                    else:
                        print(error)
                        running= True
                elif choice == '3': #Upgrade Car Safety
                    if 3 in choices_available:
                        cost= 200
                        if (player.cash-cost) <= 0.5:
                            print("\nYou can't afford this upgrade!")
                        else:
                            print("\nImproving Car Safety...")
                            car.safety+=0.2
                            player.cash-=cost
                            player.money_spent+=cost
                            running= False
                    else:
                        print(error)
                        running= True

                elif choice == '4': #Exit
                    if 4 in choices_available:
                        print("\nGoing back to the Garage...")
                        running= False
                        upgrade_loop= False
                    else:
                        running= True
                        print(error)
                else:
                    running= True
                    print(error)
            time.sleep(2)

    @staticmethod
    def service():  #Perform service on car, accessed from garage_main()
        print("\n"+"-=-"*21)
        print("{:^63}".format("Car Service"))
        print("-=-"*21+"\n")

        #Calculate prices for repair, depending on distance driven since last repair
        if car.km_since_repair > 1000:  #if player don't take care of their car
            cost= (car.km_since_repair)/(car.durability*0.6)

        else:   #if player takes care of their car
            cost= (car.km_since_repair/1.5)/car.durability

        #Let player make decision, if any repairs are possible
        if (player.cash-cost) <= 0.5:   #Not enough cash
            print("You can't afford any repairs right now!")
            time.sleep(2)

        elif car.km_since_repair == 0:  #No repairs needed
            print("Your car don't need any service right now!")
            time.sleep(2)

        else:   #If player got enough cash
            print("Current amount of cash: {0:.0f} $\nA repair will cost: {1:.0f} $".format(player.cash, cost))
            print("\nMake your choice:\n'1': Repair your car\n'2': Cancel")
            running= True
            while running:
                choice= input("")

                if choice == '1':   #Repair
                    if car.km_since_repair > 1000:
                        print("""Since you have driven the car for more than 1000 km
without service, some parts are very urgent to get repaired.
This repair will therefore be more expensive than usual.""")
                        input("\nPress Enter to continue...")

                    print("\n\nRepairing your car for {:.0f} $...".format(cost))
                    car.km_since_repair= 0
                    player.cash-= cost
                    player.money_spent+= cost
                    print("Current amount of cash: {:.0f}".format(player.cash))
                    input("\nPress Enter to continue...")
                    running= False

                elif choice == '2': #Cancel
                    print("\nGoing back to the Garage...")
                    time.sleep(2)
                    running= False

                else:
                    print("\nI don't understand. Try again!")
                    running= True

    @staticmethod
    def replace_tires():    #Fix tires for car, accessed from garage_main()
        print("\n"+"-=-"*21)
        print("{:^63}".format("Tire Change"))
        print("-=-"*21+"\n")
        if car.tires == 4 and car.extra_tire:   #No need to change old tires
            print("Your tires are working perfectly!\n\n")
            time.sleep(2)
        else:   #Repairs possible
            amount= (4-car.tires)
            cost= amount*75
            print("{} broken tire(s) on the car.".format(amount))

            if not car.extra_tire and player.cash-(cost+50) >= 0.5:
                print("\nYou don't have an extra tire. Buy new?\n'1': Buy an extra tire for 50 $\n'2': Skip")
                running= True
                while running:
                    choice= input("")
                    if choice== '1':
                        running= False
                        cost+= 50
                        amount+= 1
                    elif choice== '2':
                        running= False
                    else:
                        print("\nI don\'t understand. Try again!")

            print("\nReplacing {} tire(s) for {} $".format(amount, cost))
            player.cash-= cost
            player.money_spent+=cost
            print("Current amount of cash: {:.0f} $".format(player.cash))
            time.sleep(2)

            if car.tires+amount > 4:
                car.extra_tire= True
                car.tires+= amount-1
            else:
                car.tires+= amount
            print("\nDone! With new tires, you can run missions again!\n")
            print("You now have {} tires, extra tire= {}".format(car.tires, car.extra_tire))
            input("\n\nPress Enter to continue...")

    @staticmethod
    def styling():  #Change looks of car, accessed from garage_main()
        print("\n"+"-=-"*21)
        print("{:^63}".format("Car Styling Studio"))
        print("-=-"*21+"\n")
        if car.color== "White":
            print("This is where you can change the appearance of your car...")
            print("\nThe current color of your {} is:\n{}".format(car.type, car.color))
            print("As you can see your car currently has a quite boring color...")
            time.sleep(2)
            print("\nLet's change that!\nJust enter...\n* Any color you like...\n* Any object with a color you like...\n* Any object with a similar color to the color you like...")

            color_loop= True
            while color_loop:
                choice= input("\nColor?\n")
                if len(choice) >= 15:
                    running= True
                    print("\nAre you kidding me or something?\nThat can NOT be a color!")

                elif choice== "gr33n":
                    car.color= choice
                    color_loop= False
                    print("\nYeah! Now we are talking nice colors!")
                    if world.color_bonus== False:
                        world.color_bonus= True
                        print("Adding 500 bonus cash! ;)")
                        player.cash+=500
                        print("Current amount of cash: {0:.0f}".format(player.cash))

                elif choice == car.color:
                    color_loop= True
                    print("\nLoL? You can't repaint the car with same color...\nThat makes you look so poor and oldfashioned \nwho can\'t afford new colors!")

                elif "blue"in choice or"yellow"in choice or"green"in choice or"orange"in choice or"black"in choice:
                    color_loop= True
                    print("\nI am afraid that I have forgot the hexadecimal value\nfor this one...\n\nYou can\'t use this color, even if it is nice!")
                    print("You could try to enter ANY object with this color!")
                elif choice == '':
                    color_loop= True
                    print("I don't understand. Try again!")
                else:
                    color_loop= False
                    car.color= choice
                    print("\nGood choice! ;)")

        else:
            print("The current color of your {} is:\n{}".format(car.type, car.color))
            print("\n\nAre you happy with the color?\n'1': Change color\n'2': Keep color")
            running= True
            while running:
                choice= input("")

                if choice== '1':
                    running= False
                    print("\nJust enter...\n* Any color you like...\n* Any object with a color you like...\n* Any object with a similar color to the color you like...")
                    color_loop= True
                    while color_loop:
                        choice= input("\nColor?\n")

                        if len(choice) >= 15:
                            color_loop= True
                            print("\nAre you kidding me or something?\nThat can NOT be a color!")

                        elif choice == car.color:
                            color_loop= True
                            print("\nLoL? You can't repaint the car with same color...\nThat makes you look so poor and oldfashioned \nwho can\'t afford new colors!")

                        elif choice== "gr33n" and choice != car.color:
                            car.color= choice
                            color_loop= False
                            running= False
                            print("\nYeah! Now we are talking nice colors!")
                            if world.color_bonus== False:
                                world.color_bonus= True
                                print("Adding 500 bonus cash! ;)")
                                player.cash+=500
                                print("Current amount of cash: {0:.0f}".format(player.cash))

                        elif "blue"in choice or"yellow"in choice or"green"in choice or"orange"in choice or"black"in choice:
                            running= True
                            print("\nI am afraid that I have forgot the hexadecimal value\nfor this one...\n\nYou can\'t use this color, even if it may look nice nice! ^^")
                            print("You could try to enter ANY object with this color!")
                        elif choice == '':
                            color_loop= True
                            print("I don\'t understand. Try again!")
                        else:
                            running= False
                            color_loop= False
                            car.color= choice
                            print("\nGood choice! ;)")

                elif choice== '2':
                    running= False
                    if car.color != "gr33n":
                        print("\nYour current color is ugly. Just sayin...")

                else:
                    running= True
                    print("\nI don\'t understand. Try again!")

        print("\nThe current color of your {} is:\n{}".format(car.type, car.color))
        time.sleep(2)

def menu(recent_user):
    if recent_user:
        player.username= recent_user
        world.is_active = True
        running = True
        while running:
            print("\n\nChange username?\n'1': Continue as '{}'\n'2': Change user".format(player.username))
            choice= input("")
            if choice == '1':
                running= False
                print("\n")
            elif choice == '2':
                player.username= input("\n\nEnter your username:\n")
                running= False
                print("\n")
            else:
                print("I don\'t understand. Try again!")
                running= True
    else:
        player.username= input("\n\nEnter your username:\n")

    print("-=-"*21)
    print(" "*12+"The not so busy business - Version {}".format(gameversion))
    print("-=-"*21)

    main_menu= """\n                  +-------------------------+
                  |        Main Menu        |
                  +-------------------------+
                  |  '1': Play              |
                  |  '2': Highscores        |
                  |  '3': About The Game    |
                  |  '4': Quit              |
                  +-------------------------+\n
                   Made in MMXIV by Samuel P
                   www.github.com/greenheart
\nEnter your choice:"""
    menu_loop= True
    while menu_loop:
        print(main_menu)
        running= True
        while running:
            choice= input("")
            if choice == '1':   #Start the game
                running= False
                menu_loop= False
            elif choice == '2': #Display highscores (not in-game hs, but another function)
                highscores(None)
                running= False
            elif choice == '3': #View info about the game
                about_game()
                running= False
            elif choice == '4': #Quit
                sys.exit()
            else:
                running= True
                print("\nI don\'t understand. Try again!\n")

def about_game():
    print("\n"+"-=-"*21)
    print("{:^63}".format("About The Game"))
    print("-=-"*21)

    print("""\nYou have accepted to challenge a friend to see whom of you
that can earn the most money in a month.
The rules you set up are simple; To prove how much money
you earn, you have to transfer your profits to a special
bank-account.

But you still have to make a living during this month
and therefore you can\'t move all of your cash to the bank.""")

    input("\nPress Enter to continue...")

    print("""\nYou love cars and therefore you will now try to run your
own taxi/delivery service for the next month.
But you soon realise that the taxi- and delivery- business
is riskier than you first thought. Some people or goods you
drive come with a greater risk - and of course with bigger
profits!""")

    input("\nPress Enter to continue...")

    print("""\nHow much are you willing to risk for some money?
Your car? Your future career? YOUR LIFE?

Should your business focus on risky but profitable missions or
stick to the ones that pay less but will give you a stable
income?
It is time for you to get down to business!\n""")

    input("\nPress Enter for some useful tips!")

    print("""\n* Be prepared for unexpected costs!
* Only money in your bank-account will affect the final score!
* Be smart! Try to find the perfect balance between money spent
  on car-upgrades and profits transfered to the bank.
* The faster you complete a mission - The more money you make\n""")
    input("\nPress Enter to continue...")

def start_new_session(): #Display the game's startscreen
    print(" "*24+"""Welcome {}!\n
* Use your car to complete missions and earn cash.
* A riskier mission will earn you more cash, but if you fail...
...bad things will happen!
* Money in the bank will improve your score...
...but remember to keep some cash for unexpected costs!

* Make sure you always have fuel...
...because you don\'t want an engine breakdown!
* Repair your car in the garage from time to time...
...because repairs always costs more when they are urgent!""".format(player.username))
    input("\nPress Enter to continue...")

def endgame():
    endgame_msg= None
    win= False

    if car.fuel_cur <= 0: #You lose if you run out of fuel
        endgame_msg= "Your car got an engine breakdown!\nRemember to always to have some extra fuel..."
    elif car.tires < 4 and (player.cash-((4-car.tires)*100)<= 0.5): #You lose since you can't earn more money if your car is broken
        endgame_msg= "You can't afford the tires you need to use your car!\nWithout a functional car, you will never be able to earn any \nmoney and pay for new tires!"
    elif car.km_since_repair >= 2000:
        endgame_msg= "Your car is in a too bad shape to drive. \nYou have to repair the car from time to time!"
    elif not player.alive:
        endgame_msg= "You died!"
    elif player.cash <= 0:    #You lose if you have less than 0 $ cash
        endgame_msg= "You've used all your cash!\nRemember to always keep some extra cash for unexpected costs..."
    elif world.cur_day == 30:   #The game will end
        player.money_banked += int(round(player.cash))
        if player.money_banked > 3500: #You won!
            win= True
            world.is_active = False
            endgame_msg= "The month have passed and the challenge between you and your \nfriend is over!\nYou won the challenge by earning {:.0f} $ more than your friend!\nWell done!".format(float(player.money_banked-3500))
        else:   #You failed!
            world.is_active = False
            endgame_msg= "The month have passed and the challenge between you and your \nfriend is over!\nYour friend earned {:.0f} $ more than you!".format(float(3500-player.money_banked))
    else:   #The game continues and the next day starts
        world.cur_day+=1

    if not win and endgame_msg:
        time.sleep(2)
        print("\n\n"+"-=-"*21)
        print("{:^63}".format("Game Over!"))
        print("-=-"*21+"\n{}".format(endgame_msg))

    elif win and endgame_msg:
        time.sleep(2)
        print("\n\n"+"-=-"*21)
        print("{:^63}".format("Victory!"))
        print("-=-"*21+"\n{}".format(endgame_msg))

    if endgame_msg:
        datetime= time.strftime("%H:%M:%S - %d/%m/%Y")
        datarow= player.username, player.money_banked, gameversion, datetime
        input("\nPress Enter to view the highscores!\n")
        highscores(datarow)

def highscores(datarow):  #Read and write highscores
    corrupt_file= False
    if datarow== None:
        hs_type= 1 #If highscores called from main menu --> Read Only-Mode
    else:
        hs_type= 2 #If highscores called in-game --> Write & Read

    try:    #Try opening the hsdb
        with open("hsdb.csv") as hs_db:
            pass
    except IOError: #File not found
        print("\nCouldn't find any file with previous highscores.")
        print("Creating 'hsdb.csv' in the same folder as this game.")

        with open("hsdb.csv", "w") as hs_db:   #Creating new file
            csv_handler = csv.writer(hs_db, delimiter=';', quoting=csv.QUOTE_ALL)
            if hs_type== 2:
                csv_handler.writerow(datarow)
            else:
                csv_handler.writerow("")

    if hs_type== 2:
        #Append the data from current session to the last line in file
        with open("hsdb.csv", "a") as hs_db:
            csv_handler = csv.writer(hs_db, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
            csv_handler.writerow(datarow)

    try:#Read from ('hsdb.csv') --> Store each line in dict --> Store each dict in a list
        highscores = []
        with open("hsdb.csv", "rt") as hs_db:
            for line in csv.reader(hs_db, delimiter=';', quoting=csv.QUOTE_NONNUMERIC):
                if line != []:  #quick fix to skip empty lines
                    hs = {'username': line[0][0:16],
                          'money_banked': int(line[1]),
                          'gameversion': line[2],
                          'datetime': line[3]}
                    highscores.append(hs)
            if hs_type== 2:
                session_entry = highscores[-1]
                session_score = session_entry.get('money_banked')

    except ValueError:  #The file has less or more keys than it should have (File is Corrupt)
        print("\nThe file ('hsdb.csv') is corrupt and won\'t work.")
        corrupt_file = True

    if not corrupt_file:    #The flow for normal executions of the script
        #Sort the scores using the key 'money_banked' from highscores dict.
        sorted_by_scores = sorted(highscores, key = lambda x: x['money_banked'], reverse = True)

        if hs_type== 2:
            session_position = 1
            total_entries = len(sorted_by_scores)
            for line in sorted_by_scores:   #Try to find the current session_position
                if line == session_entry:   #in the ('hsbd.csv')-file
                    break
                else:
                    session_position += 1

        print("\n"+"-=-"*21) #Format and print highscores
        print('{0:^63}'.format("Highscores: All Time Top 10"))
        print("-=-"*21)
        print(' {0:^16s} {1:^8s} {2:^13s} {3:^21s} '.format("Username", "Score", "Version", "Time & Date"))
        print("-=-"*21)
        for score in sorted_by_scores[:10]:
            print(' {0:^16s} {2:^8d} {1:^13s} {3:>21s} '.format(*list(score.values())))
        print("-=-"*21+"\n")

        if hs_type== 2:
            print("{0}, Your score for this session was {1:.0f} points.\nThis placed you on position {2}/{3}".format(player.username, session_score, session_position, total_entries))

    else:   #The ('hsdb.csv')-file is corrupt and won't work
        print("\nThe highscores can't be printed since the file storing the data is corrupt.\nDON\'T MODIFY ('hsdb.csv') MANUALLY!.")
        print("Delete the file ('hsdb.csv') and restart the game to fix the problem.")
    time.sleep(6)   #Long sleep to let player view highscores
    input("\nPress Enter to continue...")

if __name__=='__main__':
    recent_user= None
    game_running= True
    while game_running:
        player= Player()    #Create player-object -> variables connected to the player.
        world= World()      #Create world-object -> variables connected to the world.

        menu(recent_user)   #Main Menu
        start_new_session() #Startscreen - Displayed when game session starts

        print("\nDecide what car you want to use:")
        print("'1': Ferrari - HIGH speed, HIGH fuel consumption, LOW safety\n'2': Mini Cooper - LOW speed, LOW fuel consumption, MEDIUM safety")
        running= True
        while running:
            carchoice= input("")    #Let player decide type of car
            if carchoice == '1':
                print("\nFerrari chosen!")
                car, running= Ferrari(), False
            elif carchoice == '2':
                print("\nMini Cooper chosen!")
                car, running = MiniCooper(), False
            else:
                print("I don\'t understand. Try again!")
                running= True

        car.car_stats()
        time.sleep(2)
        input("\n\nPress Enter to start the game!\n")

        #Main Gameplay-Loop
        while (player.cash > 0.5 and world.cur_day <= 30
                                 and player.alive
                                 and (player.cash-(4-car.tires)*75) >= 0.5
                                 and world.is_active):
            world.new_day() #Display current world and player stats
            player.mission()    #Simulate mission
            if player.cash > 0.5:#Only run if the player actually can do stuff
                if car.tires < 4 and (player.cash-((4-car.tires)*75))<= 0.5:
                    pass
                elif not player.alive:
                    pass
                else:
                    world.evening() #Post-mission
            endgame()   #Check if the game should continue
        recent_user= player.username
        #This is the last line!
