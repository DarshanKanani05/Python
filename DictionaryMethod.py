Dictionary = {
    "Name": "Darshan",
    "Last Name": "Kanani",
    "Marks": [76, 90, 83],
    "NestedDictionary": {
        "Course": "MScIT",
        "Sem": "3rd"
    }
}

Update = {
    "Father Name": "Bhagavanbhai"
}

print(Dictionary.keys())
print(Dictionary.values())
print(Dictionary.items())
Dictionary.update(Update)
print(Dictionary)
print(Dictionary.get("Name"))
