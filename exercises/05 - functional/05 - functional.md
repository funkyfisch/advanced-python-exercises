## Functional programming exercise

1. Write a function that returns `true` if an input integer is prime.
   Try with list comprehensions and lambdas. Check the `is_prime`
   implementation in the first exercise for some hints.

2. Try to find all the prime numbers between 2 and 10000.
   Time the results. (*Hint*: `import time` and `time.time()`)

3. Now try to rewrite this so that memoization helps.
   Time the results.

4. Create a decorator that measures the time for invoking a function
   and prints it. Refactor your code and use it to measure the time.

If you finish with the above:

### List flattening, map, reduce and comprehensions

A warehousing system (naturally NOT written in python) had a bug in processing
XML messages regarding shipped products.  The shipping notifications were not
processed and the data has been extracted from a series of invoices that must
be handed to operations for adjustment.  Although this only happened with three
invoices this time, you are asked to come up with a way to transform the data
so it can be handled automatically if this repeats.

See the `datatrans.py` file your instructor provides you with.  Your immediate
task is to take the data structure and transform it to a list of dictionaries
mapping from `partnumber` to `qty` like this:

```python
[
  {'E133433': 5, 'P1222': 2, 'C1222333': 4, 'C1222334': 4},
  {'E133433': 7},
  {'E133433': 15, 'E133439': 15, 'P1222': 100}
]
```

The `get_invoices` function returns sample data from parsing the XML files.

**Part 1:**

1. Do this imperatively using loops.
2. Try the same with comprehensions.
3. Try the same with `map` and optionally dictionary comprehensions.

So this works but now you want to create a list instead of tuples representing
(`partnumber`, `qty`).  How easy is this to do with the tools above?

**Part 2:**

How hard is it to create a dictionary merging and summing the affected records up?

1. Do it imperatively using loops. (*Hint:* `defaultdict` can be useful here).
2. Try it using `map`, `filter`, `sum`, and/or comprehensions. (*Hint:* start by
   creating a set of all unique part numbers).
3. Try it using `reduce`.

Which do you prefer in this case?  Why?
