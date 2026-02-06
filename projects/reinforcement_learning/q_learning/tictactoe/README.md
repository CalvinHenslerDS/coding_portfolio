---
layout: post
title: "Tic-Tac-Toe Q-Learning Application"
date: 2026-02-04
categories: [Projects, Reinforcement Learning, Algorithms]
---

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
        
        if np.all(board[i, :] == 1):
            return 1
        if np.all(board[i, :] == 2):
            return 2
        
        if np.all(board[:, i] == 1):
            return 1
        if np.all(board[:, i] == 2):
            return 2
    
    if np.all(np.diag(board) == 1):
        return 1
    if np.all(np.diag(board) == 2):
        return 2
    
    if np.all(np.diag(np.fliplr(board)) == 1):
        return 1
    if np.all(np.diag(np.fliplr(board)) == 2):
        return 2
    
    return None
```
The function returns a `1` if Player One has satisfied a win condition, a `2` if Player Two has satisfied a win condition, and `None` if neither player has satisfied a win condition.  This function is called after each agent's action to determine whether play should continue or a reward should be distributed.


The `QAgent` class utilizes the Bellman Equation to build a Q Table which describes the value of each available action for a given state.

It first initializes all of the relevant attributes:
- **player_id**: The identifier used to distinguish two participating players from one another.
- **q_table**: The table in which the quality of each potential action for a given board state will be stored.
- **epsilon**: The exploration rate, which determines the percentage of the time that a move will be randomized (instead of selecting the highest value action from the Q-Table).
- **alpha**: The learning rate, which shapes the evolution of the Q-Values in the Q-Table when new information is introduced.
- **gamma**: The discount factor, which determines the importance of future rewards compared to immediate rewards. 


```python
class QAgent:

    def __init__(self, player_id, epsilon=0.2, alpha=0.3, gamma=0.9):
        self.player_id = player_id
        self.q_table = {}
        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma
```

Next, it defines a function, `get_state_id`, which compresses the board state (a NumPy array) into a 9-character string.  This makes storage and processing much more efficient throughout the training process.
```python
    def get_state_id(self,board):
        return "".join(map(str, board.flatten()))
```

The `choose_action` function accepts the current board state and the range of available actions, then references the Q-Table to determine the highest quality move from the current position.

First, `get_state_id` is called to compress the array into a string. Then, the function checks whether the key is already listed in `q_table`.  If it isn't, it is added, and the quality of all legal moves is defaulted to zero.

```python
    def choose_action(self, board, available_moves):

        state = self.get_state_id(board)

        if state not in self.q_table:
            self.q_table[state] = {move: 0.0 for move in available_moves}
```

A randomly-generated value between zero and one is compared to the exploration rate, `epsilon`, to determine whether an exploratory (randomly-selected) action will be performed.

```python
        if random.uniform(0,1) < self.epsilon:

            return random.choice(available_moves)
```

To select the best action, the function initializes a variable, `best_value` as negative infinity (to ensure that the first Q-Value the agent sees will exceed it). An empty list of `best_moves` is also initialized, and the function loops over the legal actions and their associated Q-Values for the current board state. If an encountered Q-Value is greater than the current `best_value`, `best_value` will be updated to the encountered Q-Value, and the list of `best_moves` will be replaced by the current move.  If an encountered Q-Value is equal to the current `best_value`, the associated action will be appended to `best_moves` instead.  Once all of the legal moves have been examined, an action will be selected from randomly from `best_moves`.

```python
        best_value = -float('inf')

        best_moves = []

        for move, value in self.q_table[state].items():

            if value > best_value:
                best_value = value
                best_moves = [move]

            elif value == best_value:
                best_moves.append(move)

        return random.choice(best_moves)
```

The `learn` function accepts the current board state, a selected action, a reward, the next board state, and a boolean stating whether the game has ended. It updates the Bellman Equation to populate the Q-Table with a new Q-Value for the selected action.

It starts by calling `get_state_id` on both the current and the next board (as determined by the selected action).  Then, it checks the Q-Table for its current estimate of the Q-Value for the selected move.

```python
    def learn(self, board, action, reward, next_board, game_over):

        state = self.get_state_id(board)

        next_state = self.get_state_id(next_board)

        current_q = self.q_table.get(state, {}).get(action, 0.0)
