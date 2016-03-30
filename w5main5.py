In [1]: def TestMarks(marks):
   ...:     if(90<=marks<=100):
   ...:         grade='A'
   ...:     elif(80<=marks<90):
   ...:         grade='B'
   ...:     elif(70<=marks<80):
   ...:         grade='C'
   ...:     elif(60<=marks<70):
   ...:         grade='D'
   ...:     elif(marks<60):
   ...:         grade='F'
   ...:     return grade
   ...:



In [2]: def jungmo():
   ...:     entermarks=raw_input("enter your marks")
   ...:     marks=float(entermarks)
   ...:     mygrade=TestMarks(marks)
   ...:     print mygrade
   ...:




In [3]: def main():
   ...:     jungmo()
   ...:


In [4]:main()
enter your marks60
D

