def numIslands(gridMap):
    '''
      Function to take in a 2D grid map of 11's and 0's
      Return number of islands in map
    '''
    q = deque()

# Examples
map1 = [
    [1, 1, 1, 1, 0],
    [1, 1, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
assert numIslands(map1) == 1

map2 = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1]
]
assert numIslands(map2) == 3


def timeToRot(grid):
    """
    Take in a grid of numbers, where 0 is an empty space, 1 is a fresh orange, and 2 is a rotten
    orange. Each minute, a rotten orange contaminates its 4-directional neighbors. Return the number
    of minutes until all oranges rot.
    """
    pass


# Test Cases
oranges1 = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]
assert timeToRot(oranges1) == 4

oranges2 = [
    [2, 1, 1],
    [0, 1, 1],
    [1, 0, 1]
]
assert timeToRot(oranges2) == -1

oranges3 = [
    [0, 2]
]
assert timeToRot(oranges3) == 0


def courseOrder(numCourses, prerequisites):
    """Return a course schedule according to the prerequisites provided."""
    pass


# Test Cases
courses1 = [[1, 0]]
assert courseOrder(2, courses1) == [0, 1]

courses2 = [[1, 0], [2, 0], [3, 1], [3, 2]]
possibleSchedules = [[0, 1, 2, 3], [0, 2, 1, 3]]
assert courseOrder(4, courses2) in possibleSchedules


# Example 1
Input: 4, [[1, 0], [2, 0], [3, 1], [3, 2]]
Output: [0, 1, 2, 3] or [0, 2, 1, 3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both
courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0, 1, 2, 3]. Another correct ordering is [0, 2, 1, 3].

# Example 2
Input: 4, [[1, 0], [2, 0], [3, 1], [3, 2]]
Output: [0, 1, 2, 3] or [0, 2, 1, 3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both
courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0, 1, 2, 3]. Another correct ordering is [0, 2, 1, 3].


def wordLadderLength(beginWord, endWord, wordList):
    """Return the length of the shortest word chain from beginWord to endWord, using words from wordList."""
    pass


# Test Cases
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

assert wordLadderLength(beginWord, endWord, wordList) == 5

# Example 1
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
