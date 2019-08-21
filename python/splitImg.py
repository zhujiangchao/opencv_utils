#!/usr/bin/python
# coding: utf-8

import cv2
import os
import glob

def main(imgPath, split_num):

	total_num = len(glob.glob(imgPath + "/*.jpg"))
	cnt = 0
	for imgName in os.listdir(imgPath):
		img = cv2.imread(imgPath + "/" + imgName)
		fileName = os.path.expanduser('~/' + str(int(cnt/split_num)))
		if not os.path.exists(fileName):
			print(fileName + " does not exist")
			os.mkdir(fileName)
		cv2.imwrite(fileName + "/" + imgName, img)
		cnt = cnt + 1
	print("cnt = ", cnt)


if __name__ == '__main__':
	imgPath = os.path.expanduser("~/data/")
	split_num = 500
	main(imgPath, split_num)