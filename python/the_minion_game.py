'''
Challenge: The Minion Game
Difficulty: Medium
Topic: Python (Basic)
Max Score: 40
Success Rate: 86.75%
Task: Given a string, judge the winner of the minion game.
Problem: https://www.hackerrank.com/challenges/the-minion-game/problem
'''

# Imports
import time
from io import StringIO

# Data
# raw_data = "BANANA" # Expected output: Stuart 12
# raw_data = "BAANANAS" # Expected output: Kevin 19
# raw_data = "ANANAS" # Expected output: Kevin 12
# raw_data = "BANAASA" # Expected output: Draw
# raw_data = "BANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASABANAASA" # Expected output: Draw
raw_data = "NANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANAN"
    # Expected output: Stuart 7501500

# Simulate User Input
input = StringIO(raw_data)

# Solution
# TODO: Optimize code

# Generate profile line by line
# First step:  pip install line-profiler
# Second step: Uncomment @profile below
# Third step:  kernprof -l --view --unit 1e-3 python/the_minion_game.py
# @profile

# Generate coverage of funtion
# from profilehooks import coverage
# @coverage

def minion_game(string):

    start_time_funtion = time.time()
    
    str_len = len(string)+1
    vowels = ['A', 'E', 'I', 'O', 'U']

    substrings = (string[i:j+1] for i in range(str_len) for j in range(i+1, str_len) if string[i:j+1] in string)
    s_score, k_score = 0, 0
    for s in substrings:
        if s[0] not in vowels:
            s_score += 1
        else:
            k_score += 1

    print(f"Stuart: {s_score}", f"Kevin: {k_score}")

    if s_score == k_score:
        result = 'Draw'
    elif s_score > k_score:
        result = f'Stuart {s_score}'
    else:
        result = f'Kevin {k_score}'
    
    end_time_function = time.time()
    print(f"Execution time of function: {end_time_function - start_time_funtion} seconds")

    return print(result)

# Main
if __name__ == '__main__':
    s = input.readline()
    minion_game(s)
