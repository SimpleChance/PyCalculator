"""
Main program loop for the GUI version of PyCalc.
"""
from sys import exit
from enum import Enum
import pygame as pg
import pygame_gui as pg_gui
from pygame_gui.elements import UIButton
from pygame_gui.elements import UILabel
import pycalc


class STATES(Enum):
    INIT = 0
    FIRST_INPUT = 1
    OPERATION = 2
    SECOND_INPUT = 3
    RESULT = 4

class GUI_PyCalc(object):
    def __init__(self, window_dimensions):
        pg.init()
        self.window_dimensions = window_dimensions
        self.window_surface = pg.display.set_mode(window_dimensions)
        self.background_surface = pg.Surface(window_dimensions)
        self.ui_manager = pg_gui.UIManager(window_dimensions, 'data/themes/theme1.json')

        self.numeric_buttons: dict[str, UIButton] = dict.fromkeys(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '+/-'])
        self.operation_buttons: dict[str, UIButton] = dict.fromkeys(['=', 'CE', '+', '-', '*', '/', 'x^y', 'yroot(x)'])
        self.text_box: UILabel

        self.state = STATES.INIT

        self.x: float = 0
        self.y: float = 0
        self.result: float = 0
        self.prev_op: str = ""
        self.input_str: str = ""
        self.display_str: str = "0"

        self._initialize()

    def _initialize(self):
        pg.display.set_caption('PyCalc GUI')

        # Text box
        text_box_size = (self.window_dimensions[0], self.window_dimensions[1]//5)
        self.text_box = UILabel(relative_rect=pg.Rect((0, 0), text_box_size), text='0',
                              object_id="label")

        # Numerics
        button_size = (self.window_dimensions[0]//5, self.window_dimensions[1]//5)
        tmp = 1
        for i in range(2, -1, -1):
            for j in range(3):
                button_pos = (j * button_size[0], i * button_size[1] + text_box_size[1])
                label = str(tmp)
                tmp += 1
                new_button = UIButton(relative_rect=pg.Rect(button_pos, button_size), text=label, object_id="numeric_button")
                self.numeric_buttons[label] = new_button
        button_pos = (button_size[0], 3 * button_size[1] + text_box_size[1])
        new_button = UIButton(relative_rect=pg.Rect(button_pos, button_size), text='0', object_id="numeric_button")
        self.numeric_buttons['0'] = new_button
        button_pos = (0, 3 * button_size[1] + text_box_size[1])
        new_button = UIButton(pg.Rect(button_pos, button_size), text='.', object_id="numeric_button")
        self.numeric_buttons['.'] = new_button
        button_pos = (button_size[0] * 3, text_box_size[1])
        new_button = UIButton(pg.Rect(button_pos, button_size), text='+/-', object_id="numeric_button")
        self.numeric_buttons['+/-'] = new_button

        # Operations
        button_pos = (button_size[0] * 2, 3 * button_size[1] + text_box_size[1])
        new_button = UIButton(pg.Rect(button_pos, button_size), text='=', object_id="operation_button")
        self.operation_buttons['='] = new_button
        button_pos = (button_size[0] * 4, text_box_size[1])
        new_button = UIButton(pg.Rect(button_pos, button_size), text='CE', object_id="operation_button")
        self.operation_buttons['CE'] = new_button

        tmp = ['x^y', 'yroot(x)', '*', '/', '+', '-']
        _ = 0
        for i in range(1, 4):
            for j in range(3, 5):
                button_pos = (j * button_size[0], i * button_size[1] + text_box_size[1])
                new_button = UIButton(pg.Rect(button_pos, button_size), text=tmp[_], object_id="operation_button")
                self.operation_buttons[tmp[_]] = new_button
                _ += 1

    def clear(self):
        self.x  = 0
        self.y = 0
        self.result = 0
        self.input_str = ""
        self.display_str = "0"
        self.prev_op = ""
        self.state = STATES.FIRST_INPUT

    def draw(self, dt):
        self.ui_manager.update(dt)

        self.window_surface.blit(self.background_surface, (0, 0))
        self.ui_manager.draw_ui(self.window_surface)

        pg.display.flip()

    def append_input(self, input_button):
        if input_button == self.numeric_buttons['0'] and len(self.input_str) == 1 and self.input_str[0]:
            pass
        elif input_button == self.numeric_buttons['.'] and '.' in self.input_str:
            pass
        elif input_button == self.numeric_buttons['+/-']:
            if self.input_str[0] == '-':
                self.input_str.replace('-', '')
            else:
                self.input_str = '-' + self.input_str
            self.display_str = self.input_str
        else:
            index = list(self.numeric_buttons.values()).index(input_button)
            self.input_str += list(self.numeric_buttons.keys())[index]
            self.display_str = self.input_str

    def update(self, input_button):
        if input_button in self.numeric_buttons:
            if self.state == STATES.RESULT:
                self.input_str = ''
                self.state = STATES.FIRST_INPUT
            self.append_input(input_button)

        elif input_button in self.operation_buttons:
            if input_button == self.operation_buttons['CE']:
                self.clear()
            elif self.state == STATES.INIT or self.state == STATES.FIRST_INPUT:
                self.x = float(self.input_str)
                self.input_str = ''
                self.state = STATES.SECOND_INPUT
            elif self.state == STATES.SECOND_INPUT:
                self.y = float(self.input_str)
                self.input_str = ''
                self.state = STATES.RESULT
            elif self.state == STATES.RESULT:
                self.state == STATES.SECOND_INPUT

            match self.prev_op:
                case '+':
                    self.result = pycalc.add(self.x, self.y)
                case '-':
                    self.result =

            index = list(self.operation_buttons.values()).index(input_button)
            op = list(self.operation_buttons.keys())[index]
            if op != 'CE' or op != '=':
                self.prev_op = op


def check_input(calcGUI_object):
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            pg.quit()
            exit()

        if event.type == pg_gui.UI_BUTTON_PRESSED:
            calcGUI_object.update(event.ui_element)


        calcGUI_object.ui_manager.process_events(event)


def run() -> None:
    pg.init()

    window_dimensions = (300, 340)
    calcGUI = GUI_PyCalc(window_dimensions)

    clock = pg.time.Clock()
    max_fps = 60
    dt: float

    while True:
        dt = clock.tick(max_fps) / 1000.0
        check_input(calcGUI)
        calcGUI.draw(dt)


if __name__ == '__main__':
    run()
