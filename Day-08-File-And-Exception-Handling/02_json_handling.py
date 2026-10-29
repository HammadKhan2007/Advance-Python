# Day 08: Working with JSON in Python

import json
import os

print("=" * 60)
print("DAY 08: WORKING WITH JSON DATA")
print("=" * 60)

# Sample Python Dictionary
developer_profile = {
    "name": "Muhammad Hammad",
    "course": "Advance Python",
    "current_day": 8,
    "skills": ["Python", "Data Structures", "Git", "File I/O"],
    "is_active_learner": True,
    "stats": {
        "completed_days": 8,
        "github_commits": 130
    }
}

json_file = "developer_profile.json"

# 1. json.dump() -> Writing Python dict directly into a JSON file
print("\n--- 1. Writing Dict to JSON File (json.dump) ---")
with open(json_file, "w", encoding="utf-8") as f:
    json.dump(developer_profile, f, indent=4)
print(f"Profile saved to '{json_file}'.")

# 2. json.load() -> Reading JSON file back into a Python dict
print("\n--- 2. Reading JSON File into Python (json.load) ---")
with open(json_file, "r", encoding="utf-8") as f:
    loaded_data = json.load(f)

print(f"Student Name: {loaded_data['name']}")
print(f"Current Day : {loaded_data['current_day']}")
print(f"Skills List : {', '.join(loaded_data['skills'])}")
print(f"Commits     : {loaded_data['stats']['github_commits']}")

# 3. json.dumps() vs json.loads() (String conversions)
print("\n--- 3. String Conversions (dumps & loads) ---")
# dict to JSON formatted string
json_string = json.dumps(developer_profile, indent=2)
print("Type of json_string:", type(json_string))

# JSON string back to dict
parsed_dict = json.loads(json_string)
print("Type of parsed_dict:", type(parsed_dict))
print("Name from parsed dict:", parsed_dict["name"])

# Cleanup
if os.path.exists(json_file):
    os.remove(json_file)
    print(f"\nTemporary file '{json_file}' cleaned up.")
