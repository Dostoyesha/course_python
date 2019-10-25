def to_string(*args):
	# return [str(x) for x in [*args]]
	return list(map(str, [*args]))


li = [1, 2, 4]
print(to_string(*li))