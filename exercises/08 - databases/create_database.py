import sqlite3

recipes = {
    'pancakes': {
        'flour': [3.5, 'dL'],
        'baking powder': [3.5, 'teaspoon'],
        'salt': [1, 'teaspoon'],
        'sugar': [1, 'tablespoon'],
        'milk': [3, 'dL'],
        'eggs': [1, ''],
        'butter': [3, 'tablespoon'],
    },
    'omelet': {
        'eggs': [2, ''],
        'milk': [0.3, 'dL'],
        'butter': [2, 'tablespoon'],
        'salt': [1, 'teaspoon'],
        'pepper': [1, 'teaspoon'],
    },
    'spaghetti carbonara': {
        'bacon': [250, 'gram'],
        'garlic': [1, 'tablespoon'],
        'pepper': [1, 'teaspoon'],
        'spaghetti': [500, 'gram'],
        'eggs': [4, ''],
        'salt': [1, 'tablespoon'],
        'parmesan': [2, 'dL'],
        'parsley': [1, 'tablespoon'],
    },
}

pantry = {
    'flour': [2, 'dL'],
    'baking powder': [40, 'teaspoon'],
    'salt': [250, 'teaspoon'],
    'sugar': [140, 'tablespoon'],
    'milk': [9, 'dL'],
    'eggs': [6, ''],
    'butter': [30, 'tablespoon'],
    'garlic': [4, 'tablespoon'],
    'spaghetti': [1000, 'gram'],
}

conn = sqlite3.connect('cooking.db')

c = conn.cursor()

c.execute('DROP TABLE IF EXISTS recipe')
c.execute('''CREATE TABLE recipe
          (name TEXT, ingredient TEXT, amount_required REAL, unit TEXT)''')

for recipe, ingredients in recipes.items():
    for ingredient in ingredients:
        amount, unit = ingredients[ingredient]
        c.execute('INSERT INTO recipe VALUES (?, ?, ?, ?)',
                    (recipe, ingredient, amount, unit))

c.execute('DROP TABLE IF EXISTS pantry')
c.execute('''CREATE TABLE pantry
          (ingredient TEXT, amount_stocked REAL, unit TEXT)''')

for ingredient in pantry:
    amount, unit = pantry[ingredient]
    c.execute('INSERT INTO pantry VALUES (?, ?, ?)',
                (ingredient, amount, unit))

conn.commit()
conn.close()

print('Database successfully created.')
