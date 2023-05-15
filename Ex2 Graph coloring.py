"""# **Ex. 2 Graph Coloring**"""

# A function to print the color configuration.
def printConfiguration(colorArray):
    print("The assigned colors are as follows:")
    for i in range(4):
        print("Vertex: ",
              i, " Color: ", colorArray[i])


# function to check if graph valid
def isSafe(graph, colorArray):
    for i in range(4):
        for j in range(i + 1, 4):
            if (graph[i][j] and colorArray[j] == colorArray[i]):
                return False
    return True



#recursive function to return true and false if the color m can be applied to vertex i
def graphColoringAlgorithm(graph, m, i, colorArray):
    # If we have reached the last vertex then check and print the configuration.
    if (i == 4):
        if (isSafe(graph, colorArray)):
            printConfiguration(colorArray)
            return True
        return False

    # Assigning color to the vertex and recursively calling the function.
    for j in range(1, m + 1):
        colorArray[i] = j
        if (graphColoringAlgorithm(graph, m, i + 1, colorArray)):
            return True
        colorArray[i] = 0
    return False


if __name__ == '__main__':
    graph = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0],
    ]
    m = 3

    # Initially the color list is initialized with 0.
    colorArray = [0 for i in range(4)]

    if (graphColoringAlgorithm(graph, m, 0, colorArray)):
        print("Coloring is possible!")
    else:
        print("Coloring is not possible!")
