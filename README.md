# XPLoader

A .xp file parser for use with libtcod. 

# Demo

Just demonstrates loading a simple .xp file with layers. esc quits, a toggles display of the second layer.

# Use

Copy xp\_loader.py into your project, import xp\_loader, and call load\_xp\_string. Note: By default, .xp files are gzipped, and you'll need to use the gzip library to decompress them first. The code's fairly readable if you want to look at it, and I tried to comment things that aren't obvious. load\_layer\_to\_console makes it easier to load the data into libtcod consoles (root or otherwise). Have fun!

# links

[Screenshot](http://prntscr.com/8c96vo)

[REXPaint](http://rexpaint.blogspot.com/), without which this would have no reason to exist