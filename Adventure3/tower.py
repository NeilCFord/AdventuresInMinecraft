# Adventure 3: tower.py

# From the book: "Adventures in Minecraft"
# written by David Whale and Martin O'Hanlon, Wiley, 2014
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-111894691X.html
#
# This program builds a tall tower inside Minecraft, using a for loop.

# Import necessary modules
import mcpi.minecraft as minecraft

# Constants for the various block types
STONE = 1

# Connect to the Minecraft game
mc = minecraft.Minecraft.create()

# Get the player position
x, y, z = mc.player.getTilePos()

# Build a tower 50 blocks high
for a in range(50):
    # Each block is at height: y+a
    mc.setBlock(x+3, y+a, z, STONE)

# END
