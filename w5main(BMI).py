def ComputeBmi():
   ...:     h=input ("user height:")
   ...:     w=input ("user weight:")
   ...:     bmi=w/(h*h)
   ...:     if bmi<18.5:
   ...:         result='low weight'
   ...:     elif bmi>=18.5 and bmi<23:
   ...:         result='normal weight'
   ...:     elif bmi>=23 and bmi<25:
   ...:         result='over weight'
   ...:     elif bmi>=25 and bmi<30:
   ...:         result='obesity'
   ...:     elif bmi>=30:
   ...:         result='try exercise'
   ...:     return result
   ...: 


print ComputeBmi()