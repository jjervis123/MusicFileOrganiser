import os
import shutil

# List of common music file extensions
music_extensions = ['mp3', 'aac', 'ogg', 'wma', 'flac', 'alac', 'm4a', 'ape', 'wav', 'aiff', 'mid', 'midi', 'dsf', 'dff']

directory = "~/Downloads/"
os.chdir(directory)

for file in os.listdir():
  file_extension = file.split('.')[-1].lower()
  if file_extension in music_extensions:
    shutil.move(file, file_extension + "/" + file)

print("Music files have been organized...")
