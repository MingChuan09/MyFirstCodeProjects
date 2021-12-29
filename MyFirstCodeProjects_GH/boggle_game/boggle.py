"""
File: boggle.py
Name: 陳名娟 Jenny Chen
----------------------------------------
When user inputs 4*4 letters, the program will find all vocabularies.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

# global variable
dictionary = []


def main():
	"""
	When user inputs 4*4 letters, the program will find all vocabularies.
	"""
	start = time.time()
	####################
	read_dictionary()
	boggle_letter = []    # 將字母盤存成一個list
	count = [0]   # 總共找到的單字數

	for j in range(4):
		letter = input(f'{j+1} row of letters:')
		line_lst = []
		if len(letter) < 4:
			print('Illegal input')
			break
		else:
			for i in range(len(letter)):
				word = letter[i]    # 4*4中每一個字母
				if i % 2 == 0 and word.isalpha():   # 確認有4個字母,且為case-insensitive
					pass
				elif i % 2 == 1 and word.isspace():  # 確認字母間係空白分隔
					pass
				else:
					print('Illegal input')
					break
				letter = letter.lower()
				line_lst = letter.split()  # 將使用者每次輸入的字母刪除空白部分後,存成一個list
		boggle_letter.append(line_lst)  # 再將該list存入4*4的大list
	find_vocabulary(boggle_letter, count, [])
	print('There are ' + str(count[0]) + ' words in total.')

	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_vocabulary(boggle_list, count, ans_lst):
	"""
	:param boggle_list: list, include 4 list at index 0~3
	:param count: list, the index 0 is the number of vocabularies this program found.
	:param ans_lst: lst, the letter this program found.
	"""
	for y in range(len(boggle_list)):
		line = boggle_list[y]
		for x in range(len(line)):
			find_vocabulary_helper(boggle_list, count, ans_lst, x, y, '',  [])


def find_vocabulary_helper(boggle_list, count, ans_list, current_x, current_y, current_s, index_list):
	"""
	:param boggle_list: list, 字母盤, 裡面包含4個list
	:param count: list, the index 0 is the number of the vocabulary
	:param current_x: int, 中心點x
	:param current_y: int, 中心點y
	:param current_s: str, 目前存取到的字母
	:param ans_list: list, 目前確定有在字典且找到的單字
	:param index_list: list, 存著經過的每個座標
	"""
	if len(current_s) >= 4:
		if current_s in dictionary:
			if current_s not in ans_list:
				ans_list.append(current_s)
				count[0] += 1
				print(f'Find: \"{current_s}\"')

	for n in range(-1, 2, 1):       # 直接執行for loop, 使字母數大於4時仍繼續進行
		for m in range(-1, 2, 1):
			around_x = m + current_x
			around_y = n + current_y
			if 0 <= around_x < 4:
				if 0 <= around_y < 4:
					# choose
					if (around_x, around_y) not in index_list:
						current_s += boggle_list[around_y][around_x]
						index_list.append((around_x, around_y))

						# explore
						if has_prefix(current_s):
							find_vocabulary_helper(boggle_list, count, ans_list, around_x, around_y, current_s, index_list)

						# un-choose
						current_s = current_s[0:len(current_s)-1]
						index_list.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		for line in f:
			dictionary.append(line.strip())


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dictionary:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
