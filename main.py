from button import Button

import pygame as pg


class KeyBindTest:
    def __init__(self) -> None:
        pg.init()
        # game settings
        self.running: bool = True
        self.speed: int = 10
        self.clock = pg.time.Clock()
        self.fps: int = 60
        self.display = pg.display.set_mode((800, 600))
        
        # player settings
        self.player: pg.Surface = pg.Surface((50, 50))
        self.player.fill((255, 0, 0))
        self.pos = pg.Vector2((375, 275))

        # button stuff
        self.font = pg.font.SysFont("comicsans", 32)
        

        # key settings as str
        self.up: str = "K_UP"
        self.down: str = "K_DOWN"
        self.left: str = "K_LEFT"
        self.right: str = "K_RIGHT"

        self.bind_keys()

    def bind_keys(self) -> None:
        # keybinding via getattr
        self.key_up = getattr(pg, self.up)
        self.key_down = getattr(pg, self.down)
        self.key_left = getattr(pg, self.left)
        self.key_right = getattr(pg, self.right)

    def handle_events(self) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            
            elif event.type == pg.KEYDOWN:
                if event.key == self.key_up:
                    self.pos.y -= self.speed
                if event.key == self.key_down:
                    self.pos.y += self.speed
                if event.key == self.key_left:
                    self.pos.x -= self.speed
                if event.key == self.key_right:
                    self.pos.x += self.speed

    def draw_window(self) -> None:
        self.display.fill((0, 0, 0))
        self.display.blit(self.player, self.pos)

        pg.display.update()


    def run(self) -> None:
        while self.running:
            self.clock.tick(self.fps)
            self.handle_events()
            self.draw_window()


if __name__ == "__main__":
    test = KeyBindTest()
    test.run()