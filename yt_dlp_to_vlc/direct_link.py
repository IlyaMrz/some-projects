import subprocess
from yt_dlp import YoutubeDL
import win32clipboard


def direct_link(format_ID):
    yt_data = YoutubeDL({'format': format_ID})
    link = yt_data.extract_info(URL, download=False)['url']
    print(link)
    #return link

win32clipboard.OpenClipboard()
URL = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()


command_get_formats = f'yt-dlp -F {URL}'
subprocess.call(command_get_formats)

print('Choose a format'.center(70, '_'))
ur_format_ID = input('Enter your format :  ')

while ur_format_ID:
    direct_link(ur_format_ID)
    ur_format_ID = input('Press enter to exit... or format ID to run again:  ')
