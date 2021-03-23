import os
print('Youtube Downloader'.center(40, '_'))
URL = input('Enter youtube url :  ')
id = URL.split('/watch?v=')[1]
command = f'cmd /k youtube-dl -x --audio-format opus {id}'
print(command)
os.system(f'{command}')

# youtube-dl -x --audio-format opus shXAjhcXP58
# command for bat
# python "C:\Games\VScodeProjects\some-projects\youtube_dl_mp3s\main.py"
# cmd /k