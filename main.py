import numpy as np
import pygame
import sys
import jrpy as jrpy


Particles = []
Nx = 64
Ny = 36
x = np.linspace(-0.1,1.1,Nx)
y = np.linspace(-0.1,1.1,Ny)
X,Y = np.meshgrid(x,y)
X = X.flatten()
Y = Y.flatten()
pos = np.zeros([Nx*Ny,2])
pos[:,0] = X*1280
pos[:,1] = Y*720
Particles = jrpy.swarm(pos,5,mu=5,a=100,rgb=(255,255,255))
#for i in range(Nx*Ny):
#    pos = np.array([X[i],Y[i]])*np.array([1280,720])
#    r = 5
#    Particles.append(jrpy.particle(pos, r, trail_len=2, a=1 ,mu=0.005,rgb=(255,255,255)))
# Initialize Pygame
player = jrpy.player(np.array([640,360]), radius=5, rgb=(255,0,0), mu=5, trail_len=15)

pygame.init()

a = 1.0     # Length of the box

# Time parameters
dt = 0.01         # Time step
total_time = 2  # Total simulation time
steps = int(total_time / dt)

# Pygame window settings
width, height = 1280, 720  # Window size
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('JRPY')

# Scaling factors
x_scale = width / (a)
y_scale = height * 0.8  # Scale to 80% of window height
y_offset = height   # Center vertically

# Color settings
background_color = (0, 0, 0, 255)  # Black

# Font settings
font = pygame.font.SysFont('Arial', 20)

# Main simulation loop
running = True
clock = pygame.time.Clock()
step = 0
steps = 2000
t = np.linspace(0,2*np.pi,int(steps/2))
fx = 10*np.sin(t)
fy = 10*np.cos(t)

fx_reverse = -fx[::-1]
fy_reverse = -fy[::-1]

fx = np.append(fx,fx_reverse)
fy = np.append(fy,fy_reverse)

while running:

    # Manejo de eventos
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (event.type==pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
            break
    jrpy.movement(player)

    # Clear the screen
    screen.fill(background_color)

#    for particle in Particles:
#        particle.move(player,dt)
#        particle.draw(screen)
    Particles.move(player,dt)
    Particles.draw(screen)
    #if step<steps:
        #player.forces = np.array([fx[step],fy[step]])
    #if step==steps:
        #player.forces = np.array([0.0,0.0])
    player.move(dt)
    if player.pos[0]<0+player.r:
        player.forces[0] = 0
    if player.pos[1]<0+player.r:
        player.forces[1] = 0
    if player.pos[0]>width-player.r:
        player.forces[0] = 0
    if player.pos[1]>height-player.r:
        player.forces[1] = 0
    player.draw(screen)
    # Display time
    time_text = font.render(f'Time: {step * dt:.5f} s', True, (255, 255, 255))
    screen.blit(time_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)  # Limit to 60 FPS

    step += 1

# Quit Pygame
pygame.quit()
sys.exit()
