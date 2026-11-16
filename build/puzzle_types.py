"""The declared table of puzzle types the build renders (Plan 1537).

Written once, here. build-puzzles.py checks every puzzle's type against it
(an undeclared type is a build error naming the puzzle), renders the
container named in the `container` column, and emits the JS dispatch
`initPuzzleByType` from the `js_init` column. puzzle-status.py reports a
puzzle whose type has no row as `not-built`.

Every type present in puzzle-data.yaml has a row.
"""

PUZZLE_TYPES = {
    # type     container   JS statement that initialises one puzzle (el = container, d = data)
    'mc':    {'container': 'generic', 'js_init': 'initMC(el, d);'},
    'ord':   {'container': 'generic', 'js_init': 'initORD(el, d);'},
    'tower': {'container': 'tower',   'js_init': 'initTower(el, d);'},
    'sim':   {'container': 'generic',
              'js_init': 'if (d.sim_type === "resilience") initResilience(el, d); else initThreads(el, d);'},
    'mat':   {'container': 'generic', 'js_init': 'initMAT(el, d);'},
    'cip':   {'container': 'generic', 'js_init': 'initCIP(el, d);'},
    'ba':    {'container': 'generic', 'js_init': 'initBA(el, d);'},
    'log':   {'container': 'generic', 'js_init': 'initLOG(el, d);'},
    'gd':    {'container': 'gd',      'js_init': 'initGD(el, d);'},
    'km':    {'container': 'km',      'js_init': 'initKM(el, d);'},
}

# sim puzzles choose their simulation by `sim_type`; the JS row above names both.
SIM_TYPES = ('threads', 'resilience')


def js_dispatch():
    """The JS function initPuzzleByType(type, el, d), one case per declared type."""
    cases = '\n'.join(f'    case "{t}": {row["js_init"]} return;' for t, row in PUZZLE_TYPES.items())
    return ('function initPuzzleByType(type, el, d) {\n'
            '  switch (type) {\n'
            f'{cases}\n'
            '    default: throw new Error("undeclared puzzle type: " + type);\n'
            '  }\n'
            '}')
