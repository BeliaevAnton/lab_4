items = [
    ("rifle", "r", 3, 25),
    ("pistol", "p", 2, 15),
    ("ammo", "a", 2, 15),
    ("medkit", "m", 2, 20),
    ("inhaler", "i", 1, 5),
    ("knife", "k", 1, 15),
    ("axe", "x", 3, 20),
    ("talisman", "t", 1, 25),
    ("flask", "f", 1, 15),
    ("antidote", "d", 1, 10),
    ("supplies", "s", 2, 20),
    ("crossbow", "c", 2, 20)
]

capacity = 9
start_points = 15

best_score = -999
best_combo = []


from itertools import combinations

for r in range(len(items) + 1):

    for combo in combinations(items, r):

        total_size = sum(item[2] for item in combo)
        total_score = sum(item[3] for item in combo)

        if total_size <= capacity:

            final_score = start_points + total_score

            if final_score > best_score:
                best_score = final_score
                best_combo = combo


inventory = [["-" for _ in range(3)] for _ in range(3)]

row = 0
col = 0

for item in best_combo:

    symbol = item[1]
    size = item[2]

    for i in range(size):

        inventory[row][col] = symbol

        col += 1

        if col == 3:
            col = 0
            row += 1


print("Инвентарь:")

for row in inventory:
    print(row)

print("\nИтоговые очки выживания:", best_score)