import re
from collections import Counter  

#
# 关卡2
#   任务1
#       字词统计
#
def wordcount(text):
    # 使用正则表达式去除文本中的所有标点符号，并分割成单词  
    # \W+ 匹配一个或多个非单词字符（包括标点符号和空格）  
    words = re.findall(r'\b[\w|\']+\b', text.lower())  
      
    # 使用Counter对象来统计每个单词的出现次数  
    word_counts = Counter(words)  
    wordList= {}  
    # 打印每个单词及其出现次数  
    for word, count in word_counts.items(): 
        wordList[word] = count
        # print(f"'{word}': {count}")  
    
    print(wordList)
    pass

text = """
Got this panda plush toy for my daughter's birthday,
who loves it and takes it everywhere. It's soft and
super cute, and its face has a friendly look. It's
a bit small for what I paid though. I think there
might be other options that are bigger for the
same price. It arrived a day earlier than expected,
so I got to play with it myself before I gave it
to her.
"""

# 调用函数并打印结果  
wordcount(text)