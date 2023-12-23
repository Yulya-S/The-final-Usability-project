import pygame
import pyperclip

pygame.init()
screen = pygame.display.set_mode((1200, 720), pygame.SCALED)
font = pygame.font.SysFont('Comic Sans MS', 25)


class Text:
    def __init__(self, text):
        self.text = text

    def split_to_size(self, width: int = 300, otherFont=font):
        text = self.text.split(' ')
        text_copy = []
        lines = []
        for i in text:
            if otherFont.render(' '.join(text_copy + [i]), True, (34, 0, 0)).get_width() > width - 20:
                lines.append(' '.join(text_copy + ['']))
                big_word = ''
                if otherFont.render(i, True, (34, 0, 0)).get_width() > width - 20:
                    for l in i:
                        if otherFont.render(big_word + l, True, (34, 0, 0)).get_width() > width - 20:
                            lines.append(big_word)
                            big_word = ''
                        big_word += l
                else:
                    text_copy = [i]
                if big_word != '':
                    text_copy = [big_word]
            else:
                text_copy.append(i)
        lines.append(' '.join(text_copy))
        return lines


class Text_container:
    def __init__(self, text: str, mod: str = "text", width: int = 300, height: int = 0):
        self.text = Text(text)
        self.width = width
        self.height = 55 if height == 0 else height
        self.hovered = False
        self.active = False
        self.mod = mod
        self.animation = 0
        self.offset = 0
        self.press = 0

    def hover(self, mouse_pos, coordinate):
        self.hovered = pygame.Rect(coordinate[0], coordinate[1], self.width, self.height)
        self.hovered = self.hovered.collidepoint(mouse_pos[0], mouse_pos[1])
        return self.hovered

    def draw(self, coordinate, colors, other_guidance: bool = False, lineHeight=50, otherFont=font):
        rect = pygame.Rect(coordinate[0], coordinate[1], self.width, self.height)
        self.hovered = self.hovered and not other_guidance
        Draw_block_with_text(self.text.split_to_size(self.width), (coordinate[0], coordinate[1]),
                             (self.width, self.height), colors[1:], (0 < self.animation < 15), True, self.offset,
                             lineHeight=lineHeight, otherFont=otherFont)
        self.animation += 1
        if self.animation > 29 or not self.active:
            self.animation = 0

        if self.animation % 3 == 0:
            if (self.press == 2 and self.offset < len(self.text.text)):
                self.text.text = self.text.text[:len(self.text.text) - self.offset - 1] + \
                                 self.text.text[len(self.text.text) - self.offset:]
            elif (self.press == 3 and self.offset > 0):
                self.text.text = self.text.text[:len(self.text.text) - self.offset] + \
                                 self.text.text[len(self.text.text) - self.offset + 1:]
                self.offset -= 1
            elif ((self.press == 1 and self.offset < len(self.text.text)) or (self.press == -1 and self.offset > 0)):
                self.offset += self.press

        if self.active:
            pygame.draw.rect(screen, colors[3], rect, 1)
        elif self.hovered:
            pygame.draw.rect(screen, colors[0], rect, 1)
        else:
            pygame.draw.rect(screen, colors[2], rect, 1)

    def write(self, event):
        if event.key != pygame.K_TAB:
            text = self.text.text[:len(self.text.text) - self.offset] + str(event.unicode) + \
                   self.text.text[len(self.text.text) - self.offset:]
            if self.mod != 'number' and len(text) <= 255:
                self.text.text = text
            elif self.mod == 'number' and text.isdigit() and int(text) < 9223372036854775807:
                self.text.text = text

    def Press(self, event):
        if event.type == pygame.KEYUP and \
                (event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_BACKSPACE, pygame.K_DELETE]):
            self.press = 0
        elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.hovered):
            self.active = True
            return True
        elif (event.type == pygame.KEYDOWN and self.active):
            if event.key == pygame.K_RETURN:
                self.active = False
            elif event.key == pygame.K_LEFT:
                self.press = 1
            elif event.key == pygame.K_RIGHT:
                self.press = -1
            elif event.key == pygame.K_BACKSPACE:
                self.press = 2
            elif event.key == pygame.K_DELETE:
                self.press = 3
            elif event.mod & pygame.KMOD_CTRL:
                if event.key == pygame.K_c:
                    pyperclip.copy(self.text)
                elif event.key == pygame.K_v:
                    self.text.text = self.text[:len(self.text.text) - self.offset] + pyperclip.paste() + \
                                     self.text[len(self.text.text) - self.offset:]
            else:
                self.write(event)


