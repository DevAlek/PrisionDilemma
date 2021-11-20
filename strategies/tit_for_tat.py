#!/usr/bin/env python3
'''
This strategy will cooperate until you cheat.
Then it will cheat once and repeat.
'''

def run(turns: list, memory: list) -> tuple:
	return ((True if turns[-1] else False), None)

# [ SIMPLE VERSION ]
# def run(turns: list, memory: list) -> tuple:
# 	decision = True
# 	remember = None'
# 	
# 	if not turns[-1]:
# 		decision = False
# 	
# 	return (decision, remember)