# This is a WIP script that splits a video into a few segments
import os
import subprocess
import json
import datetime


def sec_to_timeformat(sec: int) -> str:
    '''
    This function returns the @sec in the format XX:XX:XX
    '''
    return str(datetime.timedelta(seconds = sec))


def timeformat_to_sec(timef: str) -> int:
    '''
    This function returns the @timef (XX:XX:XX) into seconds
    '''
    hours, minutes, seconds = map(int, timef.split(":"))
    return hours * 3600 + minutes * 60 + seconds


def get_video_length(file_path: str) -> int:
    '''
    Returns the length of the mp4 file @file_path
    '''
    cmd = [
        'ffprobe',
        '-v', 'error',
        '-show_entries', 'format=duration',
        '-of', 'json',
        file_path
    ]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    data = json.loads(result.stdout)
    return int(data['format']['duration'])


def split_video(file_path: str, total_len: int, n: int) -> None:
    '''
    Split the video @file_path with @total_len into n segments with each the same length
    '''
    # There will be situations which the video cannot be equally divided
    # In this situation, the last video segment contains the extra seconds
    # TODO: There may be another way to do this division perfectly.
    # Check ffmpeg document for more information
    seg_len = total_len / n
    extra_sec = total_len % n

    for i in range(n):
        if i == n - 1:
            # TODO: check the multiple line to see if it passes PEP 8
            # TODO: Add a try-except block and also for else block
            os.system(f"ffmpeg -i {file_path} -ss {i * seg_len} -t \
                 {sec_to_timeformat(total_len)} -c copy {file_path}_{i}.mp4")
        else:
            # TODO: also check here for PEP 8
            os.system(f"ffmpeg -i {file_path} -ss {i * seg_len} -t \
                 {(i + 1) * seg_len} -c copy {file_path}_{i}.mp4")

    # TODO: Put the print into each segment output
    print("[INFO] Success: Output file")


if __name__ == "__main__":
    file_path = input("Please enter your file path: ", end="")
    n = input("How many segments do you want to have? ", end="")
    # TODO: Check if file path exists

    split_video(file_path, get_video_length(file_path), n)