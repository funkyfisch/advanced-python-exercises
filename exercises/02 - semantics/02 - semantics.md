
## Syntax and semantics exercise

In this exercise, it is recommended that you create a file `semantics.py`
somewhere, and run Python on that file, for example by typing `python3
semantics.py` in the terminal.

A *hailstone sequence* works like this. Start with a number `n`. The next
number in the sequence is calculated like this:

* If `n` is even, the next number is `n // 2`.
* If `n` is odd, the next number is `3 * n + 1`.

This process is repeated, generating new numbers from each last one, until
finally the sequence stops at 1.

For example, if we start at 10, then the next number (by the above rule) is
5, the next after that is 16, then 8, then 4, 2, and finally 1.

(No-one knows if it always stops at 1, but people have been trying really big
numbers, and the sequence has always stopped at 1 so far.)

* Write a `hailstone` function with a parameter `n` that does this. (*Hint*:
  you'll need a list in a variable, a `while` loop, an `if` statement, and the
  `.append` method which adds an element at the end of a list.)
* Try it on a few numbers. Suggestions: 3, 19, 27.
* Create a dictionary that maps each of the numbers `n` (between 1 and 50, say)
  to the length of the `hailstone(n)` sequence.
* What `n` below a million (1 000 000) has the longest hailstone sequence?
* Look back at your `hailstone` function. Is there anything you could have
  written in a different way, while still having the function work? Try it
  that way instead. Consider pros and cons of either way of writing the
  function.
