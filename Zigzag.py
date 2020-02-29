import sys
import time


indent = 0
increaingIndent = True

try:
    while True:
        print(' ' * indent, end='')
        print('****')
        time.sleep(0.02)
        if increaingIndent:
            indent += 1
            if indent == 15:
                increaingIndent = False
        else:
            indent -= 1
            if indent == 0:
                increaingIndent = True
except KeyboardInterrupt:
    sys.exit()
