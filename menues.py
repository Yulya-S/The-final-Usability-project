import details
import window
import pygame
import data_sets

font48 = pygame.font.SysFont('Comic Sans MS', 48)


class tree:
    def hover(self, mouse_pos):
        if self.family_set.persons_Mother != []:
            self.family_set.set_shift(self.shift)
        for i in self.humans_out_tree:
            i.set_shift(self.shift)
        self.shift = [0, 0]

        if self.family_set.persons_Mother != []:
            self.family_set.hover(mouse_pos)

        self.gender_button.hover(mouse_pos)
        for i in self.humans_out_tree:
            i.hover(mouse_pos)
        self.persons_button.hover(mouse_pos)
        self.plus.hover(mouse_pos)
        if self.append_person.open:
            self.append_person.hover(mouse_pos)

        if self.off_screen_people.open:
            self.off_screen_people.hover(mouse_pos)

        self.hovered[0] = pygame.Rect(12, 12, 109, 35).collidepoint(mouse_pos[0], mouse_pos[1])
        self.hovered[1] = pygame.Rect(139, 12, 109, 35).collidepoint(mouse_pos[0], mouse_pos[1])

    def draw(self, mouse_pos):
        details.screen.fill((255, 255, 255))

        if self.family_set.persons_Mother != []:
            self.family_set.draw()

        window.menu()
        self.active_person_box.draw(mouse_pos)

        self.gender_button.draw()
        self.persons_button.draw()
        self.plus.draw()

        for i in self.humans_out_tree:
            i.draw()

        if self.off_screen_people.open:
            self.off_screen_people.draw()
        if self.append_person.open:
            self.append_person.draw()

        human = self.family_set.get_hover()
        human2 = None
        for i in self.humans_out_tree:
            if i.hovered:
                human2 = i
        if human and self.off_screen_people.take() == -1 and not self.off_screen_people.open:
            data_sets.pop_up_window(mouse_pos, human)
        elif self.off_screen_people.take() == -1 and human2 and not self.off_screen_people.open:
            data_sets.pop_up_window(mouse_pos, human2)

        pygame.draw.rect(details.screen, (156, 196, 153), (12, 12, 109, 35))
        size = 1 if not self.hovered[0] else 3
        pygame.draw.rect(details.screen, (0, 0, 0), (12, 12, 109, 35), size)
        details.draw_text("Создать дерево", (12 + 54, 12 + 9), (0, 0, 0), False, window.font12)

        pygame.draw.rect(details.screen, (156, 196, 153), (139, 12, 109, 35))
        size = 1 if not self.hovered[1] else 3
        pygame.draw.rect(details.screen, (0, 0, 0), (139, 12, 109, 35), size)
        details.draw_text("Загрузить дерево", (139 + 54, 12 + 9), (0, 0, 0), False, window.font12)

    def press(self, event, mouse_pos):
        ss = self.off_screen_people.press(event, pygame.mouse.get_pos())
        if ss not in [None, True]:
            self.humans_out_tree.append(ss)
        elif ss == True:
            self.append_person.open = True
        if self.persons_button.press(event):
            self.off_screen_people.open = not self.off_screen_people.open
        self.plus.press(event, pygame.mouse.get_pos())
        if self.append_person.open:
            self.append_person.press(event)
        if self.off_screen_people.take() == -1 and not self.plus.take and not self.append_person.open:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.hovered[0]:
                    return tree_empty
                elif self.hovered[1]:
                    return tree_Ivanovs
                click = self.family_set.press(event)
                if click:
                    self.active_person_box.set_personality(click)
                elif 720 - 58 > pygame.mouse.get_pos()[1] > 58:
                    self.mouse_start = pygame.mouse.get_pos()
                else:
                    if self.gender_button.press(event):
                        for i in self.humans_out_tree:
                            self.off_screen_people.peoples.append(window.HumanInBox(i.FIO, i.date, i.gender))
                        self.humans_out_tree = []
                        self.family_set.rejim = not self.family_set.rejim
                        if self.family_set.persons_Mother != []:
                            self.active_person_box.set_personality(self.family_set.get_active())
            if self.mouse_start != 0:
                self.shift = [mouse_pos[0] - self.mouse_start[0], mouse_pos[1] - self.mouse_start[1]]
                self.mouse_start = mouse_pos
            else:
                self.active_person_box.action(event)
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                self.shift = [0, 0]
                self.mouse_start = 0


class tree_empty(tree):
    def __init__(self):
        self.family_set = data_sets.empty()
        self.active_person_box = window.active_person_box(None)
        self.gender_button = window.gender_button()
        self.persons_button = window.persons_button()
        self.plus = window.plus()
        self.append_person = window.append_person()
        self.off_screen_people = window.off_screen_people()
        self.humans_out_tree = []
        self.mouse_start = 0
        self.shift = [0, 0]
        self.hovered = [False, False]


class tree_Ivanovs(tree):
    def __init__(self):
        self.family_set = data_sets.Ivanov()
        self.active_person_box = window.active_person_box(self.family_set.get_active())
        self.gender_button = window.gender_button()
        self.persons_button = window.persons_button()
        self.plus = window.plus()
        self.append_person = window.append_person()
        self.off_screen_people = window.off_screen_people()
        self.humans_out_tree = []
        self.mouse_start = 0
        self.shift = [0, 0]
        self.hovered = [False, False]


class menu:
    def __init__(self):
        self.hovered = [False, False]

    def hover(self, mouse_pos):
        self.hovered[0] = pygame.Rect(166, 310, 356, 85).collidepoint(mouse_pos[0], mouse_pos[1])
        self.hovered[1] = pygame.Rect(678, 310, 356, 85).collidepoint(mouse_pos[0], mouse_pos[1])

    def draw(self, mouse_pos):
        details.screen.fill((211, 238, 202))
        pygame.draw.rect(details.screen, (156, 196, 153), (166, 310, 356, 85))

        details.draw_text("Построение Генеалогического древа", (600, 159 - 20), (0, 0, 0), False, font48)
        pygame.draw.rect(details.screen, (0, 0, 0), (600 - 3, 199, 6, 60))
        pygame.draw.rect(details.screen, (0, 0, 0), (341, 260 - 3, 518, 6))
        pygame.draw.rect(details.screen, (0, 0, 0), (341, 259, 6, 51))
        pygame.draw.rect(details.screen, (0, 0, 0), (853, 259, 6, 51))

        size = 1 if not self.hovered[0] else 5
        pygame.draw.rect(details.screen, (0, 0, 0), (166, 310, 356, 85), size)
        details.draw_text("Создать новое дерево", (166 + 178, 346 - 15), (0, 0, 0), False, window.font32)

        pygame.draw.rect(details.screen, (156, 196, 153), (678, 310, 356, 85))
        size = 1 if not self.hovered[1] else 5
        pygame.draw.rect(details.screen, (0, 0, 0), (678, 310, 356, 85), size)
        details.draw_text("Загрузить дерево", (678 + 178, 346 - 15), (0, 0, 0), False, window.font32)

    def press(self, event, mouse_pos):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.hovered[0]:
                return tree_empty
            elif self.hovered[1]:
                return tree_Ivanovs
