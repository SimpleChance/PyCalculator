"""
Main program loop for the GUI version of PyCalc.
"""
from sys import exit
import pygame as pg
import pygame_gui as pg_gui
from pygame_gui.elements import UIButton
import pycalc


def initialize_ui_buttons() -> dict[str, UIButton]:
    button_dictionary = dict.fromkeys(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '+/-', '=', 'CE', '+',
                                       '-', '*', '/', 'x^y', 'yroot(x)'])
    y_offset = 100

    # Numerics
    button_size = (60, 60)
    pos = (0, 3*button_size[1] + y_offset)
    new_button = UIButton(relative_rect=pg.Rect(pos, button_size), text='0')
    button_dictionary['0'] = new_button
    tmp = 1
    for i in range(2, -1, -1):
        for j in range(3):
            pos = (j * button_size[0], i * button_size[1] + y_offset)
            label = str(tmp)
            tmp += 1
            new_button = UIButton(relative_rect=pg.Rect(pos, button_size), text=label)
            button_dictionary[label] = new_button

    # Decimal and Equals
    pos = (button_size[0], 3*button_size[1] + y_offset)
    new_button = UIButton(pg.Rect(pos, button_size), text='.')
    button_dictionary['.'] = new_button

    pos = (button_size[0]*2, 3*button_size[1] + y_offset)
    new_button = UIButton(pg.Rect(pos, button_size), text='=')
    button_dictionary['='] = new_button

    # Operations
    tmp = ['x^y', 'yroot(x)', '*', '/', '+', '-']
    _ = 0
    for i in range(3):
        for j in range(3, 5):
            pos = (j * button_size[0], i * button_size[1] + y_offset)
            new_button = UIButton(pg.Rect(pos, button_size), text=tmp[_])
            button_dictionary[tmp[_]] = new_button
            _ += 1

    return button_dictionary


def run() -> None:
    pg.init()
    pg.display.set_caption("PyCalc GUI by Chance Jewell")

    window_dimensions = (300, 340)
    window_surface = pg.display.set_mode(window_dimensions)

    background_surface = pg.Surface(window_dimensions)
    background_surface.fill(pg.Color('black'))

    ui_manager = pg_gui.UIManager(window_dimensions)

    button_dictionary = initialize_ui_buttons()

    clock = pg.time.Clock()
    max_fps = 60
    dt: float

    display_str = ""
    input_length = 0
    x: float = 0
    y: float
    dec = False
    while True:
        dt = clock.tick(max_fps) / 1000.0
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                exit()

            if event.type == pg_gui.UI_BUTTON_PRESSED:
                input_length = len(display_str)
                if event.ui_element == button_dictionary['0']:
                    if input_length == 1 and display_str[0] == '0':
                        pass
                    else:
                        display_str += '0'
                if event.ui_element == button_dictionary['1']:
                    display_str += '1'
                if event.ui_element == button_dictionary['2']:
                    display_str += '2'
                if event.ui_element == button_dictionary['3']:
                    display_str += '3'
                if event.ui_element == button_dictionary['4']:
                    display_str += '4'
                if event.ui_element == button_dictionary['5']:
                    display_str += '5'
                if event.ui_element == button_dictionary['6']:
                    display_str += '6'
                if event.ui_element == button_dictionary['7']:
                    display_str += '7'
                if event.ui_element == button_dictionary['8']:
                    display_str += '8'
                if event.ui_element == button_dictionary['9']:
                    display_str += '9'

                if event.ui_element == button_dictionary['.'] and not dec:
                    if input_length == 0:
                        display_str += '0'
                        display_str += '.'
                        dec = True

                if input_length == 0:
                    pass
                else:
                    if event.ui_element == button_dictionary['+']:
                        if display_str[-1] == '.':
                            display_str = display_str[0::-1]


            ui_manager.process_events(event)
        ui_manager.update(dt)

        window_surface.blit(background_surface, (0, 0))
        ui_manager.draw_ui(window_surface)

        pg.display.flip()


if __name__ == '__main__':
    run()
