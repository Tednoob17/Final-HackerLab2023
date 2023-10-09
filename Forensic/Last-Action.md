#### Categorie: Forensic 
#### **Author**: W1z4rd
#### Solve: 17/20 
#### Points: 200 pts (at first)| 120 pts (at end)

#### Write-up by: Amoweak ([Amoweak](https://))
#### Description :
#### **[FR]**
L'équipe d'investigation en réponse aux incidents (IR) des gardiens des trésors a mené une opération de perquisition chez un membre du groupe DokounXosu.

Vous êtes chargé de trouver les éléments suivants :

- Le fichier le plus récemment modifié par l'utilisateur sur la machine, y compris son extension
- La date à laquelle ce fichier a été ouvert, au format yyyy-mm-dd hh:mm:ss
- Le nom du répertoire où se trouve ce fichier

**[EN]**

The Treasure Guardians’ Incident Response Investigation (IR) team conducted a search operation at the home of a member of the DokounXosu group.

You are responsible for finding the following:

- The file most recently modified by the user on the machine, including its extension
- The date this file was opened, in the format yyyy-mm-dd hh:mm:ss
- The name of the directory where this file is located

#### Information
**Format du FLAG**: CTF_**filename**:**yyyy-mm-dd hh:mm:ss**:**Nomdurepertoire**


- ### Write-Ups
  ### FR Version
  > Challenge
  ![last](Images/lastaction.png)

Après téléchargement du fichier, première chose, on vérifie le type du fichier, et il s’avère que c’est un Microsoft Windows registry file.

![file1](Images/amo1.png)
Nous remarquons aussi que l'extension `.copy0` ne sert a rien dns notre cas donc nous pouvons l'enlever

On chercher sur internet un outil permettant d’ouvrir le fichier. L’observateur des évènements de Windows peut le faire d’après une recherche. On essaie donc de l’ouvrir avec mais on reçoit une erreur « fichier endommagé ».

![file2](Images/amo2.png) 
On cherche donc un autre moyen. Après des recherches, un membre de l’équipe 
« [Jekyll](https://twitter.com/Ted_Kouhouenou) » découvre un outil qui pourrait nous aider. Il s’agit de cet outil : 
**RegRipper 3.0** 


![file3](Images/amo3.png) 
> Source : `https://github.com/keydet89/RegRipper3.0` 

Je clone le répertoire 
```bash
git clone https://github.com/keydet89/RegRipper3.0
```

Puis j'exécute la commande rr.exe qui nous permettra de démarrer l’outil.


![file4](Images/amo4.png)
Le logiciel s'execute 
Ensuite, on entre le fichier où on veut récupérer les informations et le fichier qui recevra les résultats, puis on clique sur « rip ! » pour lancer l’action.
![file5](Images/amo5.png)

On examine ensuite le fichier apres la sortie du resultat. 
Après examination, on note un **faux flag**  et un mot clé « Recent » et on se charge aussi de découvrir la date la plus récente dans le fichier, qui s’avère être le **28 septembre 2023.** 
![file6](Images/amo6.png)

Chose intrigante ici est le mot clé  **MRUListEx** .
Après des recherches, on note qu’il fallait se concentrer sur l’ordre des numéros « le premier est le dernier objet ouvert », et non sur le chiffre pour représenter l’ordre d’ouverture.

On sait que le format du Flag est comme ceci :
- CTF_**filename**:**yyyy-mm-dd hh:mm:ss**:**Nomdurepertoire** 


 Ainsi donc, on obtient comme flag : CTF_link.txt:2023-09-28 13:43:41:Adipol.

Flag : `CTF_link.txt:2023-09-28 13:43:41:Adipol.`
