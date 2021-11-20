#!/usr/bin/env python3
from os.path import dirname, basename, isfile, join
from glob import glob

def loadStrategies() -> list:
	modules = glob(join(dirname(__file__)+'/strategies', "*.py"))
	raw = [__import__('strategies.'+basename(f)[:-3]) for f in modules if isfile(f) and not f.endswith('__init__.py')][-1]
	return [eval(f'raw.{strat}',{'raw':raw}) for strat in dir(raw) if not strat.startswith('_')]
