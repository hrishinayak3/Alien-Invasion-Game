class GameStats:
    """Track the statics of the game"""

    def __init__(self, ai_game):
        """Initialize Stsatistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        self.game_active = False

        #High score should nevr be reset
        self.high_score = 0



    def reset_stats(self):
        """Initialize stats that can change di=uring game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1


