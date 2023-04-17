import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("path")
args = parser.parse_args()

print("Path argument is", args.path)
