#!/usr/bin/env python3
"""Rebuild current Task 1 deliverables from task1_design.json and recorded evidence.
Does not execute tests or invent results. Keep evidence/results.json under version control.
"""
import runpy
from pathlib import Path
runpy.run_path(str(Path(__file__).resolve().parents[1]/'task1/scripts/build_deliverables.py'),run_name='__main__')
