# for each character in file name, check for [, ], {, }, (, ), ''
# if it's a .part file, leave it out of dirs
# do a regex search for substrings starting and ending with '.' and replace with ''
# if there is substring of 4 digits, and the first 2 aren't 10 (1080), then slice and append to end?
# if a single file in a folder, mv out of folder and delete folder

import os
import re

os.chdir(os.path.expanduser('~/Downloads'))
dirs = os.listdir('.')
# remove files with .part

for filename in dirs:
	if '.part' not in filename:
		print(filename)
		new_name = filename
		for ch in new_name:
			if ch in ['[', ']', '(', ')', '{', '}', "'", '"', '-', ' ', '/', '\\', '_', ',', '*']:
				new_name = new_name.replace(ch, '.')
		new_name = re.sub(r'\.\.+', '.', new_name)
		if new_name[len(new_name) - 1] == '.':
			new_name = new_name[:-1]
		print('new_name', new_name)
		os.rename(filename, new_name)
		print(f'{filename} successfully renamed to {new_name}')
