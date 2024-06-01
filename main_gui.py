"""
Main program loop for the GUI version of PyCalc.
"""
import pygame as pg
import pygame_gui as pg_gui
import pycalc


def main() -> None:
    pg.init()
    pg.display.set_caption('PyCalc by Chance Jewell')

    settings: dict = {
        'Window Dimensions': (400, 400),
        'Max FPS': 60,
    }
    settings['Button Size'] = (settings['Window Dimensions'][0] // 5, settings['Window Dimensions'][1] // 5)
    settings['Display Field Size'] = (settings['Window Dimensions'][0], settings['Button Size'][1])

    # Initialize all surfaces and UIManager
    window_surface: pg.Surface = pg.display.set_mode(settings['Window Dimensions'])
    background: pg.Surface = pg.Surface(settings['Window Dimensions'])
    background.fill(pg.Color('black'))
    manager: pg_gui.UIManager = pg_gui.UIManager(settings['Window Dimensions'])

    # Create and store all buttons
    # Numerics
    numeric_buttons: list[pg_gui.elements.UIButton] = []
    label: int = 0
    for i in range(3):
        for j in range(3):
            new_numeric_button: pg_gui.elements.UIButton = pg_gui.elements.UIButton(relative_rect=pg.Rect(
                                        (j*settings['Button Size'][0],
                                         settings['Display Field Size'][1] + i * settings['Button Size'][1]),
                                        (settings['Button Size'][0], settings['Button Size'][1])),
                                        text=str(label + 1),
                                        manager=manager)
            numeric_buttons.append(new_numeric_button)
            label += 1
    new_numeric_button = pg_gui.elements.UIButton(relative_rect=pg.Rect(
                                        (settings['Button Size'][0],
                                         settings['Display Field Size'][1] + 3 * settings['Button Size'][1]),
                                        (settings['Button Size'][0], settings['Button Size'][1])),
                                        text='0',
                                        manager=manager)
    numeric_buttons.append(new_numeric_button)
    # Operations
    operation_buttons: list[pg_gui.elements.UIButton] = []
    labels: list[str] = ['+', '-', '*', '/', 'x^y', 'yroot(x)', 'clr', '+M/-M', '.', '=']
    ind: int = 0
    for i in range(4):
        for j in range(2):
            new_operation_button = pg_gui.elements.UIButton(relative_rect=pg.Rect(
                                        (3*settings['Button Size'][0] + j * settings['Button Size'][0],
                                         settings['Button Size'][1] + i * settings['Button Size'][1]),
                                        (settings['Button Size'][0], settings['Button Size'][1])),
                                        text=labels[ind],
                                        manager=manager)
            operation_buttons.append(new_operation_button)
            ind += 1
    new_operation_button = pg_gui.elements.UIButton(relative_rect=pg.Rect(
                                                    (0, settings['Button Size'][1] + 3 * settings['Button Size'][1]),
                                                    (settings['Button Size'][0], settings['Button Size'][1])),
                                                    text=labels[ind],
                                                    manager=manager)
    operation_buttons.append(new_operation_button)
    ind += 1
    new_operation_button = pg_gui.elements.UIButton(relative_rect=pg.Rect(
                                                    (2 * settings['Button Size'][0],
                                                     settings['Button Size'][1] + 3 * settings['Button Size'][1]),
                                                    (settings['Button Size'][0], settings['Button Size'][1])),
                                                    text=labels[ind],
                                                    manager=manager)
    operation_buttons.append(new_operation_button)

    # Simulation loop
    clock: pg.time.Clock = pg.time.Clock()
    running: bool = True
    numeric_input: str = ""
    operation: str = ""
    while running:
        time_delta = clock.tick(settings['Max FPS']) / 1000.0
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                running = False
            if event.type == pg_gui.UI_BUTTON_PRESSED:
                if event.ui_element == numeric_buttons[0]:
                    print("Number '1' pressed!")

            manager.process_events(event)

        manager.update(time_delta)

        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)

        pg.display.flip()


if __name__ == '__main__':
    main()
