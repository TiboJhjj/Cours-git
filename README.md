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
## Nommer une série de commits et les combiner entre eux

- `git tag` : Cette commande permet de créer, lister et supprimer des tags dans Git. Un tag est un nom qui peut être associé à un commit spécifique dans l'historique du dépôt. Les tags sont souvent utilisés pour marquer des versions stables ou importantes du dépôt, par exemple une version de production ou une version de développement en cours. Par exemple, pour créer un nouveau tag nommé v1.0 qui pointe sur le dernier commit, vous pouvez utiliser la commande suivante : `git tag v1.0`

- `git branch` : Cette commande permet de gérer les branches dans Git. Une branche est une série de commits qui évolue indépendamment des autres branches. Les branches sont souvent utilisées pour développer de nouvelles fonctionnalités ou corriger des bogues, tout en maintenant une version stable du dépôt sur la branche principale (appelée "master"). Par exemple, pour créer une nouvelle branche nommée new-feature, vous pouvez utiliser la commande suivante : `git branch new-feature`

- `git merge` : Cette commande permet de combiner les commits d'une branche dans une autre. Elle est souvent utilisée pour fusionner les modifications apportées sur une branche de développement dans la branche principale une fois que le travail est terminé. Par exemple, pour fusionner les commits de la branche new-feature dans la branche master, vous pouvez utiliser la commande suivante : `git merge new-feature`

- `git cherry-pick` : Cette commande permet de sélectionner un commit spécifique et de l'appliquer à la branche courante. Elle est souvent utilisée pour sélectionner individuellement des commits d'une branche et les appliquer à une autre, au lieu de fusionner tous les commits d'une branche avec git merge. Par exemple, pour appliquer le commit avec l'ID abcdefg à la branche courante, vous pouvez utiliser la commande suivante : `git cherry-pick abcdefg`

## Exclure des modifications et des fichiers du dépôt

Un fichier .gitignore est un fichier de configuration qui permet de définir une liste de fichiers et de dossiers à ignorer par Git. Lorsque vous ajoutez un fichier ou un dossier à ce fichier, Git ne suivra pas les modifications apportées à ces éléments et ne les inclura pas dans les commits.

Voici comment utiliser un fichier .gitignore pour exclure des fichiers et des chemins temporaires :

1. Créez un fichier .gitignore dans le répertoire racine de votre dépôt Git.
2. Ajoutez la liste des fichiers et dossiers à ignorer, un par ligne. Vous pouvez utiliser des caractères génériques comme * et ? pour ignorer plusieurs fichiers similaires. Par exemple, pour ignorer tous les fichiers terminant par .tmp, vous pouvez ajouter la ligne suivante au fichier .gitignore : *.tmp
3. Enregistrez le fichier .gitignore. Git commencera à ignorer les fichiers et dossiers spécifiés dans ce fichier lors de l'exécution de la commande git add.

> Notez que si vous avez déjà ajouté des fichiers ou dossiers à Git avant de les ajouter au fichier .gitignore, ils resteront suivis par Git et inclu dans les commits futurs. Vous pouvez utiliser la commande git rm --cached pour arrêter de suivre ces fichiers et les exclure des commits futurs.

## Mettre en suspens des modifications non finies pour y revenir plus tard

- `git stash` : Cette commande permet de mettre en attente les modifications en cours et de les cacher temporairement. Elle est souvent utilisée lorsque vous souhaitez changer de branche ou effectuer une autre action qui nécessite de nettoyer votre dépôt local, tout en conservant les modifications en cours pour y revenir plus tard. Par exemple, pour mettre en attente les modifications en cours et nettoyer votre dépôt, vous pouvez utiliser la commande suivante : `git stash`

- `git stash list` : Cette commande permet de voir la liste des modifications mises en attente avec git stash. Elle peut être utile pour savoir combien de modifications sont en attente et leur contenu.

- `git stash apply` : Cette commande permet de réappliquer les modifications mises en attente avec git stash. Elle peut être utilisée pour continuer le travail sur les modifications mises en attente à un moment donné. Par exemple, pour réappliquer les dernières modifications mises en attente, vous pouvez utiliser la commande suivante : `git stash apply`

- `git stash pop` : Cette commande fait la même chose que git stash apply, mais en plus elle supprime la modification mise en attente de la liste des modifications mises en attente. Cela peut être utile lorsque vous avez terminé de travailler sur les modifications mises en attente et que vous souhaitez nettoyer votre liste de modifications mises en attente. Par exemple, pour réappliquer et supprimer les dernières modifications mises en attente, vous pouvez utiliser la commande suivante : `git stash pop`

- `git stash drop` : Cette commande permet de supprimer une modification mise en attente de la liste des modifications mises en attente. Elle peut être utilisée pour supprimer une modification mise en attente dont vous n'avez plus besoin. Par exemple, pour supprimer la dernière modification mise en attente, vous pouvez utiliser la commande suivante : `git stash drop`

## Référencer un dépôt distant et synchroniser l'historique de versions

- `git remote` : Cette commande permet de gérer les connexions à d'autres dépôts distants. Elle peut être utilisée pour ajouter un dépôt distant à votre dépôt local en utilisant la sous-commande add, comme dans l'exemple suivant : `git remote add origin https://github.com/user/repo.git`

`git fetch` : Cette commande permet de télécharger les commits et les objets associés à partir d'un dépôt distant, sans les fusionner dans votre branche courante. Elle est souvent utilisée pour récupérer les modifications apportées par d'autres personnes au dépôt distant et les préparer pour une fusion ultérieure avec git merge. Par exemple, pour télécharger les commits du dépôt distant nommé origin, vous pouvez utiliser la commande suivante : `git fetch origin`

`git pull` : Cette commande permet de récupérer et de fusionner les commits d'un dépôt distant dans votre branche courante. Elle est souvent utilisée pour synchroniser votre dépôt local avec le dépôt distant et intégrer les modifications apportées par d'autres personnes. Par exemple, pour récupérer et fusionner les commits du dépôt distant nommé origin dans votre branche courante, vous pouvez utiliser la commande suivante : `git pull origin`

`git push` : Cette commande permet de publier les commits de votre dépôt local sur un dépôt distant.