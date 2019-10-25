import sys

in_str = int(sys.argv[1])

in_list = [' ' for x in range(in_str)]
for i in range(in_str):
	in_list[- (i + 1)] = '#'
	print(''.join(in_list))
