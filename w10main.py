def NewDATA():

  newData=[['english',100],['math',200],['english',200],['math',200],['english',100],['math',300]]
  en=newData[0],newData[2],newData[4]
  ma=newData[1],newData[3],newData[5]
  a=0
  for i in en:
      a=a+i[1]
  
  b=0
  for i in ma:
      b=b+i[1]
  
  engrade = a/len(en)
  magrade = b/len(ma)
  
  print engrade
  print magrade

def ALLDATA():
  allData=[
  ["Coffee","Water","Milk","Icecream"],
    ["Espresso","No","No","No"],
    ["Long Black","Yes","No","No"],
    ["Flat White","No","Yes","No"],
    ["Cappuccino","No","Yes - Frothy","No"],
    ["Affogato","No","No","Yes"]
      ]
  data=allData[1:]
  c=0
  for i in data:
      print i[0],i[2]
      if(i[2]=="No"):
          c=c+1
  a=len(data)
  b=a-c
  print (b*100)/a
  

d=dict()
let=list()
let=(
    "when I find myself in times of trouble mother Mary comes to me speaking words of wisdom let it be and in my hour of darkness she is standing right in front of me speaking words of wisdom let it be let it be let it be whisper words of wisdom let it be and when the broken hearted people living in the world agree  there will be an answer let it be for though they may be parted there is still a chance that they will see there will be an answer let it be let it be let it be there will be an answer let it be and when the night is cloudy there is still a light that shines on me shine on until tomorro let it be"
    )
for i in let.split():
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
