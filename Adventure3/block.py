# Adventure 3: block.py

# From the book: "Adventures in Minecraft"
# written by David Whale and Martin O'Hanlon, Wiley, 2014
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-111894691X.html
#
# This program builds a block next to your player.

# Import necessary modules
import mcpi.minecraft as minecraft

# Connect to the Minecraft game
mc = minecraft.Minecraft.create()

# Create constant for STONE block
STONE = 1

# Get the player position
x, y, z = mc.player.getTilePos()

# Create a block in front of the player
mc.setBlock(x+3, y, z, STONE)

# END
