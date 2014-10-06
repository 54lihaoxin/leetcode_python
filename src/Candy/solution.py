# Candy
# 
# There are N children standing in a line. Each child is assigned a rating value.
# 
# You are giving candies to these children subjected to the following requirements:
# 
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# What is the minimum candies you must give?


debug = True
debug = False


# from CommonClasses import * # hxl: comment out this line for submission


class Solution:
    
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        
        # hxl: handle edge cases
        if len(ratings) == 1:
            return 1
        elif len(ratings) == 2:
            if ratings[0] == ratings[1]:
                return 2
            else:
                return 3
            
        dict = {}  # hxl: K: rating; V: a set of indexes in the given array for the key rating
        candies = []
        
        for i in range(len(ratings)):
            candies.append(0)
            rating = ratings[i]
            if rating not in dict:
                dict[rating] = set([i])
            else:
                dict[rating].add(i)
                 
        sortedRatings = dict.keys()
        sortedRatings.sort()
        
        # hxl: give candies starting from the lower rating kids
        for i in range(len(sortedRatings)):
            rating = sortedRatings[i]
            for j in dict[rating]:
                if i == 0:  # hxl: everyone gets at least one candy, even for the kids with lowest rating
                    candies[j] = 1
                else:
                    if j == 0:  # hxl: first kid
                        if ratings[j] > ratings[j + 1]:
                            candies[j] = candies[j + 1] + 1
                        else:
                            candies[j] = 1
                    elif j == len(candies) - 1: # hxl: last kid
                        if ratings[j] > ratings[j - 1]:
                            candies[j] = candies[j - 1] + 1
                        else:
                            candies[j] = 1
                    else:   # hxl: any kid in the middle
                        if (ratings[j - 1] < ratings[j]
                            and ratings[j] > ratings[j + 1]):
                                candies[j] = max(candies[j - 1], candies[j + 1]) + 1
                        elif ratings[j - 1] < ratings[j]:
                            candies[j] = candies[j - 1] + 1
                        elif ratings[j] > ratings[j + 1]:
                            candies[j] = candies[j + 1] + 1
                        else:
                            candies[j] = 1

        if debug: print dict
        if debug: print candies
        
        return sum(candies)