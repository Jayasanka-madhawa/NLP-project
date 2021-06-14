f=open ("LectureNote.txt")
lines = f.read()
Source = lines.split()

Question=input("Question :")
Que=Question.split()


SCE=[]
QUE=[]

for r in range(len(Source)):
    if Source[r][-1]=="." or Source[r][-1]=="," or Source[r][-1]=="?" :
        SCE.append(Source[r][:-1].lower())
    else:
        SCE.append(Source[r].lower())

    
for i in range(len(Que)):
    if Que[i][-1]=="." or Que[i][-1]=="," or Que[i][-1]=="?" :
        QUE.append(Que[i][:-1].lower())
    else:
        QUE.append(Que[i].lower())

a1=["what","when","where","who","whom","whose","why","how","much","which","many"]
b1=["is","am","are","was","were","has","have","had","to","be","will","would","can","could","a","an","of"]
c1=["i","he","she","they","it","them","we","my","me","us","this","that","these","those"]

va=0
n=0

for j in range(len(QUE)):
    if QUE[j] in b1 or QUE[j] in a1 or QUE[j] in c1:
        continue
    else:
        if QUE[j] in SCE:
            a=SCE.count(QUE[j])
            va=va+(0.9)**(1/a)
            print(QUE[j]+" "+str(a))
        else:
            print(QUE[j]+" 0")
        n=n+1

if n==0:
    print(0)
else:
    print(va/n)
