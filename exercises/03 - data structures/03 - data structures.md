
## Data structures exercise

* So, you can get the reverse of a string `s` in Python by doing `s[::-1]`. Try
  storing some text in a variable `s`, and checking whether it's a palindrome by
  doing `s == s[::-1]`.

* We use `==` here to test for string equality. Would `is` (reference equality)
  work just as well? Try it. Would you expect reference equality to be a good
  idea in that case? (*Hint*: two strings can be equal but have different
  references.)

* Put the palindrome-detecting behavior into a function `is_palindrome`. Make sure
  that it works. (*Hint*: you're on the right track if you're using one parameter,
  the comparison above, and a `return` statement.)

* Write a function `invert` that accepts a dictionary and returns another one
  with keys and values interchanged. (You can assume that the values are
  hashable and unique.)

Let's talk about graphs. A **graph** is a bunch of nodes, each with arrows
pointing to the node's neighbors. Here, let's define four nodes. We might as
well use simple dictionaries with an `id` key and a `neighbors` key.

### Part 1:  Basic theory:

    >>> n1 = { 'id': '[1]', 'neighbors': [] }
    >>> n2 = { 'id': '[2]', 'neighbors': [] }
    >>> n3 = { 'id': '[3]', 'neighbors': [] }
    >>> n4 = { 'id': '[4]', 'neighbors': [] }

And let's connect them up like this:

    >>> n1['neighbors'].append(n2)
    >>> n2['neighbors'].append(n3)
    >>> n2['neighbors'].append(n4)

* Write a function `dfs` (for "depth-first search") that starts from a given
  node, and traverses all neighbor nodes it finds by calling itself
  recursively. (*Hint*: you'll need a for loop with a recursive call in it.
  Not much more.)

With debug statements at the start and end of the function, a call should look
something like this:

```python
>>> dfs(n1, '[4]')
Entering node [1]
Entering node [2]
Entering node [3]
Leaving node [3]
Entering node [4]
Found path [1], [2], [4]
```

Note that such a `dfs` search might freak out if it ever encountered a cycle in
the graph. It would just try calling itself on a cycle of the same node until it
ran out of call stack.

```python
n4['neighbors'].append(n1)  # a cycle! (n1->n2->n4->n1)
n3['neighbors'].append(n2)  # oh man... (n2->n3->n2)
```

Try it.

```python
>>> dfs(n1, '[4]')
[many lines of stacktrace omitted]
RecursionError: maximum recursion depth exceeded while calling a Python object
```

### Part 2:  More Practical Exercises

Take the `graph.py` file provided by your instructor for a basic map of
air routes between airports.  Write a dfs function to search from one airport
(by node) to another airport (by airport code).  can you find a path from cgk
to jfk?  From cph to tpe?

* Write a function `bfs` ("breadth-first search") that keeps track of `seen`
  nodes and `visited` nodes. (These variables could be either lists or dicts,
  it's up to you.) Start with only the start node in `seen` and no nodes in
  `visited`. With each iteration, pick a node in `seen` but not in `visited`, and
  do the following:
    * Mark the current node as `visited`.
    * Mark the current node's neighbors as `seen`.

And it should keep going until all `seen` nodes are also `visited`.

* Run it on the airport graph.
* Which function do you prefer? Why?
