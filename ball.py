import pygame

class Ball:
    def __init__(self, img, x, y, d, x_speed, y_speed):
        self.img = img
        self.x = x
        self.y = y
        self.d = d
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.lose = False
        self.score = 0

        # sounds
        self.hit_sound = pygame.mixer.Sound("sounds/hitWall.wav")
        self.loss_sound = pygame.mixer.Sound("sounds/lifeLoss.wav")

    def move(self, screen_width, screen_height):
        if self.y <= 0:
            self.y_speed *= -1
        if self.x >= screen_width - self.d or self.x <= 0:
            self.x_speed *= -1

        self.x += self.x_speed
        self.y += self.y_speed

        return self.lose, self.score

    def draw(self, screen):
        if not self.lose:
            screen.blit(self.img, (self.x, self.y))

    def get_pos(self):
        return [self.x, self.y]

    def get_size(self):
        return self.d

    def set_lose(self):
        self.lose = True

    def add_score(self):
        self.score += 1
        
    def reverse_y_speed(self):
        self.y_speed *= -1

    def play_lose_sound(self):
        self.loss_sound.play()

    def play_hit_sound(self):
        self.hit_sound.play()

