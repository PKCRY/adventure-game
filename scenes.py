import textwrap
import enemy

# basic scene class
class Scene(object):

    def enter(self):
        print("This scene isn't made yet.")

class Death(Scene):
    
    def enter(self):
        print('You are dead!')

#the other more specific scenes
#commented out scenes will be added later

class Tavern(Scene):

    def __init__(self):
        self.bar_visited = False
        self.strange_man_visited = False

    #This method decides what to do when offered an ale
    def bar_tend(self, choice, character):
        if choice == '1':
            if character.coins > 1:
                if character.coins > 0:
                    print('You buy an ale for 1 coin, and return to the tavern.')
                    character.coins -= 1
                    print(f"You have {character.coins} coins left")
                    return 'tavern'
                else:
                    print('You get caught trying to steal the barkeepers ale, he stabs you in the jugular.')
                    return 'death'
            else:
                print("You can't afford the ale, so you return the the tavern.")
                return 'tavern'
        elif choice == '2':
            print("You return to the tavern.")
            return 'tavern'

    def enter(self, character):
        print("You enter the Tavern. To your left is a trader who is")
        print("sitting alone in the corner. Straight ahead, there is the bar. To")
        print("your right there is a strange man, staring at you. Do you:")
        print("1. Go to the bar. \n2. Talk to the trader \n3. Talk to the strange man\n4. Leave the tavern.")
        user_input = input('> ')

        if user_input == '1':
            #If the user hasn't visited the bar before, give different dialogue.
            if self.bar_visited == False:
                self.bar_visited = True
                print("The bartender sees you coming and offers you some ale...")
                print("And some advice. \"Avoid the strange man over there!\"")
                print("Do you:\n1. Buy an ale.\n2. Go back to the tavern.")
                choice = input('> ')
                return self.bar_tend(choice, character)
                
            else:
                print("The bartender welcomes you back and offers you some ale!")
                print("Do you:\n1. Buy an ale.\n2. Go back to the tavern.")
                choice = input('> ')
                return self.bar_tend(choice, character)

        elif user_input == '2':
            print("As you approch the trader he says, \"If you wish to see my wares, meet me at my wagon!\"")
            print("You make your way back to tavern.")
            return 'tavern'

        elif user_input == '3':
            #If the user hasn't approached the stranger man before, give different dialogue.
            if self.strange_man_visited == False:
                self.strange_man_visited = True
                print("As you approach the strange man he gazes on you with curious eyes. He says to you:")
                print("You look like just the person I was looking for. Let me ask you a question...")
                print("Would you like to have enough gold to buy whatever you heart desired?")
                print("Well if you're interested, I can tell you where you might be able to find some. For a price.")
                print("For 3 gold, I'll tell you where the treasure is and how to reach it.")
                print("Do you:\n1. Give the strange man the 3 gold.\n2. Decline and return to the tavern.")
                choice = input('> ')

                if choice == '1':
                    if character.coins >= 3:
                        character.coins -= 3
                        print("You give the strange man 3 gold. He tells you: ")
                        print(f"You have {character.coins} coins left")
                        print("The treasure can be found in the Imbued Ruins Treasure room, the chest is locked.")
                        print("But I know the combination is 3, 4, 5. There's also another chest in the Ancient Mines ")
                        print("Treasure room, and that ones combination is 7, 6, 5.")
                        print("You take this information and return to the tavern")
                        return 'tavern'
                    else:
                        print("The strange man catches you trying to scam him, and stabs you.")
                        return 'death'

                elif choice == '2':
                    print("You politely decline and return to the tavern")
                    return 'tavern'

                else:
                    print("You accidentally trip and break every bone in your body, and then get impaled by a sword.")
                    return 'death'

            else:
                print("The strange man asks how it's been going. You reply 'Good' and head back to the tavern.")
                return 'tavern'

        elif user_input == '4':
            return 'town_center'

        else:
            print("Unforunately the ceiling collapses and lands directly on your head.")
            return 'death'
            
                

class TownCenter(Scene):
    
    def enter(self, character):
        print("In the town center you see a tavern, a general store, a trader's wagon, and a way out of town.")
        print("Do you go to:\n1. Tavern\n2. General Store\n3. Trader's Wagon\n4. Head out of town.")
        user_choice = input('> ')
        
        if user_choice == '1':
            print('You head towards the tavern.')
            return 'tavern'
        elif user_choice == '2':
            print('You head towards the general store.')
            return 'general_store'
        elif user_choice == '3':
            print('You head towards the trader wagon.')
            return 'trader_wagon'
        elif user_choice == '4':
            print('You head out of town on the road.')
            return 'road_out_of_town'
        else:
            print('While trying to make up your mind you get stabbed by a horse. What a shame.')
            return 'death'

class GeneralStore(Scene):
    
    def enter(self, character):
        print('General Store')

class TraderWagon(Scene):
    
    def enter(self, character):
        print('Trader Wagon')

class RoadOutOfTown(Scene):

    def enter(self, character):
        print('Road Out of town')

#From the Gloomy Forest, you get to explore the Imbued Ruins
class GloomyForest(Scene):
    pass

class ImbuedRuinsEntrance(Scene):
    pass

#class ImbuedRuinsFountain(Scene):
#    pass

#class ImbuedRuinsThrone(Scene):
#    pass

#class ImbuedRuinsGarden(Scene):
#    pass

class ImbuedRuinsTreasure(Scene):
    pass

#From the Somber Mountains, you get to explore the Ancient Mines.
class SomberMountains(Scene):
    pass

class AncientMinesEntrance(Scene):
    pass

#class AncientMinesMainHall(Scene):
#    pass

#class AncientMinesForge(Scene):
#    pass

#class AncientMinesJail(Scene):
#    pass

class AncientMinesTreasureRoom(Scene):
    pass