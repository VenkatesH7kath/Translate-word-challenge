import csv
import time
import psutil


timeuse=time.process_time()
mem=psutil.Process()

with open('find_words.txt','r')  as f:
    words=f.read().splitlines()
    #read the file

csvans=[]
with open('french_dictionary.csv','r') as f:
    csvread=csv.reader(f)
    for i in csvread:
        csvans.append(i)

dic={}
for i in csvans:
    dic[i[0]]=i[1]

with open('t8.shakespeare.txt','r') as f:
    convert=f.read()
for word in words:
    if word in dic:
        convert=convert.replace(word,dic[word])

with open('t8.shakespeare.translated.txt','w')as f:
    f.write(convert)

with open('frequency.csv','w',newline='')as f:
    csvwrite =csv.writer(f)
    csvwrite.writerow(['English word','French word','Frequency'])
    for key ,value in dic.items():
        csvwrite.writerow([key,value,convert.count(value)])


timeend=time.process_time()
memory=mem.memory_info()
time=("{:.2f}".format(timeend-timeuse))
memo=(memory.rss)//(1024*1024)
times="Time to process: "+str(time)+" sec\n"+"Memory used: "+str(memo)+ "MB"

with open('performance.txt','w')as f:
    f.writelines(times)

