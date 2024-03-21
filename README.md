# CROSS WALLON

- Les fichiers Excel ainsi que les fichiers HTML contenant les données personnelles ont été masqués pour garantir leurs protections.
- Se réferer à la template dans `./excel` si besoin pour la création du fichier excel.

https://github.com/Magicienghost/crossWallon/blob/main/python/cross.py#L5

## Explications préliminaires
- Le dossier [python](https://github.com/Magicienghost/crossWallon/blob/main/python/) contient les fichiers relatifs au fonctionnement propre du programme.
- Le dossier [excel](https://github.com/Magicienghost/crossWallon/blob/main/excel/) contient une unique template à dupliquer pour créer un fichier propre pour l'année en cours qui devra être mis dans ce même dossier. 
- Le dossier [styles](https://github.com/Magicienghost/crossWallon/blob/main/styles/) contient les différents fichiers CSS et images pour la bonne mise en page des fichiers HTML. 
- Le dossier `html` n'existe pas ici car il est vide avant l'éxécution du programme. 
❗Les fichiers contenus dans `./styles` n'ont pas à être modifié d'une année à l'autre. 

## Fonctionnement 
- Le fichier principal est [cross.py](https://github.com/Magicienghost/crossWallon/blob/main/python/cross.py) (les autres fichiers python tendent à disparaître)
- Les fonctions ne seront pas presque pas à modifier d'une année à l'autre, leur fonctionnement est quasi autonome. 
- Voici les points auxquels il faut prêter attention avant le Cross : 
  - [`fileName`](https://github.com/Magicienghost/crossWallon/blob/main/python/cross.py#L6) : correspond au nom du fichier Excel utilisé pour l'inscription (situé par défaut dans [./excel](https://github.com/Magicienghost/crossWallon/blob/main/excel/))
  - [`dateCross`](https://github.com/Magicienghost/crossWallon/blob/main/python/cross.py#L8) : bon là c'est trivial
  - [`hourTab`](https://github.com/Magicienghost/crossWallon/blob/main/python/cross.py#L10) : contient les heures des départs des différentes courses à la seconde près (à entrer avant la compilation des résultats du Cross car elles évoluent chaque année).
  - [`distTab`](https://github.com/Magicienghost/crossWallon/blob/main/python/cross.py#L11) : contient la longueur réelle de chacune des courses (elles ne devraient pas changer si le parcours n'évolue pas d'une année à l'autre).
  - [`effectDic`](https://github.com/Magicienghost/crossWallon/blob/main/python/cross.py#L236-L248) : contient les effectifs totaux de chaque classe participante (à modifier avant le cross au moment de la réceptions des listings). 
  - 
WIP