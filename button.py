import pygame
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BRIGHT_RED = (238, 75, 43)
LIGHT_BLUE = (173, 216, 230)


class ToggleButton:
    def __init__(self, x, y, width):
        self.x = x

        self.y = y

        self.width = width

        self.colour = WHITE

    def draw(self, WIN):
        pygame.draw.rect(WIN, self.colour,
                         pygame.Rect(self.x, self.y, self.width, self.width))
        pygame.draw.line(WIN, BLACK, (self.x, self.y), (self.x, self.y+self.width), width=2)
        pygame.draw.line(WIN, BLACK, (self.x+self.width, self.y), (self.x+self.width, self.y+self.width), width=2)
        pygame.draw.line(WIN, BLACK, (self.x, self.y+self.width), (self.x+self.width, self.y+self.width), width=2)
        pygame.draw.line(WIN, BLACK, (self.x, self.y), (self.x+self.width, self.y), width=2)

        myfont = pygame.font.SysFont("Comic Sans MS", 35)
        # apply it to text on a label
        label = myfont.render("History Grid", 1, BLACK)
        # put the label object on the screen at point x=100, y=100
        WIN.blit(label, (self.x+25, self.y-2))

    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.width:
                print("isOver")
                if self.colour == WHITE:
                    self.colour = BRIGHT_RED
                else:
                    self.colour = WHITE
                return True

        return False

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y


class button():

    def __init__(self, color, x,   y, width, height, text=''):
        self.x = x
        self.y = y
        self.color = color
        self.height = height
        self.width = width
        self.text = text

    def draw(self, win, outline=None):
        if outline:
            pygame.draw.rect(win, outline, (self.x-2, self.y-2, self.width+4, self.height+4), 0)
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (self.x +(self.width/2-text.get_width()/2), self.y +(self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                print(self.text)
                return True

        return False


class OptionBox():

    def __init__(self, x, y, w, h, color, highlight_color, font, option_list, title, selected=0):
        self.color = color
        self.highlight_color = highlight_color
        self.rect = pygame.Rect(x, y, w, h)
        self.font = font
        self.option_list = option_list
        self.title = title
        self.selected = selected
        self.draw_menu = False
        self.menu_active = False
        self.active_option = -1

    def draw(self, surf):
        myfont = pygame.font.SysFont("Comic Sans MS", 35)
        label = myfont.render(self.title, 1, BLACK)

        surf.blit(label, (self.rect.x, self.rect.y - 30))
        pygame.draw.rect(surf, self.highlight_color if self.menu_active else self.color, self.rect)
        pygame.draw.rect(surf, (0, 0, 0), self.rect, 2)
        msg = self.font.render(self.option_list[self.selected], 1, (0, 0, 0))
        surf.blit(msg, msg.get_rect(center=self.rect.center))

        if self.draw_menu:
            for i, text in enumerate(self.option_list):
                rect = self.rect.copy()
                rect.y += (i + 1) * self.rect.height
                pygame.draw.rect(surf, self.highlight_color if i == self.active_option else self.color, rect)
                msg = self.font.render(text, 1, (0, 0, 0))
                surf.blit(msg, msg.get_rect(center=rect.center))
            outer_rect = (
            self.rect.x, self.rect.y + self.rect.height, self.rect.width, self.rect.height * len(self.option_list))
            pygame.draw.rect(surf, (0, 0, 0), outer_rect, 2)

    def update(self, event_list):
        mpos = pygame.mouse.get_pos()
        self.menu_active = self.rect.collidepoint(mpos)

        self.active_option = -1
        for i in range(len(self.option_list)):
            rect = self.rect.copy()
            rect.y += (i + 1) * self.rect.height
            if rect.collidepoint(mpos):
                self.active_option = i
                break

        if not self.menu_active and self.active_option == -1:
            self.draw_menu = False

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.menu_active:
                    self.draw_menu = not self.draw_menu
                elif self.draw_menu and self.active_option >= 0:
                    self.selected = self.active_option
                    self.draw_menu = False
                    return self.active_option
        return -1

    def isOver(self, pos):
        if pos[0] > self.rect.x and pos[0] < self.rect.x + self.rect.y:
            if pos[1] > self.rect.y and pos[1] < self.rect.y + self.rect.h:
                print("CIAO")
                return True

        return False

    def set_rect_x(self, x):
        self.rect.x = x

    def set_selected(self, select_option):
        self.selected = select_option


