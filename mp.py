#   This file is part of MediaPython.

#   MediaPython is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 2 of the License, or
#   (at your option) any later version.

#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.

#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.

#   MIT License is 2-way compatible with the GPL, all versions.

#!/usr/bin/python3

try:
  from colorama import *
except ImportError:
  print("Missing dependency. Installing...")
  import os
  os.system("python -m pip install colorama")
  print(f"{Fore.GREEN}Finished!{Style.RESET_ALL} Please restart MediaPython to apply these changes.")
  input("Press Enter to exit... ")
  exit()

"""
    userinfo.py
    MediaWiki API Demos
    Demo of `Userinfo` module: Get general user info and user rights
    MIT License
    (c) 2013-2021 MediaWiki.org editors at https://www.mediawiki.org/w/index.php?title=API:Userinfo&action=history
    
    Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software
    without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
    persons to whom the Software is furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
    WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
    
    (This is not the license for MediaPython!)
"""
SITE = input("Please enter the site domain or if your wiki is not ready, your IP: ")
try:
  import requests
except ImportError:
  print("Missing dependency. Installing...")
  import os
  os.system("python -m pip install requests")
  print(f"{Fore.GREEN}Finished!{Style.RESET_ALL} Please restart MediaPython to apply these changes.")
  input("Press Enter to exit... ")
  exit()

S = requests.Session()

URL = "http://" + SITE + "/w/api.php"
you = input(Fore.BLUE + "Please login to " + SITE + " by entering your username: " + Style.RESET_ALL)
print("Checking if you are a Bureaucrat...")
PARAMS = {
    "action": "query",
    "meta": "userinfo",
    "uiprop": "rights",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print("Results:\n" + DATA)
