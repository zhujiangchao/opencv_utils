import cv2
import glob
import numpy as np

fps = 6
video_size = (1280, 720)
fourcc = cv2.VideoWriter_fourcc(*"MJPG")
videoWriter = cv2.VideoWriter('video4.avi',fourcc, fps, size)

for img in glob.glob("/home/zuzu/YueLake_16/" + "/*.jpg"):
	read_img = cv2.imread(img)
	read_img = np.rot90(read_img)
	videoWriter.write(read_img)

# for img in glob.glob("/home/zuzu/YueLake_17/" + "/*.jpg"):
# 	read_img = cv2.imread(img)
# 	read_img = np.rot90(read_img)
# 	videoWriter.write(read_img)

# for img in glob.glob("/home/zuzu/YueLake_18/" + "/*.jpg"):
# 	read_img = cv2.imread(img)
# 	read_img = np.rot90(read_img)
# 	videoWriter.write(read_img)

# for img in glob.glob("/home/zuzu/YueLake_19/" + "/*.jpg"):
# 	read_img = cv2.imread(img)
# 	read_img = np.rot90(read_img)
# 	videoWriter.write(read_img)

# for img in glob.glob("/home/zuzu/YueLake_20/" + "/*.jpg"):
# 	read_img = cv2.imread(img)
# 	read_img = np.rot90(read_img)
# 	videoWriter.write(read_img)

videoWriter.release()