
## Database exercise

* Run the script `create-database.py` (provided to you by the teacher),
  to create the file `cooking.db` in the current directory.

* Create a new file `query-recipes.py`. Have it import `sqlite3`, connect
  to the `cooking.db` database, and then close the connection. Run it to make
  sure it works.

Now add the following statements (between opening the connection and closing
it):

```python
c = conn.cursor()

recipe_tuples = c.execute('SELECT DISTINCT name FROM recipe')
recipes = [t[0] for t in recipe_tuples]
```

* For each recipe, print its name and all its ingredients. The SQL statement
  you'll want for getting the ingredients is `SELECT ingredient FROM recipe
  WHERE name = ?`. (Remember that the name of the recipe needs to be sent in
  a one-element tuple.) Run it and make sure it works.

Now alter the program so that it instead lists the ingredients in each recipe
but not in the pantry. The new SQL statement could look like this:

```sql
SELECT r.ingredient
  FROM recipe AS r
  WHERE r.name = ?
  AND NOT EXISTS
    (SELECT ingredient FROM pantry AS p
      WHERE r.ingredient = p.ingredient)
```

* Run the program and make sure it works.

The output should be something like this:

```
Recipe: pancakes

Recipe: spaghetti carbonara
    pepper
    parmesan
    bacon
    parsley

Recipe: omelet
    pepper
```

Now this is fine, but it doesn't take into account the amounts needed. Change
the query to this:

```sql
SELECT r.ingredient, r.amount_required - IFNULL(p.amount_stocked, 0), r.unit
    FROM recipe AS r LEFT OUTER JOIN pantry AS p ON r.ingredient = p.ingredient
    WHERE r.name = ?
    AND (p.amount_stocked IS NULL
          OR p.amount_stocked < r.amount_required)
```

The result, when you print all the things, should be something like this:

```
Recipe: pancakes
    flour        1.5 dL

Recipe: spaghetti carbonara
    pepper       1.0 teaspoon
    parmesan     2.0 dL
    bacon      250.0 gram
    parsley      1.0 tablespoon

Recipe: omelet
    pepper       1.0 teaspoon
````
