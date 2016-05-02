def Juso():
    word = 'sangmyung university'
    d=dict()
    for c in word:
        if c not in d:
            d[c]=1
        else:
            d[c]=d[c]+1
    
    
    
    %matplotlib inline
    import matplotlib 
    import matplotlib.pyplot as plt
    
    plt.bar(range(len(d)),d.values(),align='center')
    plt.xticks(range(len(d)),list(d.keys()))
    plt.show()
def countDig():
    word = 'sangmyung university,7 hongji,seoul '
    print len(word)
    d=dict()
    d['number']=0
    d['text']=0
    for c in word:
        if c.isdigit():
            d['number']=d['number']+1
        else:
            d['text']=d['text']+1
    
    %matplotlib inline
    import matplotlib 
    import matplotlib.pyplot as plt
    
    plt.bar(range(len(d)),d.values(),align='center')
    plt.xticks(range(len(d)),list(d.keys()))
    plt.show()

def lab8_1():
    Juso()
    counDig()

def main():
    lab8_1()


if __name__=="__main__":
    main()
