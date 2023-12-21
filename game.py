import customtkinter
import pygame
import math

import main_menu
import config
import functions


def start_game(main_menu_window: customtkinter.CTk) -> None:
    """start_game close main menu and start the game

    Arguments:
        main_menu_window {customtkinter.CTk} -- tkinter main menu window
        theme {str} -- game theme string 'dark' or 'light'
    """
    # -- loading settings
    game_background_color = main_menu_window["bg"]
    dark_mode = main_menu_window["bg"] == "gray14"
    hangman_color = "gray92" if dark_mode else "gray14"
    keyboard_color = "gray92" if dark_mode else "gray14"

    main_menu_window.destroy()

    # -- pygame setup
    pygame.init()
    clock = pygame.time.Clock()
    is_running = True

    # -- game window size
    game_screen = pygame.display.set_mode(
        (config.GAME_SCREEN_WIDTH, config.GAME_SCREEN_HEIGHT)
    )
    used_characters = []
    hangman_step = 0

    # -- game loop
    while is_running:
        for event in pygame.event.get():
            # -- pygame.QUIT event means the user clicked X to close your window
            if event.type == pygame.QUIT:
                is_running = False
                main_menu.start_main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked_mouse_x, clicked_mouse_y = pygame.mouse.get_pos()
                for x, y, character, is_visible in keyboard:
                    if is_visible:
                        distance = math.sqrt(
                            (x - clicked_mouse_x) ** 2 + (y - clicked_mouse_y) ** 2
                        )
                        if distance < config.WIDTH // 2:
                            used_characters.append(character)

        game_screen.fill(game_background_color)

        functions.draw_hangman(game_screen, hangman_step, hangman_color)
        keyboard = functions.draw_keyboard(game_screen, used_characters, keyboard_color)

        pygame.display.update()

        # -- set FPS to 60
        clock.tick(60)

    # -- close game window
    pygame.quit()
