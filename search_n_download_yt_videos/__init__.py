
from pytube import Search
import os


def download(q, number_of_videos, location):
    root_dir = os.getcwd()
    
    location = location.strip()
    if location:
        download_location = os.path.join(root_dir, os.path.split(location)[-1])
    else:
        download_location = root_dir
    s = Search(q)

    count = 0

    while True:
        for video in s.results:
            count += 1
            print(f"[{count}] Downloading '{video.title}'")
            video.streams.filter(progressive=True, file_extension='mp4')\
                .order_by('resolution').desc().first()\
                    .download(output_path=download_location)
            if count == number_of_videos:
                break

        if count == number_of_videos:
            break
        s.get_next_results()


