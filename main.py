import pygame
import sys

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Game states
MENU, PLAYING, PAUSED, GAME_OVER, LEVEL_COMPLETE = 'menu', 'playing', 'paused', 'game_over', 'level_complete'

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Mind Heist')
        self.clock = pygame.time.Clock()
        self.state = MENU
        self.font = pygame.font.Font(None, 36)

    def run(self):
        while True:
            self.handle_events()
            self.update_state()
            self.render()
            self.clock.tick(FPS)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if self.state == MENU:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    self.state = PLAYING
            elif self.state == PLAYING:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                    self.state = PAUSED
            elif self.state == PAUSED:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    self.state = PLAYING
            elif self.state == GAME_OVER:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                    self.state = MENU
            elif self.state == LEVEL_COMPLETE:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                    self.state = MENU

    def update_state(self):
        pass  # Placeholder for game logic updates

    def render(self):
        self.screen.fill((0, 0, 0))  # Clear the screen
        if self.state == MENU:
            self.render_menu()
        elif self.state == PLAYING:
            self.render_game()
        elif self.state == PAUSED:
            self.render_paused()
        elif self.state == GAME_OVER:
            self.render_game_over()
        elif self.state == LEVEL_COMPLETE:
            self.render_level_complete()
        pygame.display.flip()  # Update the full display Surface to the screen

    def render_menu(self):
        title_surface = self.font.render('Mind Heist - Press Enter to Start', True, (255, 255, 255))
        self.screen.blit(title_surface, (WIDTH // 2 - title_surface.get_width() // 2, HEIGHT // 2))

    def render_game(self):
        # Placeholder for game rendering
        game_surface = self.font.render('Game Running...', True, (255, 255, 255))
        self.screen.blit(game_surface, (WIDTH // 2 - game_surface.get_width() // 2, HEIGHT // 2))

    def render_paused(self):
        paused_surface = self.font.render('Game Paused - Press R to Resume', True, (255, 255, 255))
        self.screen.blit(paused_surface, (WIDTH // 2 - paused_surface.get_width() // 2, HEIGHT // 2))

    def render_game_over(self):
        game_over_surface = self.font.render('Game Over - Press M for Menu', True, (255, 0, 0))
        self.screen.blit(game_over_surface, (WIDTH // 2 - game_over_surface.get_width() // 2, HEIGHT // 2))

    def render_level_complete(self):
        level_complete_surface = self.font.render('Level Complete - Press M for Menu', True, (0, 255, 0))
        self.screen.blit(level_complete_surface, (WIDTH // 2 - level_complete_surface.get_width() // 2, HEIGHT // 2))

if __name__ == '__main__':
    Game().run()