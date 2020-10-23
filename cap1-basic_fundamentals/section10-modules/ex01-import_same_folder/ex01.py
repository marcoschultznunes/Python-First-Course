# We'll import the breaks file

import breaks as br # Importing and using an alias

br.sb()
print('Main Menu')
br.br()
print('Hello')
br.br()

"""
This will make a folder called __pycache__ be created. This folder contains the bytecode
It will make it run a little bit faster

When you're sending your code to other people, the common practice is to delete that folder, 
but it doesn't really matter whether you do or don't. When you're using version control (git), 
this folder is typically listed in the ignore file (.gitignore) and thus not included.
"""