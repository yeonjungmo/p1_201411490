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
  

def Beatles():
    d=dict()
    beatles= list()
    most=set()
    beatles=("When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness She is standing right in front of me peaking words of wisdom let it be Let it be let it be let it be let it be hisper words of wisdom let it be nd when the broken-hearted people Living in the world agree There will be an answer let it be For though they may be parted There is still a chance that they will see There will be an answer let it be Let it be let it be Let it be let it be Yeah there will be an answer let it be Let it be let it be Let it be let it be Whisper words of wisdom let it be Let it be let it be Ah let it be yeah let it be Whisper words of wisdom let it be And when the night is cloudy There is still a light that shines on me Shine on until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be Let it be yeah let it be Oh there will be an answer let it be Let it be let it be Let it be yeah let it be Whisper words of wisdom let it be")

    for i in beatles.split():
        if i not in d:
            d[i]=1
        else:
            d[i]  = d[i]+1
    print "The most words are:"

    for i in d:
        if d[i]>20:
            print i
            
  def lab10():
    NewDATA()
    ALLDATA()
    Beatles()
    
def main():
    lab10()
if __name__=="__main__":
    main()
