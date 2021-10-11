import os
print('Youtube Downloader'.center(40, '_'))
URL = input('Enter youtube url :  ')
id = URL.split('/watch?v=')[1]
# command = f'cmd /k yt-dlp -x -f bestaudio {URL}' # default with youtube_ID a the end
command = f'cmd /k youtube-dl -o "%(title)s.%(ext)s" -x -f bestaudio {URL}'
# print(command)
os.system(f'{command}')

# https://wiki.archlinux.org/index.php/Youtube-dl  docs
# https://github.com/ytdl-org/youtube-dl/blob/master/README.md#readme
# youtube-dl -x --audio-format opus shXAjhcXP58
# command for bat
# python "C:\Games\VScodeProjects\some-projects\youtube_dl_mp3s\main.py"
# cmd /k