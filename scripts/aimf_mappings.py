#!/usr/bin/env python3
"""Repository-root entry point for the AIMF mapping generator.

The generator itself ships inside the distribution bundle so that a recipient
of the bundle can run the drift check the mapping documents cite.  The single
source of truth is::

    documents/AIMF-Full-Documentation/scripts/aimf_mappings.py

This shim exists only so the historical repository-root invocation keeps
working::

    python3 scripts/aimf_mappings.py check
    python3 scripts/aimf_mappings.py generate
    python3 scripts/aimf_mappings.py report

It resolves the packaged directory from its own location, so it behaves
identically from any working directory.
"""

from __future__ import annotations

import runpy
import sys
from pathlib import Path

TARGET = (
    Path(__file__).resolve().parents[1]
    / "documents"
    / "AIMF-Full-Documentation"
    / "scripts"
    / "aimf_mappings.py"
)

if not TARGET.is_file():
    print(f"aimf_mappings shim: generator not found at {TARGET}", file=sys.stderr)
    sys.exit(2)

runpy.run_path(str(TARGET), run_name="__main__")
