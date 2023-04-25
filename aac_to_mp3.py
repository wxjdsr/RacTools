# aac to mp3 file converter

from pydub import AudioSegment
import os

def convert_to_mp3(song_path):
    aac_version = AudioSegment.from_file(song_path, "aac")
    mp3_name = song_path.replace(".aac", ".mp3")

    try:
        aac_version.export(mp3_name, format="mp3") 
    except:
        print(f'Error: Could not convert the file {song_path} to mp3')
    else:
        print(f'Success: Output the file {mp3_name}')


option = int(input("Do you want to convert a single file[1] or a folder[2]?: "))

if option == 1:
    song_path = input("Enter the path of the song: ")
    convert_to_mp3(song_path)
elif option == 2:
    folder_path = input("Enter the path of the folder: ")
    for song in os.listdir(folder_path):
        song_path = os.path.join(folder_path, song)
        convert_to_mp3(song_path)
else:
    print("Invalid option")





