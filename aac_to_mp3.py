# This file is adapted based on chatGPT
# The basic function written by chatGPT is convert_to_song(),
# and the rest is refactored and extended
from pydub import AudioSegment
import os


def convert_to_mp3():
    choice = input("Enter '1' to convert a song or '2' to convert a folder: ")

    if choice == "1":
        song_path = input("Enter the path of the song: ")
        convert_song(song_path)
    elif choice == "2":
        folder_path = input("Enter the path of the folder containing songs: ")
        convert_songs_in_folder(folder_path)
    else:
        print("[ERROR] Invalid choice. Please enter '1' or '2'.")


def convert_song(song_path):
    if not os.path.isfile(song_path):
        print(f'[ERROR] Invalid file path: {song_path}')
        return

    file_extension = os.path.splitext(song_path)[1].lower()

    if file_extension == ".aac":
        aac_version = AudioSegment.from_file(song_path, "aac")
        mp3_name = song_path.replace(".aac", ".mp3")

        try:
            aac_version.export(mp3_name, format="mp3")
        except:
            print(f'[ERROR] Could not convert the file {song_path} to MP3')
        else:
            print(f'[INFO] Success: Output file: {mp3_name}')

        try:
            os.remove(song_path)
        except:
            print(f'[ERROR] failed to delete {song_path}')
        else:
            print(f'[INFO] Success: Delete file: {song_path}')

    else:
        print(f'[ERROR] Invalid file format. Only AAC files are supported.')


def convert_songs_in_folder(folder_path):
    if not os.path.isdir(folder_path):
        print(f'[ERROR] Invalid folder path: {folder_path}')
        return

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            song_path = os.path.join(root, file)
            convert_song(song_path)


convert_to_mp3()
