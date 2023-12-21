import customtkinter
import pygame


def change_theme(theme: str) -> None:
    """change_theme change application theme

    Arguments:
        theme {str} -- only "dark" , "light" and "system"
    """
    if theme in ("dark", "light", "system"):
        customtkinter.set_appearance_mode(theme)
    else:
        raise ValueError("theme should be in 'dark' , 'light' and 'system'")


def draw_hangman(screen: pygame.surface.Surface, step: int) -> None:
    """draw_hangman draw hangman on game screen

    Arguments:
        screen {pygame.surface.Surface} -- game screen
        step {int} -- how many of hangman should draw
    """
    if step >= 1:
        footer_rect = pygame.Rect(75, 350, 300, 10)
        pygame.draw.rect(screen, "white", footer_rect)
    if step >= 2:
        body_rect = pygame.Rect(125, 75, 10, 275)
        pygame.draw.rect(screen, "white", body_rect)
    if step >= 3:
        horizontal_header_rect = pygame.Rect(body_rect.x, body_rect.y, 150, 10)
        pygame.draw.rect(screen, "white", horizontal_header_rect)
    if step >= 4:
        vertical_header_rect = pygame.Rect(
            horizontal_header_rect.right, body_rect.y, 10, 50
        )
        pygame.draw.rect(screen, "white", vertical_header_rect)
    if step >= 5:
        man_head = pygame.draw.circle(
            screen,
            "white",
            (280, 155),
            30,
            4,
        )
    if step >= 6:
        man_body = pygame.Rect(man_head.centerx - 2, man_head.bottom, 4, 75)
        pygame.draw.rect(screen, "white", man_body)
    if step >= 7:
        pygame.draw.line(
            screen,
            "white",
            (man_body.centerx, man_body.centery - 20),
            (man_body.centerx + 40, man_body.centery + 10),
            4,
        )
    if step >= 8:
        pygame.draw.line(
            screen,
            "white",
            (man_body.centerx, man_body.centery - 20),
            (man_body.centerx - 40, man_body.centery + 10),
            4,
        )
    if step >= 9:
        pygame.draw.line(
            screen,
            "white",
            (man_body.centerx - 2, man_body.bottom),
            (man_body.centerx - 30, man_body.bottom + 40),
            4,
        )
    if step >= 10:
        pygame.draw.line(
            screen,
            "white",
            (man_body.centerx, man_body.bottom),
            (man_body.centerx + 30, man_body.bottom + 40),
            4,
        )
