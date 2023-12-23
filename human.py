import details
import pygame

font = pygame.font.SysFont('Comic Sans MS', 11)


def center():
    pass


class Human_out_of_tree:
    def __init__(self, FIO, date, gender, coord, image="none.png", biography="", active=False):
        self.image = pygame.image.load(f"images/{image}")
        self.image = pygame.transform.scale(self.image, (87, 87))
        self.FIO = FIO
        self.date = date
        self.gender = gender
        self.coord = coord
        self.biography = biography
        self.active = active
        self.size = [117, 43]
        self.hovered = False
        self.take = False

    def __str__(self):
        return f"Human( {self.FIO}, {self.gender} )"

    def hover(self, mouse_pos):
        self.hovered = pygame.Rect(self.coord[0], self.coord[1], self.size[0], self.size[1])
        self.hovered = self.hovered.collidepoint(mouse_pos[0], mouse_pos[1])
        return self.hovered

    def set_shift(self, shift):
        self.coord = (self.coord[0] + shift[0], self.coord[1] + shift[1])

    def draw(self, other_hovered: bool = False):
        if self.hovered and not other_hovered:
            if self.gender:
                border_color = (78, 153, 245)
            else:
                border_color = (240, 122, 220)
        else:
            border_color = (0, 0, 0)

        if self.gender:
            color = (174, 209, 251)
        else:
            color = (249, 212, 243)
        pygame.draw.rect(details.screen, color, (self.coord[0], self.coord[1], self.size[0], self.size[1]))
        if self.active or (self.hovered and not other_hovered):
            pygame.draw.rect(details.screen, border_color,
                             (self.coord[0], self.coord[1], self.size[0], self.size[1]), 3)

        details.draw_text(self.FIO.split()[0], (self.coord[0] + self.size[0] // 2, self.coord[1] + 5), (0, 0, 0),
                          False, otherFont=font)
        details.draw_text(self.FIO.split()[1], (self.coord[0] + self.size[0] // 2, self.coord[1] + 20), (0, 0, 0),
                          False, otherFont=font)

    def press(self, event, mouse_pos):
        rtr = False
        if self.hovered:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.take = True
                self.mouse_start = mouse_pos
                rtr = True
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                self.take = False
            if self.take:
                shift = [mouse_pos[0] - self.mouse_start[0], mouse_pos[1] - self.mouse_start[1]]
                self.set_shift(shift)
        return rtr


class Human():
    def __init__(self, FIO, date, gender, coord, image="none.png", biography="", active=False):
        self.image = pygame.image.load(f"images/{image}")
        self.image = pygame.transform.scale(self.image, (87, 87))
        self.FIO = FIO
        self.date = date
        self.gender = gender
        self.coord = coord
        self.biography = biography
        self.active = active
        self.size = [117, 43]
        self.hovered = False

    def __str__(self):
        return f"Human( {self.FIO}, {self.gender} )"

    def hover(self, mouse_pos):
        self.hovered = pygame.Rect(self.coord[0], self.coord[1], self.size[0], self.size[1])
        self.hovered = self.hovered.collidepoint(mouse_pos[0], mouse_pos[1])
        return self.hovered

    def set_shift(self, shift):
        self.coord = (self.coord[0] + shift[0], self.coord[1] + shift[1])

    def draw(self, other_hovered: bool = False):
        if self.hovered and not other_hovered:
            if self.gender:
                border_color = (78, 153, 245)
            else:
                border_color = (240, 122, 220)
        else:
            border_color = (0, 0, 0)

        if self.gender:
            color = (174, 209, 251)
        else:
            color = (249, 212, 243)
        pygame.draw.rect(details.screen, color, (self.coord[0], self.coord[1], self.size[0], self.size[1]))
        if self.active or (self.hovered and not other_hovered):
            pygame.draw.rect(details.screen, border_color,
                             (self.coord[0], self.coord[1], self.size[0], self.size[1]), 3)

        details.draw_text(self.FIO.split()[0], (self.coord[0] + self.size[0] // 2, self.coord[1] + 5), (0, 0, 0),
                          False, otherFont=font)
        details.draw_text(self.FIO.split()[1], (self.coord[0] + self.size[0] // 2, self.coord[1] + 20), (0, 0, 0),
                          False, otherFont=font)

    def press(self, event, other_hovered: bool = False):
        if self.hovered and not other_hovered:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.active = True
                return True
        return False
