"""
Main program loop for the GUI version of PyCalc.
"""
from sys import exit
import pygame as pg
import pygame_gui as pg_gui
from pygame_gui.elements import UIButton
import pycalc


def initialize_ui_buttons() -> tuple[dict[str, UIButton], dict[str, UIButton]]:
    button_dictionary = dict.fromkeys(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '+/-'])
    operations_dictionary = dict.fromkeys(['=', 'CE', '+', '-', '*', '/', 'x^y', 'yroot(x)'])
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
    operations_dictionary['='] = new_button

    pos = (button_size[0]*3, 3 * button_size[1] + y_offset)
    new_button = UIButton(pg.Rect(pos, button_size), text='+/-')
    button_dictionary['+/-'] = new_button

    pos = (button_size[0] * 4, 3 * button_size[1] + y_offset)
    new_button = UIButton(pg.Rect(pos, button_size), text='CE')
    operations_dictionary['CE'] = new_button

    # Operations
    tmp = ['x^y', 'yroot(x)', '*', '/', '+', '-']
    _ = 0
    for i in range(3):
        for j in range(3, 5):
            pos = (j * button_size[0], i * button_size[1] + y_offset)
            new_button = UIButton(pg.Rect(pos, button_size), text=tmp[_])
            operations_dictionary[tmp[_]] = new_button
            _ += 1

    return button_dictionary, operations_dictionary


def run() -> None:
    pg.init()
    pg.display.set_caption("PyCalc GUI by Chance Jewell")

    window_dimensions = (300, 340)
    window_surface = pg.display.set_mode(window_dimensions)

    background_surface = pg.Surface(window_dimensions)
    background_surface.fill(pg.Color('black'))

    ui_manager = pg_gui.UIManager(window_dimensions)

    button_dictionary, operations_dictionary = initialize_ui_buttons()

    clock = pg.time.Clock()
    max_fps = 60
    dt: float

    input_str = ''
    input_length = 0
    prev_op = ''
    negative_flag = False
    while True:
        print(input_str)
        dt = clock.tick(max_fps) / 1000.0
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                exit()

            if event.type == pg_gui.UI_BUTTON_PRESSED:
                input_length = len(input_str)
                # Numerics
                if event.ui_element in button_dictionary.values():
                    if event.ui_element == button_dictionary['0'] and input_length == 1 and input_str[0] == '0':
                        pass
                    elif event.ui_element == button_dictionary['.'] and '.' in input_str:
                        pass
                    elif event.ui_element == button_dictionary['+/-']:
                        if negative_flag:
                            input_str = input_str.replace('-', '')
                        else:
                            input_str = '-' + input_str
                        negative_flag = not negative_flag
                    else:
                        position = list(button_dictionary.values()).index(event.ui_element)
                        input_str += list(button_dictionary.keys())[position]
                # Operations
                if event.ui_element in operations_dictionary.values():
                    if event.ui_element == operations_dictionary['=']:
                        pass
                    elif event.ui_element == operations_dictionary['CE']:
                        input_str = ''
                        prev_op = ''
                    else:
                        position = list(operations_dictionary.values()).index(event.ui_element)
                        prev_op = list(operations_dictionary.keys())[position]

                    match prev_op:
                        case '+':
                            pass
                        case '-':
                            pass
                        case '*':
                            pass
                        case '/':
                            pass
                        case 'x^y':
                            pass
                        case 'yroot(x)':
                            pass
                        case _:
                            pass



            ui_manager.process_events(event)

        ui_manager.update(dt)

        window_surface.blit(background_surface, (0, 0))
        ui_manager.draw_ui(window_surface)

        pg.display.flip()


if __name__ == '__main__':
    run()
