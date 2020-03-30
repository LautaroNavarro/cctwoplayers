import pygame


class EventMapper:

    def __init__(
        self,
        game,
        player_one_key,
        player_two_key,
        restart_game_key,
    ):
        self.game = game
        self.mapper = {
            player_one_key: game.increase_player_one_counter,
            player_two_key: game.increase_player_two_counter,
            restart_game_key: game.restart_game,
        }

    def register_event(self, event):
        if event.type == pygame.KEYDOWN:
            if self.mapper.get(event.key):
                self.mapper[event.key]()
