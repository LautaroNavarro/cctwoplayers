import pygame
from game import Game
from event_mapper import EventMapper

pygame.init()

screen = pygame.display.set_mode((640, 320))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

running = True

GAME_NAME = "Clicker"

pygame.display.set_caption(GAME_NAME)

pygame.font.init()

player_font = pygame.font.SysFont('Comic Sans MS', 30)
counter_font = pygame.font.SysFont('Comic Sans MS', 200)

game = Game()

event_mapper = EventMapper(
    game=game,
    player_one_key=pygame.K_q,
    player_two_key=pygame.K_p,
    restart_game_key=pygame.K_RETURN
)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        event_mapper.register_event(event)

    if game.is_finished:
        winner = player_font.render(
            '{} wins.'.format(game.winner.name),
            False,
            game.winner.color,
        )

    screen.fill(BLACK)

    if game.is_finished:
        screen.blit(winner, (220, 200))
    else:
        screen.blit(player_font.render(
            game.player_one.name,
            False,
            game.player_one.color
        ), (0, 0))
        screen.blit(player_font.render(
            game.player_two.name,
            False,
            game.player_two.color,
        ), (510, 0))

        screen.blit(
            counter_font.render(
                str(game.player_one.counter),
                False,
                game.player_one.color,
            ),
            (150, 200),
        )
        screen.blit(
            counter_font.render(
                str(game.player_two.counter),
                False,
                game.player_two.color,
            ),
            (400, 200),
        )

    pygame.display.update()

pygame.quit()
