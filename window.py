import pygame
from human import Human_out_of_tree
import details

font32 = pygame.font.SysFont('Comic Sans MS', 32)
font24 = pygame.font.SysFont('Comic Sans MS', 24)
font20 = pygame.font.SysFont('Comic Sans MS', 20)
font = pygame.font.SysFont('Comic Sans MS', 15)
font12 = pygame.font.SysFont('Comic Sans MS', 12)


class plus:
    def __init__(self):
        self.size = 1
        self.hovered = False
        self.take = False
        self.mouse_start = 0

    def hover(self, mouse_pos):
        self.hovered = pygame.Rect(27, 218 + self.size, 17, 20).collidepoint(mouse_pos[0], mouse_pos[1])
        return self.hovered

    def draw(self):
        pygame.draw.rect(details.screen, (255, 255, 255), (32, 218, 7, 288))
        pygame.draw.rect(details.screen, (0, 0, 0), (32, 218, 7, 288), 1)
        if self.hovered:
            pygame.draw.rect(details.screen, (255, 255, 255), (27, 218 + self.size, 17, 20), border_radius=15)
        else:
            pygame.draw.rect(details.screen, (0, 0, 0), (27, 218 + self.size, 17, 20), border_radius=15)
        pygame.draw.rect(details.screen, (0, 0, 0), (27, 218 + self.size, 17, 20), 1, border_radius=15)
        pygame.draw.circle(details.screen, (217, 217, 217), (36, 208), 15)
        pygame.draw.circle(details.screen, (0, 0, 0), (36, 208), 15, 1)
        details.draw_text("+", (28, 183), (0, 0, 0), otherFont=font32)
        pygame.draw.circle(details.screen, (217, 217, 217), (36, 491), 15)
        pygame.draw.circle(details.screen, (0, 0, 0), (36, 491), 15, 1)
        details.draw_text("-", (28, 464), (0, 0, 0), otherFont=font32)

    def press(self, event, mouse_pos):
        if self.hovered:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.take = True
                self.mouse_start = mouse_pos[1]
        if self.take and event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.take = False
        elif self.take:
            if mouse_pos[1] >= 208 + 20 and mouse_pos[1] <= 491 - 20:
                shift = mouse_pos[1] - self.mouse_start
                self.mouse_start = mouse_pos[1]
                self.size = self.size + shift


