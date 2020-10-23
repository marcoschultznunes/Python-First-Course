"""
To import from other folders, python uses a package system, in which you add a file called
__init__.py to the folder, marking it as a package.

We can import it freely if it is in the folder. But if it is in another folder, things get 
really stupid. Apparently this is done by setting up the system path. I'll leave this to be 
learned in practice when the frameworks arrive

https://stackoverflow.com/questions/49039436/how-to-import-a-module-from-a-different-folder
https://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time
"""

from utils import users

print(users.u1)
print(users.u2)