import pygame
import sys
import time
import tictactoe as ttt  # Ensure your tictactoe.py handles game logic correctly

pygame.init()
pygame.display.set_caption("𝐂𝐨𝐝𝐢𝐧𝐠 𝐒𝐚𝐦𝐮𝐫𝐚𝐢 𝐈𝐧𝐭𝐞𝐫𝐧")

# Screen setup
size = width, height = 700, 600  # UPDATED: height is now 600
screen = pygame.display.set_mode(size)

# Colors
background_color = (176, 207, 222)
text_color = (0, 0, 0)
white = (255, 255, 255)

# Fonts
mediumFont = pygame.font.Font("OpenSans-Regular.ttf", 28)
largeFont = pygame.font.SysFont("Arial", 40, bold=True)
moveFont = pygame.font.Font("OpenSans-Regular.ttf", 60)
scoreFont = pygame.font.Font("OpenSans-Regular.ttf", 24)

# Load sound effects
click_sound = pygame.mixer.Sound("Sounds/click.wav")
ai_sound = pygame.mixer.Sound("Sounds/ai_move.wav")
button_sound = pygame.mixer.Sound("Sounds/button.wav")
tie_sound = pygame.mixer.Sound("Sounds/tie.wav")
win_x_sound = pygame.mixer.Sound("Sounds/win.wav")   # For X wins
win_o_sound = pygame.mixer.Sound("Sounds/win.wav")  # For O wins

