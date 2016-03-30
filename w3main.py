

In [1]: import turtle

In [2]: def Converttem():
   ...:     cf=raw_input("Choose! c or f:")
   ...:     if(cf=='c'):
   ...:         print"you entered c,enter it`s value"
   ...:         temp=raw_input("c value:")
   ...:         ftemp=float(temp)
   ...:         tem=(ftemp*1.8)+32
   ...:         print tem
   ...:     else:
   ...:         print"you entered f,enter it`s value"
   ...:         temp=raw_input("f value:")
   ...:         ctemp=float(temp)
   ...:         tem=(ctem-32)/1.8
   ...:         print tem
   ...:

In [3]: Converttem()
Choose! c or f:c
you entered c,enter it`s value
c value:110
230.0

In [4]: