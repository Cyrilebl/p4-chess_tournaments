<div align="center">
  <img src="src/images/chess.png" alt="Chess Image">
</div>

# Chess Tournament Application

Gestionnaire de tournois d'échecs.

## Table des matières

1. [Initialisation du projet](#initialisation-du-projet)
   - [Windows](#windows)
   - [MacOS et Linux](#macos-et-linux)
2. [Générer un rapport Flake8](#générer-un-rapport-flake8)
3. [Options des menus](#options-des-menus)
   - [Menu principal](#menu-principal)

## 1. Initialisation du projet

### Windows :

Récupération du projet

```
$ git clone https://github.com/Cyrilebl/p4-chess_tournaments.git
```

Créer et activer l'environnement virtuel

```
$ cd p4-chess_tournaments
$ python -m venv env
$ ~env\Scripts\activate
```

Installer les dépendances listées dans `requirements.txt`.

```
$ pip install -r requirements.txt
```

Exécuter le programme

```
$ python main.py
```

### MacOS et Linux :

Récupération du projet

```
$ git clone https://github.com/Cyrilebl/p4-chess_tournaments.git
```

Créer et activer l'environnement virtuel

```
$ cd p4-chess_tournaments
$ python3 -m venv env
$ source env/bin/activate
```

Installer les dépendances listées dans `requirements.txt`.

```
$ pip install -r requirements.txt
```

Exécuter le programme

```
$ python3 main.py
```

## Générer un rapport flake8

Exécuter la commande suivante :

```
flake8 src/ main.py
```

Le rapport sera généré dans le dossier `flake8_report`.

## Options des menus

### Menu principal

Le menu principal est divisé en 2 options.

1. Gestion des tournois
2. Gestion des joueurs
