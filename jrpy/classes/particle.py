import pygame
import jrpy
import numpy as np

class particle:
    def __init__(self, pos, radius, a=1, mu=1.0, rgb=[0,0,0], trail_len=2):
        """
        :param pos: Particle positions, np.array([x,y,[z]])
        :param vel: Particle velocity,  np.array([vx,vy,[vz]])
        :param radio: Particle radius,  float
        :param rgb:  Color in rgb format
        """
        self.pos   = pos
        self.trail = [tuple(pos.copy())]*trail_len
        self.vel   = pos*0
        self.r     = radius
        self.color = rgb
        self.mu    = mu
        self.a     = a

    def mu_rpy(self,other):
        return jrpy.mu_rpy(self.pos,other.pos,a=self.a)

    def interact(self,other):
        muF = np.einsum('...ij,...j->...i', self.mu_rpy(other), other.forces)
        self.vel = self.mu*muF

    def move(self, other, dt):
        self.interact(other)
        self.pos = self.pos + self.vel*dt
        self.trail.pop(0)
        self.trail.append(tuple(self.pos.copy()))

    def draw(self,surface):
        """
        :param surface: surface to draw on
        """
        pygame.draw.circle(surface, self.color, self.pos, self.r)
        pygame.draw.lines(surface, self.color, False, self.trail, 2)

    def __str__(self):
        """Devuelve una representación en cadena de la partícula."""
        return f"Partícula en ({self.x}, {self.y}) con velocidad ({self.vx}, {self.vy}) y radio {self.radio}"


class player(particle):
    def __init__(self, pos, radius, a=1,vel=np.zeros(2), mu=1.0, rgb=[0,0,0], trail_len=2):
        super().__init__(pos, radius, mu=mu, rgb=rgb,trail_len=trail_len)
        self.forces = np.array([0.0 ,0.0])

    def move(self, dt):
        self.vel    = self.mu*self.forces
        self.pos    = self.pos + self.vel*dt
        self.trail.pop(0)
        self.trail.append(tuple(self.pos.copy()))

    def move_CM(self, swarm, dt):
        self.vel  = self.mu*self.forces
        swarm.pos = swarm.pos - self.vel*dt
        self.trail.pop(0)
        trail_array = np.array(self.trail)
        trail_array = trail_array - self.vel*dt
        self.trail = list(trail_array)
        self.trail.append(self.pos)


class swarm(particle):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.N = np.shape(self.pos)[0]

    def draw(self, surface):
        for i in range(self.N):
            pygame.draw.circle(surface, self.color, self.pos[i], self.r)

