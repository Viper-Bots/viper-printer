Viper Printer, v3.0
===================

![Viper printer image](https://github.com/Viper-Bots/viper-printer/blob/main/jpg/printer1-for-repo.jpg)

In June 2021, our coach redesigned his old EV3-powered dot-matrix printer project from 2017. The latest version of the printer is v3.0.

Learn more about the redesign of the printer by reading [our coach's blog post](https://www.joshrenaud.com/family/archives/2021/06/revisiting-my-dot-matrix-ev3-lego-printer.html).

This repo has been tested with Python 3 and the `ev3dev-stretch-ev3-generic-2020-04-10` version of ev3dev.


How to use this repository
--------------------------

1. Build your own Viper Printer from Lego parts using this LXF file in Lego Digital Designer or Stud.io: [viper-printer.lxf](https://github.com/Viper-Bots/viper-printer/blob/main/lxf/viper-printer.lxf) (Note: this model requires a large number of parts 3743 and 64179)

2. [Install the ev3dev](https://www.ev3dev.org/docs/getting-started/) operating system on your EV3 brick. Follow the tutorial to set up networking and SSH access on your brick.

3. Clone this repo to your brick, then change to the new viper-printer directory:

```
git clone https://github.com/Viper-Bots/viper-printer.git
cd viper-printer
```

4. Install the `PurePNG` library.

```
mkdir purepng
cd purepng
curl -LO https://raw.githubusercontent.com/Scondo/purepng/master/png/png.py
touch __init__.py
cd ..
```

5. Now you're ready to try the scripts in this repo.


What's included?
----------------

This repository contains one Python script for running the Viper Printer:

1. `printer.py` - This is the printer script, and probably the only file in this repo you need. To specify a PNG image to print, use the `-f` command line argument:

```
python3 printer.py -f png/cartoon.png
```


Notes on construction
---------------------

The key difference between the v3.0 build of the printer and previous versions is the use of gear-driven racks on Technic bricks, instead of the tank tread belt mechanism. 

There are two Technic brick/rack stacks. Each one fits inside a sandwich of liftarm 5x7 frames. 

The longer of these brick/rack stacks serves as the "print head track," with a parallel track of beams underneath it to support the weight of the print head.  These two tracks are separated by a vertical space of two plates.

![Viper printer image](https://github.com/Viper-Bots/viper-printer/blob/main/jpg/printer1-for-repo.jpg)

Unfortunately this vertical space is _slightly_ smaller than the height of a beam, so Lego Digital Designer and Stud.io will not allow me to build a model where the print head is actually on the print head track. For this reason, the .LXF and .IO files include all the parts, but the print head is shown assembled separately from the print head track. 

We advise you to use the photos in this repo to see how it all fits together.



Caveats
-------

For best results, you need to convert or draw your own 1-bit (black and white) PNG images. You can convert photos using Photoshop, Gimp, or other image editing tools. The scripts in this repo do NOT convert, color-correct, or optimize PNG images.

Here's an example of how to convert photos to bitmaps in Photoshop:

1. Change the image to grayscale by selecting `Image` > `Mode` > `Grayscale`.

2. Reduce the image width to 200px.

3. Use `Image` > `Adjustments` > `Levels` to tweak the contrast in the image.

4. Reduce the image width to 100px.

5. Change the image to bitmap by selecting `Image` > `Mode` > `Bitmap`. In the “Method” dropdown, try “diffusion dither" or “halftone."



Notes
-----

In the future, we may revise `printer.py` to work with the normal `pypng` library, rather than `PurePNG`, which is an old, unsupported fork. 

We also hope to add a Python script that can be used to precisely align print head vertically. This future script would allow the user to complete the alignment process using a touch sensor.



About the Viper Bots
--------------------
The Viper Bots are an [FLL](https://firstlegoleague.org) robotics team from Ferguson, Missouri. As of the 2020-21 RePLAY season, we have five team members ages 10-13.