# Game variables
user = None
board = ttt.initial_state()
ai_turn = False
win_sound_played = False
rounds_played = 0
x_wins = 0
o_wins = 0
ties = 0
total_rounds = 3
game_series_over = False # Flag to indicate if all 3 rounds are finished

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(background_color)

    if user is None:
        # Title
        title = largeFont.render("PLAY TIC-TAC-TOE", True, text_color)
        titleRect = title.get_rect(center=((width / 2), 50))
        screen.blit(title, titleRect)

        # Buttons
        playXButton = pygame.Rect((width / 8), (height / 2), width / 4, 50)
        playX = mediumFont.render("Play as X", True, text_color)
        playXRect = playX.get_rect(center=playXButton.center)
        pygame.draw.rect(screen, white, playXButton)
        screen.blit(playX, playXRect)

        playOButton = pygame.Rect(5 * (width / 8), (height / 2), width / 4, 50)
        playO = mediumFont.render("Play as O", True, text_color)
        playORect = playO.get_rect(center=playOButton.center)
        pygame.draw.rect(screen, white, playOButton)
        screen.blit(playO, playORect)

        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse = pygame.mouse.get_pos()
            if playXButton.collidepoint(mouse):
                button_sound.play()
                time.sleep(0.2)
                user = ttt.X
            elif playOButton.collidepoint(mouse):
                button_sound.play()
                time.sleep(0.2)
                user = ttt.O

    else:
        # Draw board
        tile_size = 80
        # Adjusted tile_origin to move board UP for new height
        tile_origin = (width / 2 - (1.5 * tile_size), height / 2 - (1.5 * tile_size) + 20)
        tiles = []

        for i in range(3):
            row = []
            for j in range(3):
                rect = pygame.Rect(
                    tile_origin[0] + j * tile_size,
                    tile_origin[1] + i * tile_size,
                    tile_size, tile_size
                )
                pygame.draw.rect(screen, white, rect, 3)

                if board[i][j] != ttt.EMPTY:
                    move = moveFont.render(board[i][j], True, text_color)
                    moveRect = move.get_rect(center=rect.center)
                    screen.blit(move, moveRect)
                row.append(rect)
            tiles.append(row)

        game_over = ttt.terminal(board)
        player = ttt.player(board)

        # Main Title (always "PLAY TIC-TAC-TOE")
        title_render = largeFont.render("PLAY TIC-TAC-TOE", True, text_color)
        titleRect = title_render.get_rect(center=((width / 2), 30))
        screen.blit(title_render, titleRect)

        # Scoreboard
        if not game_over:
            current_round_display = rounds_played + 1  # We're still playing this round
        else:
            current_round_display = rounds_played  # Round just completed

        score_text = scoreFont.render(
            f"Round: {current_round_display}/{total_rounds}   X Wins: {x_wins}   O Wins: {o_wins}   Ties: {ties}",
            True, text_color)
        scoreRect = score_text.get_rect(center=(width / 2, 75))
        screen.blit(score_text, scoreRect)


        # Current Round Status Message (e.g., "AI Thinking...", "Game Over: X wins.")
        if game_over:
            winner = ttt.winner(board)
            if winner is None:
                current_round_status_text = "Game Over: Tie."
                if not win_sound_played:
                    tie_sound.play()
                    ties += 1
                    win_sound_played = True
            else:
                current_round_status_text = f"Game Over: {winner} wins."
                if not win_sound_played:
                    if winner == ttt.X:
                        win_x_sound.play()
                        x_wins += 1
                    elif winner == ttt.O:
                        win_o_sound.play()
                        o_wins += 1
                    win_sound_played = True
        elif user == player:
            current_round_status_text = f"Play as {user}"
        else:
            current_round_status_text = "AI Thinking..."

        current_round_status_render = mediumFont.render(current_round_status_text, True, text_color)
        current_round_status_rect = current_round_status_render.get_rect(center=(width / 2, 120))
        screen.blit(current_round_status_render, current_round_status_rect)


        # AI move
        if user != player and not game_over and not game_series_over:
            if ai_turn:
                time.sleep(0.5)
                move = ttt.minimax(board)
                board = ttt.result(board, move)
                ai_sound.play()
                ai_turn = False
            else:
                ai_turn = True

        # User move
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1 and user == player and not game_over and not game_series_over:
            mouse = pygame.mouse.get_pos()
            for i in range(3):
                for j in range(3):
                    if board[i][j] == ttt.EMPTY and tiles[i][j].collidepoint(mouse):
                        board = ttt.result(board, (i, j))
                        click_sound.play()

        # Logic after a round (or the series) is over
        if game_over:
            if rounds_played < total_rounds - 1: # Not the final round yet (rounds 0 and 1)
                nextRoundButton = pygame.Rect(width / 5, height - 65, width / 3.5, 50)
                nextRound = mediumFont.render("Next Round", True, text_color)
                nextRoundRect = nextRound.get_rect(center=nextRoundButton.center)
                pygame.draw.rect(screen, white, nextRoundButton)
                screen.blit(nextRound, nextRoundRect)

                quitButton = pygame.Rect(3 * width / 5, height - 65, width / 3.5, 50)
                quit_text = mediumFont.render("Quit", True, text_color)
                quitRect = quit_text.get_rect(center=quitButton.center)
                pygame.draw.rect(screen, white, quitButton)
                screen.blit(quit_text, quitRect)

                click, _, _ = pygame.mouse.get_pressed()
                if click == 1:
                    mouse = pygame.mouse.get_pos()
                    if nextRoundButton.collidepoint(mouse):
                        button_sound.play()
                        time.sleep(0.2)
                        rounds_played += 1 # Increment round count
                        board = ttt.initial_state() # Reset board
                        ai_turn = False
                        win_sound_played = False # Reset sound flag
                    elif quitButton.collidepoint(mouse):
                        button_sound.play()
                        time.sleep(0.2)
                        pygame.quit()
                        sys.exit()
            else: # Final round completed (rounds_played is 2, and current round just finished)
                game_series_over = True # Set flag to indicate series is truly over

                final_winner_message = ""
                if x_wins > o_wins:
                    final_winner_message = "Series Winner: X!"
                elif o_wins > x_wins:
                    final_winner_message = "Series Winner: O!"
                else:
                    final_winner_message = "Series: It's a Tie!"
                
                final_winner_render = largeFont.render(final_winner_message, True, text_color)
                # UPDATED: Adjusted position for the final winner message (moved down)
                final_winner_rect = final_winner_render.get_rect(center=((width / 2), height - 100))
                screen.blit(final_winner_render, final_winner_rect)

                # Play Again and Quit buttons for the end of the series
                playAgainButton = pygame.Rect(width / 5, height - 65, width / 3.5, 50)
                playAgain = mediumFont.render("Play Again", True, text_color)
                playAgainRect = playAgain.get_rect(center=playAgainButton.center)
                pygame.draw.rect(screen, white, playAgainButton)
                screen.blit(playAgain, playAgainRect)

                quitButton = pygame.Rect(3 * width / 5, height - 65, width / 3.5, 50)
                quit_text = mediumFont.render("Quit", True, text_color)
                quitRect = quit_text.get_rect(center=quitButton.center)
                pygame.draw.rect(screen, white, quitButton)
                screen.blit(quit_text, quitRect)

                click, _, _ = pygame.mouse.get_pressed()
                if click == 1:
                    mouse = pygame.mouse.get_pos()
                    if playAgainButton.collidepoint(mouse):
                        button_sound.play()
                        time.sleep(0.2)
                        # Reset ALL game state variables for a fresh series
                        user = None
                        board = ttt.initial_state()
                        ai_turn = False
                        win_sound_played = False
                        rounds_played = 0
                        x_wins = 0
                        o_wins = 0
                        ties = 0
                        game_series_over = False
                    elif quitButton.collidepoint(mouse):
                        button_sound.play()
                        time.sleep(0.2)
                        pygame.quit()
                        sys.exit()

    pygame.display.flip()