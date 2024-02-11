# code copied from stackoverflow to make pyinstaller work
import sys
import os
def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



import pygame

# class for file reading
class Line:
    def __init__(self, stimulus, delay):
        self.stimulus = stimulus
        self.delay = delay

file = []
# reading csv file
with open("stimulus.csv", "r") as f:
    for line in f:
        l = Line(line.rstrip('\n').split(';')[1].strip(), line.strip('\n').split(';')[3].strip())
        file.append(l)

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

center = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
circlePos = pygame.Vector2(screen.get_width() / 2, 3* screen.get_height()/4)
circleRaius = screen.get_height() * 0.1 / 2

#ratio is for scaling the width of the cross arms easier
ratio = 0.1
# determining the point of the cross in the center of the screen
poly = [
    center + pygame.Vector2(-1*(circleRaius/2), (circleRaius * ratio) / 2),
    center + pygame.Vector2(-1*((circleRaius * ratio) / 2), (circleRaius * ratio) / 2),
    center + pygame.Vector2(-1*((circleRaius * ratio) / 2), circleRaius / 2),
    center + pygame.Vector2((circleRaius * ratio) / 2, circleRaius / 2),
    center + pygame.Vector2((circleRaius * ratio) / 2, (circleRaius * ratio) / 2),
    center + pygame.Vector2(circleRaius / 2, (circleRaius * ratio) / 2),
    center - pygame.Vector2(-1*(circleRaius/2), (circleRaius * ratio) / 2),
    center - pygame.Vector2(-1*((circleRaius * ratio) / 2), (circleRaius * ratio) / 2),
    center - pygame.Vector2(-1*((circleRaius * ratio) / 2), circleRaius / 2),
    center - pygame.Vector2((circleRaius * ratio) / 2, circleRaius / 2),
    center - pygame.Vector2((circleRaius * ratio) / 2, (circleRaius * ratio) / 2),
    center - pygame.Vector2(circleRaius / 2, (circleRaius * ratio) / 2),
    ]

# booleans used for knowing when to show the circle, and other stuff
showCircle = True
showed = False
waitingForAnswer = False
start = False
answer = False

# the soun 
beep = pygame.mixer.Sound('./beep.mp3')

# index counter used in the game cicle
i = 0

