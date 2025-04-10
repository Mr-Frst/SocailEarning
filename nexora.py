#!/usr/bin/env python3

from main import sys, __start__

# Check if '--auth' argument is passed in the command line
if '--auth' in sys.argv:
    print (
      f"\n{('-' * 23)}[\033[91mINFO\033[0m]{('-' * 23)}\n"
       "A window will open shortly, Please log in to your social media account (\033[1mX/Twitter\033[0m) enabling the bot can perform tasks seamlessly\n"
       "You can close the window properly by pressing \033[1mEnter\033[0m after finish logging in to your social media accounts\n"
    )

if __name__ == '__main__':
   __start__()

