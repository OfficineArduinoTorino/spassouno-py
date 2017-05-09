#(S)passoUno

[github.com/OfficineArduinoTorino/spassouno-py](https://github.com/OfficineArduinoTorino/spassouno-py)

![SpassoUno](http://tongatron.it/img/spassuno-preview.png)

Uno speciale tavolo da riprese per creare cortometraggi animati con la tecnica dell’animazione stop-motion. 

(S)passoUno è basato su Python 2.7 e testato su Raspberry Pi 3 con distribuzione Minibian "Jessie" con LXDE GUI.

Componenti (S)passoUno:		
- Raspberry Pi 3		
- Raspberry camera		

Componenti Interfaccia Kids:		
- 1 genuino micro		
- 1 Big red button	
- 4 pulsanti arcade	
- 1 Buzzer	
- 5 resistenze da 10 KΩ	


##Sistema operativo
Scarica l'ultima versione del sistema operativo Minibian "Jessie": [minibianpi.wordpress.com/download](https://minibianpi.wordpress.com/download/)

Per creare il sistema su microSD puoi seguire [questa procedura](https://minibianpi.wordpress.com/setup/).

per installare l'ambiente grafico puoi seguire [questa guida](https://www.therryvanneerven.nl/how-to-install-raspbian-jessie-on-an-old-raspberry-pi.html)

##Installa (S)passoUno e le librerie necessarie

Ottieni l'accesso come amministratore:
```bash
sudo su
```
inserisci come password: 'raspberry'

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

Imposta spasso uno in autoavvio
'''bash
sudo mv autostart.sh /etc/init.d/
chmod +x /etc/init.d/autostart.sh 
sudo update-rc.d autostart.sh defaults
'''

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

Installa la libreria pygame:
```bash
apt-get install python-pygame
```

Installa la libreria imagemagick per salvare su usb e automount per montare le chiavette usb automaticamente:
```bash
apt-get install python-pygame
```

```bash
apt-get install usbmount
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

Posizionati nella cartella del repository:
```bash
cd /opt/spassouno-py
```
Lancia il programma:
```bash
python spassouno.py
```

####Ops, qualcosa non funziona?

![almeno ci hai provato](http://dailycentral.me/wp-content/uploads/2015/06/at-least-you-tried-656x487.png)

##Interfaccia e comandi
###Tastiera
Di seguito i comandi che possono essere utilizzati da tastiera:

TASTIERA | FUNZIONE
------------ | -------------
SPACE_KEY | Take a snapshot
DOWN_KEY | Accelerate preview
UP_KEY | Decelerate preview
D_KEY | Delete session (new session)
X_KEY | Delete a frame
M_KEY | Make video (not implemented)
G_KEY | Make animated GIF (not implemented)
Q_KEY | Quit
F_KEY | Toggle fullscreen
PLUS_KEY | Zoom preview in
MIN_KEY | Zoom preview out


###Interfaccia Kids
Abbiamo costruito un'interfaccia semplice e intuitiva per i bambini:


![SpassoUno](http://tongatron.it/img/spassouno-interfaccia.png)

INTERFACCIA KIDS | FUNZIONE
------------- | -------------
Aggiungi fotogramma| Take a snapshot
Diminuisci velocità| Accelerate preview
Aumenta velocità| Decelerate preview
Nuova storia| Delete session (new session)
Cancella ultimo fotogramma| Delete a frame


Circuito: [123d.circuits.io](https://123d.circuits.io/circuits/1926939-spassunouno-kids-interface)	
Arduino sketch: [ArduinoSpassoUno.ino](https://github.com/OfficineArduinoTorino/spassouno-py/tree/master/arduinoSpassoUno)	
Design: [Design folder](https://github.com/OfficineArduinoTorino/spassouno-py/tree/master/design)
