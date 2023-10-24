#### Categorie: Cryptography 
#### **Author**: r3s0lv3r
#### **FLAG** : CTF_**password** 

#### Solve: 14/20 
#### Points: 30 pts (at first)|  17 pts (at end)

### File: [Transpose.txt](Files/Transpose.txt)
#### Write-up by:  [OxJekyll](https://twitter.com/Ted_Kouhouenou)

## Solution :
### Fr Version : 

`For ENG version scroll down` 

![pose](Images/transpose.png)


Le contenu du fichier est le suivant : 

`YISFNE OGSPENOORRD UACOCIRIEE RLTTRTMTCV FFEAO` 

Le nom du challenge doit surement etre un indice tentons voir avec [dcode](https://www.dcode.fr/) 
et essayons de rechercher le terme *Transposition* 
Nous obtenons une liste contenants tout les chiffrements par transposition ,et tentons chacun d'eux
![](Images/transposition.png)


FInalement le chiffrement qui etait le bon etait le ` Rail Fence (Zig-Zag)` 

![](Images/flagg.png)

### Flag :  `CTF_TOPSECRETINFORMATIONRECOVERED`


---------------------------------------------------------------------------------

## Eng Version 



![pose](Images/transpose.png)


The contents of the file are as follows:

`YISFNE OGSPENOORRD UACOCIRIEE RLTTRTMTCV FFEAO`

The name of the challenge must surely be a clue, let's try to see with [dcode](https://www.dcode.fr/)
and try to search for the term *Transposition*
We obtain a list containing all the transposition ciphers, and try each of them
![](Images/transposition.png)


Finally the cipher that was the right one was the `Rail Fence (Zig-Zag)` 

![](Images/flagg.png)

### Flag :  `CTF_TOPSECRETINFORMATIONRECOVERED`
