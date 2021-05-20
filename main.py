
# Rhythm

# -- BASIC INFORMATION -- 
# Author: Sunil Shastry.
# Date: 19 May, 2021.

#  --- BACKGROUND --- 
# Rhythm is an open-source software written in Python 3 programming language. Rhythm is free to download and use for everyone. The main objective of the software is to accurately fetch the lyrics of any and every song available*. However, since the software uses a third-party API (lyrics.ovh), and it is quite frankly impossible to confirm if the API consists of every song you would search, although it most certainly consists. 
# *Every song available on the lyrics.ovh API.

# --- SYNOPSIS ---
# Search for a song performed by any artist and gives access to its lyrics, that is available to view and/or download (.txt).

# -- MORE ABOUT THE AUTHOR ---
# Rhythm is a simple and open-source project designed and built by Sunil Shastry. Sunil is an undergraduate student at the University of Saskatchewan, Canada; majoring in Computer Science. During his first year, he developed the Rhythm application as a "side-project", applying all the knowledge and experience he learnt throughout the academic year. To contact Sunil about the project or for any contact purpose, please view the contact section below.

from util.rhythm import Rhythm
from termcolor import colored
from pyfiglet import figlet_format
import colorama

# Fancy introduction
try:
	colorama.init()
except:
	pass
print()
try:
	rhythm_format = figlet_format("Rhythm")
	rhythm_format = colored(rhythm_format, color="magenta")
except:
	pass
else:
	print(rhythm_format)

print()
try:
	print(colored("WELCOME TO RHYTHM!", color="magenta"))
except:
	print("WELCOME TO RHYTHM!")

print("You're at the right place to search, view and download the lyrics of any song.")
print("Using the lyrics.ovh API, we are able to access the lyrics of thousands of songs!\n")

username = input("To get started, please enter your first name: ")
while True:
	if len(username) == 0:
		username = input("Oops we didn't get that, please try entering your first name: ")
	else:
		break
username = username.capitalize()
print(f"Welcome again {username}, we hope you have a pleasant experience using our application :)")

print()
print("Time to put our money where our mouth is...")

rhythm = Rhythm(username)
