Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
b = "kadirbaba"
b[1]
'a'
b[0]
'k'
b[:6]
'kadirb'
b[:]
'kadirbaba'
len (d)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    len (d)
NameError: name 'd' is not defined. Did you mean: 'id'?
len(b)
9
len("kadirnaba")
9
3+4
7
2+3
5
1-2+3
2
1-2
-1
34+3
37
2**3
8
3**4
81
>>> 2//3
0
>>> 4//3
1
>>> 3/4
0.75
>>> 22/7
3.142857142857143
>>> print("kadir")
kadir
>>> print("kadir" + str(7))
kadir7
>>> print(int"9" + 8)
SyntaxError: invalid syntax
>>> print (int "8" + 4)
SyntaxError: invalid syntax
>>> print (int ("8") + 4)
12
>>> eymen = terörist
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    eymen = terörist
NameError: name 'terörist' is not defined
>>> eymen = "terörist"
>>> kadir = "counter terörist"
>>> eymen + kadir
'teröristcounter terörist'
>>> print (eymen - kadir)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    print (eymen - kadir)
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> len (eymen)
8
>>> len (kadir)
16
>>> print (float("4.75") + 8)
12.75
