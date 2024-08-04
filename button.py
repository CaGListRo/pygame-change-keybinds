import pygame as pg


class Button:
    def __init__(self, text: str, font: pg.font.Font, mid_pos:tuple[int], size: tuple[int]) -> None:
        self.text: pg.surface = font.render(text, True, "black")
        self.mid_pos: tuple[int] = mid_pos
        self.size: tuple[int] = size
        self.click_offset: int = 5
        self.bottom_rect: pg.Rect = pg.Rect(self.mid_pos[0] - self.size[0] / 2, self.mid_pos[1] - self.size[1] / 2, self.size[0], self.size[1])
        self.top_rect: pg.Rect = pg.Rect(self.mid_pos[0] - self.size[0] / 2, self.mid_pos[1] - self.size[1] / 2, self.size[0], self.size[1])
        self.top_color: pg.Color = (235, 235, 235)

    def check_collision(self) -> bool:
        collided: bool = self.top_rect.collidepoint(pg.mouse.get_pos())
        if collided:
            self.top_color = (255, 255, 255)
            if collided and pg.mouse.get_pressed()[0]:
                self.click_offset = 0
                return True
            else:
                self.click_offset = 5
        else:
            self.top_color = (235, 235, 235)
            self.click_offset = 5

    def render(self, surf) -> None:
        border_radius: int = 5
        pg.draw.rect(surf, (175, 175, 175), self.bottom_rect, border_radius=border_radius)
        pg.draw.rect(surf, self.top_color, (self.top_rect[0], self.top_rect[1] - self.click_offset, self.top_rect[2], self.top_rect[3]), border_radius=border_radius)
        surf.blit(self.text, (self.mid_pos[0] - self.text.get_width() / 2, self.mid_pos[1] - self.text.get_height() / 2 - self.click_offset))
        pg.draw.rect(surf, (100, 100, 100), (self.top_rect[0], self.top_rect[1] - self.click_offset, self.top_rect[2], self.top_rect[3]), border_radius=border_radius, width=2)
