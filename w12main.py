import os 
mydir=os.getcwd()
def file1():
    filename='python.txt'
    myfilename=os.path.join(mydir,filename)
    try:
        myfile=open(myfilename, 'r')
        for line in myfile:
            if line.find('Python')>=0:
                print line
        myfile.close()
    except IOError as e:
        print e          

import os
mydir=os.getcwd()
def file2():
    filename='output.txt'
    myfilename=os.path.join(mydir,filename)
    myfile=open('output.txt', 'w')
    line1='first line\n'
    myfile.write(line1)
    line2='\tsecond line\n'
    myfile.write(line2)
    line3='third line'
    myfile.write(line3)
    myfile.close()
    myfile2=open(myfilename,'r')
    for line in myfile2:
        if line.find('line')>=0:
            print 'line'.upper()    
def lab12():
       file1()      
       file2()
def main():
       lab12() 
       input()

if __name__=="__main__":
    main()
