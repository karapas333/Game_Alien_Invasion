import os
import pickle

class GameStats():
    """Отслеживание статистики игры Alien Invasion."""

    def __init__(self, ai_settings):
        """Инициализирует статистику."""
        self.ai_settings = ai_settings
        self.reset_stats()
        #Игра Alien Invasion запускается в неактивном состоянии.
        self.game_active = False
        #Загрузка рекорда из файла.
        self.load_high_score()


    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры."""
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def save_high_score(self):
        """Сохраняет лучший рекорд."""
        with open("high_score.pkl", "wb") as f:
            pickle.dump(str(self.high_score), f, 0)

    def load_high_score(self):
        if os.path.exists("high_score.pkl"):
            with open("high_score.pkl", "rb") as f:
                try:
                    str_high_score = pickle.load(f)
                    self.high_score = int(str_high_score)
                except EOFError:
                    self.high_score = 0
        else:
            self.high_score = 0
        self.save_high_score()

    def __del__(self):
        """Сохраняет лучший рекорд при закрытии игры."""
        self.save_high_score()