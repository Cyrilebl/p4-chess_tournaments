<div align="center">
  <img src="src/images/chess.png" alt="Chess Image">
</div>

# Chess Tournament Application

Écrit en Python, cette application permet de gérer facilement des tournois d'échecs via une interface en ligne de commande. Il permet d'organiser des tournois selon le modèle suisse, incluant la gestion des joueurs et le suivi des résultats.
Ce programme est conçu pour être utilisé directement depuis la console, sans nécessiter de connexion Internet.

## 1. Initialisation du projet

### Windows :

Récupération du projet

```
$ git clone https://github.com/Cyrilebl/p4-chess_tournaments.git
```

Créez et activez l'environnement virtuel

```
$ cd p4-chess_tournaments
$ python -m venv env
$ ~env\Scripts\activate
```

Installez les dépendances listées dans `requirements.txt`.

```
$ pip install -r requirements.txt
```

Exécutez le programme

```
$ python main.py
```

### MacOS et Linux :

Récupération du projet

```
$ git clone https://github.com/Cyrilebl/p4-chess_tournaments.git
```

Créez et activez l'environnement virtuel

```
$ cd p4-chess_tournaments
$ python3 -m venv env
$ source env/bin/activate
```

Installez les dépendances listées dans `requirements.txt`.

```
$ pip install -r requirements.txt
```

Exécutez le programme

```
$ python3 main.py
```

## 2. Générer un rapport flake8

Exécutez la commande suivante :

```
flake8 src/ main.py
```

Le rapport sera généré dans le dossier `flake8_report`.