class Button:
    def __init__(self, text: str, width: int = 300, height: int = 0):
        self.text = Text(text)
        self.width = width
        self.height = 5 + 50 * len(self.text.split_to_size(self.width)) if height == 0 else height
        self.hovered = False

    def hover(self, mouse_pos, coordinate):
        self.hovered = pygame.Rect(coordinate[0], coordinate[1], self.width, self.height)
        self.hovered = self.hovered.collidepoint(mouse_pos[0], mouse_pos[1])
        return self.hovered

    def draw(self, coordinate, colors: list, other_hovered: bool = False):
        self.hovered = self.hovered and not other_hovered
        text = self.text.split_to_size(self.width)
        Draw_block_with_text(text, coordinate, (self.width, self.height), colors[1:])
        if self.hovered:
            pygame.draw.rect(screen, colors[0], (coordinate[0], coordinate[1], self.width, self.height), 1)
        else:
            pygame.draw.rect(screen, colors[2], (coordinate[0], coordinate[1], self.width, self.height), 1)

    def Press(self, event):
        return self.hovered and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1


def Draw_block_with_text(text: list, coordinate: tuple, size: tuple, colors, animation=False, left=False, offset=0,
                         lineHeight=50, otherFont=font):
    pygame.draw.rect(screen, colors[0], (coordinate[0], coordinate[1], size[0], size[1]))
    if text[0] == '' and len(text) > 1:
        text.pop(0)

    line = 0
    for i in range(len(text) - 1):
        if offset > len(text[(i * -1) - 1]):
            offset -= len(text[(i * -1) - 1])
            line += 1
        else:
            break
    if (line + 1 > len(text) and offset > len(text[0])):
        offset = len(text[0])
    copy_line = line

    if len(text) - line - (size[1] // lineHeight) < 0:
        line = len(text) - (size[1] // lineHeight)
    text_for_draw = text[len(text) - line - (size[1] // lineHeight): len(text) - line]
    for i in range(len(text_for_draw)):
        text_b = otherFont.render(text_for_draw[i], True, colors[1])
        text_rect = text_b.get_rect(
            center=(coordinate[0] + size[0] / 2, coordinate[1] + lineHeight * i + lineHeight // 2))
        if left:
            text_rect.left = coordinate[0] + 10
        screen.blit(text_b, text_rect)

    if animation:
        left_margin = otherFont.render(text[(copy_line * -1) - 1][:len(text[(copy_line * -1) - 1]) - offset], True,
                                       (0, 0, 0)).get_width()
        copy_line = len(text) - copy_line - 1 if len(text) - copy_line < size[1] // lineHeight else size[
                                                                                                        1] // lineHeight - 1
        pygame.draw.rect(screen, colors[1],
                         (coordinate[0] + left_margin + 9, coordinate[1] + 10 + lineHeight * copy_line, 1, otherFont.get_height()))

    if text[0] != text_for_draw[0]:
        draw_text('<-', (coordinate[0] + 3, coordinate[1] - 10), colors[1], True, otherFont=otherFont)
    if text[-1] != text_for_draw[-1]:
        draw_text('->', (coordinate[0] - 23 + size[0], coordinate[1] + size[1] - 30), colors[1], True,
                  otherFont=otherFont)


def draw_line(x, y, left: int = 0, top: int = 0, color=(0, 0, 0)):
    return pygame.draw.line(screen, color, [x, y], [x + left, y + top], 5)


def draw_line_to_end(x, y, left_end: int = None, top_end: int = None, color=(0, 0, 0)):
    return pygame.draw.line(screen, color, [x, y],
                            [left_end if (left_end != None) else x, top_end if (top_end != None) else y], 5)


def draw_text(text: str, coordinate: tuple, color, left: bool = True, otherFont=font):
    text = otherFont.render(text, True, color)
    if left:
        text_rect = text.get_rect(center=(coordinate[0] + text.get_width() / 2, coordinate[1] + text.get_height() / 2))
    else:
        text_rect = text.get_rect(center=(coordinate[0], coordinate[1] + text.get_height() // 2))
    screen.blit(text, text_rect)
