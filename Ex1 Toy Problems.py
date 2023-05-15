# Ex1 Toy Problems

## banana and camel problem
"""

dp = [[-1 for i in range(3001)] for j in range(1001)]
 
# Recursive function to find the maximum
# number of bananas that can be transferred
# to A distance using memoization
def recBananaCnt(A, B, C):
 
    # Base Case where count of bananas
    # is less that the given distance
    if (B <= A):
        return 0
         
    # Base Case where count of bananas
    # is less that camel's capacity
    if (B <= C):
        return B - A
     
    # Base Case where distance = 0
    if (A == 0):
        return B
     
 
    # If the current state is already
    # calculated
    if (dp[A][B] != -1):
        return dp[A][B]
     
 
    # Stores the maximum count of bananas
    maxCount = -2**32
 
    # Stores the number of trips to transfer
    # B bananas using a camel of capacity C
    tripCount = ((2 * B) // C) - 1 if(B % C == 0 ) else ((2 * B) // C) + 1
 
    # Loop to iterate over all the
    # breakpoints in range [1, A]
    for i in range(1,A+1):
 
        # Recursive call over the
        # remaining path
        curCount = recBananaCnt(A - i, B - tripCount * i, C)
 
        # Update the maxCount
        if (curCount > maxCount):
            maxCount = curCount
 
            # Memoize the current value
            dp[A][B] = maxCount
         
    # Return answer
    return maxCount
 
# Function to find the maximum number of
# bananas that can be transferred
def maxBananaCnt(A, B, C):
 
    # Function Call
    return recBananaCnt(A, B, C)
 
# Driver Code
A = 1000
B = 3000
C = 1000
print("Maximum Bananas the camel can carry",maxBananaCnt(A, B, C))

def can_measure_water(x: int, y: int, z: int) -> bool:
    """
    Determines whether it is possible to measure z liters of water using two jugs of x and y liters.

    Args:
        x: An integer representing the capacity of the first jug.
        y: An integer representing the capacity of the second jug.
        z: An integer representing the desired amount of water to measure.

    Returns:
        A boolean indicating whether it is possible to measure z liters of water using the two jugs.
    """
    if x + y < z:
        return False
    if z == 0:
        return True
    if x == 0 and y == 0:
        return False
    gcd = find_gcd(x, y)
    return z % gcd == 0

def find_gcd(a: int, b: int) -> int:
    """
    Finds the greatest common divisor of two integers using the Euclidean algorithm.

    Args:
        a: An integer.
        b: An integer.

    Returns:
        An integer representing the greatest common divisor of a and b.
    """
    while b:
        a, b = b, a % b
    return a

can_measure_water(5,3,4)

"""### Water Jug Problem"""

# This function is used to initialize the
# dictionary elements with a default value.
from collections import defaultdict

# jug1 and jug2 contain the value
# for max capacity in respective jugs
# and aim is the amount of water to be measured.
jug1, jug2, aim = 4, 3, 2

# Initialize dictionary with
# default value as false.
visited = defaultdict(lambda: False)

# Recursive function which prints the
# intermediate steps to reach the final
# solution and return boolean value
# (True if solution is possible, otherwise False).
# amt1 and amt2 are the amount of water present
# in both jugs at a certain point of time.
def waterJugSolver(amt1, amt2):

	# Checks for our goal and
	# returns true if achieved.
	if (amt1 == aim and amt2 == 0) or (amt2 == aim and amt1 == 0):
		print(amt1, amt2)
		return True
	
	# Checks if we have already visited the
	# combination or not. If not, then it proceeds further.
	if visited[(amt1, amt2)] == False:
		print(amt1, amt2)
	
		# Changes the boolean value of
		# the combination as it is visited.
		visited[(amt1, amt2)] = True
	
		# Check for all the 6 possibilities and
		# see if a solution is found in any one of them.
		return (waterJugSolver(0, amt2) or
				waterJugSolver(amt1, 0) or
				waterJugSolver(jug1, amt2) or
				waterJugSolver(amt1, jug2) or
				waterJugSolver(amt1 + min(amt2, (jug1-amt1)),
				amt2 - min(amt2, (jug1-amt1))) or
				waterJugSolver(amt1 - min(amt1, (jug2-amt2)),
				amt2 + min(amt1, (jug2-amt2))))
	
	# Return False if the combination is
	# already visited to avoid repetition otherwise
	# recursion will enter an infinite loop.
	else:
		return False

print("Steps: ")

# Call the function and pass the
# initial amount of water present in both jugs.
waterJugSolver(0, 0)
