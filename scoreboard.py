from turtle import Turtle

FONT = ("Arial", 18, "normal")

LEVEL = 1  # Global seviyeyi burada tanımlıyoruz

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-280, 260)
        self.hideturtle()  # Başlangıçta görünmez yap
        self.update_scoreboard()

    def update_scoreboard(self):
        """Skorborddaki yazıyı günceller."""
        self.clear()  # Eski yazıyı siler
        self.write(f"LEVEL {LEVEL}", False, "left", FONT)  # Yeni seviyeyi yazdır

    def level_up(self):
        """Seviyeyi artırır ve yazıyı günceller."""
        global LEVEL  # LEVEL'ı global olarak güncelle
        LEVEL += 1
        self.update_scoreboard()  # Skorborddaki yazıyı güncelle
    def is_lose(self):
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.write(f"Game Over", False, "center", FONT)
