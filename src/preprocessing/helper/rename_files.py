"""
The following code files to match the naming convention used for nnU-Net.
"""

import re
import os
from pathlib import Path

# define paths
SOURCE_DIR = Path("data/masks/collapsed/post_processed_combined_aligned_cleaned/")
DESTINATION_DIR = Path("data/masks/collapsed/post_processed_combined_aligned_cleaned/")

#PATTERN = re.compile(r"^colon_(\d+)_pos-(prone|supine).*\.mha$")
PATTERN = re.compile(r"^colon_(\d+)-(prone|supine).*\.mha$")

for f in sorted(SOURCE_DIR.glob("*.mha")):
    print(f)
    m = PATTERN.match(f.name)
    if not m:
        print(f"Skipping: {f.name}")
        continue

    number = int(m.group(1))
    position = m.group(2)
    new_name = f"colon_{number:04d}-{position}.mha"
    new_path = DESTINATION_DIR / new_name

    print(f"{f.name} -> {new_name}")
    os.rename(f, new_path)
