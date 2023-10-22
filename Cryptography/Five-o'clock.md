#### Categorie: Cryptography
#### **Author**: r3s0lv3r
#### Solve: 14/20 
#### Points: 70 pts (at first)|  57 pts (at end)

### File : [message\(1\).txt](./Files/message\(1\).txt) 
#### Write-up by: 
#### Description : 
#### **[FR]**
Vous interceptez un message secret du mystérieux groupe Djakpataglo. Il semble que les membres de ce groupe utilisent une technique de cryptage unique basée sur une sorte de déplacement de bits. Trouvez comment récupérer le message transmis pour éviter une catastrophe imminente.
#### **[EN]**
You intercept a secret message from the mysterious Djakpataglo group. It seems that the members of this group are using a unique encryption technique based on a kind of bit shifting. Find out how to retrieve the transmitted message to avoid imminent disaster.


## Solution :
### Fr Version : 

`For ENG version scroll down` 

![crypt](Images/fiveclock.png)


Nous avons en description un fichier contenant une suite de caracteres ressemblant a de l'hexadecimal 
`688ac8eb66eb29cd6c4e66ad66cd8e26cde8eb8966cc8eeb4a068e868e2d06cd6eebe6a666864626646464` 
Comme pour la plupart des autres challenges presenter nous ne connaissons pas au debut le chiifrement mais grace a [Dcode](https://www.dcode.fr/) et utilisons l'[identification de chiffrement ](https://www.dcode.fr/identification-chiffrement) utiliser 

![option](Images/option.png)

Nous avons toutes les options possibles avec la chaine donner en entier, alors commence une petite fouille pour savoir quel est le bon chiffrement .Nous finissons par tomber sur le 
[Dealage Binaire Circulaire](https://www.dcode.fr/decalage-circulaire-binaire)  qui nous donne un apercu du flag ,voila donc d'ou venait le nom du challenge **Five o'clock ** pour faire reference a un chiffrement circulaire .

Pour cette partie nous avons du faire par tatonement pour determiner a combien de decalage de bits il a ete effectuer
![flag](Images/flag.png)


Flag : `CTF_encoding_utf-8_to_utf-16_234452.` 


-------------------------------------------------------------------------
### Eng Version 

![crypt](Images/fiveclock.png)


Nous avons en description un fichier contenant une suite de caracteres ressemblant a de l'hexadecimal 
`688ac8eb66eb29cd6c4e66ad66cd8e26cde8eb8966cc8eeb4a068e868e2d06cd6eebe6a666864626646464` 
Comme pour la plupart des autres challenges presenter nous ne connaissons pas au debut le chiifrement mais grace a [Dcode](https://www.dcode.fr/) et utilisons l'[identification de chiffrement ](https://www.dcode.fr/identification-chiffrement) utiliser 

![option](Images/option.png)

Nous avons toutes les options possibles avec la chaine donner en entier, alors commence une petite fouille pour savoir quel est le bon chiffrement .Nous finissons par tomber sur le 
[Dealage Binaire Circulaire](https://www.dcode.fr/decalage-circulaire-binaire)  qui nous donne un apercu du flag ,voila donc d'ou venait le nom du challenge **Five o'clock ** pour faire reference a un chiffrement circulaire .

Pour cette partie nous avons du faire par tatonement pour determiner a combien de decalage de bits il a ete effectuer
![flag](Images/flag.png)


Flag : `CTF_encoding_utf-8_to_utf-16_234452.` 

