"""# Ex.4 Water Jug using BFS and DFS"""

graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph, '5')    # function calling

from collections import deque


def BFS(a, b, target):

	m = {}
	isSolvable = False
	path = []


	q = deque()

	q.append((0, 0))

	while (len(q) > 0):
		u = q.popleft()# If this state is already visited
		if ((u[0], u[1]) in m):
			continue
		if ((u[0] > a or u[1] > b or
			u[0] < 0 or u[1] < 0)):
			continue

		# Filling the vector for constructing
		# the solution path
		path.append([u[0], u[1]])

		# Marking current state as visited
		m[(u[0], u[1])] = 1

		# If we reach solution state, put ans=1
		if (u[0] == target or u[1] == target):
			isSolvable = True

			if (u[0] == target):
				if (u[1] != 0):

					# Fill final state
					path.append([u[0], 0])
			else:
				if (u[0] != 0):

					# Fill final state
					path.append([0, u[1]])

			# Print the solution path
			sz = len(path)
			for i in range(sz):
				print("(", path[i][0], ",",
					path[i][1], ")")
			break

		# If we have not reached final state
		# then, start developing intermediate
		# states to reach solution state
		q.append([u[0], b]) # Fill Jug2
		q.append([a, u[1]]) # Fill Jug1

		for ap in range(max(a, b) + 1):

			# Pour amount ap from Jug2 to Jug1
			c = u[0] + ap
			d = u[1] - ap

			# Check if this state is possible or not
			if (c == a or (d == 0 and d >= 0)):
				q.append([c, d])

			# Pour amount ap from Jug 1 to Jug2
			c = u[0] - ap
			d = u[1] + ap

			# Check if this state is possible or not
			if ((c == 0 and c >= 0) or d == b):
				q.append([c, d])

		# Empty Jug2
		q.append([a, 0])

		# Empty Jug1
		q.append([0, b])

	# No, solution exists if ans=0
	if (not isSolvable):
		print("No solution")


# Driver code
if __name__ == '__main__':

	Jug1, Jug2, target = 4, 3, 2
	print("Path from initial state "
		"to solution state ::")

	BFS(Jug1, Jug2, target)

# This code is contributed by mohit kumar 29

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
    def dfs(curr):
        if curr[0] + curr[1] == z:
            return True

        if curr in visited:
            return False

        visited.add(curr)

        # fill x jug
        if curr[0] < x:
            if dfs((x, curr[1])):
                return True

        # fill y jug
        if curr[1] < y:
            if dfs((curr[0], y)):
                return True

        # empty x jug
        if curr[0] > 0:
            if dfs((0, curr[1])):
                return True

        # empty y jug
        if curr[1] > 0:
            if dfs((curr[0], 0)):
                return True

        # pour from x to y
        if curr[0] > 0 and curr[1] < y:
            amount = min(curr[0], y - curr[1])
            if dfs((curr[0] - amount, curr[1] + amount)):
                return True

        # pour from y to x
        if curr[1] > 0 and curr[0] < x:
            amount = min(curr[1], x - curr[0])
            if dfs((curr[0] + amount, curr[1] - amount)):
                return True

        return False

    if x + y < z:
        return False
    if z == 0:
        return True
    if x == 0 and y == 0:
        return False

    visited = set()
    return dfs((0, 0))

can_measure_water(5,3,4)

def dfs(jug1, jug2, goal):
    # Check if the goal has been reached
    if jug1 == goal or jug2 == goal:
        return True

    # Check if we have already explored this state
    if (jug1, jug2) in visited:
        return False

    # Mark this state as visited
    visited.add((jug1, jug2))

    # Recursively explore all possible states
    for action in actions:
        new_jug1, new_jug2 = apply_action(jug1, jug2, action)
        if dfs(new_jug1, new_jug2, goal):
            return True

    return False


def apply_action(jug1, jug2, action):
    if action == "fill1":
        return jug1, 4
    elif action == "fill2":
        return 0, jug2
    elif action == "empty1":
        return 0, jug1
    elif action == "empty2":
        return jug1, 0
    elif action == "pour12":
        return min(jug1, 4 - jug2), jug2 + min(jug1, 4 - jug2)
    elif action == "pour21":
        return jug1 + min(jug2, 3 - jug1), min(jug2, 3 - jug1)


def main():
    # Initialize the state of the jugs
    jug1, jug2 = 0, 0

    # Initialize the set of visited states
    visited 

    # Solve the problem using DFS
    if dfs(jug1, jug2, 2):
        print("The goal has been reached!")
    else:
        print("The goal cannot be reached.")


if __name__ == "__main__":
    main()
