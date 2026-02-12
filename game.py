import os
import random
import subprocess
import sys


# =========================
# Shared Utilities
# =========================
def clear_screen():
    if not sys.stdout.isatty():
        print("\n" * 2)
        return

    if os.name == 'nt':
        os.system('cls')
    else:
        if os.environ.get('TERM'):
            subprocess.run(['clear'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            sys.stdout.write('\x1b[2J\x1b[H')
            sys.stdout.flush()

def press_enter():
    input("\n(Press Enter to continue) ")

def roll(pct):
    return random.randint(1, 100) <= pct


# =========================
# Constants / Catalog
# =========================
RARITIES = ["Common", "Rare", "Epic", "Legendary", "Mythic"]

PLAYER_BASE_CRIT = 20

PLAYER_ACTIONS = {
    "1": {"name": "Punch", "damage": 10, "hit": 80},
    "2": {"name": "Kick", "damage": 20, "hit": 50},
    "3": {"name": "Counter", "damage": 50, "hit": 20},
    "4": {"name": "Guard", "damage": 0, "hit": 0},
}

MONSTER_HIT = 80
GUARD_BLOCK = 70


EQUIPMENT_CATALOG = {

    # Common
    "Plastic Gloves": {"rarity": "Common", "desc": "Attack success +3%", "effect": {"hit_pp": 3}},
    "Bracelet": {"rarity": "Common", "desc": "Damage reduction -2", "effect": {"dmg_reduce": 2}},
    "Nails": {"rarity": "Common", "desc": "HP +5", "effect": {"hp_plus": 5}},

    # Rare
    "Rubber Gloves": {"rarity": "Rare", "desc": "Attack success +5%", "effect": {"hit_pp": 5}},
    "Chain": {"rarity": "Rare", "desc": "Critical chance +5%", "effect": {"crit_pp": 5}},
    "Watch": {"rarity": "Rare", "desc": "First hit +20 damage", "effect": {"clock_first_hit_bonus": 20}},

    # Epic
    "Winter Gloves": {"rarity": "Epic", "desc": "Critical damage +20%", "effect": {"crit_mult_bonus": 0.2}},
    "Golf Gloves": {"rarity": "Epic", "desc": "Enemy hit rate -10%p", "effect": {"enemy_hit_minus_pp": 10}},
    "Wrist Guard": {"rarity": "Epic", "desc": "Guard success +10%p", "effect": {"guard_pp": 10}},
    "Work Gloves": {"rarity": "Epic", "desc": "Damage reduction -5", "effect": {"dmg_reduce": 5}},

    # Legendary
    "Boxing Gloves": {"rarity": "Legendary", "desc": "Attack success +10%", "effect": {"hit_pp": 10}},
    "Knuckle": {"rarity": "Legendary", "desc": "Damage +10", "effect": {"dmg_flat": 10}},
    "Claw": {"rarity": "Legendary", "desc": "Bleed: enemy takes 2 damage per turn", "effect": {"claw_bleed": True}},

    # Mythic
    "Gauntlet": {"rarity": "Mythic", "desc": "40% chance: 10 dmg + stun", "effect": {"gauntlet": True}},
    "Spirit Fist": {"rarity": "Mythic", "desc": "50% chance: steal 5 HP on hit", "effect": {"spirit_fist": True}},
}

STONE_BASE = {"Common":100, "Rare":300, "Epic":500, "Legendary":1000, "Mythic":1500}

ITEMS_BY_RARITY = {r: [] for r in RARITIES}
for name, meta in EQUIPMENT_CATALOG.items():
    ITEMS_BY_RARITY[meta["rarity"]].append(name)


# =========================
# Game State
# =========================
class GameState:
    def __init__(self):
        self.gold = 0
        self.gems = 0
        self.enhance_stones = 0
        self.owned_levels = {}
        self.equipped = None

    def count_owned_by_rarity(self):
        c = {r:0 for r in RARITIES}
        for it in self.owned_levels:
            c[EQUIPMENT_CATALOG[it]["rarity"]] += 1
        return c

    def acquire_random_item_from_rarity_no_dupe(self, rarity):
        candidates = [x for x in ITEMS_BY_RARITY[rarity] if x not in self.owned_levels]
        if not candidates:
            return None
        choice = random.choice(candidates)
        self.owned_levels[choice] = 1
        return choice

    def show_home(self):
        clear_screen()
        print("=== HOME ===")
        print(f"Gold: {self.gold}")
        print(f"Gems: {self.gems}")
        print(f"Enhance Stones: {self.enhance_stones}")
        print(f"Equipped: {self.equipped or '(None)'}")

        print("\n[Owned Equipment by Rarity]")
        for r, n in self.count_owned_by_rarity().items():
            print(f"- {r}: {n}")

        print("\n1) Hunt  2) Tournament  3) PVP  4) Gacha  5) Equipment  0) Exit")


# =========================
# Monster
# =========================
class Monster:
    def __init__(self, name, hp, dmg, crit):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.dmg = dmg
        self.crit_chance = crit


MONSTER_TEMPLATES = {
    "Normal": Monster("Normal Monster", 20, 5, 10),
    "Elite": Monster("Elite Monster", 50, 15, 15),
    "Boss": Monster("Boss Monster", 100, 25, 20),
}


# =========================
# Hunting Mode (Basic Version Shown)
# =========================
class HuntingMode:
    def __init__(self, state):
        self.state = state

    def discover_grade(self):
        r = random.randint(1,100)
        if r <= 80:
            return "Normal"
        if r <= 95:
            return "Elite"
        return "Boss"

    def new_monster(self, grade):
        t = MONSTER_TEMPLATES[grade]
        return Monster(t.name, t.max_hp, t.dmg, t.crit_chance)

    def battle(self, m):
        player_hp = 100
        while player_hp > 0 and m.hp > 0:
            print(f"\nYour HP: {player_hp} | Enemy HP: {m.hp}")
            print("1) Punch  2) Kick  3) Counter  4) Guard")
            action = input(">> ")

            act = PLAYER_ACTIONS.get(action)
            if not act:
                continue

            if action == "4":
                print("You guarded!")
            else:
                if roll(act["hit"]):
                    dmg = act["damage"]
                    if roll(PLAYER_BASE_CRIT):
                        dmg *= 2
                        print("Critical hit!")
                    m.hp -= dmg
                    print(f"You dealt {dmg} damage!")
                else:
                    print("Missed!")

            if m.hp <= 0:
                break

            if roll(MONSTER_HIT):
                dmg = m.dmg
                if roll(m.crit_chance):
                    dmg *= 2
                    print("Monster critical!")
                player_hp -= dmg
                print(f"Monster dealt {dmg} damage!")
            else:
                print("Monster missed!")

        if player_hp > 0:
            print("Victory!")
            self.state.gold += 1000
        else:
            print("Defeat...")

        press_enter()

    def run(self):
        grade = self.discover_grade()
        m = self.new_monster(grade)
        self.battle(m)


# =========================
# PVP Mode
# =========================
class PvPMode:
    def run(self):
        print("=== PVP MODE ===")
        hp1 = 100
        hp2 = 100

        while hp1 > 0 and hp2 > 0:
            print(f"\nP1 HP: {hp1} | P2 HP: {hp2}")
            input("P1 attacks (press enter)")
            if roll(80):
                hp2 -= 10
            input("P2 attacks (press enter)")
            if roll(80):
                hp1 -= 10

        print("P1 Wins!" if hp1 > 0 else "P2 Wins!")
        press_enter()


# =========================
# Gacha Mode
# =========================
class GachaMode:
    def __init__(self, state):
        self.state = state

    def run(self):
        if self.state.gems < 100:
            print("Not enough gems!")
            press_enter()
            return

        self.state.gems -= 100
        rarity = random.choice(RARITIES)
        item = self.state.acquire_random_item_from_rarity_no_dupe(rarity)

        if item:
            print(f"You obtained: {item} ({rarity})")
        else:
            print("Duplicate! Gems refunded.")
            self.state.gems += 100

        press_enter()


# =========================
# Main Loop
# =========================
def main():
    state = GameState()

    while True:
        state.show_home()
        sel = input(">> ")

        if sel == "1":
            HuntingMode(state).run()
        elif sel == "2":
            print("Tournament coming soon!")
            press_enter()
        elif sel == "3":
            PvPMode().run()
        elif sel == "4":
            GachaMode(state).run()
        elif sel == "5":
            print("Equipment system active (simplified).")
            press_enter()
        elif sel == "0":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()