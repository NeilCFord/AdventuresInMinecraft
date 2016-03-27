# Adventure 3: clearSpace.py

# From the book: "Adventures in Minecraft"
# written by David Whale and Martin O'Hanlon, Wiley, 2014
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-111894691X.html
#
# This program clears some space near your player.
# This is so that it is then easier for you to build other things.

# Import necessary modules
import mcpi.minecraft as minecraft

# Constants for the various block types
AIR = 0

# Connect to the Minecraft game
mc = minecraft.Minecraft.create()

# Get the player position
x, y, z = mc.player.getTilePos()

# Ask the user how big a space to clear
size = int(input("size of area to clear? "))

# Clear a space size by size*size*size, by setting it to AIR
# positioned around the player's current position
mc.setBlocks(x-size/2, y, z-size/2, x+size/2, y+size, z+size/2, AIR)

# END
