# (S)passoUno

Uno speciale tavolo da riprese per creare cortometraggi animati con la tecnica dell’animazione stop-motion.

## Interfaccia e comandi

### Tastiera
Di seguito i comandi che possono essere utilizzati da tastiera:

| TASTIERA | FUNZIONE | GPIO RASPBERRY PI | UI |
|------------ | ------------- | ----------- | ------ |
SPACE_KEY | Take a snapshot | GPIO 2 | Big Red Button
DOWN_KEY | Accelerate preview | GPIO 4 | Pink Button
UP_KEY | Decelerate preview | GPIO 3 | Yellow Button
D_KEY | Delete session (new session) | NC | NC
X_KEY | Delete a frame | GPIO 27 | Black Button
M_KEY | Make video | GPIO 17 | Green Button
G_KEY | Make animated GIF (not implemented) | NC | NC
Q_KEY | Quit | NC | NC
F_KEY | Toggle fullscreen | NC | NC
PLUS_KEY | Zoom preview in | NC | NC
MIN_KEY | Zoom preview out | NC | NC

### Setup (S)passouno Singolo

![Spasso Uno Singolo](/design/graphics/singolo.png)

### Setup (S)passouno Piovra Mode (Maker Faire Rome 2019)

![Spasso Uno Multiplo](/design/graphics/multiplo.png)

### RJ45 Pin Mapping

![RJ45 Pin Mapping](/design/graphics/RJ45-Pin-Mapping.png)


Design: [Design folder](https://github.com/OfficineArduinoTorino/spassouno-py/tree/master/design)
