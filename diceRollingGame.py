""" This is a dice rolling game, written in Python. 

    So the question is ... 
        If a player rolls 2, 6 sided dice 1000 times.
        What number will the 2 dice sum to most often, 
        and what is the expected frequency of this number?
    
    To win the game, 
        a) predict the correct number that the 2 dice will most likely sum to and,
        b) correctly predict the frequency of rolls at this number. 
    To play, take your best guess, run the program, and see if you were correct!    
   
    Note that, the 2 dice are generated and 
    the results and frequencies data is visualized and analyzed 
    in diceRollingGame__.html 
    
    Full disclosure, this project is inspired by __begginerscode__ """


# imports
from random import randint
from plotly.graph_objs import Bar, Layout 
from plotly import offline

# create a class (definition of something) representing a single dice
class dice:
    def __init__(self, num_sides=6): #initialize a 6 sided dice, CAN CHANGE # SIDES HERE
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides) #returning a random # between 1 and number of sides

#create instances of the class dice 
dice_1 = dice()
dice_2 = dice()
#dice_3 = dice() 
#dice_4 = dice() 
#dice_5 = dice()
#dice_6 = dice()  

allResults = [] # create an empty list for results

for num in range (1000): # roll the dice 1000 times and mark it in a results list
    result = dice_1.roll() + dice_2.roll() 
    allResults.append(result)

#print(allResults)


allFrequencies = [] #create an empty list for frequencies

max_result = dice_1.num_sides + dice_2.num_sides # Dice 1 (6) + Dice 2 (6)

for value in range(2, max_result+1): # since we have 2 dice the min # is 2, the max # is 12 but since we start by 0 we have to add +1.
                                     # Don't want to hard code in case we want to change our # of sides.
    frequency = allResults.count(value)
    allFrequencies.append(frequency) # how many times we get each number (2-12)

#print(allFrequencies) 

x_val = list(range(2, max_result+1)) #defining x value in graph (2-12)
diceData = [Bar(x=x_val, y=allFrequencies)] # creating data into a bar graph plotting x (values), y (frequencies)

x_axis_config = {'title': 'SUM of 2, 6 sided DICE', 'dtick': 1} 
y_axis_config = {'title': 'Frequency'}

graphLayout = Layout(title='Did you WIN OR LOSE the game? Results of rolling 2, 6 sided dice, 1000 times', xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({'data': diceData, 'layout':graphLayout}, filename = "diceRollingGame__.html") 