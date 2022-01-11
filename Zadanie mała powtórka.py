shopping_dict = {
    "piekarnia": ["chleb", "pączek", 'bułki'],
    "warzywniak": ["marchew", "seler", 'rukola']
}

for n, value in enumerate(shopping_dict["piekarnia"]):
    shopping_dict["piekarnia"][n] = value.title()
for n, value in enumerate(shopping_dict["warzywniak"]):
    shopping_dict["warzywniak"][n] = value.title()
for shops in shopping_dict:
    print(shops.capitalize())


print("Lista zakupów")
#Jak tutaj zamieścić "piekarnia" z dużej to potrzebuje jakiejś rady
print(f"Idę do {shops.capitalize()}, kupuję tu następujące rzeczy: {shopping_dict['piekarnia']}")
print(f"Idę do {shops.capitalize()}, kupuje tu następujące rzeczy: {shopping_dict['warzywniak']}")
print(f"W sumie kupuję {len(shopping_dict.get('piekarnia'))+len(shopping_dict.get('warzywniak'))} produktów.")


