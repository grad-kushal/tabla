
prices = {
    "Chilli Chicken": 13.99,
    "Chicken 65 Biryani": 15.99,
    "Chicken Lollipop": 14.99,
    "Chicken Noodles": 13.99,
    "Paneer Biryani": 14.99,
    "Raita": 0.75,
    "Onion Kulcha": 4.99,
    "Kadai Chicken": 14.99,
    "Chilli Garlic Naan": 4.49,
    "Beer": 8.00,
    "Veg Hot and Sour Soup": 4.99,
    "Garlic Naan": 4.49,
    "Goli Soda": 6.00,
    "Diet Coke": 1.99,
    "Limca": 2.99
}


subtotal = 128.38
large_party_fee = 25.68
tax = 10.53
total = 164.59
additional_tip = 6.42


people = ["Kushal", "Aditya", "Tejas", "Vedant", "Geetesh", "Iniya"]


shared_items = ["Chilli Chicken", "Chicken Lollipop"]


orders = {
    "Kushal": ["Paneer Biryani", "Raita", "Kadai Chicken", "Chilli Garlic Naan", "Beer"],
    "Aditya": ["Paneer Biryani", "Raita", "Onion Kulcha", "Kadai Chicken", "Limca"],
    "Tejas": ["Chicken Noodles", "Diet Coke"],
    "Vedant": ["Chicken 65 Biryani", "Raita", "Kadai Chicken", "Beer", "Veg Hot and Sour Soup", "Garlic Naan"],
    "Geetesh": ["Chicken Noodles", "Veg Hot and Sour Soup", "Goli Soda"],
    "Iniya": ["Chicken 65 Biryani", "Raita"]
}

number_of_people_item_split_between = {
    "Paneer Biryani": 2,
    "Raita": 2,
    "Kadai Chicken": 3,
    "Chilli Garlic Naan": 1,
    "Beer": 2,
    "Onion Kulcha": 1,
    "Chicken Noodles": 2,
    "Diet Coke": 1,
    "Chicken 65 Biryani": 2,
    "Veg Hot and Sour Soup": 2,
    "Garlic Naan": 1,
    "Goli Soda": 1,
    "Limca": 1
}

cost_per_person = {person: 0 for person in people}


for person, items in orders.items():
    for item in items:
        # Print item and price
        cost_per_person[person] += prices[item]/number_of_people_item_split_between[item]

# Print cost per person before shared items
print("Cost per person before shared items: " + str(cost_per_person))


shared_cost = sum(prices[item] for item in shared_items) / len(people)

# Print shared cost
print("Shared cost per person: " + str(shared_cost))

for person in people:
    cost_per_person[person] += shared_cost

# Print cost per person after shared items
print("Cost per person after shared items: " + str(cost_per_person))


additional_costs = (large_party_fee + tax + additional_tip) / len(people)

# Print additional costs
print("Additional costs per person: " + str(additional_costs))

for person in people:
    cost_per_person[person] += additional_costs


print("Cost per person after additional costs: " + str(cost_per_person))

# Print the total bill
print(sum(cost_per_person.values()))
