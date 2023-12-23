from human import Human
import pygame
from details import screen, draw_text, Text

font20 = pygame.font.SysFont('Comic Sans MS', 20)
font17 = pygame.font.SysFont('Comic Sans MS', 17)
font16 = pygame.font.SysFont('Comic Sans MS', 16)
font13 = pygame.font.SysFont('Comic Sans MS', 13)


def pop_up_window(mouse_pos, human):
    y = mouse_pos[1] + 10 if (mouse_pos[1] + 10 + 324 <= 720) else mouse_pos[1] - 10 - 324
    x = mouse_pos[0] + 10 if (mouse_pos[0] + 10 + 310 <= 1200) else mouse_pos[0] - 10 - 310

    pygame.draw.rect(screen, (255, 255, 255), (x, y, 310, 324), border_radius=15)
    pygame.draw.rect(screen, (0, 0, 0), (x, y, 310, 324), 1, 15)
    draw_text(human.FIO.split()[0], (x + 108, y + 30), (0, 0, 0), otherFont=font17)
    draw_text(human.FIO.split()[1], (x + 108, y + 55), (0, 0, 0), otherFont=font17)
    draw_text(human.date, (x + 14, y + 99), (0, 0, 0), otherFont=font20)
    draw_text("Краткая биография:", (x + 14, y + 138), (0, 0, 0), otherFont=font16)
    screen.blit(human.image, (x + 11, y + 12))
    pygame.draw.rect(screen, (216, 246, 221), (x + 12, y + 161, 282, 148), border_radius=10)
    if human.biography != "":
        lines = Text(human.biography).split_to_size(282, font13)
        for i in range(len(lines)):
            draw_text(lines[i], (x + 19, y + 168 + (13 * i)), (0, 0, 0), otherFont=font13)


class Empty:
    def hover(self, mouse_pos):
        self.hovered = -1
        if self.rejim:
            for i in range(len(self.persons_Father) - 1):
                if self.persons_Father[i].hover(mouse_pos):
                    self.hovered = i
        else:
            for i in range(len(self.persons_Mother) - 1):
                if self.persons_Mother[i].hover(mouse_pos):
                    self.hovered = i

    def find_active(self, array):
        for i in array:
            if i.active:
                return i
        return None

    def get_active(self):
        if self.rejim:
            human = self.find_active(self.persons_Father)
        else:
            human = self.find_active(self.persons_Mother)
        return human

    def find_hover(self, array):
        for i in range(len(array) - 1):
            if array[i].hovered:
                return array[i]
        return None

    def get_hover(self):
        if self.rejim:
            human = self.find_hover(self.persons_Father)
        else:
            human = self.find_hover(self.persons_Mother)
        return human

    def set_shift_to_line(self, shift, array):
        for i in array:
            if i[-1] == 'rect':
                i[0] += shift[0]
                i[1] += shift[1]
            else:
                for l in range(len(i) - 1):
                    i[l] = [i[l][0] + shift[0], i[l][1] + shift[1]]

    def set_shift(self, shift):
        for i in range(len(self.persons_Father) - 1):
            self.persons_Father[i].set_shift(shift)
        for i in range(len(self.persons_Mother) - 1):
            self.persons_Mother[i].set_shift(shift)
        self.set_shift_to_line(shift, self.persons_Father[-1])
        self.set_shift_to_line(shift, self.persons_Mother[-1])

    def draw_last_object(self, array):
        for i in array:
            if i[-1] == "rect":
                pygame.draw.rect(screen, (0, 0, 0), (i[0], i[1], i[2], i[3]))
            else:
                pygame.draw.polygon(screen, (0, 0, 0), [i[0], i[1], i[2]])

    def draw(self):
        if self.rejim:
            self.draw_last_object(self.persons_Father[-1])
            for i in range(len(self.persons_Father) - 1):
                self.persons_Father[i].draw(i != self.hovered)
        else:
            self.draw_last_object(self.persons_Mother[-1])
            for i in range(len(self.persons_Mother) - 1):
                self.persons_Mother[i].draw(i != self.hovered)

    def press(self, event):
        if self.rejim:
            for i in range(len(self.persons_Father) - 1):
                if self.persons_Father[i].press(event):
                    for l in range(len(self.persons_Father) - 1):
                        if i != l and self.persons_Father[l].active:
                            self.persons_Father[l].active = False
                    return self.persons_Father[i]
        else:
            for i in range(len(self.persons_Mother) - 1):
                if self.persons_Mother[i].press(event):
                    for l in range(len(self.persons_Mother) - 1):
                        if i != l and self.persons_Mother[l].active:
                            self.persons_Mother[l].active = False
                    return self.persons_Mother[i]
        return None


class empty(Empty):
    def __init__(self):
        self.hovered = -1
        self.rejim = True
        self.persons_Mother = []
        self.persons_Father = []

class Ivanov(Empty):
    def __init__(self):
        self.hovered = -1
        self.rejim = True
        self.persons_Mother = [
            Human("Виталий Иванов", "10.10.2008", 1, (430, 351), "vitaliy.png", "Любит изучать генеологию", True),
            Human("Степан Иванов", "08.05.2010", 1, (600, 351)),
            Human("Светлана Иванова", "22.03.1984", 0, (430, 267)),
            Human("Алексей Иванов", "15.02.1982", 1, (600, 267)),
            [
                [488, 338, 173, 6, 'rect'], [488, 320, 170, 6, 'rect'], [655, 338, 6, 13, 'rect'],
                [485, 338, 6, 13, 'rect'], [570, 320, 6, 18, 'rect'], [655, 310, 6, 16, 'rect'],
                [485, 310, 6, 16, 'rect'], [487, 245, 6, 21, 'rect'], [[489, 236], [499, 256], [479, 256], 'triangle']
            ]
        ]
        self.persons_Father = [
            Human("Виталий Иванов", "10.10.2008", 1, (430, 351), "vitaliy.png", "Любит изучать генеологию", True),
            Human("Степан Иванов", "08.05.2010", 1, (600, 351)),
            Human("Светлана Иванова", "22.03.1984", 0, (430, 267)),
            Human("Алексей Иванов", "15.02.1982", 1, (600, 267)),
            Human("Елизавета Сидорова", "15.10.1949", 0, (338, 183)),
            Human("Виктор Сидоров", "30.10.1944 - 10.12.2022", 1, (515, 183)),
            [
                [488, 338, 173, 6, 'rect'], [488, 320, 170, 6, 'rect'], [655, 338, 6, 13, 'rect'],
                [485, 338, 6, 13, 'rect'], [570, 320, 6, 18, 'rect'], [655, 310, 6, 16, 'rect'],
                [485, 310, 6, 16, 'rect'], [486, 236, 6, 31, 'rect'], [396, 236, 180, 6, 'rect'],
                [393, 226, 6, 16, 'rect'], [573, 226, 6, 16, 'rect']
            ]
        ]