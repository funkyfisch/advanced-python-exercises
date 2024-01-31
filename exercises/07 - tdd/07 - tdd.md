## TDD exercise

Let's implement a data parser, that involves opening a csv file, reading data from it using
regular expressions, and then returning the data in a structured format.

* make file called parse_csv.py
* Make sure that you handle the condition that the file doesn't exist correctly!
* Use the provided open_csv() function to read a csv file's contents
* The main goal is to output the csv entries using a list of dicts in the following format:
  `[{name: "Jane Doe", "age": 33, "email": "janedoe@gmail.com"}]`
* Make a separate file called test_parse_csv.py and import the function(s) that you think
  can be tested.
* If you are having difficulty to easily test how an entry is validated, maybe its time to
  revisit your original code and start refactoring!

Sample csv contents:

```csv
Name, Age, Email
John Doe, 25, john.doe@email.com
Jane Smith, 30, jane.smith@email.com
```

The provided skeleton for you to use:

```python
import re

def open_csv(file_path):
    with open(file_path, 'r') as file:
            csv_contents = file.read()
    return csv_contents

# get contents of a specific file - handle it appropriately
# ...

# make a list of the different lines
# ...

# for each of the lines, separate the columns and assign each value to a
# candidate dict
#...

# within the same iteration, check if each of Name, Age, Email are valid
# you might want to declare a helper function to check for validity
# ...

```
