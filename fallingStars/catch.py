# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 09:31:23 2024

@author: chris
"""
import pygame, random, simpleGE

class Wish(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("wishyStar.png")
        self.setSize(50, 50)
        self.reset()
    
    def reset(self):
        self.y = 10
        self.x = random.randint(0, self.screenWidth)
        self.dy = random.randint(1, 8)
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()
        


class Bunny(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("seaBunny.png")
        self.setSize(100, 100)
        self.position = (320, 430)
        self.moveSpeed = 7
        
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed


class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.background.fill((18, 22, 41))
        self.setImage("night.PNG")
        
        self.bunny = Bunny(self)
        self.wishes = []
        for i in range(15):
            self.wishes.append(Wish(self))
        
        self.sprites = [self.bunny, self.wishes]
    
    def process(self):
        for wish in self.wishes:
            if self.bunny.collidesWith(wish):
                wish.reset()
            
def main():
    pygame.display.set_caption("Collect the falling stars and make these ethereal wishes a reality.")
    game = Game()
    game.start()

if __name__ == "__main__":
    main()