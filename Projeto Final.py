from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
import pywhatkit
import lyricsgenius
from lyricsgenius import Genius
genius = Genius(token)
artist = genius.search_artist("Mariah Rose Faith", max_songs=3, sort="title")
print(artist.songs)