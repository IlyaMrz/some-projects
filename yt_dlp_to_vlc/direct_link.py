import subprocess
from yt_dlp import YoutubeDL
import win32clipboard


VLC_PATH = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"


def direct_link(format_ID):
    yt_data = YoutubeDL({'format': format_ID})
    link = yt_data.extract_info(URL, download=False)['url']
    print(link)
    return link


win32clipboard.OpenClipboard()
URL = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()


command_get_formats = f'yt-dlp -F {URL}'
subprocess.call(command_get_formats)

print('Choose a format'.center(70, '_'))
user_input = input('Enter your format :  ')
ur_format_ID = user_input

while user_input:
    if user_input == ur_format_ID:
        link = direct_link(ur_format_ID)
    user_input = input("""
    Press enter to exit... 
    or format ID to run again:  
    or g / п to run link above in VLC:

    """)
    if user_input == 'g' or user_input == 'п':
        command = f'{VLC_PATH} {link}'
        subprocess.call(command)
    elif user_input:
        ur_format_ID = user_input
