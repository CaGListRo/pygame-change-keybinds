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
        self.state: str = "play"
        self.display = pg.display.set_mode((800, 600))

        # options stuff
        self.texts: list[str] = ["Steer up", "Steer down", "Steer left", "Steer right"]
        self.collision_rects: list[pg.Rect] = [pg.Rect(350, 200 + i * 40, 100, 35) for i in range(4)]
        
        # player settings
        self.player: pg.Surface = pg.Surface((50, 50))
        self.player.fill((255, 0, 0))
        self.pos = pg.Vector2((375, 275))

        # button stuff
        self.font = pg.font.SysFont("comicsans", 23)
        self.options_button = Button(text="OPTIONS", font=self.font, mid_pos=(80, 50), size=(150, 80))
        self.back_button = Button(text="BACK", font=self.font, mid_pos=(720, 50), size=(150, 80))

        # funstuff for the options background
        self.options_background = pg.Surface((800, 600))
        color_value_change: float = 255 / 600
        for i in range(600):
            blue_value = int(0 + color_value_change * i)
            if blue_value > 255:
                blue_value = 255
            pg.draw.line(surface=self.options_background, color=(0, 0, blue_value), start_pos=(0, i), end_pos=(800, i), width=1)

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

    def change_key(self, index) -> None:
        print("in")
        match index:
            case 0:
                pass
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass

    def check_rect_collisions(self) -> None:
        for idx, rect in enumerate(self.collision_rects):
            if rect.collidepoint(pg.mouse.get_pos()):
                if pg.mouse.get_pressed()[0]:
                    self.szaze = "change key"
                    self.change_key(idx)

    def draw_window(self) -> None:
        if self.state == "play":
            self.display.fill((0, 0, 0))       
            self.display.blit(self.player, self.pos)
            self.options_button.render(self.display)
        elif self.state == "options":
            self.display.blit(self.options_background, (0, 0))
            self.back_button.render(self.display)
            text_to_blit = self.font.render("Click in the square to change key.", True, "white")
            self.display.blit(text_to_blit, (100, 100))
            for idx, text in enumerate(self.texts):
                text_to_blit = self.font.render(text, True, "white")
                self.display.blit(text_to_blit, (200, 200 + idx * 40))
            text_to_blit = self.font.render(self.up.strip("K_"), True, "white")
            self.display.blit(text_to_blit, (360, 200))
            text_to_blit = self.font.render(self.down.strip("K_"), True, "white")
            self.display.blit(text_to_blit, (360, 240))
            text_to_blit = self.font.render(self.left.strip("K_"), True, "white")
            self.display.blit(text_to_blit, (360, 280))
            text_to_blit = self.font.render(self.right.strip("K_"), True, "white")
            self.display.blit(text_to_blit, (360, 320))
            for rect in self.collision_rects:
                pg.draw.rect(self.display, "white", rect, width=1)


        pg.display.update()


    def run(self) -> None:
        while self.running:
            self.clock.tick(self.fps)
            self.handle_events()
            self.draw_window()
            if self.state == "play":
                if self.options_button.check_collision():
                    self.state = "options"
            elif self.state == "options":
                self.check_rect_collisions()
                if self.back_button.check_collision():
                    self.state = "play"


if __name__ == "__main__":
    test = KeyBindTest()
    test.run()