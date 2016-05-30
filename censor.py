#program to censor repeated word by * 
def censor(text, word):
    result=""
    final=[]
    result=text.split()
    print
    for var in result:
        if var==word:
            var="*"*(len(var))
            final.append(var)
        else:
            final.append(var)
    return " ".join(final)
    
print censor("aakash shah", "shah")