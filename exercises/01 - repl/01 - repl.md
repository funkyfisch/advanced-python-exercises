## REPL exercise

Run `python3` on the terminal. You should see something like this:

```sh
Python 3.7.5 (default, Nov  1 2019, 02:16:23)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Do the following tasks:

* Make Python print a string containing 100 exclamation marks (`!`). (*Hint*:
  you may be able to multiply the string `'!'` by 100. Try it.)

* Explore the difference between `1 // 3` and `1 / 3` &mdash; what's going on
  there? (If you have a Python 2 interpreter ready, try the same on it.)

* Try `1.2 - 1.0` &mdash; did you expect quite so many nines?

* First write `from math import sqrt` on a line to get access to the `sqrt`
  function which calculates the square root. Next define a small utility
  function: write

  ```python
  def has_divisor(n): return n > 1 and any(n % i == 0 for i in range(2, int(sqrt(n) + 1)))
  ```

  as a single line. (Need to hit Enter twice
  to finish the definition.) Try it out with different values, like this:
  `has_divisor(5)` or `has_divisor(65537)`.

* Define a list of primes:

  ```python
  primes = [p for p in range(2, 100) if not has_divisor(p)]
  ```

  show the result by simply typing `primes` on the next line.

* How many primes between 2 and 100 are there? (*Hint*: The `len` function works on
  lists, like this: `len(some_list)`)

* How many primes are there between 2 and 1000?
