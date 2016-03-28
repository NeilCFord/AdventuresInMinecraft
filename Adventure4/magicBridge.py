# Adventure 4: MagicBridge.py

# From the book: "Adventures in Minecraft"
# written by David Whale and Martin O'Hanlon, Wiley, 2014
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-111894691X.html
#
# This program builds a bridge under your feet as you walk around.

# Import necessary modules
import mcpi.minecraft as minecraft

# Constants for the block types
AIR = 0
FLOWING_WATER = 8
WATER = 9
GLASS = 20

# Connect to the Minecraft game
mc = minecraft.Minecraft.create()

# Define a function to build a bridge if your feet are not safe
# This function will be reusable in other programs
def buildBridge():
  # Get the players position
  x, y, z = mc.player.getTilePos()

  # Get the block directly below your player
  b = mc.getBlock(x, y-1, z)
  # Is the player unsafe?
  if b == AIR or b == FLOWING_WATER or b==WATER:
    # If unsafe, build a glass block directly under the player
    mc.setBlock(x, y-1, z, GLASS)

# Game loop
while True:
  # There is no delay here, this loop needs to run really fast
  # otherwise your bridge might not build quick enough and you will fall off
  buildBridge()

# END
