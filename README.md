# A&D Pandemiesimulator

> Programmierprojekt im Modul Algorithmen und Datenstrukturen  
> Fakultät für Wirtschaftswissenschaften, Universität Bielefeld  
> Sommersemester 2021

## Abstract

Die Wirksamkeit von Mitteln zur Pandemiebekämpfung wird seit Ausbruch der Corona-Pandemie zu Recht regelmäßig kritisch hinterfragt. Wenn eine bestimmte Maßnahme eine Ansteckung nur in einem von zehn Fällen verhindern kann, erscheint sie uns oft als vernachlässigbar und vom Aufwands-/Nutzenverhältnis her nicht sinnvoll.

Doch dabei laufen wir Gefahr, uns zu sehr auf die direkten Auswirkungen auf uns selbst und den aktuellen Zeitpunkt zu fokussieren. Durch das exponentielle Wachstum der Fallzahlen bei Infektionserkrankungen ist es möglich, dass relativ kleine Veränderungen in der Weiterverbreitungsrate sich schon in kurzer Zeit zu riesigen Unterschieden bei den Gesamtfallzahlen entwickeln können.

Das Gefühl für dieses exponentielle Wachstum fehlt uns jedoch oft, weshalb wir mit unserem Projekt zumindest ganz grob die Auswirkungen von Veränderungen der Weiterverbreitungsrate $R$ auf den Pandemieverlauf, aus einer Makroperspektive betrachtet, approximieren wollen.

## Installation und Benutzung

### Benötigte Software

Um das Projekt starten zu können, werden folgende Runtimes benötigt:

1.  [Node.JS](https://nodejs.org/en/)

2.  [Python oder Anaconda](https://www.python.org/)

### Backend-Bibliotheken

Wechseln Sie in das Verzeichnis `backend/` und installieren Sie die folgenden Libraries:

1.  Flask (entsprechend der [hier](https://flask.palletsprojects.com/en/2.0.x/installation/) verlinkten Anweisungen)

2.  Flask-CORS (mit dem Befehl `pip install -U flask-cors`)

### Frontend-Bibliotheken

Navigieren Sie nun in den Ordner `frontend/`. Die benötigten Libraries sind bereits in der Datei `package.json` gespeichert und können automatisiert installiert werden:

1.  Führen Sie im Terminal `npm install` aus, um alle benötigten Libraries zu installieren

### Starten der Anwendung

1.  Wechseln Sie in das Verzeichnis `backend/`
2.  Starten Sie das Backend mit dem Kommando `flask run`
3.  Öffnen Sie ein neues Terminal und navigieren Sie darin zum Verzeichnis `frontend/`
4.  Starten Sie das Frontend mit dem Kommando `npm run dev`

### Nutzung der App

1.  Starten Sie einen beliebigen Browser und navigieren Sie zur URL [http://localhost:3000](http://localhost:3000)

2.  Daraufhin öffnet sich die App und Sie können die gewünschten
    Eingaben durchführen


