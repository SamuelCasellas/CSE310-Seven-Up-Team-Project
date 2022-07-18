# Main Menu
# Thanks to https://www.youtube.com/watch?v=GMBqjxcKogA

import sys
import os
import pygame
from constants import * 
from button import Button
from display import Display

"""
MENU CLASS
This class renders all of the menus in the game, including
the Main menu, options menu, and the pause menu.
"""

class Menu(Display):

    def __init__(self):
        self.choices = []
        super().__init__()
        self.BG = pygame.transform.scale(pygame.image.load(os.path.join(ASSET_PATH, "Pictures", "Backgrounds", "nebula.jpg")), (WIDTH,HEIGHT))


    # This function returns the font
    def _get_font(self, size): # Returns Press-Start-2P in the desired size
        return pygame.font.Font(os.path.join(ASSET_PATH, "font.ttf"), size)


    # This is the MAIN MENU - the first menu that comes up when the game is started.
    def draw_window(self):
        WIN.blit(self.BG, (0, 0))
        
        # Set up the text and buttons
        MENU_TEXT = self._get_font(50).render("GALACTIC TYPER", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(WIDTH/2, HEIGHT/6))
        
        # Define the buttons
        PLAY_BUTTON = Button(image=pygame.image.load(os.path.join(ASSET_PATH, "Play Rect.png")), pos=(WIDTH/2, HEIGHT/6 * 3), 
                            text_input="PLAY", font=self._get_font(40), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load(os.path.join(ASSET_PATH, "Quit Rect.png")), pos=(WIDTH/2, HEIGHT/6 * 4), 
                            text_input="QUIT", font=self._get_font(40), base_color="#d7fcd4", hovering_color="White")
        BUTTONS = (PLAY_BUTTON, QUIT_BUTTON) 
        
        # Loop to listen for events and respond accordingly
        while True:
            MENU_MOUSE_POS = pygame.mouse.get_pos()
            WIN.blit(MENU_TEXT, MENU_RECT)

            # See if any of the options are being hovered over.
            # If so, change and update color
            for button in BUTTONS:
                button.changeColor(MENU_MOUSE_POS)
                button.update(WIN)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Move on to the first options menu
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.display.update()
                        return self.math_or_typing()
                        
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()

    
    # This is the FIRST OPTIONS MENU where the player chooses which mode to play.
    # This comes up when the player chooses 'play' on the Main Menu.
    def math_or_typing(self):
        WIN.blit(self.BG, (0, 0))

        # Set up the text and buttons
        OPTIONS_TEXT = self._get_font(45).render("OPTIONS", True, "#b68f40")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(WIDTH/2, HEIGHT/6))
        WIN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        # Define the buttons
        OPTIONS_BACK = Button(image=pygame.image.load(os.path.join(ASSET_PATH, "Play Rect.png")), pos=(WIDTH/2, HEIGHT/6 * 4.5), 
                            text_input="BACK", font=self._get_font(50), base_color="Grey", hovering_color="White")

        TYPING = Button(image=pygame.image.load(os.path.join(ASSET_PATH, "Play Rect.png")), pos=(WIDTH/5 * 1.5, HEIGHT/6 * 2.5), 
                            text_input="TYPING", font=self._get_font(30), base_color="#d7fcd4", hovering_color="White", options_size=True)

        MATH = Button(image=pygame.image.load(os.path.join(ASSET_PATH, "Play Rect.png")), pos=(WIDTH/5 * 3.5, HEIGHT/6 * 2.5), 
                            text_input="MATH", font=self._get_font(30), base_color="#d7fcd4", hovering_color="White", options_size=True)

        OPTIONS = (OPTIONS_BACK, TYPING, MATH)

        # Loop to listen for events and respond accordingly
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

            # See if any of the options are being hovered over.
            # If so, change and update color
            for option in OPTIONS:
                option.changeColor(OPTIONS_MOUSE_POS)
                option.update(WIN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for option in OPTIONS:
                        if option.text_input == "BACK" and option.checkForInput(OPTIONS_MOUSE_POS):
                            # Go back to main function
                            self.draw_window()
                        elif option.checkForInput(OPTIONS_MOUSE_POS):
                            # Update the difficulty
                            self.choices.append(option.text_input.lower())
                            MUSIC.load(Button.select_button_sound)
                            MUSIC.play()
                            self.options() 
                            return self.choices   

            pygame.display.update()


    # This is the SECOND OPTIONS MENU where the player chooses what difficulty level they want.
    # This comes up after the player chooses the typing or math mode.
    def options(self):
        WIN.blit(self.BG, (0, 0))

        # Set up the text and buttons
        OPTIONS_TEXT = self._get_font(45).render("DIFFICULTY", True, "#b68f40")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(WIDTH/2, HEIGHT/6))
        WIN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        # Define the buttons
        OPTIONS_BACK = Button(image=pygame.image.load(os.path.join(ASSET_PATH, "Play Rect.png")), pos=(WIDTH/2, HEIGHT/6 * 4.5), 
                            text_input="BACK", font=self._get_font(50), base_color="Grey", hovering_color="White")

        EASY = Button(image=pygame.image.load(os.path.join(ASSET_PATH, "Play Rect.png")), pos=(WIDTH/5, HEIGHT/6 * 2.5), 
                            text_input="EASY", font=self._get_font(30), base_color="#d7fcd4", hovering_color="White", options_size=True)

        MEDIUM = Button(image=pygame.image.load(os.path.join(ASSET_PATH, "Play Rect.png")), pos=(WIDTH/5 * 2.5, HEIGHT/6 * 2.5), 
                            text_input="MEDIUM", font=self._get_font(30), base_color="#d7fcd4", hovering_color="White", options_size=True)

        HARD = Button(image=pygame.image.load(os.path.join(ASSET_PATH, "Play Rect.png")), pos=(WIDTH/5 * 4, HEIGHT/6 * 2.5), 
                            text_input="HARD", font=self._get_font(30), base_color="#d7fcd4", hovering_color="White", options_size=True)
        
        OPTIONS = (OPTIONS_BACK, EASY, MEDIUM, HARD)

        # Loop to listen for events and respond accordingly 
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

            # See if any of the options are being hovered over.
            # If so, change and update color
            for option in OPTIONS:
                option.changeColor(OPTIONS_MOUSE_POS)
                option.update(WIN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for option in OPTIONS:
                        if option.text_input == "BACK" and option.checkForInput(OPTIONS_MOUSE_POS):
                            # Go back to main function
                            self.draw_window()
                        elif option.checkForInput(OPTIONS_MOUSE_POS):
                            # Update the difficulty
                            self.choices.append(option.text_input.lower())
                            MUSIC.load(Button.select_button_sound)
                            MUSIC.play()
                            return

            pygame.display.update()


    # This is the PAUSE MENU, it comes up when the player presses the space bar.
    def pause_menu(self):
        WIN.blit(self.BG, (0, 0))

        # Set up the text and buttons
        MENU_TEXT = self._get_font(50).render("PAUSED", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(WIDTH/2, HEIGHT/6))

        # Define the buttons
        CONTINUE_BUTTON = Button(image=pygame.image.load(os.path.join(ASSET_PATH, "Play Rect.png")), pos=(WIDTH/2, HEIGHT/6 * 3), 
                            text_input="CONTINUE", font=self._get_font(40), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load(os.path.join(ASSET_PATH, "Quit Rect.png")), pos=(WIDTH/2, HEIGHT/6 * 4), 
                            text_input="QUIT", font=self._get_font(40), base_color="#d7fcd4", hovering_color="White")
        BUTTONS = (CONTINUE_BUTTON, QUIT_BUTTON) 

        # Loop to listen for events and respond accordingly
        while True:
            MENU_MOUSE_POS = pygame.mouse.get_pos()
            WIN.blit(MENU_TEXT, MENU_RECT)

            # See if any of the options are being hovered over.
            # If so, change and update color
            for button in BUTTONS:
                button.changeColor(MENU_MOUSE_POS)
                button.update(WIN)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if CONTINUE_BUTTON.checkForInput(MENU_MOUSE_POS):
                        # close pause menu and continue game
                        self.pause = False
                        return   
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()
