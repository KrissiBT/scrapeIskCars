abc = "abcdefghijklmnopqrstuvwxyz"
char1 = "a"
char2 = "b"
platechars = "something"


for i in range(1, 1000):
    pass

for x in range(0,26):
	char1 = abc[x]
	for b in range(0,26):
		char2 = abc[b]
		platechars = char1 + char2
		for c in range(1,1000):
			print platechars + '{0:0>3}'.format(c)