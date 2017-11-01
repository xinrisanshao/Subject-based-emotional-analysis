#encoding=utf-8
import jieba
import jieba.analyse
import jieba.posseg as pseg
import csv

TrainingDataSetPath = "E:\PycharmProjects\PythonProject\SubjectBasedEmotionalAnalysis\CCFCompetition\Data\TrainingData\TrainingDataSet.csv"
csv_reader = csv.reader(open(TrainingDataSetPath, encoding='gb18030'))

out = open("nullTest.csv", 'w', newline='',encoding='gb18030')
csv_writer = csv.writer(out, dialect='excel')

count = 1
for row in csv_reader:
    if(row[3]==""):
        print(row)
        csv_writer.writerow(row)
        print(count)
        count+=1
out.close()
