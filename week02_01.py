import os
import tempfile
import argparse
import json

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


def get_data_from_storage():
	if not os.path.exists(storage_path):
		return {}
	with open(storage_path, 'r') as r_file:
		js_data = r_file.read()
		if js_data:
			return json.loads(js_data)
		return {}


def append_new_value(key, value):
	data = get_data_from_storage()
	if key in data:
		data[key].append(value)
	else:
		data[key] = [value]
	with open(storage_path, 'w') as wr_file:
		wr_file.write(json.dumps(data))


def get_value(key):
	data = get_data_from_storage()
	if data.get(key):
		return ', '.join(data.get(key))
	else:
		return None


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('--key')
	parser.add_argument('--val')
	args = parser.parse_args()

	if args.key and args.val:
		append_new_value(args.key, args.val)
	else:
		print(get_value(args.key))
