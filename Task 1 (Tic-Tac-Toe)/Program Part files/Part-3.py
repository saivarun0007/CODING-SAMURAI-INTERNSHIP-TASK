import pygame
import sys
import time
import tictactoe as ttt

pygame.init()
pygame.display.set_caption("𝐂𝐨𝐝𝐢𝐧𝐠 𝐒𝐚𝐦𝐮𝐫𝐚𝐢 𝐈𝐧𝐭𝐞𝐫𝐧")

# Screen setup
width, height = 700, 600
screen = pygame.display.set_mode((width, height))

# Colors
background_color = (176, 207, 222)
text_color = (0, 0, 0)
button_color = (255, 255, 255)
hover_color = (200, 200, 255)
active_color = (150, 150, 255)
border_color = (50, 50, 50)
white = (255, 255, 255)
green = (144, 238, 144)
yellow = (255, 255, 153)
red = (255, 102, 102)

# Fonts
mediumFont = pygame.font.Font("OpenSans-Regular.ttf", 28)
largeFont = pygame.font.SysFont("Arial", 40, bold=True)
moveFont = pygame.font.Font("OpenSans-Regular.ttf", 60)
scoreFont = pygame.font.Font("OpenSans-Regular.ttf", 24)

# Sounds
click_sound = pygame.mixer.Sound("Sounds/click.wav")
ai_sound = pygame.mixer.Sound("Sounds/ai_move.wav")
button_sound = pygame.mixer.Sound("Sounds/button.wav")
tie_sound = pygame.mixer.Sound("Sounds/tie.wav")
win_x_sound = pygame.mixer.Sound("Sounds/win.wav")
win_o_sound = pygame.mixer.Sound("Sounds/win.wav")


