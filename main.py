# anagram for words beginning with the letter 'v'

def sortString(aStr,dict):
    list1=list(aStr)
    list1.sort()
    result=""
    listOfWords=dict["v"].split("\n")
    for item in listOfWords:
        list2=list(item)
        list2.sort()
        if(list1==list2):
            result=result+item+" "
    return result

def fillVWords(fname, aDict):
    fs = open(fname,'r')
    for line in fs:
        line=line.lower()
        if(line[0] not in aDict.keys()):
            aDict[line[0]]=line
        else:
            aDict[line[0]]+=line


vWordDict = {}
fillVWords('wordList.txt',vWordDict)


word=input('anagram beginning with v of what word:')
while word != 'quit':
    word = word.lower()
    print (sortString(word,vWordDict))
    word=input('anagram beginning with v of what word:')


