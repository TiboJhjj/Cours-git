# Git Cheat Sheet - ESGI

Le versionning est un projet logiciel qui a pour but final d'ecrire des programmes c'est à dire du texte.
L'idée est de l'idee est de sauvegarder des informations afin de pouvoir s'y referer en cas d'erreurs, beugs ou oublis.

Les principaux avantes sont donc listés comme suite : 
- La sauvegarde de version
- La sauvegarde de l'historique des versions
- L'agnostique vis à vis du langage
- Gerer du texte
- L'aide au passage d'une version à une autre (livraison fluide des modifications sans que ça soit lourd)
- Cela facilite également la collaboration et sert à resoudre facilement les conflits.

## Systeme de gestion de version
NB:  Dans le git on ne met que le code source, pas le compilé ni tout ce qui tourne autour

 on distingue ainsi plusieurs types de systèmes :
 
 - le systeme centralisé : tout part du serveur qui gere les historiques en local sur notre ordinateur qui lui est allimenté par les fichers qu'on peut stocker 
 - le système distribué : git est un systeme distribué mais quand meme centralisé et fonctionne de la façon suivante
   une copie de l'historique des versions est disponible localement
   possibilité de travailler sans latence et hors ligne
   possibilte de modifier le local avant de le lancer sur le server
   distribué mais pas centralisé
   server populaire : git hub et git lab
   on eut eglement utiliser github desktop comme interface graphique
 
  Cas pratiques

- `git clean` : permet de supprimer les fichiers non suivis de votre dépôt, c'est-à-dire les fichiers qui ne sont pas dans l'index de Git.

- `git gc` : (garbage collection)  permet d'optimiser votre dépôt en supprimant les commits inutiles et en regroupant les données de manière plus efficace.

- `git mv` : permet de déplacer ou de renommer des fichiers dans votre dépôt, tout en conservant l'historique des modifications apportées à ces fichiers. 
 
 - le fichier .gitignore permet de garder la trace du code souce uniquement
 lorsqu'on ouvre un fichier
  head = la version chargée sur mon ordinateur

- Pour retrouver les commits qui concernent notre fichier renommé avec son ancien nom faire : `git log --follow`

- `git reset <id>` : annule les modifications apportées à un fichier 

- `git reset --hard` : (on abondonne tout le travail, a la fois les commits et tous les fichiers à l'interieure)

- `git rebase` : Le rebase est l'un des deux utilitaires Git spécialisé dans l'intégration des changements d'une branche à une autre. L'autre utilitaire d'intégration des changements est git merge. Le merge est toujours un enregistrement des changements vers l'avant. Alternativement, le rebase dispose de puissantes fonctionnalités de réécriture de l'historique

- `pull request` : demande l'autorisation pour merger une branche


Parcours des fichiers

 working directory[a la creation du fichier]=> [lorqu'on utilise la commande add]stage(index)=>[lorsqu'on utilise le comit]history

 Ps : 
 
       - l'identifiant des objets de commit est un hash
        une branche est un pointeur vers un commit
        - à chaque fois qu'on ajoute un commit la tete de lecture bouge dans l'historique
       - ne jamais vraiment modifier un commit dans le git
       - la fusion de deux branches peut causer un conflit

# Github

GitHub est un service en ligne qui permet à des développeurs de stocker et de suivre les versions de leur code source. C'est un outil très utile pour le travail en équipe sur un projet de développement de logiciel, car il permet à plusieurs personnes de travailler sur le même code en même temps et de suivre les changements apportés au fil du temps.

GitHub utilise Git, un logiciel de contrôle de version, pour gérer le suivi des changements apportés au code. Chaque fois qu'un développeur modifie le code, il peut utiliser Git pour enregistrer ces changements (ce que l'on appelle "committer" les changements). Les développeurs peuvent également "pusher" leurs changements sur GitHub, ce qui permet de les partager avec d'autres membres de l'équipe.

GitHub offre également de nombreuses autres fonctionnalités, telles que la gestion des tâches, la documentation du projet, et l'intégration avec d'autres services populaires. C'est devenu une plateforme de développement de logiciel incontournable pour de nombreuses équipes à travers le monde.

## Configuration des outils

- `git config` : Cette commande permet de configurer les paramètres de Git à différents niveaux (système, utilisateur ou local au niveau d'un dépôt). Elle peut être utilisée pour définir votre nom d'utilisateur et votre adresse électronique, qui seront utilisés pour les opérations de commit. Par exemple : git config --global user.name "Mon Nom"

- `git init` : Cette commande permet de créer un nouveau dépôt Git local. Elle doit être utilisée dans le répertoire qui doit être suivi par Git.

- `git clone` : Cette commande permet de créer une copie locale d'un dépôt Git existant. Elle est souvent utilisée pour travailler sur un projet en collaboration avec d'autres personnes, car elle permet de télécharger tout le contenu du dépôt ainsi que l'historique complet des commits. Par exemple : `git clone https://github.com/user/repo.git`

- `git remote` : Cette commande permet de gérer les connexions à d'autres dépôts distants. Elle peut être utilisée pour ajouter un dépôt distant à votre dépôt local en utilisant la sous-commande add, comme dans l'exemple suivant : `:wq
git remote add origin https://github.com/user/repo.git`

## Qu'est-ce qu'un commit ?

Un commit Git (ou simplement commit) est une sauvegarde de l'état actuel du dépôt dans l'historique. En d'autres termes, un commit permet de conserver une version de tous les fichiers du dépôt à un moment donné. Lorsque vous effectuez un commit, vous spécifiez un message de commit qui décrit les modifications apportées au dépôt depuis le dernier commit. Cela peut être utile pour comprendre les changements apportés au dépôt au fil du temps et pour revenir à une version précédente du dépôt si nécessaire.

Les commits forment une chaîne dans l'historique du dépôt, chaque commit faisant référence au commit précédent. Cela permet de suivre l'évolution du dépôt au fil du temps et de naviguer dans l'historique des commits.

En utilisant des commits de manière régulière, vous pouvez maintenir un historique clair et organisé de votre travail et faciliter la collaboration avec d'autres personnes sur un projet.

## Consulter les modifications et effectuer des commits

- `git status` : Cette commande permet de voir les fichiers modifiés et ceux qui sont en attente de commit. Elle est souvent utilisée pour savoir où en est l'état du dépôt local par rapport au dernier commit.

- `git diff` : Cette commande permet de voir les différences entre les fichiers modifiés et ceux du dernier commit. Elle est souvent utilisée pour voir les détails des modifications apportées aux fichiers.

- `git add` : Cette commande permet de mettre des fichiers en attente de commit. Elle est souvent utilisée pour ajouter des fichiers modifiés ou nouvellement créés au prochain commit. Par exemple : `git add path/to/file.txt`

- `git commi`t : Cette commande permet de créer un commit, c'est-à-dire de sauvegarder l'état actuel du dépôt dans l'historique. Elle doit être utilisée avec un message de commit qui décrit les modifications apportées. Par exemple : `git commit -m "Ajout d'une nouvelle fonctionnalité"`

> Voici un exemple de workflow courant avec ces commandes :
> 
> 1. Modifiez un ou plusieurs fichiers dans votre dépôt local.
> 2. Utilisez git status pour voir quels fichiers ont été modifiés.
> 3. Utilisez git diff pour voir les détails des modifications apportées aux fichiers.
> 4. Utilisez git add pour mettre en attente les fichiers modifiés que vous souhaitez inclure dans le prochain commit.
> 6. Utilisez git commit avec un message de commit pour enregistrer les modifications dans l'historique du dépôt.
