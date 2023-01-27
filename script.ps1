# Declare the path of the folder where the video files are located
$folder_path = ".\"

# Get a list of all video files in the folder and its subfolders
$all_files = Get-ChildItem -Path $folder_path -Recurse -Include *.mp4,*.avi,*.mkv | Select-Object -ExpandProperty FullName

Write-Output $all_files

# Read the list of already played video files from a file
if (Test-Path "played_files.txt") {
    $played_files = Get-Content "played_files.txt"
} else {
    $played_files = @()
}

# Create a list of files that haven't been played yet
$unplayed_files = @()
foreach ($file in $all_files) {
    if ($played_files -notcontains $file) {
        $unplayed_files += $file
    }
}

# If there are no unplayed files, print a message and exit
if ($unplayed_files.Length -eq 0) {
    Write-Output "All files have already been played."
    exit
}

# Pick a random file from the list of unplayed files
$random_num = Get-Random -Minimum 0 -Maximum $unplayed_files.Length
$file_to_play = $unplayed_files[$random_num]

# Play the selected file
Start-Process "C:\Program Files (x86)\K-Lite Codec Pack\MPC-HC64\mpc-hc64.exe" -ArgumentList $file_to_play

# Add the file to the list of played files
Add-Content -Path "played_files.txt" -Value $file_to_play
