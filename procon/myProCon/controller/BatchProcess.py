# -*- coding:utf-8 -*-
# @Time: 2021/4/12 8:53 PM 
# @Author: Edgar Qian
# @Email: qianneng_se@163.com
# @File: BatchProcess.py

from myProCon.service import TripletFinder, MutualInformation, ProbabilityCalculator
import os
import math


filePath = 'D:/Downloads/BlastFileFasta/'
fileList = os.listdir(filePath)
outFilePath1 = 'D:/Downloads/Results/PyCheSimilarity/'
outFilePath2 = 'D:/Downloads/Results/Covariant/'

resultlista = []
resultlistb = []
flag = 1
seq_gap = 0
seq_ave_gap = 0
for fileName in fileList:
    tempName = fileName.split('.')
    try:
        print("-------- Processing of the file: {} --------".format(filePath + fileName))
        flag += 1
        a = ProbabilityCalculator.ProbabilityCalculator(filePath + fileName)
        seq_gap = a.get_min_gap()
        seq_ave_gap = a.get_ave_gap()
        b = MutualInformation.MutualInformation(a)
        b.mut_inf_to_file(outFilePath1 + tempName[0] + '.pcs')
        c = TripletFinder.TripletFinder(b)
        c.tps_to_file(outFilePath2 + tempName[0] + '.tri')
    except ZeroDivisionError as e:
        print("Gap percent error. Current gap percent setting is {}, "
              "but the minimum value of the sequence is {} "
              "and the average value is {}".format(0.1, seq_gap, seq_ave_gap))
        new_seq_gap = math.ceil(seq_gap * 10) / 10
        print("Attention!!! Automatically set the gap percent to {}".format(new_seq_gap))
        a = ProbabilityCalculator.ProbabilityCalculator(filePath + fileName, new_seq_gap)
        seq_gap = a.get_min_gap()
        b = MutualInformation.MutualInformation(a)
        b.mut_inf_to_file(outFilePath1 + tempName[0] + '.pcs')
        c = TripletFinder.TripletFinder(b)
        c.tps_to_file(outFilePath2 + tempName[0] + '.tri')