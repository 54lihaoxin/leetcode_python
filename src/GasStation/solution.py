# Gas Station
# 
# There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
# 
# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.
# 
# Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.
# 
# Note:
# The solution is guaranteed to be unique.

 
debug = True
debug = False


# from CommonClasses import * # hxl: comment out this line for submission


class Solution:
    
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        
        # hxl: determine whether it's possible to run a circle
        tank = 0
        for i in range(len(gas)):
            tank += gas[i]
            tank -= cost[i]        
        if tank < 0:
            return -1
        
        # hxl: now we know it's possible to run a circle
        tank = 0
        startStation = 0
        for i in range(len(gas)):
            tank += gas[i]
            tank -= cost[i]
            i += 1
            if tank < 0:    # hxl: then we know the start must exists in the rest of the stations
                tank = 0
                startStation = i

        return startStation
    