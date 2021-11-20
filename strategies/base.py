#!/usr/bin/env python3
'''
Use this template to make your own strategy.

Turns:    Return a list of previous decisions of the opponent.
Memory:   Return a list of past “remember”s the strategy returned. 
Decision: The final decision for the turn. True means cooperate and False means cheat.
Remember: Store a value to the list “memory”. Every turn a new memory is created and stored in the “memory” list.

OBS: This function always need to return a tuple of at least 2 items.
'''

def run(turns: list, memory: list) -> tuple:
	decision, remember = True, ''

	return (decision, remember)