import random
import subprocess
import glob


# Declare the path of the folder where the video files are located
folder_path = ".\\mov"
# Declare the path of MPC-HC
player_path = "C:\\Program Files (x86)\\K-Lite Codec Pack\\MPC-HC64\\mpc-hc64.exe"
# Declare playable file formats
file_formats = ['mp4', 'mkv', 'avi']


# Get a list of all video files in the folder
all_files = list()
for file_format in file_formats:
    all_files.extend(glob.glob(folder_path + '/**/*.' + file_format, recursive=True))


# Read the list of already played video files from a file
try:
    with open("played_files.txt", "r") as f:
        played_files = f.read().splitlines()
except FileNotFoundError:
    played_files = []


# Create a list of files that haven't been played yet
unplayed_files = list(set(all_files) - set(played_files))


# If there are no unplayed files, print a message and exit
if not unplayed_files:
    print("All files have already been played.")
    exit()


# Pick a random file from the list of unplayed files
file_to_play = random.choice(unplayed_files)


# Play the selected file
print(player_path)
subprocess.Popen([player_path, file_to_play, "/play", "/fullscreen"])


# Add the file to the list of played files
played_files.append(file_to_play)


# Write the updated list of played files to the file
with open("played_files.txt", "w") as f:
    for file in played_files:
        f.write(file + "\n")
