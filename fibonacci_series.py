"""_This module print the Fibonacci series
"""
nterm= int(input("Enter the number of terms:"))
COUNT= 0
n1= 0
n2= 1
if nterm<=0:
    print("Invalide value, Enter positive number")
elif nterm==1:
    print(f"Fibonacci series : {n1}")
else:
    while COUNT<nterm:
        print(n1)
        nth=n1+n2 #sum of two terms
        #updating values
        n1=n2
        n2=nth
        COUNT+=1