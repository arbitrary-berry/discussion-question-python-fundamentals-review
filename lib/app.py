import ipdb
import random

foods = {
    "pie": "delicious",
    "broccoli": "not delicious",
    "carrots": "not delicious",
    "apples": "delicious",
    "peanut butter": "delicious",
}

for food in foods:
    if foods[food] == "delicious":
        print(food)

delete = [food for food in foods if foods[food] == "not delicious"]

for food in delete:
    del foods[food]

character_names = [
    "Daenerys Targaryen",
    "Jon Snow",
    "Arya Stark",
    "Tyrion Lannister",
    "Sansa Stark",
    "Cersei Lannister",
    "Margaery Tyrell",
]


def downcase_all(list_of_strings):
    lowercase = []
    for one_string in list_of_strings:
        lowercase.append(one_string.lower())
    return lowercase


cooper = {
    "name": "Dale Bartholomew Cooper",
    "co-workers": ["Diane", "Sheriff Harry S. Truman"],
    "favorite_drink": "Coffee",
    "quotes": [
        "Damn fine cup of coffee",
        "Diane...",
        "This must be where pies go when they die",
        "That's what you do in a town where a yellow light still means slow down, not go faster.",
        "Every day, once a day, give yourself a present",
        "I have no idea where this will lead us, but I have a definite feeling it will be a place both wonderful and strange.",
    ],
}


def random_quotes():
    return random.choice(cooper["quotes"])


ipdb.set_trace()
