#### Categorie: Steganography 
#### **Author**: r3s0lv3r
#### Solve: 3/20 
#### Points: 200 pts (at first)| 190 pts (at end)
#### Files: [proj_.png](./Files/proj_.png)   
#### Write-up by: [Jekyll](https://twitter.com/Ted_Kouhouenou)
#### Description :
#### **[FR]**
En dehors de la boîte !
#### **[EN]**
Outside the box !

## Solution :
### Fr Version : 

`For ENG version scroll down` 


![ouais](nuxoxo.png)
Pour commencer avec ce challenge je peux vous dire que le contexte ne sert pas a grand chose.
Apres plusieurs recherche et tentative de trouver le flag ,nous n'avons pas d'autre choix que de demander un **hint** .L'indice est la **resolution** ,oui la resolution de l'image .
Nous augmentons donc la resolution de l'image . Nous cherchons donc un moyen de faire e genre de travail ,nous trouvons donc un article de la team [bi0s](https://wiki.bi0s.in/steganography/tweak-png/ ) parlent d'un outil appeller 
[tweakpng](https://entropymine.com/jason/tweakpng/  ) .Permettant de faire le travail.

Le fichier est un **executable** donc uniquement installable sous windows.
N'etant pas sous windows je decide d'utiliser wine .

```
sudo apt install wine-stable
```
Nous demarrons avec cette commande

```bash
wine ./tweakpng.exe

```

![weak](Images/tweak.png) 

Nos choisissons la premiere option pour modifier a resolution de l'image
Au fur et a mesure que nous elargissons l'image nous remarquons qu'un petit message se forme en bas de l'image

![flou](Images/flou.jpeg)

Mais l'image n'est pas tres claire ,nous decidons donc d'uploader l'image sur stegonline
et d'appliquer des effets sur l'image afin de pouvoir mieux distinguer ce qui est ecrit
nous appliquons l'effet rouge qui nous parait assez net.
![toj](Images/toj_.png)

l'ecriture afficher ne semble pas etre du en **ASCII** .Nous avons ete assez aveugle pour ne pas reconnaitre du **Braille** x) .
Nous nous rendons sur [Dcode](https://www.dcode.fr/) et cherchons [l'alphabet braille](https://www.dcode.fr/alphabet-braille) 

et entrons ce qui est afficher 
![decrypt](Images/braille.png)

nous obtenons ceci `ctfforg3n10usforh4c 3rforfind!` les caracteres underscores ne s'etant pas afficher nous tentons de les faires mettre dans la chaine 
ctf_forg3n10us_forh4ckerfor_find!


Flag : `ctfforg3n10usforh4c 3rforfind!`

----------------------------------------------------------------------------

### Eng Version