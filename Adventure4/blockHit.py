# Adventure 4: blockHit.py

# From the book: "Adventures in Minecraft"
# written by David Whale and Martin O'Hanlon, Wiley, 2014
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-111894691X.html
#
# This program senses that a block has been hit.

# Import necessary modules
import mcpi.minecraft as minecraft
import time

# Constant for block type
DIAMOND_BLOCK = 57

# Connect to the Minecraft game
mc = minecraft.Minecraft.create()

# Work out the position of the player
diamond_x,  diamond_y, diamond_z = mc.player.getTilePos()

# Move the diamond slightly away from the player position
diamond_x = diamond_x + 1

# Build a diamond treasure block
mc.setBlock(diamond_x, diamond_y, diamond_z, DIAMOND_BLOCK)

# Define a function that checks if the diamond treasure has been hit
# You can reuse this function in other programs
def checkHit():
  # Get a list of hit events that have happened
  events = mc.events.pollBlockHits()

  # Process each event in turn
  for e in events:
    # Get the coordinate that the hit happened at
    x, y, z = e.pos

    # If the diamond was hit
    if x == diamond_x and y == diamond_y and z == diamond_z:     
      mc.postToChat("HIT")

# Game loop
while True:
  # Run the game loop once every second
  # Don't run it too fast or your computer might crash
  time.sleep(1)

  # Check to see if the diamond treasure has been hit
  checkHit()

# END
