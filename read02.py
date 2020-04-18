# read02.py 留言記錄檔分析 
import time


# 讀取檔案並寫入list
def read_file(filename):
	data = [] #存放每筆留言的list
	with open(filename, 'r') as f :
		for line in f :
			data.append(line)
	return data

# 計算單字出現次數
def cal_word(data):
	dic_word = {} # dictionary紀錄 "單字:出現次數"
	for review in data:
		words = review.split(' ') # 若split()留空白，則預設會以空白來分割，且連續空白時會跳過
		for word in words:
			if word in dic_word:
				dic_word[word] += 1
			else:
				dic_word[word] = 1
	return dic_word

#主程式
def main():
	data       = read_file('reviews.txt')
	start_time = time.time() 
	dic_word   = cal_word(data)
	end_time   = time.time()
	print('執行計算各個單字出現次數，所花費的時間: ', end_time - start_time, '秒')
	print('留言總筆數: ', len(data))
	print('字典內單字總數: ', len(dic_word))

	# 印出指定次數的單字
	for word in dic_word:
		if dic_word[word] > 1000000:
			print(word, '出現次數: ', dic_word[word])
	# 使用者互動		
	while True:
		search = input('請輸入要查詢的單字: ')
		if search == 'q':
			break
		if search in dic_word:
			print(search, '出現次數: ', dic_word[search])
		else:
			print('This word not exist in the dictionary.')		
	print('Thank you for using this searching program!! Bye~')

# 執行
main()	