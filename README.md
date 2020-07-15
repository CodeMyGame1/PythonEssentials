# PythonEssentials
This repository contains python modules that are very useful for coding.

# Available Variables
- alphabet_lowercase
- alphabet_uppercase
- alphabet_lowercase_list
- alphabet_uppercase_list
- testphrase

# Available Functions
- checkAlphabet()
- getNumbers(start, stop, jump, listorstr, strornum=False, space=False)
    - start is the start for the loop (if not mentioned, 0 will be used as default)
    - stop is the end of the loop **(mandatory)**
    - jump is the number to jump (i.e. if the start was 1 and the stop was 10, setting the jump to 2 will return a string `"13579"` and a list `[1,3,5,7,9]`, printing every other number.)
    - listorstr **(mandatory)**
        - True means the result will be a list
        - False means the result will be a str
    - strornum (mandatory if listorstr is True)
        - True means the list items will be strings
        - False means the list items will be integers
    - space (mandatory if list or str is False)
        - True means there will be a space between the numbers
        - False means there will be no space between the numbers
- getNumbers2(start, stop, jump, options):
    - Same as getNumbers(), except that the last three parameters have been consolidated into a list, where the first item is listorstr, the second item is strornum, and the third item is space