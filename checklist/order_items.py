"""Compatibility view of the reviewed Task 1 design; authoritative source is JSON.
The original 70-item draft remains available in the baseline Git commit.
"""
import json
from pathlib import Path
DESIGN=json.loads(Path(__file__).with_name('task1_design.json').read_text())
ITEMS=[(d['ia'],d['screen'],d['expected'],d['spec'],d['origin']) for d in DESIGN]
