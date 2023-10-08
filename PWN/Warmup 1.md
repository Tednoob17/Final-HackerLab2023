#### Categorie: PWN 
#### **Author**: W1z4rd
#### Solve: 3/20 
#### Points: 30 pts (at first)| 14 pts (at end)

#### Write-up by: Jekyll ([0xJekyll](https://twitter.com/Ted_Kouhouenou))


- ### Write-Ups

    - FR Version
![warm](Images/warmup.png)

#### Information : 
`nc 54.37.70.250 3012`
Nous avons comme information l'adresse **Ip** et le **port** ,et nous pouvons nous connecter au serveur via la commande **Netcat** (`nc`)

Tentons voir 
![war](Images/war1.png)

Lorsqu'on se connecte nous avons ce message de bienvenue, mais rien d'autre ne s'affiche à l'écran, c'est comme si une entrée était attendue de notre part 

Ne sachant pas quoi entrer, vaut mieux entrer n'importe quoi.

![war2](Images/war2.png)

Bon j'ai entrer un certains nombre de `a` pour voir ce qu'on aura comme sortie , et nous avons un `segmentation fault` .Le core dump fait référence à l'enregistrement de l'état du programme, c'est à dire de ses ressources en mémoire et en processeur.


Cela me fait aussi penser que ce challenge peut bien etre du Stack Overflow
Ce qui voudrait aussi dire que ce que j'ai envoyé comme entrer est un peu trop.
Je retente en essayant de dimunier le nombre de caractere .

![war3](Images/war3.png)

Voila nous avons le flag.

Flag: `CTF_574ck_overfl0w_1s_to_easy_!!`


-------------------------------------------------------------------

 - EN Version
![warm](Images/warmup.png)

#### Information : 
`nc 54.37.70.250 3012`
We have as information the **Ip** address and the **port**, and we can connect to the server via the **Netcat** command (`nc`)

Let's try to see
![war](Images/war1.png)

When we log in we get this welcome message, but nothing else is displayed on the screen, it's as if an entry was expected from us

Not knowing what to enter, it's better to enter anything.

![war2](Images/war2.png)

Well I entered a certain number of `a` to see what we would have as output, and we have a `segmentation fault`. The core dump refers to the recording of the state of the program, it is to say about its memory and processor resources.


This also makes me think that this challenge may well be Stack Overflow
Which would also mean that what I sent as input is a bit too much.
I try again, trying to reduce the number of characters.

![war3](Images/war3.png)

Voila nous avons le flag.

Flag: `CTF_574ck_overfl0w_1s_to_easy_!!`