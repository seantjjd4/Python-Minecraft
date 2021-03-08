# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

print(mc.player.getTilePos())


mc.setTilePos(125,60,60)


x = 123
y = 60
z = 30
mc.player.setTilePos(x,y,z)


