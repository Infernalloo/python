# Dictionaries
# Key - Value Pairs
{"Key": "Value"}
# To fetch a value = nameOfTheDictionary["Key"]
#                  we tap into the dic, assign the key, assign the value.
# To add a value = nameOfTheDictionary["KeyOne"] = "ValueOne"

# Nesting list into dictionary
travel_log = {
    "France" : ["Paris", "Lille", "Dijion"],  
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting dictionary into dictionary
travel_log = {
    "France" : {"cities_visited" : ["Paris", "Lille", "Dijion"], "total_visits" : 12},

    "Germany": {
        "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits" : [5, 2, 2],
    },
}

# Nesting dictionary into a list
travel_log = [
    {"country" : "France", "cities_visited" : ["Paris", "Lille", "Dijion"], "total_visits" : 12},
    {
        "country" : "Germany", 
        "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits" : [5, 2, 2],
    },
]
