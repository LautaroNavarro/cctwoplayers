import pytest
from game import (
    Game,
    InvalidGameStatus,
)
from game import Player


class TestGame:

    def test_it_create_game_instance(self):
        game = Game()
        assert type(game) == Game
        assert game.max_points == 100
        assert game.is_finished is False
        assert type(game.player_one) == Player
        assert type(game.player_two) == Player

        assert game.player_one.counter == 0
        assert game.player_one.name == "Player one"
        assert game.player_one.color == (255, 0, 0)

        assert game.player_two.counter == 0
        assert game.player_two.name == "Player two"
        assert game.player_two.color == (0, 0, 255)

        assert game.winner is None

    def test_it_create_game_with_200_max_points(self):
        game = Game(max_points=200)
        assert game.max_points == 200

    def test_is_finished_property_returns_false_when_playing(self):
        game = Game()
        assert False is game.is_finished

    def test_is_finished_property_returns_true_when_finished(self):
        game = Game()
        game.status = Game.Status.FINISHED.value
        assert True is game.is_finished

    def test_increase_player_one_counter(self):
        game = Game()
        game.increase_player_one_counter()
        assert game.player_one.counter == 1
        assert game.is_finished is False

    def test_increase_player_one_counter_raise_when_game_is_finished(self):
        game = Game(max_points=1)
        game.increase_player_one_counter()
        assert game.player_one.counter == 1
        assert game.is_finished is True
        with pytest.raises(InvalidGameStatus):
            game.increase_player_one_counter()

    def test_increase_player_two_counter(self):
        game = Game()
        game.increase_player_two_counter()
        assert game.player_two.counter == 1
        assert game.is_finished is False

    def test_increase_player_two_counter_raise_when_game_is_finished(self):
        game = Game(max_points=1)
        game.increase_player_two_counter()
        assert game.player_two.counter == 1
        assert game.is_finished is True
        with pytest.raises(InvalidGameStatus):
            game.increase_player_two_counter()

    def test_update_game_status_and_winner_when_player_two_wins(self):
        game = Game(max_points=1)
        game.increase_player_two_counter()
        assert game.player_two.counter == 1
        assert game.is_finished is True
        assert game.winner == game.player_two

    def test_update_game_status_and_winner_when_player_one_wins(self):
        game = Game(max_points=1)
        game.increase_player_one_counter()
        assert game.player_one.counter == 1
        assert game.is_finished is True
        assert game.winner == game.player_one

    def test_restart_game_change_attributes(self):
        game = Game(max_points=1)
        game.increase_player_one_counter()
        assert game.player_one.counter == 1
        assert game.is_finished is True
        assert game.winner == game.player_one
        game.restart_game()
        assert game.player_one.counter == 0
        assert game.player_two.counter == 0
        assert game.is_finished is False
        assert game.winner is None
