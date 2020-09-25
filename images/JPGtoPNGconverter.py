# Image files should be in a folder with a script or in a folder in descent tree from a script.
# directories of which you givin like an arguments
# You can run a script with "python *script.py 1 2" where 1 nd 2 folders


from sys import argv
import os
from PIL import Image


conv_to = 'png'  # choose a format convert to

dir_path = os.path.dirname(os.path.realpath(__file__)  # settin path to a folder with script)

# Grab first and second arguments
try:
    first=int(argv[1])  # folder name where we should pick up images
    first=f'{dir_path}\\{first}'
    second=int(argv[2])  # folder where we should put converted images
    second=f'{dir_path}\\{second}\\'
except:
    first=dir_path
    second=f'{dir_path}\\new\\'
    print(
        f'No arguments were given. Defaults paths setted from \"{first}\" to \"{second}\" ')

# Check if new\ exist if not create it
if not os.path.isdir(second):
    print('no path folder. lets create then')
    os.mkdir(second)
    print('new path folder created!')

# Loop through images folder and convert to png.
images=[f for f in os.listdir(first) if os.path.splitext(f)[-1] == '.jpg']

for image in images:
    opend=Image.open(image)
    name=os.path.splitext(image)[0]
    opend.save(f'{second}{name}.{conv_to}', conv_to)
    print(
        f'{name}{os.path.splitext(image)[-1]} <<< CONVERTED to \"{conv_to}\" and saved.')


# Save to new folder.
