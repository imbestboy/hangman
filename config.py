import customtkinter

# -- MAIN MENU SECTION

# --  main menu screen config
MAIN_MENU_SCREEN_WIDTH: int = 1000
MAIN_MENU_SCREEN_HEIGHT: int = 400

# -- theme config
customtkinter.set_default_color_theme("green")
customtkinter.set_appearance_mode("system")

# -- creating temp window for config fonts this window will destroy
temp_window = customtkinter.CTk()

# -- font config
normal_font = customtkinter.CTkFont("Helvetica", 20)
bold_font = customtkinter.CTkFont("Helvetica", 20, "bold")
small_normal_font = customtkinter.CTkFont("Helvetica", 15)
small_bold_font = customtkinter.CTkFont("Helvetica", 15, "bold")

temp_window.destroy()

# -- GAME SECTION

# -- game screen config
GAME_SCREEN_WIDTH = 800
GAME_SCREEN_HEIGHT = 600

# -- keyboard config
WIDTH = 40
GAP = 15
START_X = round((GAME_SCREEN_WIDTH - (WIDTH + GAP) * 13) / 2)
START_Y = 450
