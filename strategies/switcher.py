#!/usr/bin/env python3
'''
Every time you cheat it will switch between Coop or Cheat.
'''

def run(turns: list, memory: list) -> tuple:
	decision = bool(memory[-1])

	if not turns[-1]:
		decision = not decision
	
	return (decision, decision)