import customtkinter

import config
import functions
import game


def start_main_menu() -> customtkinter.CTk:
    """start_main_menu create main menu window

    Returns:
        customtkinter.CTk -- main menu window
    """
    # -- create main menu window
    main_menu_window = customtkinter.CTk()

    # -- main menu window config
    main_menu_window.geometry(
        f"{config.MAIN_MENU_SCREEN_WIDTH}x{config.MAIN_MENU_SCREEN_HEIGHT}"
    )
    main_menu_window.title("Main Menu")
    main_menu_window.resizable(False, False)

    # -- theme section in main menu
    theme_frame = customtkinter.CTkFrame(
        main_menu_window, config.MAIN_MENU_SCREEN_WIDTH, fg_color="transparent"
    )

    customtkinter.CTkLabel(
        theme_frame,
        text="Choose game theme (default : system) : ",
        font=config.normal_font,
    ).grid(column=0, row=0, padx=10)
    customtkinter.CTkButton(
        theme_frame, text="Dark", command=lambda: functions.change_theme("dark")
    ).grid(column=1, row=0)
    customtkinter.CTkButton(
        theme_frame, text="Light", command=lambda: functions.change_theme("light")
    ).grid(column=2, row=0, padx=10)

    theme_frame.pack(pady=30)

    # -- change word category
    change_category_frame = customtkinter.CTkFrame(
        main_menu_window, config.MAIN_MENU_SCREEN_WIDTH, fg_color="transparent"
    )
    customtkinter.CTkLabel(
        change_category_frame,
        text="Word Category : ",
        font=config.normal_font,
    ).grid(column=0, row=0, padx=10)

    words = functions.load_words()
    categories = list(words.keys())
    optionmenu_var = customtkinter.StringVar(value=categories[0])
    optionmenu = customtkinter.CTkOptionMenu(
        change_category_frame,
        values=categories,
        variable=optionmenu_var,
        font=config.small_bold_font,
    ).grid(column=1, row=0, padx=10)

    change_category_frame.pack()

    # -- start game section
    start_game_frame = customtkinter.CTkFrame(
        main_menu_window, width=config.MAIN_MENU_SCREEN_WIDTH, fg_color="transparent"
    )

    customtkinter.CTkButton(
        start_game_frame,
        text="Start game",
        command=lambda: game.start_game(
            main_menu_window=main_menu_window, category=optionmenu_var
        ),
        width=220,
        height=50,
        font=config.bold_font,
    ).grid(column=2, row=0, padx=55)

    customtkinter.CTkButton(
        start_game_frame,
        text="Quit",
        command=main_menu_window.destroy,
        width=220,
        height=50,
        font=config.normal_font,
    ).grid(column=0, row=0, padx=55)

    start_game_frame.pack(pady=30)

    return main_menu_window
