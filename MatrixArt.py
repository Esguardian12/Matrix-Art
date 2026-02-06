import pygame,random, sys, time
pygame.init()
W, H = 1000, 700
screen = pygame.display.set_mode((W,H))
clock = pygame.time.Clock()
BG = (0,0,0)
GREEN = (0,255,0)
WHITE = (255,255,255)
CHARS = list("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
LAYERS = [
    {"size": 16, "speed": 1.4, "alpha": 60, "glow": True},
    {"size": 22, "speed": 2.3, "alpha": 90, "glow": True},
    {"size": 30, "speed": 4.0, "alpha": 120, "glow": False},
]
matrix_layers = []
for layer in LAYERS:
    font = pygame.font.SysFont("Consolas",
                               layer["size"], bold = True)
    cols = W //(layer["size"] + 6)
    drops = [random.randint(-300,0) for _ in range(cols)]
    matrix_layers.append({
        "font": font,
        "drops": drops,
        "cols": cols,
        "size": layer["size"],
        "speed": layer["speed"],
        "alpha": layer["alpha"],
        "glow": layer["glow"]
    })
    fade = pygame.Surface((W, H))
    fade.set_alpha(35)
    fade.fill((0,0,0))
    start_time = time.time()
    while True:
        dt = clock.tick(60)
        if time.time() - start_time > 15:
            pygame.quit()
            sys.exit()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(fade, (0,0))
        for layer in matrix_layers:
            font = layer["font"]
            drops = layer["drops"]
            size = layer["size"]
            speed = layer["speed"]
            glow = layer["glow"]
            for i in range(layer["cols"]):
                x = i * (size + 6)
                drops[i] += speed
                y = int(drops[i])
                length = random.randint(10, 18)
                for k in range(length):
                    cy = y -k * (size + 6)
                    if cy < - 50 or cy > H + 50:
                        continue
                    ch = random.choice(CHARS)
                    color = WHITE if k == 0 else GREEN
                    txt = font.render(ch, True, color)
                    if glow and k > 0:
                        g = pygame.Surface((txt.get_width()+6,
                                            txt.get_height()+6),
                                            pygame.SRCALPHA)
                        g.blit(txt, (3,3))
                        g.fill((0,255,0,40),
                               special_flags=pygame.BLEND_RGBA_MULT)
                        screen.blit(g, (x-3,  cy-3))
                        screen.blit(txt, (x, cy))
                    if drops[i] - length * 28 > H + random.randint(80,200):
                        drops[i] = random.randint(-400, -60)
            pygame.display.flip()
