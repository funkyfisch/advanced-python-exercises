
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


* You’ve probably seen the [“Mocking SpongeBob” meme](https://i.pinimg.com/736x/09/b0/de/09b0de7f56ed4c33649413851f971e28.jpg): a picture of SpongeBob
SquarePants, with a caption whose text alternates between upper- and lowercase
letters to indicate sarcasm, like this: uSiNg SpOnGeBoB MeMeS dOeS NoT mAkE YoU wItTy.
For some randomness, the text sometimes doesn’t alternate capitalization.
Write a function that will accept a string and will return it edited, in "spongecase".
(*Hint*: You can `import random` and then call `random.randint(1,100)` to get a random
integer between 1 and 100)
