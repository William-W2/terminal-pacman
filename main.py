import os
import random
import time
from colorama import Fore, Style, init

init(autoreset=True)

# Map example
maps = [
    [
        list("#########"),
        list("#.......#"),
        list("#.#.#.#.#"),
        list("#.@.#..E#"),
        list("#########")
    ],
]

current_map_index = 0
game_map = maps[current_map_index]

player_pos = [3, 2]
enemy_pos = [3, 7]
score = 0
total_dots = sum(row.count(".") for row in game_map)

# Clear screen function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Print map
def print_map():
    clear_screen()
    for i, row in enumerate(game_map):
        line = ""
        for j, cell in enumerate(row):
            if [i,j] == player_pos:
                line += Fore.YELLOW + "@"
            elif [i,j] == enemy_pos:
                line += Fore.RED + "E"
            elif cell == "#":
                line += Fore.LIGHTBLACK_EX + "#"
            elif cell == ".":
                line += Fore.WHITE + "."
            else:
                line += " "
        print(line)
    print(f"\nScore: {score}/{total_dots}")
    print("Controls: W(up), A(left), S(down), D(right), Q(quit)")

# Player movement
def move_player(dx, dy):
    global score
    x, y = player_pos
    target = game_map[x + dx][y + dy]

    if target == "#":
        return
    if [x+dx, y+dy] == enemy_pos:
        print("💀 Game Over! You hit the enemy.")
        exit()
    if target == ".":
        score += 1
    game_map[x][y] = " "
    player_pos[0] += dx
    player_pos[1] += dy

# Enemy movement is random
def move_enemy():
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    random.shuffle(directions)
    for dx, dy in directions:
        x, y = enemy_pos
        nx, ny = x+dx, y+dy
        if game_map[nx][ny] != "#" and [nx,ny] != player_pos:
            enemy_pos[0], enemy_pos[1] = nx, ny
            break

# Check for winning
def check_win():
    return score == total_dots

# Main loop
def main():
    print("Welcome to Terminal Pac-Man with Enemy!")
    input("Press Enter to start...")
    while True:
        print_map()
        if check_win():
            print("🎉 Congratulations! You ate all the dots!")
            break
        move_input = input("Move: ").lower()
        if move_input == "w":
            move_player(-1, 0)
        elif move_input == "s":
            move_player(1, 0)
        elif move_input == "a":
            move_player(0, -1)
        elif move_input == "d":
            move_player(0, 1)
        elif move_input == "q":
            print("Game quit.")
            break
        move_enemy()  # Enemy movement
        time.sleep(0.1)

if __name__ == "__main__":
    main()
