#!/usr/bin/python
# coding: utf-8

import cv2
import os
import glob

def main(imgPath):
	cnt = 0
	for imgName in os.listdir(imgPath):
		img = cv2.imread(imgPath + "/" + imgName)
		fileName = os.path.expanduser('~/' + 'zmart_new_4')
		if not os.path.exists(fileName):
			print(fileName + " does not exist")
			os.mkdir(fileName)
		cv2.imwrite(fileName + "/" + str(cnt) + '.jpg', img)
		cnt = cnt + 1
	print("cnt = ", cnt)


if __name__ == '__main__':
	imgPath = os.path.expanduser("~/zmart_4/")
	main(imgPath)