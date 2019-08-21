import xml.etree.ElementTree as ET
import pickle
import os
import sys, getopt
from os import listdir, getcwd
from os.path import join
import re

sets=[]
classes = ["ball"]

def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)


def convert_annotation(kind, num):
    labelPath = "/home/zuzu/labelImg/data/dataset/label/txt_" + kind
    if not os.path.exists(labelPath):
        os.makedirs(labelPath)
    xmlPath = "/home/zuzu/labelImg/data/dataset/xml/zmart_xml_%s/%d.xml"%(kind, num)
    
    out_file = open(os.path.join(labelPath, '%d.txt'%(num)), 'w')
    print("txtPath = ", os.path.join(labelPath, '%d.txt'%(num)))
    if os.path.exists(xmlPath):
        in_file = open(xmlPath)
        tree=ET.parse(in_file)
        root = tree.getroot()
        size = root.find('size')
        w = int(size.find('width').text)
        h = int(size.find('height').text)
        for obj in root.iter('object'):
            difficult = obj.find('difficult').text
            cls = obj.find('name').text
            if cls not in classes or int(difficult)==1:
                continue
            cls_id = classes.index(cls)
            xmlbox = obj.find('bndbox')
            b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
            bb = convert((w,h), b)
            print(str(cls_id) + " " + " ".join([str(a) for a in bb]))
            out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

def main(argv):
    pathName = '/home/zuzu/labelImg/data/dataset/pathName'
    for fileNames in os.walk(pathName):
        fileNames = list(fileNames[2])
        for file in fileNames:
            imgNamePath = os.path.join(pathName, file)
            kind = str(imgNamePath[len(imgNamePath)-5])
            with open(imgNamePath) as f:
                imgList = f.readlines()
                print("kind = %s imgList = %d"%(kind, len(imgList)))
                for num in range(len(imgList)):
                    convert_annotation(kind, num)


if __name__ == '__main__':
    main(sys.argv)