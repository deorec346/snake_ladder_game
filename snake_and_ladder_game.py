import random


class board():
    Snakes = {27: 8, 34: 7, 29: 3, 69: 31, 72: 36, 77: 46}
    Ladders = {4: 16, 6: 25, 12: 49, 30: 60, 38: 88, 58: 62}

    def __init__(self, players, verbose=False):
        self.players = players
        self.n_players = [0] * players
        self.turn = 0
        self.verbose = verbose
        self.winner = None
        self.last_pos = 100

    def die_roll(self):
        return random.randrange(1, 6)

    def move_player(self, player_i):
        prev_pos = self.n_players[player_i]
        new_pos = prev_pos + self.die_roll()

        if new_pos == self.last_pos:
            self.winner = player_i
            new_pos = self.last_pos
        elif new_pos > self.last_pos:
            new_pos = prev_pos
        elif new_pos in self.Snakes:
            new_pos = self.Snakes[new_pos]
        elif new_pos in self.Ladders:
            new_pos = self.Ladders[new_pos]
        self.n_players[player_i] = new_pos

    

if __name__ == "__main__":
    game = board(4, True)
    print(game.move_player())
