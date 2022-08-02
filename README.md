# python-excercise-2

Given a 2D grid of cells with obstacles and passages.
Write an algorithm which finds the shortest path from a cell A in the grid to a cell B in the grid, while only moving up, down, left or right through cells with passages. Log the route description to the console when done or an error message if no way was found. The grid should be represented as 2D list of booleans.
Think about test cases and write unit tests to verify your good works properly.

## Files:
* ex6.py ->program file
* test-path.py-> Test File


## Program Flow:
* The user inputs the start point and the destination point.
* A queue is initialised with the start point as the first element and a loop is iterated till the destination is reached or not found.
* The immediate neighbours of the start point to the top, left, bottom and right are searched and it moves in a direction where an obstacle is not found.
* The blocks already navigated are added to an array which containes already checked elements.
* The validated blocks without obstacle is added to the path queue.
* Once the desination is reached, the output path is displayed.

