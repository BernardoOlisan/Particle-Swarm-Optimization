import pygame 
import numpy as np
from pygame import Rect, Color
from matplotlib import colormaps
import matplotlib.pyplot as plt

WINDOW_SIZE = 500
PARTICLE_SIZE = 5 # px
S = int(WINDOW_SIZE / PARTICLE_SIZE) # Search space
N = 20 # Number of particles

# Hyperparameters
a = 0.729  # Inertia weight (constriction factor)
b = 2.0    # Cognitive coefficient
b_hat = 2.0  # Social coefficient  
c = 0.25    # Step size (usually 1.0, or remove it)

pygame.init()
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
clock = pygame.time.Clock()

cmap = colormaps.get_cmap("inferno")

# Alternative functions you can use:
# Option 1: A Gaussian function
# f = lambda x, y: np.exp(-((x - 50)**2 + (y - 50)**2) / (2 * 20**2))

# Option 2: A product of sines
# f = lambda x, y: np.sin(x/10) * np.sin(y/10)

# Option 3: A "saddle" function
# f = lambda x, y: (x - 50) * (y - 50) / 1000

# Option 4: A circular pattern (distance from center)
f = lambda x, y: np.sqrt((x - 50)**2 + (y - 50)**2)

# Option 5: Checkerboard
# f = lambda x, y: ((x//10) % 2) ^ ((y//10) % 2)

# Option 6: Rastrigin function (highly multimodal, many local optima)
# f = lambda x, y: 20 + (x/10 - 50)**2 + (y/10 - 50)**2 - 10*(np.cos(2*np.pi*(x/10 - 50)) + np.cos(2*np.pi*(y/10 - 50)))

# Option 7: Ackley function (many local optima with exponential terms)
# f = lambda x, y: -20*np.exp(-0.2*np.sqrt(((x/10-50)**2 + (y/10-50)**2)/2)) - np.exp((np.cos(2*np.pi*(x/10-50)) + np.cos(2*np.pi*(y/10-50)))/2) + np.e + 20

# Option 8: Griewank function (many local optima, product term)
# f = lambda x, y: ((x/10-50)**2 + (y/10-50)⁄**2)/4000 - np.cos((x/10-50)/np.sqrt(2))*np.cos((y/10-50)/np.sqrt(3)) + 1
# 
# Option 9: Highly oscillatory multi-peak function
# f = lambda x, y: np.sin(x/3) * np.sin(y/3) * np.exp(-((x-50)**2 + (y-50)**2)/500) + 0.5*np.sin(x/5)*np.sin(y/5) + 0.3*np.sin(x/7)*np.sin(y/7) + np.sqrt((x-50)**2 + (y-50)**2)/50

# Option 10: Combination of multiple Gaussians with oscillations (extremely complex)
# f = lambda x, y: (
#     5 * np.exp(-((x-25)**2 + (y-25)**2)/200) +
#     4 * np.exp(-((x-75)**2 + (y-75)**2)/200) +
#     3 * np.exp(-((x-25)**2 + (y-75)**2)/200) +
#     3 * np.exp(-((x-75)**2 + (y-25)**2)/200) +
#     10 * np.sin(x/4) * np.sin(y/4) * np.exp(-((x-50)**2 + (y-50)**2)/800) +
#     5 * np.sin(x/8) * np.sin(y/8) +
#     2 * np.sin(x/12) * np.cos(y/12) +
#     0.1 * ((x-50)**2 + (y-50)**2)
# )

def preview_3d():
    x = np.linspace(0, S-1, S)
    y = np.linspace(0, S-1, S)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)  # Vectorized evaluation
    
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.9, linewidth=0, antialiased=True)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('f(x, y)')
    ax.set_title('Function Landscape (3D Preview)')
    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.show()

preview_3d()

results = np.zeros((S, S)) 
for x in range(S):
    row = np.zeros(S)
    for y in range(S):
        z = f(x, y)
        row[y] = z
    results[x] = row

normalized_results = (results - np.min(results)) / (np.max(results) - np.min(results))
normalized_results = np.array(normalized_results)

X = np.array([(np.random.randint(0, WINDOW_SIZE), np.random.randint(0, WINDOW_SIZE)) for _ in range(N)])
V = np.array([(np.random.uniform(-1, 1), np.random.uniform(-1, 1)) for _ in range(N)])
P = X.copy()

p_hat = np.argmin([f(P[i][0]/PARTICLE_SIZE, P[i][1]/PARTICLE_SIZE) for i in range(N)])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for i in range(S):
        x = PARTICLE_SIZE * i
        for j in range(S):
            y = PARTICLE_SIZE * j
            z = results[i, j]
            color = cmap(normalized_results[i, j])
            color = Color(int(color[0] * 255), int(color[1] * 255), int(color[2] * 255))
            pygame.draw.rect(screen, color, Rect(y, x, PARTICLE_SIZE, PARTICLE_SIZE))

    for i in range(N):
        pygame.draw.circle(screen, Color(73, 199, 233), X[i], PARTICLE_SIZE)

    r = np.array([[np.random.uniform(), np.random.uniform()] for _ in range(N)])
    r_hat = np.array([[np.random.uniform(), np.random.uniform()] for _ in range(N)])
    
    cognitive_component = r * (P - X)
    social_component = r_hat * (P[p_hat] - X)
    V = a*V + b*cognitive_component + b_hat*social_component
    X = X + c*V

    for i in range(N):
        prev = f(P[i][0]/PARTICLE_SIZE, P[i][1]/PARTICLE_SIZE)
        new = f(X[i][0]/PARTICLE_SIZE, X[i][1]/PARTICLE_SIZE)
        if new < prev:
            P[i] = X[i]
        else:
            P[i] = P[i]
            
    p_hat = np.argmin([f(P[i][0]/PARTICLE_SIZE, P[i][1]/PARTICLE_SIZE) for i in range(N)])

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
