#coding=utf-8
import os
import os.path
import re 
import sys, getopt

"""
将所有的图片文件名写进txt文件里
"""

def img2txt(imgPath):
    for filenames in os.walk(imgPath):
        filenames = list(filenames)
        filenames = filenames[2]
        pattern = r'(?:.*\.jpg|.*\.jpeg)'
        for filename in filenames:
            if re.match(pattern, filename) is not None:
                with open (imgPath + ".txt", 'a') as f:
                    f.write(os.path.abspath(imgPath + '/' + filename)+'\n')


# def xml2txt(xmlPath):
#     for filenames in os.walk(xmlPath):
#         filenames = list(filenames)
#         filenames = filenames[2]
#         pattern = r'(?:.*\.xml)'
#         for filename in filenames:
#             if re.match(pattern, filename) is not None:
#                 with open (xmlPath + ".txt", 'a') as f:
#                     f.write(os.path.abspath(xmlPath + '/' + filename)+'\n')


def main(argv):
    dataset_dir = argv[1]
    # print(os.path.abspath(dataset_dir))
    imgFullPath = os.path.join(os.path.abspath(dataset_dir), 'image')
    for filenames in os.walk(imgFullPath):
        dirs = filenames[1]
        for imgPath in dirs:
            num = int(imgPath[len(imgPath)-1])
            imgPath = os.path.join(imgFullPath, imgPath)
            img2txt(imgPath)
            # xmlPath = os.path.join(os.path.abspath(dataset_dir), 'xml', 'zmart_xml_' + str(num))
            # xml2txt(xmlPath)

if __name__ == '__main__':
    main(sys.argv)