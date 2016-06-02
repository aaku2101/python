""" A program to find percentage using dictionary 
Here, the input should be in a form of 
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Here, 3 is the number of students
The output should be like 56.00
"""
a=int(raw_input())
d={}
for var in range(0,a):
    info=raw_input().split(" ")
    scores=map(float,info[1:])
    d[info[0]]=sum(scores)/float(len(scores))
    
print "%0.2f"% d[raw_input()]