while running:
    pygame.event.pump()
    screen.fill("black")
    # draw cross
    pygame.draw.polygon(screen, "white", poly)
    
    # get pressed keys
    keys = pygame.key.get_pressed()
    
    # before start of the stimulus
    if not start:
        # quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if keys[pygame.K_RETURN]:
            start = True
            dt = clock.tick_busy_loop(60) / 1000
            pygame.display.flip()
            pygame.time.delay(1000)
        else:
            font = pygame.font.SysFont(None, 60)
            img = font.render('Press enter to start', True, "white")
            screen.blit(img, center - pygame.Vector2(180, screen.get_height() / 4))
        dt = clock.tick_busy_loop(60) / 1000
        pygame.display.flip()
        continue
    
    # check for answer
    if waitingForAnswer and keys[pygame.K_1]:
        i += 1
        waitingForAnswer = False
        showCircle = True
        if not answer:
            answer = True
            with open("answers.txt", "a") as f:
                f.write("1\n")
        pygame.time.delay(1000)
    elif waitingForAnswer and keys[pygame.K_2]:
        i += 1
        waitingForAnswer = False
        showCircle = True
        if not answer:
            answer = True
            with open("answers.txt", "a") as f:
                f.write("2\n")
        pygame.time.delay(1000)
    elif waitingForAnswer and keys[pygame.K_BACKSPACE]:
        waitingForAnswer = False
        showCircle = True
        pygame.time.delay(1000)

    # stimulus
    if not waitingForAnswer:
    
        if file[i].stimulus == "V":
            answer = False
            if showCircle:
                pygame.draw.circle(screen, "white", circlePos, circleRaius)
                pygame.display.flip()
                dt = clock.tick_busy_loop(60) / 1000
                showCircle = False
                waitingForAnswer = True
                print("V\n")
                continue
        
        
        elif file[i].stimulus == "VA-VA":
            answer = False
            if showCircle:
                pygame.draw.circle(screen, "white", circlePos, circleRaius)
                pygame.display.flip()
                beep.play()
                dt = clock.tick_busy_loop(60) / 1000
                showCircle = False
                showed = True
                continue
            if showed:
                pygame.display.flip()
                dt = clock.tick_busy_loop(60) / 1000
                pygame.time.delay(int(file[i].delay))
                pygame.draw.circle(screen, "white", circlePos, circleRaius)
                pygame.display.flip()
                beep.play()
                dt = clock.tick_busy_loop(60) / 1000
                showed = False
                waitingForAnswer = True
                print("VA-VA\n")
                continue
                
            
        elif file[i].stimulus == "V-V":
            answer = False
            if showCircle:
                pygame.draw.circle(screen, "white", circlePos, circleRaius)
                pygame.display.flip()
                dt = clock.tick_busy_loop(60) / 1000
                showCircle = False
                showed = True
                continue
            if showed:
                pygame.display.flip()
                dt = clock.tick_busy_loop(60) / 1000
                pygame.time.delay(int(file[i].delay))
                pygame.draw.circle(screen, "white", circlePos, circleRaius)
                pygame.display.flip()
                dt = clock.tick_busy_loop(60) / 1000
                showed = False
                waitingForAnswer = True
                print("V-V\n")
                continue
        
        
        elif file[i].stimulus == "V-A": 
            answer = False
            if showCircle:
                pygame.draw.circle(screen, "white", circlePos, circleRaius)
                pygame.display.flip()
                dt = clock.tick_busy_loop(60) / 1000
                showCircle = False
                showed = True
                continue
            if showed:
                pygame.display.flip()
                dt = clock.tick_busy_loop(60) / 1000
                pygame.time.delay(int(file[i].delay))
                beep.play()
                showed = False
                waitingForAnswer = True
                print("V-A\n")
                continue
        
        
        elif file[i].stimulus == "A-V":
            answer = False
            if showCircle:
                beep.play()
                dt = clock.tick_busy_loop(60) / 1000
                showCircle = False
                showed = True
                continue
            if showed:
                pygame.time.delay(int(file[i].delay))
                pygame.draw.circle(screen, "white", circlePos, circleRaius)
                pygame.display.flip()
                dt = clock.tick_busy_loop(60) / 1000
                showed = False
                waitingForAnswer = True
                print("A-V\n")
                continue

        
        elif file[i].stimulus == "VA-V":
            answer = False
            if showCircle:
                pygame.draw.circle(screen, "white", circlePos, circleRaius)
                pygame.display.flip()
                beep.play()
                dt = clock.tick_busy_loop(60) / 1000
                showCircle = False
                showed = True
                continue
            if showed:
                pygame.display.flip()
                dt = clock.tick_busy_loop(60) / 1000
                pygame.time.delay(int(file[i].delay))
                pygame.draw.circle(screen, "white", circlePos, circleRaius)
                pygame.display.flip()
                dt = clock.tick_busy_loop(60) / 1000
                showed = False
                waitingForAnswer = True
                print("VA-V\n")
                continue

        
        elif file[i].stimulus == "V-VA":
            answer = False
            if showCircle:
                pygame.draw.circle(screen, "white", circlePos, circleRaius)
                pygame.display.flip()
                dt = clock.tick_busy_loop(60) / 1000
                showCircle = False
                showed = True
                continue
            if showed:
                pygame.display.flip()
                dt = clock.tick_busy_loop(60) / 1000
                pygame.time.delay(int(file[i].delay))
                pygame.draw.circle(screen, "white", circlePos, circleRaius)
                pygame.display.flip()
                beep.play()
                dt = clock.tick_busy_loop(60) / 1000
                showed = False
                waitingForAnswer = True
                print("V-VA\n")
                continue
            
            
        elif file[i].stimulus == "VA-A":
            answer = False
            if showCircle:
                pygame.draw.circle(screen, "white", circlePos, circleRaius)
                pygame.display.flip()
                beep.play()
                dt = clock.tick_busy_loop(60) / 1000
                showCircle = False
                showed = True
                continue
            if showed:
                pygame.display.flip()
                dt = clock.tick_busy_loop(60) / 1000
                pygame.time.delay(int(file[i].delay))
                beep.play()
                dt = clock.tick_busy_loop(60) / 1000
                showed = False
                waitingForAnswer = True
                print("VA-A\n")
                continue


        elif file[i].stimulus == "A-VA":
            answer = False
            if showCircle:
                beep.play()
                dt = clock.tick_busy_loop(60) / 1000
                showCircle = False
                showed = True
                continue
            if showed:
                pygame.time.delay(int(file[i].delay))
                pygame.draw.circle(screen, "white", circlePos, circleRaius)
                pygame.display.flip()
                beep.play()
                dt = clock.tick_busy_loop(60) / 1000
                showed = False
                waitingForAnswer = True
                print("A-VA\n")
                continue

    # quit event listener
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    
    pygame.display.flip()
    dt = clock.tick_busy_loop(60) / 1000
pygame.quit()