```

If the action resulted in a win, loss, or draw or if the next state is not already in the Q-Table, set `max_future_q` equal to zero.  Otherwise, set it equal to the highest Q-Value associated with the legal moves of `next_state`.

```python
        if game_over:
            max_future_q = 0

        else:
            if next_state not in self.q_table:
                max_future_q = 0
            
            else:
                max_future_q = max(self.q_table[next_state].values())
```

Next, `new_q` is calculated using the Bellman Equation with its associated parameters.  If the state is not in the Q-Table, it gets added.  The Q-Table is then updated with `new_q` to incorporate the learning from the selected action (which looks ahead to see if a favorable outcome is expected based on `max_future_q`). This is the bootstrapping which backpropagates rewards based on the anticipated value of future, legal actions.

```python
        new_q = current_q + self.alpha * (reward + (self.gamma * max_future_q) - current_q)

        if state not in self.q_table:
            self.q_table[state] = {}

        self.q_table[state][action] = new_q
```

Two instances of the QAgent class are then initialized as `player_1` and `player_2`, and the training parameters are established:
- **episodes**: The number of games the agents will play against each other
- **min_epsilon**: The minimum allowed value of the exploration rate
- **epsilon decay**: The rate at which `epsilon` decays from its initial value as training epsiodes are completed
- **win_reward**: The reward administered via the Bellman Equation following a winning move; +10 ensures that the agents are highly-incentivized to perform actions which may result in winning board states
- **loss_reward**: The reward administered via the Bellman Equation following a losing move; -10 ensures that the agents are highly-incentivized to avoid actions which may result in losing board states
- **draw_reward**: The reward administered via the Bellman Equation following a tying move; +2 ensures that the agents are motivated to seek wins over draws but draws over losses

```python
player_1 = QAgent(player_id=1, epsilon = 0.9)
player_2 = QAgent(player_id=2, epsilon = 0.9)

episodes = 100000
min_epsilon = 0.05
epsilon_decay = 0.99995
win_reward = 10
loss_reward = -10
draw_reward = 2
```

The agents then prepare to play 100,000 games against each other.  An empty (zero-filled) board is initialized, and `game_over` is set to `False`.  `player_1` is selected to play first, and the states and last actions of both players are set to `None`.

```python
for i in range(episodes):

    board = np.zeros((3, 3), dtype = int)

    game_over = False

    current_player = player_1

    player_1_last_state = None
    player_1_last_action = None
    player_2_last_state = None
    player_2_last_action = None
```

A list containing the zipped indices corresponding to each zero on the current board is initialized (and will be maintained throughout each game).  This informs the agents about the `available_moves` from the current board state.

If there are no zeros left on the board, the game ends in a tie.

```python
while not game_over:

        available_moves = list(zip(*np.where(board == 0)))

        if not available_moves:
            winner = None
            game_over = True
            break
```

Turns are taken by calling `choose_action` function method on `current_player`.  A copy of the previous board is saved, and the current board is updated with the selected action of the turn player.

After each action, `win_check` is called to determine whether the move resulted in a win.  If the game did not end, the Q-Table of the turn player is updated (with `reward` set to zero). The last state and action of the turn player is recorded, and the other player becomes the new turn player. As the agents learn, the exploration rate decays.

```python
        action = current_player.choose_action(board, available_moves)

        prev_board_copy = board.copy()

        board[action] = current_player.player_id

        winner_id = win_check(board)
        if winner_id == 1:
            winner = player_1
        elif winner_id == 2:
            winner = player_2
        else:
            winner = None
    
        game_over = winner is not None or 0 not in board

        if not game_over:
            if current_player == player_1 and player_2_last_state is not None:
                player_2.learn(player_2_last_state, player_2_last_action, 0, board, False)
            elif current_player == player_2 and player_1_last_state is not None:
                player_1.learn(player_1_last_state, player_1_last_action, 0, board, False)
        
        if current_player == player_1:
            player_1_last_state, player_1_last_action = prev_board_copy, action
            current_player = player_2
        else:
            player_2_last_state, player_2_last_action = prev_board_copy, action
            current_player = player_1

    player_1.epsilon = max(min_epsilon, player_1.epsilon * epsilon_decay)
    player_2.epsilon = max(min_epsilon, player_2.epsilon * epsilon_decay) 
