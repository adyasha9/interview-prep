# Q1: A town is building a watchtower. The watchtower is located at (0, 0). 
# Each unit height of the watchtower has a cost H. 
# There are N houses located at (x, y) coordinates. 
# Each house will pay cost C if it comes under the surveillance of the watchtower.
#  The horizontal distance covered by the watchtower is the same as it's height. 
# Find out the max profit you can make.


# Inputs:

# N number of houses
# list of (x, y) coordinates
# H cost to build unit height
# C cost each house pays the watchtower


# In the beginning the watchtower was located at the origin.
#  For the followup he said watchtower location will be provided.
#  The (x, y) coordinates can be floats as well as H and C.


# Height choices come from house y-coordinates.
# Each height determines a horizontal coverage range [-h, h].
# We calculate the profit for each height and maximize it.
# Sorting + Iteration results in O(N log N) complexity.

# Problem Setup:
# A watchtower is built at (0,0).
# The tower has height = h.
# It covers a square centered at (0,0) with width 2 × h.
# Houses are given as (x, y) coordinates.
# A house is covered if its x-coordinate is in the range [-h, h].
# The profit formula is:
# profit=(number of covered houses×𝐶)−(height×𝐻)
# Goal: Find the height (h) that maximizes profit.

# We iterate over different tower heights and calculate coverage.

# Tower Height (h)	Coverage Range [-h, h]	Covered Houses (x-values)	Profit Calculation	Total Profit
# h = 2	                  [-2, 2]	              (1,2), (-2,3)	          (2 × 5) - (2 × 1.5)	    7
# h = 3	        	      [-3, 3]	              (1,2), (-2,3), (3,4)     (3 × 5) - (3 × 1.5)	   10.5
# h = 4		        	  [-4, 4]                 (1,2), (-2,3), (3,4)     (3 × 5) - (4 × 1.5)	    9

# Input:
# Houses:(1,2),(−2,3),(3,4)
# Tower cost per unit height: H = 1.5
# Charge per covered house: C = 5

def maxProfit(houses,h,c):
    houses = houses.sort(key = lambda house:house[1])
    maxProf = float("-inf")
    for _ ,y in range(len(houses)):
        tempHeight = y
        covered_houses = sum(1 for x,_ in range(len(houses)) if -tempHeight<=x<=tempHeight)
        profit = (covered_houses * c) - (covered_houses * h)
        maxProf = max(maxProf,profit)
    return maxProf


# Follow-up: Watchtower at Arbitrary Location
# If the watchtower is at (wx, wy) instead of (0,0):

# The covered range becomes [wx - height, wx + height] for x.
# The houses covered should have wy ≤ y ≤ wy + height.

def maxProf(houses,wx,wy,h,c):
    houses = houses.sort(key = lambda house:house[1])
    maxProf = float("-inf")
    for _ ,y in range(len(houses)):
        tempHeight = y - wy
        if tempHeight < 0:
            continue
        covered_houses = sum(1 for x,y in range(len(houses)) if (-tempHeight + wx <=x<=tempHeight +wx) and (wy <= y <= wy + tempHeight))
        profit = (covered_houses * c) - (covered_houses * h)
        maxProf = max(maxProf,profit)
    return maxProf


# Sorting the houses: O(NlogN)
# Iterating over N heights and checking coverage: O(N2) (can be optimized using a sliding window approach)