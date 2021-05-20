
# -- BASIC INFORMATION -- 
# Author: Sunil Shastry.
# Date: 19 May, 2021.

# A separate file called "rhythm.py" that performs the simultaneous task of retrieving, validating, displaying and/or downloading the lyrics of a song.

import requests
import os

class Rhythm:
	# URL Format: https://api.lyrics.ovh/v1/artist/title
	_URL = "https://api.lyrics.ovh/v1"
	def __init__(self, name="Rick Astley"):
		self.name = name
		self.main()



	def take_input(self):
		"""Acquires user input and validates the provided inputs."""
		song_name = input("Type out the name of the song you wish to see: ")
		artist_name = input("...and the artist who perfomed it: ")
		song_name = (song_name.lower()).strip()
		artist_name = (artist_name.lower()).strip()
		while True:
			if len(song_name) == 0:
				song_name = input("Perhaps you missed the song name? Try again: ")
			elif len(artist_name) == 0:
				artist_name = input("Oh, no name for the artist? We definitely need one: ")
			else:
				break
		print("\nThe application is currently searching for the song, this might take a while...")
		return artist_name, song_name



	def get_lyrics(self):
		"""Uses the 'requests' library to fetch data from lyrics.ovh public API."""
		user_inputs = self.take_input()
		artist = user_inputs[0]
		song = user_inputs[1]
		response = requests.get(f"{self._URL}/{artist}/{song}")
		status = response.status_code

		while True:
			if status == 200:
				print("\nSong successfully found!\n".upper())
				break
			elif status >= 400:
				print("We were unable to search that song, perhaps you'd like to try again?")
				user_inputs = self.take_input()
				artist = user_inputs[0]
				song = user_inputs[1]
		self.SONG_NAME = song.capitalize()
		self.ARTIST_NAME = artist.capitalize()
		return response.json()



	def _build_directory(self, folder_name="downloads"):
		"""PRIVATE::Creates a new folder where the songs are stored; (folder_name: str)"""
		dir_exists = os.path.exists(folder_name)
		is_dir = os.path.isdir(folder_name)
		if dir_exists == True and is_dir == True:
			pass
		else:
			os.mkdir(folder_name)
	
		

	def display_options(self):
		print("To view lyrics: enter 'view' ")
		print("To download in .txt format: enter 'text'")
		choice = input("Enter your choice: ")
		choice = choice.lower()
		while True:
			if (choice == "view") or (choice == "text"):
				break
			else:
				choice = input("Please enter a valid choice: ")
				choice = choice.lower()
		return choice



	def _view_option(self, data):
		"""PRIVATE::Prints the song lyrics; (data: list)"""
		print(data)
		print(" *** END OF SONG *** ")



	def _text_option(self, filename, data, location="downloads"):
		"""PRIVATE::Builds a new text file containg song lyrics; (filename: str, data: list, location: str)"""
		brand_string = f"*****\nRhythm By Sunil Shastry.\nSong: '{self.SONG_NAME}' by '{self.ARTIST_NAME}'.\n\nTo learn more about Rhythm, please visit the GitHub site at https://github.com/sunillshastry/rhythm.\nTo contact Sunil Shastry, please view at the README file present in the GitHub repository.\nThank you for using Rhythm, and we hope to see you again.\n*****\n\n"

		textfile = open(f"{location}/{filename}.txt", mode="a")
		textfile.write(brand_string)

		for item in data:
			try:
				textfile.write(item + "\n")
			except UnicodeEncodeError:
				continue
			except:
				continue
		textfile.close()
		print("\nSong saved successfully!\n")



	def main(self):
		"""The 'daddy' of all the functions, performs every task from start-to-finish."""
		songlyrics = self.get_lyrics()
		userchoice = self.display_options()

		lyrics = songlyrics["lyrics"]
		if userchoice == "view":
			print()
			self._view_option(lyrics)

		elif userchoice == "text":
			file_name = input("Enter the file name you want to save (without .txt extension): ")
			while True:
				if len(file_name) > 1:
					break
				else:
					file_name = input("Please enter a valid name without any extension: ")

			lyricslist = lyrics.strip().split("\n")
			self._build_directory()
			self._text_option(file_name, lyricslist)

		else:
			# PREPARED FOR THE MOST IMPOSSIBLE CASE!!!
			print("Not quite sure how that happened...")

		# Ask if the user wishes to use the application all over again:
		another = input(f"\nDo you wish to search another song? (y/n): ")
		another = another.lower()
		while True:
			if another == "y" or another == "n":
				break
			else:
				another = input(f"Please enter a valid choice (y/n): ")
				another = another.lower()
		if another == "y":
			self.main()
		else:
			print()
			print(f"Thank you for using the application, {(self.name).capitalize()}! We hope you had a good time using it")

