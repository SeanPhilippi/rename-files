# for each character in file name, check for [, ], {, }, (, ), ''
# do a regex search for substrings starting and ending with '.' and replace with ''
# if there is substring of 4 digits, and the first 2 aren't 10 (1080), then slice and append to end?
# if a single file in a folder, mv out of folder and delete folder

import os
import re

os.chdir(os.path.expanduser('~'))
dirs = os.listdir('./Downloads')
for filename in dirs:
	print(filename)
	for ch in filename:
		if ch in ['[', ']', '(', ')', '{', '}', "'", '"', '-', ' ', '/', '\\', '_', ',', '*']:
			filename = filename.replace(ch, '.')
	
	print('loop 2:', filename)

	filename = re.sub(r'\.\.+', '.', filename)
	print('newname', filename)

