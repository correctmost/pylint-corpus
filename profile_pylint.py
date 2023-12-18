import cProfile
import pstats
import sys

sys.argv = ['pylint', '--recursive=y', '.']
cProfile.run('from pylint import __main__', filename='stats')

with open('profiler_stats', 'w', encoding='utf-8') as file:
    stats = pstats.Stats('stats', stream=file)
    stats.sort_stats('tottime')
    stats.print_stats()
