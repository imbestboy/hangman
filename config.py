import customtkinter

# --  main menu config
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

temp_window.destroy()
