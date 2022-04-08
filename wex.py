 python3
Python 3.8.10 (default, Mar 15 2022, 12:22:08) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> [1,2,3]
[1, 2, 3]
>>> ['cat','rat','bat','elephant']
['cat', 'rat', 'bat', 'elephant']
>>> spam= ['cat','rat','bat','elephant']
>>> spam
['cat', 'rat', 'bat', 'elephant']
>>> #liss enclosed in a square bracket.values inside called items.[is empty list regarding lists]
>>> spam[3]
'elephant'
>>> spam[2]
'bat'
>>> spam[0]
'cat'
>>> spam[-1]
'elephant'
>>> spam[4]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> 'Hello'+""+spam[0]
'Hellocat'
>>> 'Hello '+""+spam[0]
'Hello cat'
>>> #nesting of lists,two lists sharing two outside main  brackets. and are sepperated by comma,
>>> spam=[['cat','bat'],[10,20,30,40,50]]
>>> spam[0]
['cat', 'bat']
>>> spam[0][1]
'bat'
>>> spam[1][1]
20
>>> spam[0][2]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> spam[1][3]
40
>>> #so i guess there are two lists right?So the first list is index0 the second one is index2 ,they are like the parent list.Don't forget the main brackets.
>>> yasmin=[[10,29,40],['green','yellow']]
>>> yasmin[0][1]
29
>>> yasmin[1][0]
'green'
>>> yasmin[1][1]
'yellow'
>>> yasmin[0][2]
40
>>> spam=['cat','rat','bat']
>>> spam[0:4]
['cat', 'rat', 'bat']
>>> spam=['cat','rat','bat','elephant']
>>> spam[0:4]
['cat', 'rat', 'bat', 'elephant']
>>> #coz we want elephant to show will go beyond our index of string.This is clled  Getting a lis from another list with slices.
>>> spam[0:-1]
['cat', 'rat', 'bat']
>>> spam=['cat','rat','bat','elephant']
>>> spam[0:-1]
['cat', 'rat', 'bat']
>>> #NB when slicing we include numbers from the first index chosen but last item not included.

