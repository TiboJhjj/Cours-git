# Cours-git

1.6 Démarrage rapide - Paramétrage à la première utilisation de Git
Paramétrage à la première utilisation de Git
Maintenant que vous avez installé Git sur votre système, vous voudrez personnaliser votre environnement Git. Vous ne devriez avoir à réaliser ces réglages qu’une seule fois ; ils persisteront lors des mises à jour. Vous pouvez aussi les changer à tout instant en relançant les mêmes commandes.

Git contient un outil appelé git config pour vous permettre de voir et modifier les variables de configuration qui contrôlent tous les aspects de l’apparence et du comportement de Git. Ces variables peuvent être stockées dans trois endroits différents :

[chemin]/etc/gitconfig : Contient les valeurs pour tous les utilisateurs et tous les dépôts du système. Si vous passez l’option --system à git config, il lit et écrit ce fichier spécifiquement. Parce que c’est un fichier de configuration au niveau système, vous aurez besoin de privilèges admnistrateur ou super-utilisateur pour le modifier.

Fichier ~/.gitconfig : Spécifique à votre utilisateur. Vous pouvez forcer Git à lire et écrire ce fichier en passant l’option --global et cela affecte tous les dépôts avec lesquels vous travaillez sur ce système.

Fichier config dans le répertoire Git (c’est-à-dire .git/config) du dépôt en cours d’utilisation : spécifique au seul dépôt en cours. Vous pouvez forcer Git à lire et écrire dans ce fichier avec l’option --local`, mais c’est en fait l’option par défaut. Sans surprise, le répertoire courant doit être dans un dépôt Git pour que cette option fonctionne correctement.

Chaque niveau surcharge le niveau précédent, donc les valeurs dans .git/config surchargent celles de [chemin]/etc/gitconfig.

Sur les systèmes Windows, Git recherche le fichier .gitconfig dans le répertoire $HOME (%USERPROFILE% dans l’environnement natif de Windows) qui est C:\Documents and Settings\$USER ou C:\Users\$USER la plupart du temps, selon la version ($USER devient %USERNAME% dans l’environnement de Windows). Il recherche tout de même /etc/gitconfig, bien qu’il soit relatif à la racine MSys, qui se trouve où vous aurez décidé d’installer Git sur votre système Windows. Si vous utilisez une version 2.x ou supérieure de Git pour Windows, il y a aussi un fichier de configuration système à C:\Documents and Settings\All Users\Application Data\Git\config sur Windows XP, et dans C:\ProgramData\Git\config sur Windows Vista et supérieur. Ce fichier de configuration ne peut être modifié qu’avec la commande git config -f <fichier> en tant qu’administrateur.

Vous pouvez voir tous vos paramétrages et d’où ils viennent en utilisant :

$ git config --list --show-origin
Votre identité
La première chose à faire après l’installation de Git est de renseigner votre nom et votre adresse de courriel. C’est une information importante car toutes les validations dans Git utilisent cette information et elle est indélébile dans toutes les validations que vous pourrez réaliser :

$ git config --global user.name "John Doe"
$ git config --global user.email johndoe@example.com
Encore une fois, cette étape n’est nécessaire qu’une fois si vous passez l’option --global, parce que Git utilisera toujours cette information pour tout ce que votre utilisateur fera sur ce système. Si vous souhaitez surcharger ces valeurs avec un nom ou une adresse de courriel différents pour un projet spécifique, vous pouvez lancer ces commandes sans option --global lorsque vous êtes dans ce projet.

De nombreux outils graphiques vous aideront à le faire la première fois que vous les lancerez.

Votre éditeur de texte
À présent que votre identité est renseignée, vous pouvez configurer l’éditeur de texte qui sera utilisé quand Git vous demande de saisir un message. Par défaut, Git utilise l’éditeur configuré au niveau système, qui est généralement Vi ou Vim.

Si vous souhaitez utiliser un éditeur de texte différent, comme Emacs, vous pouvez entrer ce qui suit :

$ git config --global core.editor emacs
Sous Windows, si vous souhaitez utiliser un éditeur de texte différent, vous devez spécifier le chemin complet vers son fichier exécutable. Ce chemin dépend de l’installation de votre éditeur de texte.

Dans le cas de Notepad++, un éditeur de texte populaire pour la programmation, vous souhaiterez peut-être utiliser la version 32-bit, car au moment d’écrire ces lignes, la version 64-bit ne supporte pas tous les plug-ins. Si vous êtes sur un Windows 32-bit, ou si vous avez un éditeur 64-bit sur un OS 64-bit, vous utiliserez une commande du type :

$ git config --global core.editor "'C:/Program Files/Notepad++/notepad++.exe' -multiInst -notabbar -nosession -noPlugin"
Note
Vim, Emacs et Notepad++ sont des éditeurs de texte populaires chez les développeurs sur les systèmes à base Unix tels que Linux et macOS. Si vous utilisez un autre éditeur, ou une version 32-bit, veuillez trouver des instructions spécifiques sur la mise en place de votre éditeur favori avec Git dans Commandes git config core.editor.

Avertissement
Si vous ne renseignez pas un éditeur et ne connaissez pas Vim ou Emacs, vous risquez fort d’avoir des surprises lorsque Git tentera de les démarrer. Sous Windows par exemple, l’opération de Git pourrait être terminée prématurément pendant une demande de Git à saisir un texte.

Votre nom de branche par défaut
Par défaut Git crée une branche nommée master quand vous créez un nouveau repository avec git init. Depuis Git version 2.28, vous pouvez définir un nom différent pour la branche initiale.

Pour définir main comme nom de branche par défaut, utilisez la commande :

$ git config --global init.defaultBranch main
Vérifier vos paramètres
Si vous souhaitez vérifier vos réglages, vous pouvez utiliser la commande git config --list pour lister tous les réglages que Git a pu trouver jusqu’ici :

$ git config --list
user.name=John Doe
user.email=johndoe@example.com
color.status=auto
color.branch=auto
color.interactive=auto
color.diff=auto
…
Vous pourrez voir certains paramètres apparaître plusieurs fois car Git lit les mêmes paramètres depuis plusieurs fichiers ([chemin]/etc/gitconfig et ~/.gitconfig, par exemple). Git utilise la dernière valeur pour chaque paramètre unique qu’il lit.

Vous pouvez aussi vérifier la valeur effective d’un paramètre particulier en tapant git config <paramètre> :

$ git config user.name
John Doe
