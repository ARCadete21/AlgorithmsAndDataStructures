# Algorithms and Data Structures Exercises
##### Algorithms and Data Structures - Data Science Degree - NOVA IMS

##
### Exercises

#### 1
This Python program allows users to compare the performance of various sorting algorithms on lists of integers. The user can input the initial size of the list, the incremental size of the list, and the number of iterations to run. The input list is initially unsorted, and random numbers within a specified range can be generated.

##### Inputs
- Initial size of the list
- Incremental size of the list
- Number of iterations
- Range of random numbers

##### Outputs
The program generates a matrix displaying the time taken (in seconds) by each algorithm for sorting lists of different sizes across iterations. The execution times are rounded to 5 decimal places.

#### 2 
This Python program allows users to input intervals of integer numbers (negative or positive) with a limit of -999 or 999. The intervals can be continuous, overlapping, or disconnected. The program sorts the intervals in an intercalated manner: the first interval is sorted in ascending order, the second is randomly sorted within the interval, the third is sorted in ascending order, and so on.

##### User Interaction
- The user can provide intervals or choose to quit the program.
- Intervals are defined as continuous sequences of integer numbers.
- Each interval should have a limit of -999 or 999.
- If intervals are continuous, they are merged and counted as a single interval.
- Overlapping intervals delete the overlapping part.

##### Sorting Mechanism
- Custom sorting functions are implemented, as taught in class.
- The first interval is sorted in ascending order.
- The second interval is randomly sorted within its limits.
- The third interval is sorted in ascending order again.
- This pattern continues for subsequent intervals.

#### 3
- Create a more difficult 5x5 variant of the [sliding tile puzzle](https://en.wikipedia.org/wiki/Sliding_puzzle).
- Create a "solve automatically" mode, which saves the current arrangement of the tiles and then attempts up to 40 random moves and stops if they have solved the puzzle. Otherwise, the puzzle loads the saved state and attempts another 40 random moves.
##

### Project Developed by:
- [Afonso Cadete](https://www.linkedin.com/in/afonso-roque-cadete/)
- [Marcelo Junior](https://www.linkedin.com/in/marceloptajunior/)
- [Rita Centeno](https://www.linkedin.com/in/rita-centeno/)