import customtkinter
import pygame

import config


def change_theme(theme: str) -> None:
    """change_theme change application theme

    Arguments:
        theme {str} -- only "dark" , "light" and "system"
    """
    if theme in ("dark", "light", "system"):
        customtkinter.set_appearance_mode(theme)
    else:
        raise ValueError("theme should be in 'dark' , 'light' and 'system'")


def draw_hangman(screen: pygame.surface.Surface, step: int, color: str) -> None:
    """draw_hangman draw hangman on game screen

    Arguments:
        screen {pygame.surface.Surface} -- game screen
        step {int} -- how many of hangman should draw
        color {str} -- hangman color
    """
    if step >= 1:
        footer_rect = pygame.Rect(75, 350, 300, 10)
        pygame.draw.rect(screen, color, footer_rect)
    if step >= 2:
        body_rect = pygame.Rect(125, 75, 10, 275)
        pygame.draw.rect(screen, color, body_rect)
    if step >= 3:
        horizontal_header_rect = pygame.Rect(body_rect.x, body_rect.y, 150, 10)
        pygame.draw.rect(screen, color, horizontal_header_rect)
    if step >= 4:
        vertical_header_rect = pygame.Rect(
            horizontal_header_rect.right, body_rect.y, 10, 50
        )
        pygame.draw.rect(screen, color, vertical_header_rect)
    if step >= 5:
        man_head = pygame.draw.circle(
            screen,
            color,
            (280, 155),
            30,
            4,
        )
    if step >= 6:
        man_body = pygame.Rect(man_head.centerx - 2, man_head.bottom, 4, 75)
        pygame.draw.rect(screen, color, man_body)
    if step >= 7:
        pygame.draw.line(
            screen,
            color,
            (man_body.centerx, man_body.centery - 20),
            (man_body.centerx + 40, man_body.centery + 10),
            4,
        )
    if step >= 8:
        pygame.draw.line(
            screen,
            color,
            (man_body.centerx, man_body.centery - 20),
            (man_body.centerx - 40, man_body.centery + 10),
            4,
        )
    if step >= 9:
        pygame.draw.line(
            screen,
            color,
            (man_body.centerx - 2, man_body.bottom),
            (man_body.centerx - 30, man_body.bottom + 40),
            4,
        )
    if step >= 10:
        pygame.draw.line(
            screen,
            color,
            (man_body.centerx, man_body.bottom),
            (man_body.centerx + 30, man_body.bottom + 40),
            4,
        )


def draw_keyboard(
    screen: pygame.surface.Surface, used_characters: list, color: str
) -> list:
    ascii_a = 65
    font = pygame.font.SysFont("Helvetica", 20)
    available_characters = []
    for i in range(26):
        character = chr(ascii_a + i)
        is_visible = character not in used_characters
        if is_visible:
            x = (
                config.START_X
                + (config.GAP * 2)
                + ((config.WIDTH + config.GAP) * (i % 13))
            )
            y = config.START_Y + ((i // 13) * (config.GAP + config.WIDTH))
            keyboard_rect = pygame.Rect(
                x - (config.WIDTH // 2),
                y - (config.WIDTH // 2),
                config.WIDTH,
                config.WIDTH,
            )
            pygame.draw.rect(screen, color, keyboard_rect, 3)
            text = font.render(character, 1, color)
            screen.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))
            available_characters.append((x, y, character, is_visible))
    return available_characters


def draw_word(screen: pygame.surface.Surface, word: str, used_characters: list) -> bool:
    """draw_word draw word in game screen

    Arguments:
        screen {pygame.surface.Surface} -- game screen
        word {str} -- word to show
        used_characters {list} -- characters user chosen from keyboard

    Returns:
        bool -- word guessed by user or not
    """
    font = pygame.font.SysFont("Helvetica", 35)
    display_word = ""
    for character in word:
        if character in used_characters:
            display_word += character + " "
        else:
            display_word += "_ "
    text = font.render(display_word, 1, "white")
    screen.blit(text, (400, 200))
    return "_" not in display_word