class Button:
    def __init__(self, x, y, width, height, text, font, action=None, hover_color=(200, 200, 255)):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = font
        self.action = action
        self.hovered = False
        self.hover_color = hover_color

    def draw(self, surface, override_color=None):
        color = override_color if override_color else (self.hover_color if self.hovered else button_color)
        pygame.draw.rect(surface, color, self.rect, border_radius=10)
        pygame.draw.rect(surface, border_color, self.rect, 2, border_radius=10)

        text_surf = self.font.render(self.text, True, text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def check_hover(self, mouse_pos):
        self.hovered = self.rect.collidepoint(mouse_pos)

    def check_click(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)


def main():
    while True:
        user = None
        while user is None:
            screen.fill(background_color)
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            title = largeFont.render("PLAY TIC-TAC-TOE", True, text_color)
            screen.blit(title, title.get_rect(center=(width / 2, 60)))

            play_x_btn = Button(width / 8, height / 2, width / 4, 50, "Play as X", mediumFont)
            play_o_btn = Button(5 * width / 8, height / 2, width / 4, 50, "Play as O", mediumFont)

            for btn in [play_x_btn, play_o_btn]:
                btn.check_hover(mouse)
                btn.draw(screen)

            click, _, _ = pygame.mouse.get_pressed()
            if click == 1:
                if play_x_btn.check_click(mouse):
                    button_sound.play()
                    time.sleep(0.2)
                    user = ttt.X
                elif play_o_btn.check_click(mouse):
                    button_sound.play()
                    time.sleep(0.2)
                    user = ttt.O

            pygame.display.flip()

        board = ttt.initial_state()
        ai_turn = False
        win_sound_played = False
        rounds_played = 0
        x_wins = 0
        o_wins = 0
        ties = 0
        total_rounds = 3
        paused = False

        button_width = 140
        button_height = 50
        button_x = width - button_width - 20
        button_gap = 20
        start_y = 180

        pause_button = Button(button_x, start_y, button_width, button_height, "Pause", mediumFont, hover_color=yellow)
        resume_button = Button(button_x, start_y + button_gap + button_height, button_width, button_height, "Resume", mediumFont, hover_color=green)
        restart_button = Button(button_x, start_y + 2 * (button_gap + button_height), button_width, button_height, "Restart", mediumFont, hover_color=red)

        # Level buttons (left side)
        level_btn_x = 20
        level_start_y = 180
        easy_btn = Button(level_btn_x, level_start_y, button_width, button_height, "Easy", mediumFont)
        medium_btn = Button(level_btn_x, level_start_y + button_height + button_gap, button_width, button_height, "Medium", mediumFont)
        hard_btn = Button(level_btn_x, level_start_y + 2 * (button_height + button_gap), button_width, button_height, "Hard", mediumFont)

        while True:
            screen.fill(background_color)
            mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            tile_size = 100
            tile_origin = (width / 2 - 1.5 * tile_size, height / 2 - 1.5 * tile_size + 30)
            tiles = []

            for i in range(3):
                row = []
                for j in range(3):
                    rect = pygame.Rect(tile_origin[0] + j * tile_size, tile_origin[1] + i * tile_size, tile_size, tile_size)
                    pygame.draw.rect(screen, white, rect, 3)
                    if board[i][j] != ttt.EMPTY:
                        move = moveFont.render(board[i][j], True, text_color)
                        screen.blit(move, move.get_rect(center=rect.center))
                    row.append(rect)
                tiles.append(row)

            game_over = ttt.terminal(board)
            player = ttt.player(board)

            title_surface = largeFont.render("TIC-TAC-TOE", True, text_color)
            screen.blit(title_surface, title_surface.get_rect(center=(width / 2, 30)))

            status_text = "Game Paused" if paused else "AI Thinking..." if user != player else f"Play as {user}"
            if game_over:
                winner = ttt.winner(board)
                if winner:
                    status_text = f"{winner} wins!"
                    if not win_sound_played:
                        (win_x_sound if winner == "X" else win_o_sound).play()
                        if winner == "X":
                            x_wins += 1
                        else:
                            o_wins += 1
                        win_sound_played = True
                else:
                    status_text = "Tie!"
                    if not win_sound_played:
                        tie_sound.play()
                        ties += 1
                        win_sound_played = True

            status_render = mediumFont.render(status_text, True, text_color)
            screen.blit(status_render, status_render.get_rect(center=(width / 2, 80)))

            score_text = f"Round: {rounds_played + 1}/{total_rounds}  X Wins: {x_wins}  O Wins: {o_wins}  Ties: {ties}"
            score_render = scoreFont.render(score_text, True, text_color)
            screen.blit(score_render, score_render.get_rect(center=(width / 2, 120)))

            for btn in [pause_button, resume_button, restart_button]:
                btn.check_hover(mouse)
                btn.draw(screen)

            # Blinking level indication
            level_colors = [green, yellow, red]
            level_buttons = [easy_btn, medium_btn, hard_btn]
            for i, btn in enumerate(level_buttons):
                btn.check_hover(mouse)
                blink = (rounds_played == i)
                blink_color = level_colors[i] if blink else None
                btn.draw(screen, override_color=blink_color)

            click, _, _ = pygame.mouse.get_pressed()
            if click == 1:
                if pause_button.check_click(mouse):
                    button_sound.play()
                    paused = True
                    time.sleep(0.2)
                elif resume_button.check_click(mouse):
                    button_sound.play()
                    paused = False
                    time.sleep(0.2)
                elif restart_button.check_click(mouse) and not game_over:
                    button_sound.play()
                    board = ttt.initial_state()
                    win_sound_played = False
                    ai_turn = False
                    paused = False
                    time.sleep(0.2)

            if not paused and not game_over and user != player:
                if ai_turn:
                    time.sleep(0.5)
                    move = ttt.minimax(board)
                    board = ttt.result(board, move)
                    ai_sound.play()
                    ai_turn = False
                else:
                    ai_turn = True

            if click == 1 and user == player and not game_over and not paused:
                for i in range(3):
                    for j in range(3):
                        if board[i][j] == ttt.EMPTY and tiles[i][j].collidepoint(mouse):
                            board = ttt.result(board, (i, j))
                            click_sound.play()

            if game_over:
                label = "Play Again" if rounds_played >= total_rounds - 1 else "Next Round"
                next_btn = Button(width / 2 - 150, height - 70, 150, 50, label, scoreFont, hover_color=green)
                quit_btn = Button(width / 2 + 30, height - 70, 120, 50, "Quit", scoreFont, hover_color=red)

                for btn in [next_btn, quit_btn]:
                    btn.check_hover(mouse)
                    btn.draw(screen)

                if click == 1:
                    if next_btn.check_click(mouse):
                        button_sound.play()
                        if rounds_played < total_rounds - 1:
                            board = ttt.initial_state()
                            win_sound_played = False
                            ai_turn = False
                            paused = False
                            rounds_played += 1
                        else:
                            break
                        time.sleep(0.2)
                    elif quit_btn.check_click(mouse):
                        pygame.quit()
                        sys.exit()

            pygame.display.flip()


if __name__ == "__main__":
    main()
