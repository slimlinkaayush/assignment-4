#Q1

li=['a','b','c','d','e']
li.reverse()
print("1)Reversed list is = ",li)

#Q2--

str= ['T', 'q', 'B', 'F', 'j', 'O', 't', 'L', 'D']
for s in str:
    if s.isupper():
        print("2 Uppercase letter are ",s)

#Q3--

li=['1','3','6','9','12','15','18','21']
li2=[]
for n in li:
    li2.append(int(n))
li=li2
print("3)List of integers is",li2)


#Q4--

str='aca'
str1='baab'
if(str==str[::-1]):
      print("4.1)The string is palindromic")
else:
      print("The string is not palindromic")
      
if(str1==str1[::-1]):
      print("The string is palindromic")
else:
      print("4.2)The string is not palindromic")


#Q5--

import copy
l_1=[[1,2,3],[4,5,6]]
l_2=copy.deepcopy(l_1)
print("5)The new list is = ",l_2)












