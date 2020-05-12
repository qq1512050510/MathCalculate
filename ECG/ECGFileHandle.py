# -*- coding: utf-8 -*-
"""
Spyder 编辑器
ECG 文件处理

"""
import numpy as np
import re


##读写文件
def readAndWrite(fileRead, fileWrite):
    try:
        fileR = open(fileRead, 'r')
        fileW = open(fileWrite, 'w')
        print("开始读文件" + fileRead)
        i = 1
        k = 1;
        writeList = []
        for line in fileR.readlines():
            lineList = re.split(" |\x09", line.strip())
            writeList.append(lineList[-2])
            if float(i) % 1250 == 0:
                fileWString = " ".join(str(j) for j in writeList) + "\n"
                print("开始写文件" + str(i) + "-" + str(k) + ":" + fileWrite)
                # print(fileWString)
                fileW.write(fileWString)
                k += 1;
                writeList = []

            i += 1


    except OSError as reason:
        print('出错啦！' + str(reason))
    finally:
        fileR.close()
        fileW.close()


# 打标签
def readAndWriteTag(fileRead):
    dict = {}
    fileR = open(fileRead, 'r')
    for line in fileR.readlines():
        lineList = re.split(" |\x09\(", line.strip())
        tag = "N"
        if lineList[1] == "AFIB":
            tag = "AFIB"
        dict[lineList[0]] = tag
    return dict


# 计算标签，并且写入文件
def calAndWrite(fileRead, fileWrite, dict):
    try:
        fileQrs = open(fileRead, 'r')
        fileWrite = open(fileWrite, 'w')
        i = 1;
        listOnCal = [];
        k = 1;
        countAFIB = 0;
        for line in fileQrs.readlines():
            linec = float(line.strip())
            print(k)
            k += 1
            if linec < i * 5:
                listOnCal.append(str(linec));
            else:
                print(i * 5)
                print(listOnCal)
                ecgLag = classifyECG(listOnCal, dict)
                if ecgLag == "AFIB":
                    countAFIB += 1;
                fileWrite.write(ecgLag + "\n")
                listOnCal = []
                listOnCal.append(str(linec))

                i += 1;
        fileWrite.write(str(countAFIB) + "\n")
    except OSError as reason:
        print('出错啦！' + str(reason))

    finally:
        fileQrs.close()
        fileWrite.close()
    return


def classifyECG(qrsList, dictAtr):
    countN = 0;
    tag = "AFIB"
    for qrs in qrsList:
        dicAtrList = list(dictAtr.keys())
        dicAtrList.reverse()
        for keyFor in dicAtrList:
            if float(qrs) > float(keyFor):
                print(qrs + str(dictAtr))
                if tag == dictAtr.get(keyFor):
                    countN += 1;
                break
        if countN * 2 >= len(qrsList):
            return tag
    return "N"


def main(fileDataFixed, fileAtrFixed, fileQrsFixed):
    readAndWrite(fileDataFixed, fileDataFixed + '-')
    dictR = readAndWriteTag(fileAtrFixed)
    print(dictR.keys())
    print(dictR.values())
    calAndWrite(fileQrsFixed, fileQrsFixed + "-", dictR)


fileNames = ['04015', '04043', '04048', '04126', '04746', '04908', '04936', '05091', '05121', '05261', '06426', '06453',
             '06995', '07162', '07859', '07879', '07910', '08215', '08219', '08378', '08405', '08434', '08455']
fileAtrFixed = "D:\DISK\ECG数据\\04015atr.txt"
fileQrsFixed = "D:\DISK\ECG数据\\04015qrs.txt"
fileNameFixed = "D:\DISK\ECG数据\\04015dat.txt"
file = open("D:\DISK\ECG数据\\04015atr.txt")
fileW = open("D:\DISK\ECG数据\\04015atr-handle.txt", "w")

"""
try:
    f = open('一个不存在的文件.txt','r')
    print(f.read())
except OSError as reason:
    print('出错啦！'+ str(reason))
finally:
    f.close()
"""

for fileName in fileNames:
    print(fileName)
dataMat = []
labelMat = []
for line in file.readlines():
    curLine = line.strip().split(" ")
    # floatLine=map(float,curLine)#这里使用的是map函数直接把数据转化成为float类型
    # dataMat.append(curLine[0:2])
    dataMat.append(curLine[0])
    labelMat.append(curLine[-1])
fileW.write(str(dataMat))
fileW.close()
print('dataMat:', dataMat)
print('labelMat:', labelMat)
print(np.shape(dataMat))

fileNames = ['04015', '04043', '04048', '04126', '04746', '04908', '04936', '05091', '05121', '05261', '06426', '06453',
             '06995', '07162', '07859', '07879', '07910', '08215', '08219', '08378', '08405', '08434', '08455']

"""
for fileName in fileNames:
    fileAtrFixed = "D:\DISK\ECG数据\MIT-BIH-data\\"+fileName+"atr.txt"
    fileQrsFixed = "D:\DISK\ECG数据\MIT-BIH-data\\"+fileName+"qrs.txt"
    fileDatFixed = "D:\DISK\ECG数据\MIT-BIH-data\\"+fileName+"dat.txt"
    main(fileDatFixed,fileAtrFixed,fileQrsFixed)

readAndWrite(fileNameFixed, fileNameFixed + '-')
dictR = readAndWriteTag(fileAtrFixed)
print(dictR.keys())
print(dictR.values())
calAndWrite(fileQrsFixed, fileQrsFixed + "-", dictR)
"""
countA = 0
count = 0
for fileName in fileNames:
    fileQrsFixed = "D:\DISK\ECG数据\数据整理\\" + fileName + "qrs.txt-"
    file = open(fileQrsFixed)
    lineLast = 0;
    countfor = 0;
    for line in file.readlines():
        if len(line.strip()) != 0:
            lineLast = line.strip();
            countfor += 1;
    countfor -= 1;
    print(fileQrsFixed)
    print(lineLast + "----" + str(countfor))
    countA += int(lineLast)
    count += countfor;
print(count)
print(countA)

countTime = 0.0
for fileName in fileNames:
    fileQrsFixed = "D:\DISK\ECG数据\MIT-BIH-data\\" + fileName + "qrs.txt"
    file = open(fileQrsFixed)
    lineLast = 0;
    for line in file.readlines():
        if len(line.strip()) != 0:
            lineLast = line.strip();

    print(fileQrsFixed+"-"+str(lineLast))
    countTime += float(lineLast)
print(countTime)
print(countTime/5)
