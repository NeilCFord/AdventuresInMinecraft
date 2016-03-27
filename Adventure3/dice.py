# Adventure 3: dice.py

# From the book: "Adventures in Minecraft"
# written by David Whale and Martin O'Hanlon, Wiley, 2014
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-111894691X.html
#
# This program builds the face of a dice near your player.

# Import necessary modules
import mcpi.minecraft as minecraft

# Constants for the various block types
STONE = 1

# Connect to the Minecraft game
mc = minecraft.Minecraft.create()

# Get the player position
x, y, z = mc.player.getTilePos()

# Create 6 blocks in front of the player, that look like a dice
mc.setBlock(x+3, y,   z,   STONE)
mc.setBlock(x+3, y+2, z,   STONE)
mc.setBlock(x+3, y+4, z,   STONE)
mc.setBlock(x+3, y,   z+4, STONE)
mc.setBlock(x+3, y+2, z+4, STONE)
mc.setBlock(x+3, y+4, z+4, STONE)

# END
