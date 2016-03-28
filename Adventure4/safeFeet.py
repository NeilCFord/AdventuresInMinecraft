# Adventure 4: safeFeet.py

# From the book: "Adventures in Minecraft"
# written by David Whale and Martin O'Hanlon, Wiley, 2014
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-111894691X.html
#
# This program works out if your feet are safe or not.
# If you are in the air or in water, your feet are not safe.

# Import necessary modules
import mcpi.minecraft as minecraft
import time

# Constants for the block types
AIR = 0
FLOWING_WATER = 8
WATER = 9

# Connect to the Minecraft game
mc = minecraft.Minecraft.create()

# Define a function to decide if your feet are safe or not
# This function will be reusable in other programs
def safeFeet():
  # Get the players position
  x, y, z = mc.player.getTilePos()

  # Get the block directly below your player
  b = mc.getBlock(x, y-1, z)

  # Is the player safe?
  if b == AIR or b == WATER or b == FLOWING_WATER:
    mc.postToChat("not safe")
  else:
    mc.postToChat("safe")

# Game loop
while True:
  # Run the game loop once every half a second
  time.sleep(0.5)
  # Check if your feet are safe
  safeFeet()

# END
