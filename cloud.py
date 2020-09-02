# importing collecions for word iterable count
import collections

#open Tale of Two Cities file
file=open('98-0.txt',encoding="utf8")
#file=('this is. goint to. be, some? thest! that, "i have" and! I might, need.')

#removing stopwords from file
stopWords=set(line.strip() for line in open('stopwords'))

#data structure
wordCount={}

#itrate through file and add to dict if word does not exist
for word in file.read().lower().split():
    word=word.replace('.','')
    word=word.replace(',','')
    word=word.replace('\\','')
    word=word.replace('"','')
    if word not in stopWords:
        if word not in wordCount:
            wordCount[word]=1
        else:
            wordCount[word]+=1

#sorting and returing word cloud            
word_cloud=collections.Counter(wordCount)

#printing most common
for word, count in word_cloud.most_common(10):
    print(word, ": ", count)
    
#for CMD display review
input()