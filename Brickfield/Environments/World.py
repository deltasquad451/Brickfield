'''
Created on Jun 10, 2014

@author: lando
@summary: Attempt at block game taken from:
http://studentgamedev.blogspot.no/2013/08/unity-voxel-tutorial-part-1-generating.html
'''
import numpy as np
import Chunk
from noise import snoise3
from direct.directbase import DirectStart
from panda3d.core import *
from noise import pnoise3
from random import randint
class World(object):
    '''
    World Class
    '''
    worldX = 128
    worldY = 128
    worldZ = 32
    chunkSize = 16

    def __init__(self):
        '''
        Constructor
        '''
        self.data = np.zeros([self.worldX,self.worldY,self.worldZ], dtype=int)

        for x in range(0,self.worldX):
            for y in range(0,self.worldY):
                for z in range(0,self.worldZ):
                    zVal = randint(0,3)
                    if(z<=zVal):
                        self.data[x][y][z] = 1 #for now all blocks below 1 will be stone, aka 1

    def PerlinNoise(self, x, y, z, scale, height, power):
        rValue = 0

    def Block(self, x, y, z):
        if(x>= self.worldX or x < 0 or y >= self.worldY or y < 0 or z >= self.worldZ or z < 0):
            return 1
        else:
            return self.data[x][y][z]

    def GenWorld(self):
#         testChunk = Chunk.Chunk(self)
#         testChunk.chunkSize = self.chunkSize
#         testChunk.chunkX = 0
#         testChunk.chunkY = 0
#         testChunk.chunkZ = 0
#         testChunk.GenerateMesh(render)
#
#         testChunk1 = Chunk.Chunk(self)
#         testChunk1.chunkSize = self.chunkSize
#         testChunk1.chunkX = 0
#         testChunk1.chunkY = 16
#         testChunk1.chunkZ = 0
#         testChunk1.GenerateMesh(render)
#         print render.getNumChildren()
#         print render.getChildren()
        self.chunks = np.empty([self.worldX/self.chunkSize,self.worldY/self.chunkSize,
                                self.worldZ/self.chunkSize],dtype=Chunk.Chunk)
        xCord = self.worldX/self.chunkSize
        yCord = self.worldY/self.chunkSize
        zCord = self.worldZ/self.chunkSize
        print xCord
        print yCord
        print zCord
        for x in range(0,xCord):
            for y in range(0,yCord):
                for z in range(0,zCord):

                    self.chunks[x][y][z] = Chunk.Chunk(self)
                    self.chunks[x][y][z].chunkSize = self.chunkSize
                    self.chunks[x][y][z].chunkX = x*self.chunkSize
                    self.chunks[x][y][z].chunkY = y*self.chunkSize
                    self.chunks[x][y][z].chunkZ = z*self.chunkSize
                    self.chunks[x][y][z].GenerateMesh(render)


if __name__ == '__main__':
    worldTest = World()
    worldTest.GenWorld()
    slight = Spotlight('slight')
    slight.setColor(Vec4(1, 1, 1, 1))
    slnp1= render.attachNewNode(slight)
    render.setLight(slnp1)
    slnp1.setPos(0,0,1000)
    slnp1.lookAt(Point3(50, 0, 0))
    run()






