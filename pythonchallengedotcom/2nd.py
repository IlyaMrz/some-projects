message = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."


# First method
dic = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6, 'i': 9, 'h': 8, 'k': 11, 'j': 10, 'm': 13, 'l': 12,
       'o': 15, 'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21, 't': 20, 'w': 23, 'v': 22, 'y': 25, 'x': 24, 'z': 26}
recovered = []

for item in message:
    if item in dic.keys():
        x = int(dic[item])+2
        if x > 26:
            x = x - 26
        y = [letter for letter, val in dic.items() if val == x]
        recovered.append(y)
    else:
        recovered.append(item)
print('First Method:')
for i in recovered:
    print(*i, end='')
print('')

# 2nd Method
into = "abcdefghijklmnopqrstuvwxyz"
out = 'cdefghijklmnopqrstuvwxyzab'

trantab = str.maketrans(into, out)
print('2nd Method:')
print(message.translate(trantab))


# A way to the next page
message = 'map'
url_piece = message.translate(trantab)

print('Searching for a new url:')
print(f'Our url -> pythonchallenge.com/pc/def/{url_piece}.html')
