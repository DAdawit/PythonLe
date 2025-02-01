from optparse import Values


products = {
    'apple': 1.5,
    'banana': 0.5,
    'cherry': 2.0,
    'date': 3.0
}

# Create a new dictionary for products priced above 1.0
expensive_products = {product: price for product, price in products.items() if price > 1.0}

print(expensive_products)

chip_products = {product: price for product, price in products.items() if price < 1}
print(chip_products)




students_scores = {
    'Alice': {'math': 100, 'science': 90, 'english': 100},
    'Bob': {'math': 70, 'science': 82, 'english': 88},
    'Charlie': {'math': 95, 'science': 92, 'english': 91},
    'Diana': {'math': 60, 'science': 75, 'english': 80},
    'Ethan': {'math': 88, 'science': 85, 'english': 90}
}


average_scores = {name: (lambda scores: sum(scores.values()) / len(scores))(scores) for name, scores in students_scores.items()}

average_scores = {name: (lambda scores: sum(scores.values()) / len(scores))(scors) for name, scors in students_scores.items()}


highScors ={name: score for name, score in average_scores.items() if score > 80}

from functools import reduce
items = [1,2,3,4,5]


total = reduce(lambda x,y:x+y,items)

# start with
total = reduce(lambda x,y:x+y,items,2)
total = reduce(lambda x,y:x+y,items,2)

print(total)
print(sum(items))


lambda accu, curr: acc + len(curr)

names =['alicwe', 'bob', 'charlie', 'diana', 'ethan']
char_count = reduce(lambda accu, curr: accu +len(curr), names, 0)

print(char_count)
