"""The declared table of puzzle types the build renders (Plan 1537).

Every type that appears in puzzle-data.yaml today has a row here. A puzzle
whose type has no row is not rendered by anything: puzzle-status.py reports
it as `not-built`.
"""

PUZZLE_TYPES = ('mc', 'ord', 'tower', 'sim', 'mat', 'cip', 'ba', 'log', 'gd', 'km')
