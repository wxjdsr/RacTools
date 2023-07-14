import subprocess

input_file = input("Please enter your ts file: ")

if not input_file.endswith(".ts"):
    raise ValueError("[ERROR] the given filename is not a ts file")

output_file = input_file.replace(".ts", ".mp4")

cmd = ["ffmpeg", "-i", f"{input_file}", f"{output_file}"]
try:
    subprocess.check_output(cmd)
except subprocess.CalledProcessError as e:
    print(f'[ERROR] There is error when trying to run the commmand. See stdout for details')
    print(e.stdout)
else:
    subprocess.run(cmd)
    print(f'[INFO] Success: output file: {output_file}')