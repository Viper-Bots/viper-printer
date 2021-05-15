Viper Printer
=============

![Viper printer image](https://github.com/Viper-Bots/viper-printer/blob/main/png/printer-for-repo.png)

In summer 2017, our coach disassembled our EV3 robot ViperEvie and built an EV3-powered dot-matrix printer.

Learn more about the process of creating the printer by reading [our coach's blog post](https://www.joshrenaud.com/family/archives/2017/07/building-a-lego-dot-matrix-printer.html).


How to use this repository
--------------------------

1. Build your own Viper Printer from Lego parts using this LXF file in Lego Digital Designer or Stud.io: [viper-printer.lxf](https://github.com/Viper-Bots/viper-printer/blob/main/lxf/viper-printer.lxf)

2. [Install the ev3dev](https://www.ev3dev.org/docs/getting-started/) operating system on your EV3 brick. Follow the tutorial to set up networking and SSH access on your brick.

(This repo has been tested using the `ev3dev-stretch-ev3-generic-2020-04-10` version of ev3dev)

3. Clone this repo to your brick, then change to the new viper-printer directory:

```
git clone https://github.com/Viper-Bots/viper-printer.git
cd viper-printer
```

4. Install the `PurePNG` 

```
mkdir purepng; cd purepng
curl -LO https://raw.githubusercontent.com/Scondo/purepng/master/png/png.py
touch __init__.py
cd ..
```

(This is an old fork of pypng, but it does work with Python3 in ev3dev)

5. Now you're ready to try the scripts in this repo.


What's included?
----------------

This repository contains several Python scripts related to the Viper Printer:

1. `printer.py` - This is the printer script, and probably the only file in this repo you need. To specify a PNG image to print, use the `-f` command line argument:

```
python printer.py -f myimage.png
```

2. `reset-motors.py` - Utility script to reset all three motors. 

3. `read-image.py` - A simple script our coach wrote to help him understand how the `png` library parses individual PNG images. It iterates over each row of pixels, and prints the data for each pixel to the console. To specify a PNG image, use the `-f` command line argument:

```
python read-image.py -f myimage.png
```


About the Viper Bots
--------------------
The Viper Bots are an [FLL](https://firstlegoleague.org) robotics team from Ferguson, Missouri. As of the 2020-21 RePLAY season, we have five team members ages 10-13.
