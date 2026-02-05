---
layout: post
title: "Tic-Tac-Toe Q-Learning Application"
date: 2026-02-04
categories: [Projects, Reinforcement Learning, Algorithms]
---

-----WORK IN PROGRESS-----

## Overview
[Q-Learning](https://en.wikipedia.org/wiki/Q-learning) is a reinforcement learning algorithm that trains an agent to associate specific actions with long-term rewards.  By using the Bellman equation which tuned to iteratively update a Q-Table, the agent iteratively discovers the highest quality moves for any given board position. Because Tic-Tac-Toe has a relatively small state space, it serves as a perfect environment for demonstrating how Q-Learning reaches optimal decision-making.

## Problem Statement
Use Q-Learning to train an unbeatable Tic-Tac-Toe agent. 

## Strategic Approach
I will implement a Temporal Difference Q-Learning approach to train two unbeatable Tic-Tac-Toe agents. Through self-play over 100,000 episodes, the agents will iteratively refine their policies to achieve optimal decision-making.

### State Representation & Memory
The 3x3 board will be compressed into a 9-character string, which will serve as a unique identifier in a hash map (the Q-Table). This table will store the quality of every legal next action for an encountered state.

### Exploration
The agents will learn using an $\epsilon$-greedy strategy. Early on, the agents will explore aggressively. As they build out their Q-Tables, $\epsilon$ will decay, resulting in more exploitation of their understanding of the state-space and the quality of available actions. Without an $\epsilon$-greedy strategy, the agents may converge on a suboptimal local maximum (a strategy which is passable but flawed).

### Reward Structure and Bootstrapping

The agents will receive rewards at the end of each game, incentivizing sequences of actions that lead to desirable outcomes (as defined by the reward structure). Winning sequences will receive the largest rewards. Drawing sequences will receive middling rewards.  Losing sequences will receive negative rewards.  Through bootstrapping, the rewards are backpropagated, increasing the perceived value of each state leading up to a winning action and encouraging the agent to pursue those valuable states. 

This logic is called Temporal Difference Learning. In early games, all Q-Values are 0, and only the last action in a game gets a non-zero update.  As training progresses, the values from the final moves will bleed into the actions that preceded them. In the final stages of training, the agent will see a win coming many moves in advance based on the path formed by the Q-Table it references.

## Implementation
I tained the agents in `tictactoe_qlearning_train.py`. 

The `win_check` function accepts a boardstate and checks for the satisfaction of a win condition by either player.  It does this systematically by iterating over all of the rows, columns, diagonals, and antidiagonals and determining whether any are comprised of only ones or twos:
```python
def win_check(board):

    for i in range(3):
        
        # Check whether any rows contain all 1s or 2s
        if np.all(board[i, :] == 1):
            return 1
        if np.all(board[i, :] == 2):
            return 2
        
        # Check whether any columns contain all 1s or 2s
        if np.all(board[:, i] == 1):
            return 1
        if np.all(board[:, i] == 2):
            return 2
    
    # Check whether the diagonal contains all 1s or 2s
    if np.all(np.diag(board) == 1):
        return 1
    if np.all(np.diag(board) == 2):
        return 2
    
    # Check whether the antidiagonal contains all 1s or 2s
    if np.all(np.diag(np.fliplr(board)) == 1):
        return 1
    if np.all(np.diag(np.fliplr(board)) == 2):
        return 2
    
    return None
```
The function returns a one if Player One has satisfied a win condition, a two if Player Two has satisfied a win condition, and "None" if neither player has satisfied a win condition.  This function is called after each agent's action to determine whether play should continue or a reward should be distributed.


The `QAgent` class utilizes the Bellman Equation to build a Q Table which describes the value of each available action for a given state.

It first initializes all of the relevant attributes:
- **player_id**: The identifier used to distinguish two participating players from one another.
- **q_table**: The table in which the quality of each potential action for a given board state will be stored.
- **epsilon**: The exploration rate, which determines the percentage of the time that a move will be randomized (instead of selecting the highest value action from the Q-Table).
- **alpha**: The learning rate, which shapes the evolution of the Q-Values in the Q-Table when new information is introduced.
- **gamma**: The discount factor, which determines the importance of future rewards compared to immediate rewards. 


```python
# Create a class to build a q table which evaluates and stores the maximum quality of each potential action for a given board state
class QAgent:

    def __init__(self, player_id, epsilon=0.2, alpha=0.3, gamma=0.9):

        # Initialize player_id (1 or 2) to distinguish between players while training
        self.player_id = player_id

        # Initialize a q_table to store the quality of each potential action for a given board state
        self.q_table = {}

        # Initialize epsilon to establish an exploration rate (the percentage of randomized moves)
        self.epsilon = epsilon

        # Initialize alpha, the learning rate, which determineds to what extent newly-acquired information overrides old information
        self.alpha = alpha

        # Initialize gamma, the discount factor, which determines the importance of future rewards compared to immediate rewards
        self.gamma = gamma
```



-----BELOW THIS LINE IS TEMPLATE FROM ANOTHER README-----

The `save_agent` function

`list_converter` works the same in both parts of the challenge.
1. **Initialize an empty list** to store signed integers in.  
2. **Iterate over the input list** of alphanumeric strings.
3. **Initialize helper variables** to store the direction ('L' or 'R') and the following integer for each element in the elves' instructions.
4. **Assign the correct sign based on the first character of the string**: strings beginning with 'L' will be converted into negative integers, and strings beginning with 'R' will be converted into positive integers.  The magnitude of the integer is equal to the integer converted string following the first character.
5. **Append the converted list element to `signed_integer_instructions`.** 
6. **Return `signed_integer_instructions`.**
```python
def list_converter(instructions_list):

    # 1. Initialize an empty list
    signed_integer_instructions = []

    # 2. Iterate over the input list
    for item in instructions_list:
        
        # 3. Initialize helper variables
        direction = item[0]
        magnitude_int = int(item[1:])

        # 4. Assign the correct sign based on the first character of the string
        if direction == "R":
            signed_value = magnitude_int

        else:
            signed_value = -magnitude_int

        # 5. Append the converted list element to signed_integer_instructions
        signed_integer_instructions.append(signed_value)

    # 6. Return signed_integer_instructions
    return signed_integer_instructions
```
### Part 1
Counting zeros as the dial lands on them is straightforward: 
1. **Call the `list_converter` function** to convert the alphanumeric instructions into a list of usable, signed integers.
2. **Initialize helper variables**, `zero_count` and `value`.  `zero_count` stores the number of zeros on which the function lands while 'turning the dial.'  `value` stores the integer on which the dial lands after a turn.
3. **Iterate over the instructions** in `signed_instructions_list` (an output of the `list_converter` function) and apply the modulu operator to the sum of the integer the dial started on (`value`) and the current element in the elves' instructions.
4. **Add one to `zero_count` if the dial lands on zero** (meaning the modulo operator yielded a value of zero).
5. **Return `zero_count`.**

```python
def zero_counter(instructions_list):

    # 1. Call the list_converter function
    signed_instructions_list= list_converter(instructions_list)

    # 2. Initialize helper variables
    zero_count = 0
    value = 50

    # 3. Iterate over the instructions
    for item in signed_instructions_list:
        value = (value + item) % 100

        # 4. Add one to the zero count if the dial lands on zero
        if value == 0:
            zero_count += 1
    
    # 5. Return zero count
    return zero_count
```

### Part 2
Counting zeros as the dial passes them is more difficult: 
1. **Call the `list_converter` function** to convert the alphanumeric instructions into a list of usable, signed integers.
2. **Initialize helper variables**, `zero_count` and `value`.  `zero_count` stores the number of zeros on which the function lands while 'turning the dial.'  `value` stores the integer on which the dial lands after a turn.
3. **Iterate over the instructions** in `signed_instructions_list` (an output of the `list_converter` function) and apply the modulu operator to the sum of the integer the dial started on (`value`) and the current element in the elves' instructions.
4. **Do nothing for a zero magnitude turn.**
5. **Use floor division to determine the number of times zero is passed**.  When starting at zero and turning left, there is a subtlety: if a negative number is used for the floor division calculation, the result will not align with the logic we are simulating.  For this reason, flip the sign of the element of `signed_instructions_list` when performing the calculation.  Alternatively, flip the sign of the result.
6. **Use floor division to determine the number of times zero is passed.**  When performing a counter-clockwise turn starting from a nonzero `value`, we cannot simply flip the sign of the instruction and proceed with floor division as before.  Nor can we simply subtract from `value` because a quirk of floor division with negative numbers is that: `-1 // 2` returns `-1` instead of `0` as we might expect.  There are a number of ways to work around this pitfall, but I opted to maintain an approach that is consistent with the previous step: simulate a logically-equivalent clockwise turn.  To do this, we set an artificial starting value of $100$ minus the actual starting `value` and flip the sign of the element in `signed_instruction_list`.  For a starting value of 40 and an input of -110, our simulation will act as if it is starting at 60 and increasing by 110 (arriving at 170) before performing the floor division.  This may seem counterintuitive, but note that turning the dial 30 more clicks in the same direction will register the next zero.  This is logically consistent with our starting parameters and, as it turns out, holds for all edge-cases.  I have included a table comparing the way floor division operates for negative and positive float results.

7. **Use floor division to determine the number of times zero is passed.**  For a clockwise turn, no mental gymnastics are required.
8. **Update `value` using the modulo operator.**
9. **Return `zero_count`.**

```python
def zero_counter(instructions_list):

    # 1. Call the list converter function
    signed_instructions_list = list_converter(instructions_list)

    # 2. Initialize helper variables
    zero_count = 0
    value = 50

    # 3. Iterate over the instructions
    for item in signed_instructions_list:

        if item < 0:

            if value == 0:
                 # 4. Do nothing for a zero magnitude turn
                 if item == 0:
                      pass
                 
                 # 5. Use floor division to determine the number of times zero is passed
                 else:
                    zero_count += - item // 100

            # 6. Use floor division to determine the number of times zero is passed
            else:
                zero_count += (100 - value - item) // 100

        # 7. Use floor division to determine the number of times zero is passed
        else:
            zero_count +=  (value + item) // 100

        # 8. Update value using the modulo operator
        value = (value + item) % 100

    # 9. Return zero_count 
    return zero_count
```


## Complexity Analysis
The requirements of our algorithm grow with the size of our input instructions from the elves ($n$).

### Time Complexity: $O(n)$
Parts 1 and 2 both have linear time complexity: $O(n)$.
1. **Conversion:** `list_converter` makes one pass through the input list.  Because string-slicing and integer-conversion are performed on short strings, they are effectively constant-time, $O(1)$, operations, meaning their execution time does not increase with the size of the input data.  However, while processing an individual instruction is a constant-time operation, we must perform this for every instruction in the input, so `list_converter` scales linearly, $O(n)$, with the size of the input
2. **Simulation:** `zero_counter` makes a second pass through the list.  Every operation inside the loop (whether the modulo math in Part 1 or the conditional floor division logic in Part 2) takes the same amount of time, regardless of how many instructions there are.

The total time, then, is: $O(n)+O(n)=O(2n)$, which simplifies to $O(n)$, as we are only concerned with the shape of the growth, not the exact number of operations.

### Space Complexity: $O(n)$
The space complexity is also linear, $O(n)$.
1. **Storage:** `list_converter` creates a new list, `signed_integer_instructions`, which is exactly the same length as the input list.
2. **Memory Trade-Off:** While this approach uses more memory than processing the strings within the simulation loop, it makes the code more readable and modular, which I elected to prioritize.

| Step | Operation | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| Preprocessing | `list_converter` | $O(n)$ | $O(n)$ |
| Simulation | `zero_counter` | $O(n)$ | $O(1)$* |
| Total | Full Program | $O(n)$ | $O(n)$ |

**The simulation itself is $O(1)$ space, but it relies on the $O(n)$ list created in the preprocessing stage.*

## Conclusion

This challenge gave me the opportunity to utilize some common functions in unique contexts and troubleshoot edge-cases in which my code was not working as intended.  I would enjoy attempting some other methods, such as iterating over a circularly-linked list to compare efficiency and simplicity.