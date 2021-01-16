# for each character in file name, check for [, ], {, }, (, ), ''
# if there is substring of 4 digits, and the first 2 aren't 10 (1080), then slice and append to end?
# if a single file in a folder, mv out of folder and delete folder

import os

os.chdir(os.path.expanduser('~'))
dirs = os.listdir('./Downloads')
for filename in dirs:
	print(filename)
	for ch in filename:
		if ch in ['[', ']', '(', ')', '{', '}', "'", '"', '-', ' ', '/', '\\', '_', ',', '*']:
			filename = filename.replace(ch, '.')
	
	print('loop 2:', filename)
	filename_list = list(filename)
	for i, ch in enumerate(filename_list):
		length = len(filename)
		if ch == '.' and i + 1 < length and filename_list[i + 1] == '.':
			print('filename_list[i - 1], i - 1', filename_list[i - 1], i - 1)
			print('ch, i', ch, i)
			print('filename_list[i + 1], i + 1', filename_list[i + 1], i + 1)
			filename_list[i + 1] = ''
			length -= 1
			if i - 1 >= 0 and filename_list[i - 1] == '' or filename_list[i + 1] == '.':
				print('i - 1', i - 1)
				print('filename_list[i]', filename_list[i])
				filename_list[i] = ''
				length -= 1
	filename = ''.join(filename_list)
	print('newname', filename)

