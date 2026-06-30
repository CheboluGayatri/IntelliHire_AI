import json
from pprint import pprint

with open("data/candidates.jsonl", "r", encoding="utf-8") as f:
    first = json.loads(next(f))

print("TOP LEVEL KEYS")
print(first.keys())

print("\nPROFILE KEYS")
print(first["profile"].keys())

print("\nCAREER HISTORY KEYS")
print(first["career_history"][0].keys())

print("\nSKILL KEYS")
print(first["skills"][0].keys())

print("\nREDROB SIGNAL KEYS")
print(first["redrob_signals"].keys())