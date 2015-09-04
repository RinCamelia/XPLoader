import libtcodpy as libtcod
import xp_loader
import gzip

####################
# load in and read the .xp file - this is done out-of-library in case you have some other means to produce an uncompressed .xp data string
####################

xp_file = gzip.open('xptest.xp')
raw_data = xp_file.read()
xp_file.close()

xp_data = xp_loader.load_xp_string(raw_data)

screen_width = xp_data['width']
screen_height = xp_data['height']
limit_fps = 20

####################
# The default libtcod font sheet format is missing quite a few codepage 437 characters - if you want to use REXPaint, you'll need to find or make make a sprite sheet with those characters
# Currently using the 10x10 default REXPaint sheet courtesy of Kyzrati
####################

libtcod.console_set_custom_font('cp437_10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_ASCII_INROW)
libtcod.console_init_root(screen_width, screen_height, 'REXPaint Import Demo', False)
libtcod.sys_set_fps(limit_fps)

####################
# Loads the layer data to offscreen consoles. You can load a layer to the main console by passing in 0 instead of a console
####################

layer_0_console = libtcod.console_new(xp_data['layer_data'][0]['width'],xp_data['layer_data'][0]['height'])
layer_1_console = libtcod.console_new(xp_data['layer_data'][1]['width'],xp_data['layer_data'][1]['height'])

xp_loader.load_layer_to_console(layer_0_console, xp_data['layer_data'][0])
xp_loader.load_layer_to_console(layer_1_console, xp_data['layer_data'][1])

####################
# Sets the overlay layer transparency key to REXPaint's background transparency key. For completeness purposes, load_layer_to_console always writes every cell to the console - 
# REXPaint format note - layer 0 background is written out as 0,0,0. If you're making .xp files for UI overlays or whatever, be absolutely sure to 
####################

libtcod.console_set_key_color(layer_1_console, libtcod.Color(xp_loader.transparent_cell_back_r, xp_loader.transparent_cell_back_g, xp_loader.transparent_cell_back_b))


####################
# libtcod piping to actually put the console layers on screen. This will probably change quite a bit for your actual usage of libtcod
####################

draw_layers = False

while not libtcod.console_is_window_closed():

	key = libtcod.console_check_for_keypress()
	if key.vk == libtcod.KEY_ESCAPE:
		break  #exit game
	
	if key.c == ord('a'):
		draw_layers = not draw_layers

	libtcod.console_clear(0)
	libtcod.console_blit(layer_0_console, 0, 0, xp_data['layer_data'][0]['width'], xp_data['layer_data'][0]['height'], 0,0, 0)

	if draw_layers:
		libtcod.console_blit(layer_1_console, 0, 0, xp_data['layer_data'][1]['width'], xp_data['layer_data'][1]['height'], 0, 0, 0)
	libtcod.console_flush()

libtcod.console_delete(layer_0_console)
libtcod.console_delete(layer_1_console)