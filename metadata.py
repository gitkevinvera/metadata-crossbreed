from pymediainfo import MediaInfo
import ctypes
import subprocess
import json
import os

# Manually specify the path to the libmediainfo library
ctypes.CDLL('/usr/local/lib/libmediainfo.0.dylib')

def extract_metadata(video_path):
    media_info = MediaInfo.parse(video_path)
    metadata = media_info.to_data()
    metadata_json = json.dumps(metadata, indent=4)
    with open('metadata.json', 'w') as f:
        f.write(metadata_json)
    return 'metadata.json'

def assign_metadata(source_metadata_file, target_video_file):
    # Create an FFmpeg command to apply the metadata
    command = [
        'ffmpeg',
        '-i', target_video_file,
        '-i', source_metadata_file,
        '-map_metadata', '1',
        '-codec', 'copy',
        'output_video.mp4'
    ]
    subprocess.run(command)

# Paths to your videos
iphone_video = 'IMG_0355.mov'
downloaded_video = '0517.mp4'

# Extract metadata from iPhone video
metadata_file = extract_metadata(iphone_video)

# Assign metadata to the downloaded video
assign_metadata(metadata_file, downloaded_video)

# Clean up the metadata file
os.remove(metadata_file)
