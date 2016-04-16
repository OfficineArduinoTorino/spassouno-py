#(S)passoUno

[Github.com/OfficineArduinoTorino/spassouno-py](https://github.com/OfficineArduinoTorino/spassouno-py)

![SpassoUno](http://tongatron.it/img/spassuno-preview.png)

Usando uno speciale tavolo da riprese per creare cortometraggi animati con la tecnica dell’animazione stop-motion. 

(S)passoUno è basato su Python 2.7 e testato su Raspberry Pi 3 con distribuzione Minibian "Jessie".

##Interfaccia e comandi
Interfaccia kids:
![SpassoUno](http://tongatron.it/img/spassouno-interfaccia.png)

TASTIERA | INTERFACCIA KIDS | FUNZIONE
------------ | ------------- | -------------
SPACE_KEY | Aggiungi fotogramma| Take a snapshot
DOWN_KEY | Dominuisci velocità| Accelerate preview
UP_KEY | Aumenta velocità| Decelerate preview
D_KEY | Nuova storia| Delete session (new session)
X_KEY | Cancella ultimo fotogramma| Delete a frame
M_KEY || Make video (not implemented)
G_KEY || Make animated GIF (not implemented)
Q_KEY || Quit
F_KEY || Toggle fullscreen
PLUS_KEY || Zoom preview in
MIN_KEY || Zoom preview out



##Sistema operativo
Scarica l'ultima versione del sistema operativo Minibian "Jessie": [minibianpi.wordpress.com/download](https://minibianpi.wordpress.com/download/)

Per creare il sistema su microSD puoi seguire [questa procedura](https://minibianpi.wordpress.com/setup/).

##Installa (S)passoUno e le librerie necessarie

Aggiorna l'indice dei pacchetti del sistema:
```bash
apt-get update
```
Installa il tool di configurazione `raspi-config`:
```bash
apt-get install raspi-config
```

Accedi al tool di configurazione raspi-config per abilitare la camera (`expand filesystem`) ed espandere lo spazio su disco (`enable camera`):
```bash
raspi-config
```

Installa Git:
```bash
apt-get install git
```

Posizionati nella cartella opt:
```bash
cd /opt
```

Scarica il repository di (S)passoUno:
```bash
git clone https://github.com/OfficineArduinoTorino/spassouno-py.git
```
Installa Python:
```bash
apt-get install python-pip python-dev
```
Installa la libreria libjpeg62:
```bash
apt-get install libjpeg62-turbo-dev
```

```bash
apt-get install libjpeg8-dev libjpeg-dev
```
In caso di errori, prova ad eseguire il comando come amministratore:  `sudo apt-get install libjpeg8-dev libjpeg-dev`

Installa zlib1g:
```bash
apt-get install zlib1g-dev
```
Installa Pillow:
```bash
pip install pillow
```
Installa Picamera:
```bash
pip install picamera
```

##Lancia (S)passoUno!

Scarica il software da qui: [github.com/vongomben/spassouno](https://github.com/vongomben/spassouno)    

Posizionati nella cartella del repository:
```bash
cd /opt/spassouno-py
```
Lancia il programma:
```bash
python spassouno.py
```

##Ops, qualcosa non funziona?

![almeno ci hai provato](http://dailycentral.me/wp-content/uploads/2015/06/at-least-you-tried-656x487.png)