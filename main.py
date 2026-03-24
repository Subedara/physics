###########
# IMPORTS #
###########

import raylibpy as rl
import math

#########
# FLOOR #
#########

class Floor:

    def __init__(self, x, y, w, h, color) -> None:
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.color = color

    def draw(self) -> None:
        rl.draw_rectangle(self.x, self.y, self.width, self.height, self.color)

########
# BALL #
########

class Ball:
    
    def __init__(self, x, y, radius, color, speed) -> None:
        self.x = x
        self.y = y
        self.radius = radius*20
        self.color = color
        self.velocity_y = 2
        self.velocity_x = 5
        self.speed = speed

    def get_direction(self) -> float: # Unused function
        return math.atan2(self.velocity_x, self.velocity_y)

    def get_speed(self) -> float: # Unused function
        return math.sqrt(self.velocity_x**2 + self.velocity_y**2)

    def draw(self) -> None:
        rl.draw_circle(self.x, self.y, self.radius, self.color)  

    def update(self, floor=None) -> None:
        self.velocity_y += self.speed
        self.x += self.velocity_x
        self.y += self.velocity_y
        if floor == None:    
            y_pos = rl.get_screen_height()
        else:
            y_pos = floor.y
        if self.y + self.radius >= y_pos:
            self.y = y_pos - self.radius
            self.velocity_y *= -0.8
        if self.x + self.radius >= rl.get_screen_width():
            self.x = rl.get_screen_width() - self.radius
            self.velocity_x *= -0.8
        elif self.x - self.radius <= 0:
            self.x = self.radius
            self.velocity_x *= -0.8
        
###################
# INITIALISATIONS #
###################

rl.init_window(800, 600, "Physics Engine Part 1")
rl.set_target_fps(60)

ball1 = Ball(400, 20, 1, rl.DARKBLUE, 0.25)
ball2 = Ball(200, 50, 1, rl.DARKBROWN, 0.25)
ball3 = Ball(600, 100, 1, rl.DARKGREEN, 0.25)

floor = Floor(20, 500, 760, 20, rl.BLACK)

balls = [ball1, ball2, ball3]

#########
# LOGIC #
#########

while not rl.window_should_close():
    
    for ball in balls:
        ball.update(floor)

    for i in range(len(balls)):
        for j in range(i + 1, len(balls)):
            b1 = balls[i]
            b2 = balls[j]

            dx = b2.x - b1.x
            dy = b2.y - b1.y

            distance = math.sqrt(dx**2 + dy**2)

            if (distance < b1.radius + b2.radius):
                b1.velocity_x, b2.velocity_x = b2.velocity_x, b1.velocity_x
                b1.velocity_y, b2.velocity_y = b2.velocity_y, b1.velocity_y

    rl.begin_drawing()
    rl.clear_background(rl.RAYWHITE)

    floor.draw()
    for i in balls:
        i.draw()

    rl.end_drawing()

##############
# POST-LOGIC #
##############

rl.close_window()