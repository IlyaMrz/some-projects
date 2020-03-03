import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for ch in message.lower():
    count.setdefault(ch, 0)
    count[ch] = count[ch] + 1

pprint.pprint(count)