```

If the last action resulted in a win for either player, update both of their Q-Tables with the appropriate reward (corresponding to a win, loss, or tie).

While the agents are training, a print message appears in the terminal every 10,000 episodes, providing the user with the current episode, the exploration rate of `player_1` to four digits, and the size of the Q-Table.

```python
    if winner == player_1:

        player_1.learn(player_1_last_state, player_1_last_action, win_reward, board, True)
        player_2.learn(player_2_last_state, player_2_last_action, loss_reward, board, True)

    elif winner == player_2:
        player_2.learn(player_2_last_state, player_2_last_action, win_reward, board, True)
        player_1.learn(player_1_last_state, player_1_last_action, loss_reward, board, True)
        
    elif winner is None:
        player_1.learn(player_1_last_state, player_1_last_action, draw_reward, board, True)
        player_2.learn(player_2_last_state, player_2_last_action, draw_reward, board, True)

    if i % 10000 == 0:
        print(f"Episode {i}: P1 Epsilon = {player_1.epsilon:.4f}, Q-Table Size = {len(player_1.q_table)}")
```

The `save_agent` function saves a trained agent as a `.pkl` file, which converts the entire `QAgent` instance into a byte stream.

```python
save_agent(player_1, 'player_1_qagent_brain.pkl')
save_agent(player_2, 'player_2_qagent_brain.pkl')
```


## Complexity Analysis
The primary bottleneck in this implementation is Python's string manipulation and dictionary overhead.

### Time Complexity:

`win_check` has linear time complexity: $O(n)$, scaling with the side length, 3.

| Operation | Complexity (Generalized $n$) | Complexity (Fixed 3 $\times$ 3) |
| :--- | :---- | :--- |
| Row Check | $O(n^2)$ | $O(1)$ |
| Column Check | $O(n^2)$ | $O(1)$ |
| Diagonal Check | $O(n)$ | $O(1)$ |
| Total Time | $O(n)$ | $O(1)$ |

<br>

The training loop has time complexity $O(E)$, which is Linear Time relative to the number of episodes.

| Operation | Complexity (Generalized $N$) | Complexity (Fixed 3 $\times$ 3) |
| :--- | :---- | :--- |
| Finding Moves | $O(N^2)$ | $O(1)$ |
| Choosing Action | $O(A)$ | $O(1)$ |
| Bellman Update | $O(1)$ | $O(1)$ |
| Full Match | $O(N^2 \times A)$ | $O(1)$ |
| All Episodes | $O(E \times N^2)$ | $O(E)$ |

<br>


### Space Complexity:

The space complexity of `win_check` is focused on how much additional memory is required to perform the row, column, and diagonal checks.  For a 3 $\times$ 3 board, this is effectively $O(1)$.

| Component | Operation | Space Usage (Generalized $n$) | Complexity (Fixed 3 $\times$ 3) |
| :--- | :---- | :--- | :--- |
| Input Board | The 3 $\times$ 3 array stored in memory | $O(n^2)$ | $O(1)$|
| Slicing | The temporary copy created by `board[i, :]` | $O(n)$ | $O(1)$ |
| Diagonal Extraction | The new array created by `np.diag(board)` | $O(n)$ | $O(1)$ |
| Board Mirroring | The copy created by `np.fliplr(board)` | $O(n^2)$ | $O(1)$ |
| Total Complexity | The extra memory used beyond the input | $O(n^2)$ | $O(1)$ |

<br>

The space complexity of the training loop is primarily driven by the Q-Table, which grows as the agent encounters new board states.  The total complexity for the training loop using the 3 $\times$ 3 Tic-Tac-Toe board is $O(S)$.

| Component | Operation | Space Usage (Generalized $n$) | Complexity (Fixed 3 $\times$ 3) |
| :--- | :---- | :--- | :--- |
| Board State | The 3 $\times$ 3 array stored in memory | $O(n^2)$ | $O(1)$|
| Q-Table (States) | The total unique board positions stored as keys | $O(n)$ | $O(1)$ |
| Q-Table (Actions) | The dictionary of Q-Values for each move per state | $O(n)$ | $O(1)$ |
| Recursion | The loop is iterative, not recursive | $O(n^2)$ | $O(1)$ |
| Total Complexity | The cumulative memory for all encountered states | $O(n^2)$ | $O(1)$ |

## Conclusion

This project gave me the opportunity to refine my Tic-Tac-Toe simulation logic, modify it for play between agents, and optimize it for training. It also gave me exposure to the Q-Learning algorithm.  Though the application was simple, it laid the foundation for future exploration of similar, more scaleable algorithms (namely Deep Q Network, or DQN), which I will use to optimize agents for real world applications, like my [Dragon Turbo](https://github.com/CalvinHenslerDS/coding_portfolio/tree/main/projects/reinforcement_learning/deep_q_learning/dragonturbo) project.