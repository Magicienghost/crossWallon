# CROSS WALLON

- Les fichiers Excel ainsi que les fichiers HTML contenant les données personnelles ont été masqués pour garantir leurs protections.
- Se réferer à la template dans `./excel` si besoin pour la création du fichier excel.


## Explications préliminaires
- Le dossier [python](https://github.com/Magicienghost/crossWallon/blob/main/python/) contient les fichiers relatifs au fonctionnement propre du programme.
- Le dossier [excel](https://github.com/Magicienghost/crossWallon/blob/main/excel/) contient une unique template à dupliquer pour créer un fichier propre pour l'année en cours qui devra être mis dans ce même dossier. 
- Le dossier [styles](https://github.com/Magicienghost/crossWallon/blob/main/styles/) contient les différents fichiers CSS et images pour la bonne mise en page des fichiers HTML. 
- Le dossier `html` n'existe pas ici car il est vide avant l'éxécution du programme. 
- Les fichiers contenus dans `./styles` n'ont pas à être modifié d'une année à l'autre. 

## Focus sur python
- Le fichier principal est [cross.py](https://github.com/Magicienghost/crossWallon/blob/main/python/cross.py) (les autres fichiers python tendent à disparaître)
- Les modules à installer sont listés dans [requirements.txt](https://github.com/Magicienghost/crossWallon/blob/main/python/requirements.txt)
  - Nécessite d'exécuter pour les installer tous d'un coup : 
  ```cmd
    pip install -r requirements.txt ```
- Les fonctions ne seront pas presque pas à modifier d'une année à l'autre, leur fonctionnement est quasi autonome. 
- Voici les points auxquels il faut prêter attention avant le Cross : 
  - [`fileName`](https://github.com/Magicienghost/crossWallon/blob/main/python/cross.py#L6) : correspond au nom du fichier Excel utilisé pour l'inscription (situé par défaut dans [./excel](https://github.com/Magicienghost/crossWallon/blob/main/excel/))
  - [`dateCross`](https://github.com/Magicienghost/crossWallon/blob/main/python/cross.py#L8) : bon là c'est trivial
  - [`hourTab`](https://github.com/Magicienghost/crossWallon/blob/main/python/cross.py#L10) : contient les heures des départs des différentes courses à la seconde près (à entrer avant la compilation des résultats du Cross car elles évoluent chaque année).
  - [`distTab`](https://github.com/Magicienghost/crossWallon/blob/main/python/cross.py#L11) : contient la longueur réelle de chacune des courses (elles ne devraient pas changer si le parcours n'évolue pas d'une année à l'autre).
  - [`effectDic`](https://github.com/Magicienghost/crossWallon/blob/main/python/cross.py#L236-L248) : contient les effectifs totaux de chaque classe participante (à modifier avant le cross au moment de la réceptions des listings). 
  - Les [3 lignes](https://github.com/Magicienghost/crossWallon/blob/main/python/cross.py#L447-L449) permettent de modifier quelle partie du code est executée au lancement du fichier via un appel à une fonction particulière (exécution de plusieurs fonctions en même temps non recommandée).
    - La fonction `renderDossardsInit()` génére un fichier HTML `initialFile.html` contenant les listes des élèves répartis par classe ainsi qu'une mise en page permettant les inscriptions de chacun. 
    - La fonction `renderDossardsHTML()` génére un fichier HTML `recapInscription.html` qui contient comme son nom l'indique le récapitulatif des inscriptions au Cross le tout regroupé par classe : nom et prénom, type de participation et dossard attribué pr chacun.
    - La fonction `getAllTime()` génére un fichier HTML `result.html` contenant le sésame : les résultats complets du Cross, il se compose du classement des classes ayant participées ainsi que le classement individuel regroupé par sexe et distance. 
    - L'ensemble des fichiers HTML générés sont prêts pour être imprimer. 
    - Les fonctions non spécifiées ci-dessus sont des fonctions auxiliaires utilisées par les fonctions principales et ne nécessitent donc pas d'explications.
- Pour fonctionner le programme a besoin de modules qui doivent être installés sur l'ordinateur 

### En dehors des 5 variables mentionnées ci-dessus le reste des fonctions / lignes n'ont pas à être modifiées, cela pourrait rendre le code inutilisable ou fausser les résultats.

## Focus sur Excel
La réalisation du fichier Excel permettant l'enregistrement des participations et des résultats du Cross ne demande pas une connaissance experte d'Excel mais juste une forte rigueur.
- Feuille `all_eleves` : doit contenir les listings de l'ensemble des élèves élligibles à la participation au Cross (en 2024 : toutes les prépas, DCG 1, 2 et 3, et les CPES)
  - Au minimum, il faut le nom, prénom, classe et sexe de chaque élève pour ne pas obstruer le fonctionnement des fonctions des autres feuilles. 
  - Attention, il peut y avoir une distinction entre les MP et les MPI qui doivent être rassemblées en MP(I) (de même pour les MPE et MPIE).
- Feuille `inscription` : doit contenir l'ensemble des inscriptions au Cross (coureurs qu'ils soient profs ou élèves et les balises). 
  - Le remplissage de cette feuille est en partie automatique : après avoir rentré le nom & prénom d'un élève, sa classe, son sexe et son numéro seront automatiquement recherchés dans la feuille `all_eleves` (dans le cas d'un prof, son nom et prénom seront inconnus, il sera donc nécessaire d'entrer les infos à la main).
  - Il restera à entrer son équipe (ELEVE ou PROF) ainsi que sa participation (3, 5, 8 ou Balise), s'il s'agit d'un coureur, il faudra également le lui attribuer un dossard correspondant à la distance qu'il parcourt. 
- Feuille `balise` : feuille entièrement automatique, elle récupère les noms des participants identifiés comme "Balise" et dresse la liste de ces derniers. Elle permet au programme python de calculer plus rapidement les avantages apportés par les balises à chaque classe. 
- Feuille `hash` : ne sert que de base de données pour la feuille `inscription` et ne change pas d'une année à l'autre. 

## En cas de problème, ouvrir une issue Github ou me mentionner sur le discord de Wallon (`@magicien_ghost`).