class append_person:
    def __init__(self):
        self.name = details.Text_container("", width=559, height=41)
        self.last_name = details.Text_container("", width=559, height=41)
        self.biography = details.Text_container("", width=876, height=137)
        self.open = False
        self.hovered = [False, False, False, False]
        self.gender = True

    def hover(self, mouse_pos):
        self.name.hover(mouse_pos, (146 + 253, 126 + 26))
        self.last_name.hover(mouse_pos, (146 + 253, 126 + 94))
        self.biography.hover(mouse_pos, (146 + 16, 126 + 251))
        self.hovered[0] = pygame.draw.circle(details.screen, (0, 0, 0), (424, 299), 18).collidepoint(mouse_pos[0],
                                                                                                     mouse_pos[1])
        self.hovered[1] = pygame.draw.circle(details.screen, (0, 0, 0), (483, 299), 18).collidepoint(mouse_pos[0],
                                                                                                     mouse_pos[1])
        self.hovered[2] = pygame.Rect(146 + 43, 126 + 415, 359, 41).collidepoint(mouse_pos[0], mouse_pos[1])
        self.hovered[3] = pygame.Rect(146 + 512, 126 + 415, 359, 41).collidepoint(mouse_pos[0], mouse_pos[1])

    def draw(self):
        pygame.draw.rect(details.screen, (255, 255, 255), (146, 126, 908, 467))
        pygame.draw.rect(details.screen, (0, 0, 0), (146, 126, 908, 467), 1)
        self.name.draw((146 + 253, 126 + 26), [(156, 196, 153), (230, 230, 230), (0, 0, 0), (0, 0, 255)], lineHeight=38,
                       otherFont=font20)
        self.last_name.draw((146 + 253, 126 + 94), [(156, 196, 153), (230, 230, 230), (0, 0, 0), (0, 0, 255)],
                            lineHeight=38,
                            otherFont=font20)
        details.draw_text("Имя:", (146 + 152, 126 + 42 - 15), (0, 0, 0), otherFont=font24)
        details.draw_text("Фамилия:", (146 + 94, 126 + 103 - 15), (0, 0, 0), otherFont=font24)
        details.draw_text("Пол:", (146 + 155, 126 + 165 - 15), (0, 0, 0), otherFont=font24)
        details.draw_text("Краткая биография:", (146 + 16, 126 + 230 - 15), (0, 0, 0), otherFont=font20)
        self.biography.draw((146 + 16, 126 + 251), [(216, 246, 221), (216, 246, 221), (0, 0, 0), (0, 0, 255)],
                            lineHeight=26, otherFont=font20)

        color = (205, 205, 205) if not self.gender else (246, 166, 236)
        pygame.draw.circle(details.screen, color, (146 + 319 + 18, 126 + 155 + 18), 18)
        color = (205, 205, 205) if self.gender else (106, 185, 235)
        pygame.draw.circle(details.screen, color, (146 + 260 + 18, 126 + 155 + 18), 18)
        border_color = (0, 0, 0) if not self.hovered[0] else (30, 142, 212)
        pygame.draw.circle(details.screen, border_color, (146 + 260 + 18, 126 + 155 + 18), 18, 1)
        border_color = (0, 0, 0) if not self.hovered[1] else (235, 70, 213)
        pygame.draw.circle(details.screen, border_color, (146 + 319 + 18, 126 + 155 + 18), 18, 1)
        details.draw_text("M", (146 + 260 + 18, 126 + 155 + 3), (0, 0, 0), False, otherFont=font20)
        details.draw_text("Ж", (146 + 319 + 18, 126 + 155 + 3), (0, 0, 0), False, otherFont=font20)

        pygame.draw.rect(details.screen, (156, 196, 153), (146 + 43, 126 + 415, 359, 41))
        if not self.hovered[2]:
            pygame.draw.rect(details.screen, (0, 0, 0), (146 + 43, 126 + 415, 359, 41), 1)
        else:
            pygame.draw.rect(details.screen, (0, 0, 0), (146 + 43, 126 + 415, 359, 41), 3)
        details.draw_text("Добавить", (368, 561 - 20), (0, 0, 0), False, otherFont=font24)

        pygame.draw.rect(details.screen, (156, 196, 153), (146 + 512, 126 + 415, 359, 41))
        if not self.hovered[3]:
            pygame.draw.rect(details.screen, (0, 0, 0), (146 + 512, 126 + 415, 359, 41), 1)
        else:
            pygame.draw.rect(details.screen, (0, 0, 0), (146 + 512, 126 + 415, 359, 41), 3)
        details.draw_text("Отменить", (837, 561 - 20), (0, 0, 0), False, otherFont=font24)

    def press(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.hovered[0]:
                self.gender = False
            elif self.hovered[1]:
                self.gender = True
            elif self.hovered[2] or self.hovered[3]:
                self.open = False
                self.hovered = [False, False, False, False]
            else:
                self.name.active = False
                self.last_name.active = False
                self.biography.active = False
        self.name.Press(event)
        self.last_name.Press(event)
        self.biography.Press(event)


class off_screen_people:
    def __init__(self):
        self.peoples = [HumanInBox("Марина Иванова", "15.11.2015", 0), HumanInBox("Антон Иванов", "20.09.1985", 1)]
        self.open = False
        self.hovered = False

    def take(self):
        for i in range(len(self.peoples)):
            if self.peoples[i].take:
                return i
        return -1

    def hover(self, mouse_pos):
        hover = False
        self.hovered = pygame.Rect(787 + 345, 341 + 8, 33, 28).collidepoint(mouse_pos[0], mouse_pos[1])
        for i in self.peoples:
            hover = i.hover(mouse_pos)
        return hover

    def draw(self):
        pygame.draw.rect(details.screen, (255, 255, 255), (787, 341, 393, 324), border_radius=15)
        pygame.draw.rect(details.screen, (156, 196, 153), (787, 341, 393, 44), border_top_left_radius=15,
                         border_top_right_radius=15)
        pygame.draw.rect(details.screen, (0, 0, 0), (787, 385, 393, 1))
        pygame.draw.rect(details.screen, (0, 0, 0), (787, 341, 393, 324), 1, border_radius=15)

        pygame.draw.rect(details.screen, (216, 246, 221), (787 + 345, 341 + 8, 33, 28), border_radius=2)
        details.draw_text("+", (787 + 345 + 16, 341 + 8 - 10), (0, 0, 0), False, font32)
        if self.hovered:
            pygame.draw.rect(details.screen, (0, 0, 0), (787 + 345, 341 + 8, 33, 28), 1, border_radius=2)

        for i in range(len(self.peoples)):
            self.peoples[i].draw((787 + 5, 385 + 5 + (59 * i)))

    def press(self, event, mouse_pos):
        if self.hovered:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                return True
        for i in self.peoples:
            human = i.press(event, mouse_pos)
            if human and self.take() != -1:
                self.peoples.pop(self.take())
                return human
        if self.take() != -1:
            self.peoples.append(self.peoples.pop(self.take()))


class HumanInBox:
    def __init__(self, FIO, date, gender):
        self.FIO = FIO
        self.date = date
        self.gender = gender
        self.hovered = False
        self.coord = (0, 0)
        self.mouse_start = [0, 0]
        self.take = False

    def hover(self, mouse_pos):
        self.hovered = pygame.Rect(self.coord[0] + 9, self.coord[1] + 16, 14, 23)
        self.hovered = self.hovered.collidepoint(mouse_pos[0], mouse_pos[1])
        return self.hovered

    def draw(self, coord):
        if not self.take:
            self.coord = coord
        pygame.draw.rect(details.screen, (216, 246, 221), (self.coord[0], self.coord[1], 383, 54), border_radius=10)
        pygame.draw.rect(details.screen, (0, 0, 0), (self.coord[0], self.coord[1], 383, 54), 1, border_radius=10)

        color = (174, 209, 251) if self.gender else (249, 212, 243)
        pygame.draw.rect(details.screen, color, (self.coord[0] + 31, self.coord[1] + 6, 50, 43), border_radius=15)
        pygame.draw.rect(details.screen, (0, 0, 0), (self.coord[0] + 31, self.coord[1] + 6, 50, 43), 1,
                         border_radius=15)

        if not self.hovered:
            pygame.draw.rect(details.screen, (0, 0, 0), (self.coord[0] + 9, self.coord[1] + 16, 14, 23),
                             border_radius=5)
        pygame.draw.rect(details.screen, (0, 0, 0), (self.coord[0] + 9, self.coord[1] + 16, 14, 23), 1, border_radius=5)
        details.draw_text(self.FIO, (self.coord[0] + 91, self.coord[1] + 9), (0, 0, 0), otherFont=font20)
        details.draw_text(self.date, (self.coord[0] + 268, self.coord[1] + 13), (0, 0, 0), otherFont=font20)

    def press(self, event, mouse_pos):
        if self.hovered:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.take = True
                self.mouse_start = mouse_pos
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if 787 > mouse_pos[0] or 1180 < mouse_pos[0] or 341 > mouse_pos[1]:
                    return Human_out_of_tree(self.FIO, self.date, self.gender, (mouse_pos[0], mouse_pos[1]))
                self.take = False
            if self.take:
                shift = [mouse_pos[0] - self.mouse_start[0], mouse_pos[1] - self.mouse_start[1]]
                self.mouse_start = mouse_pos
                self.coord = [self.coord[0] + shift[0], self.coord[1] + shift[1]]


class persons_button:
    def __init__(self):
        self.hovered = False

    def hover(self, mouse_pos):
        self.hovered = pygame.Rect(1072, 720 - 35 - 12, 109, 35)
        self.hovered = self.hovered.collidepoint(mouse_pos[0], mouse_pos[1])
        return self.hovered

    def draw(self):
        pygame.draw.rect(details.screen, (156, 196, 153), (1072, 720 - 35 - 12, 109, 35))
        if self.hovered:
            pygame.draw.rect(details.screen, (0, 0, 0), (1072, 720 - 35 - 12, 109, 35), 3)
        else:
            pygame.draw.rect(details.screen, (0, 0, 0), (1072, 720 - 35 - 12, 109, 35), 1)
        details.draw_text("Персоны", (1086, 720 - 35 - 12 + 8), (0, 0, 0), otherFont=font12)
        pygame.draw.polygon(details.screen, (102, 125, 100), [(1160, 695), (1174, 695), (1167, 686)])
        pygame.draw.polygon(details.screen, (0, 0, 0), [(1160, 695), (1174, 695), (1167, 686)], 1)

    def press(self, event):
        if self.hovered:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                return True
        return False


class active_person_box:
    def __init__(self, personality):
        self.active_person = personality
        if self.active_person != None:
            self.text = f"{self.active_person.FIO}"
        else:
            self.text = ""
        self.container = details.Text_container(self.text, width=246, height=35)

    def set_personality(self, personality):
        self.active_person = personality
        self.text = f"{self.active_person.FIO}"
        self.container = details.Text_container(self.text, width=246, height=35)

    def draw(self, mouse_pos):
        self.container.hover(mouse_pos, (21, 720 - 58 + 11))
        self.container.draw((21, 720 - 58 + 11), [(0, 255, 0), (255, 255, 255), (0, 0, 0), (0, 0, 255)], lineHeight=35,
                            otherFont=font)

    def action(self, event):
        self.container.Press(event)


class gender_button:
    def __init__(self):
        self.gender = True
        self.hovered = False
        self.font = pygame.font.SysFont('Comic Sans MS', 20)

    def hover(self, mouse_pos):
        self.hovered = pygame.draw.circle(details.screen, (0, 0, 0), (289 + 18, 720 - 18 - 11), 18)
        self.hovered = self.hovered.collidepoint(mouse_pos[0], mouse_pos[1])
        return self.hovered

    def draw_symbol(self, symbol: str):
        details.draw_text(symbol, (289 + 18, 720 - 36 - 9), (0, 0, 0), False, self.font)

    def draw(self):
        if not self.hovered:
            border_color = (0, 0, 0)
        else:
            border_color = (235, 70, 213) if self.gender else (30, 142, 212)
        color = (246, 166, 236) if self.gender else (106, 185, 235)
        pygame.draw.circle(details.screen, color, (289 + 18, 720 - 18 - 11), 18)
        pygame.draw.circle(details.screen, border_color, (289 + 18, 720 - 18 - 11), 18, 1)
        self.draw_symbol("Ж") if self.gender else self.draw_symbol("М")

    def press(self, event):
        if self.hovered:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.gender = not self.gender
                return True
        return False


def menu():
    pygame.draw.rect(details.screen, (211, 238, 202), (0, 0, 1200, 58))
    pygame.draw.rect(details.screen, (211, 238, 202), (0, 720 - 58, 1200, 58))
