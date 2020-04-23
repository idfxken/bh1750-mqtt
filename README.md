# bh1750-mqtt
Simple python script to push bh1750 lux values to mqtt

```
Needed packages :apt install python-pip
needed python packages: pip install configparser paho-mqtt smbus
``` 


## Special variables in config. ini

### Define your pi model:

pitype: 
pitype = 0 raspberry pi 1
pitype = 1 raspberry pi 2/3/4

### Setting the lux resolution: 
set luxres to one of the following modes:

#### Start measurement at 4lx resolution. Time typically 16ms.
0x13
#### Start measurement at 1lx resolution. Time typically 120ms
0x10
#### Start measurement at 0.5lx resolution. Time typically 120ms
0x11
#### Start measurement at 1lx resolution. Time typically 120ms
#### Device is automatically set to Power Down after measurement.
0x20
#### Start measurement at 0.5lx resolution. Time typically 120ms
#### Device is automatically set to Power Down after measurement.
0x21
#### Start measurement at 1lx resolution. Time typically 120ms
#### Device is automatically set to Power Down after measurement.
0x23

