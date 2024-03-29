# OLED Stats

OLED Stats Display Script For Raspberry Pi

The script is pre-configured for 128x64 SPI OLED Display

## Screenshots:

<table align="center" style="margin: 0px auto;">
  <tr>
    <th>stats.py</th>
  </tr>
  <tr>
    <td><img align="right" src="https://i.imgur.com/42kikDA.jpg" height="220"></img></td>
  </tr>
</table>

## Installation Steps:

1. Connect **GND, VCC(3.3v), SCL, & SDA** ports of the display according to the picture shown below:

<img src="https://i.imgur.com/tp1aQ2N.jpg">

```shell
    $ DATA/D1 = 19 black
    $ CLK = 23 white
    $ DC/SA0 = 10 red
    $ RST = 8 brown
    $ CS = 24 orange
    $ 3v3 = X
    $ VCC/3v = 1 grey
    $ GND = 6 purple
```

2. Upgrade your Raspberry Pi firmware and reboot:

```shell
    $ sudo apt-get update
    $ sudo apt-get full-upgrade
    $ sudo reboot
```

3. Install python3-pip, upgrade the setuptools, install psuutil and reboot:

```shell
    $ sudo apt-get install python3-pip
    $ sudo pip3 install --upgrade setuptools
    $ sudo pip install psutil
    $ sudo reboot
```

4. Next, we’re going to install the Adafruit CircuitPython library using the following commands:

```shell
    $ cd ~
    $ sudo pip3 install --upgrade adafruit-python-shell
    $ sudo reboot

    $ wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
    $ sudo python3 raspi-blinka.py
```
5. Now we need to check we have git installed & if not we can install it

```shell
    $ git --version
```

If you don't see a response or it states git: command not found you'll need to follow the steps below.

```shell
    $ sudo apt install git
```

6. Now we know we've got git, we now need to download the python script from our github:

```shell
    $
    $ git clone https://github.com/NBarter94/RPi4-OLED-SPI-Stats.git
    $ cd RPi4-OLED-SPI-Stats
    $ cp stats.py ~/stats.py 

```

7. Now we need to add the script to crontab for startup procedure:

```shell
    $ crontab -e
```

**Add this at the bottom:**

Remember to change your username (pi below) if you're not using the default username

```
    @reboot python3 /home/pi/stats.py &
```

8. At the end DELETE the RPi4-OLED-SPI-Stats folder and reboot

```shell
    $ sudo rm -rf RPi4-OLED-SPI-Stats
    $ sudo reboot
```

<h3><p align="center">THE  END</p></h3>
