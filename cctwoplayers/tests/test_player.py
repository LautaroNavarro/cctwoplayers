from player import Player


class TestPlayer:

    def test_it_create_player_instance(self):
        player = Player(name="Lautaro", color=(0, 0, 0))
        assert player.counter == 0
        assert type(player) == Player
        assert player.name == "Lautaro"
        assert player.color == (0, 0, 0)

    def test_increate_counter_add(self):
        player = Player(name="Lautaro", color=(0, 0, 0))
        assert player.counter == 0
        player.increase_counter()
        assert player.counter == 1
        player.increase_counter(2)
        assert player.counter == 3

    def test_restart_counter(self):
        player = Player(name="Lautaro", color=(0, 0, 0))
        assert player.counter == 0
        player.increase_counter()
        assert player.counter == 1
        player.restart_counter()
        assert player.counter == 0
