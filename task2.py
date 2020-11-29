#Imports
import random

#Functions
def gen_coord ():
    # DO NOT MODIFY THIS FUNCTION
    return int(random.random() * NERVE_SIZE )

def sort_by_x(tup):
    #Helper function to sort the Neuron Positions by its x values
    return tup[0]    

def euclidean(u,v):
    #Calculates the Euclidean Distance between the 2 input points
    return ((u[0]-v[0])**2 + (u[1]-v[1])**2)**0.5


# Logic
#     Worst case time complexity of the sorting algorithm is O(N.logN)
#     Once the neuron positions are sorted by their x-values, only a small window of Neurons need to be looked at and compared 
#     with its neighbours to check for Conflict
#     By distance formula, the maximum distance between the x co-ordinate of any two neurons is the conflict_radius squared
#     So the window size to compare points is very small.
#     Thus, loop of complexity O(N*k) is used, where k is the size of the window, and the neurons in a conflicted state.
#     Since it is very unlikely, that all ten thousand neurons lie within the conlict radius, this algorithm will do much better than 
#     the N squared brute force algorithm.
#     The final complexity of this code will be O(N*logN + N*k) which is just O(N*logN)


        
def check_for_conflicts(nerves, conflict_radius):
    positions = sorted(nerves, key = sort_by_x) #Get positions sorted by x-coordinate
    s = set() #Empty set to count neurons accurately
    for ind in range(len(positions)-1):
        start = positions[ind] #First neuron at Start of the window
        nex = positions[ind+1] #First neuron to compare
        t = ind+1
        while nex[0] < start[0]+ (conflict_radius**2): #Keep comparing as long as the x-coordinate of the next neuron is lesser than conflict_radius squared
            if euclidean(start,nex)<conflict_radius: #Check the distance between the neurons
                s.add(tuple(start)) #Adding to set to ensure no duplicates 
                s.add(tuple(nex))
            #Check for next neurons
            t = t+1
            if t != len(positions): 
                nex = positions[t]
            else:
                break
    return len(s) #

#Coding the N squared solution to compare the efficiency and check answer
def conflicts_n2(nerves, radius):
    set_is  = set()
    for i in range(len(nerves)):
        for j in range(len(nerves)):
            if i!=j:
                dist = euclidean(nerves[i], nerves[j])
                if dist < radius:
                    set_is.add(i)
#                     set_is.add(j)
    return len(set_is)

#NOTE: Check the ipynb for plots comparing the 2 algorithms

#Main Code
random.seed(7) # Setting random number generator seed for repeatability
NUM_NEURONS = 10000
NERVE_SIZE = 128000 # nanometers
CONFLICT_RADIUS = 500 # nanometers

neuron_positions = [[ gen_coord () , gen_coord ()] for i in range ( NUM_NEURONS )]
print(" Final Algorithm has time complexity of O(N.logN)")
n_conflicts = check_for_conflicts (neuron_positions ,CONFLICT_RADIUS)
print (" Neurons in conflict : {}". format ( n_conflicts ))

print("\n The N^2 solutions gives the following result.")
n_conflicts = conflicts_n2 (neuron_positions ,CONFLICT_RADIUS)
print (" Neurons in conflict : {}". format ( n_conflicts ))