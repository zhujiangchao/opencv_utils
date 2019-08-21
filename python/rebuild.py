#coding=utf-8
import os
import glob
import re
import shutil
import cv2

def main():
	cnt = 0
	imgDirs = "/home/zuzu/labelImg/data/dataset/image/"
	outImgDirs = "/home/zuzu/yolo/image/"
	txtDirs = "/home/zuzu/labelImg/data/dataset/label/"
	outLabelDirs = "/home/zuzu/yolo/labels/"

	if not os.path.exists(outImgDirs):
		os.makedirs(outImgDirs)
	if not os.path.exists(outLabelDirs):
		os.makedirs(outLabelDirs)

	for file in glob.glob(imgDirs + "*/*.jpg"):
		# read the pict and rename it, then save it to a new dir
		# img = cv2.imread(file)
		kind = re.findall(r'\d+/', file)
		num = re.findall(r'\d+\.', file)
		kind = kind[0][0:len(kind[0])-1]
		num = num[0][0:len(num[0])-1]
		srcTxtName = os.path.join(txtDirs, "txt_%s"%kind, "%s.txt"%num)
		dstTxtName = os.path.join(outLabelDirs, "%d.txt"%cnt)
		dstImgName = os.path.join(outImgDirs, "%d.jpg"%cnt)
		# cv2.imwrite(outImgDirs + "%d.jpg"%cnt, img)
		shutil.copyfile(file, dstImgName)
		shutil.copyfile(srcTxtName, dstTxtName)
		cnt = cnt + 1
	print(cnt)
	# for top, dirs, files in os.walk(imgDirs):
	# 	for Dir in dirs:
	# 		fullDir = os.path.join(imgDirs, Dir)
	# 		for top, dirs, files in os.walk(fullDir):
if __name__ == '__main__':
	main()