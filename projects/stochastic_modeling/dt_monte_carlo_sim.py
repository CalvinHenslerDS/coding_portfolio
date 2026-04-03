import random
from itertools import combinations

# --- 1. DATA CONFIGURATION ---
# Using sets {} for tags allows for faster lookups and set math
CARD_LIBRARY = {

    "Red-Eyes Darkness Metal Dragon": {"val": 0, "tags": {"dragon", "dark"}},
    "Blue-Eyes White Dragon": {"val": 0, "tags": {"light", "dragon", "level 8", "beat stick"}},
    "White Stone of Legend": {"val": 0, "tags": {"light", "tuner", "dragon", "debris target", "starter"}},
    "Debris Dragon": {"val": 0, "tags": {"tuner", "dragon", "starter"}},
    "Tragoedia": {"val": 0, "tags": {"dark", "hand trap"}},
    "Vortex Trooper": {"val": 0, "tags": {"debris target"}},
    "Gorz the Emissary of Darkness": {"val": 0, "tags": {"dark", "hand trap"}},
    "Morphing Jar": {"val": 0, "tags": set()},
    "Flamvell Guard": {"val": 0, "tags": {"tuner", "dragon", "debris target", "starter"}},
    "Tri-Horned Dragon": {"val": 0, "tags": {"dark", "dragon", "level 8", "beat stick"}},
    "Koa'ki Meiru Drago": {"val": 0, "tags": {"dragon", "payoff"}},
    "Prime Material Dragon": {"val": 0, "tags": {"light", "dragon", "payoff"}},
    "Battle Fader": {"val": 0, "tags": {"dark", "hand trap"}},
    "Exodius": {"val": 0, "tags": {"dark"}},
    "Card Trooper": {"val": 0, "tags": {"debris target"}},
    "Snipe Hunter": {"val": 0, "tags": {"dark"}},
    "Frost and Flame Dragon": {"val": 0, "tags": {"dragon", "water"}},
    "Tyrant Dragon": {"val": 0, "tags": {"fire", "dragon", "level 8", "payoff"}},
    "Chaos Sorcerer": {"val": 0, "tags": {"dark"}},
    "Dark Armed Dragon": {"val": 0, "tags": {"dark", "dragon"}},
    "Dragon Ice": {"val": 0, "tags": {"water", "dragon"}},
    "White Night Dragon": {"val": 0, "tags": {"water", "dragon", "level 8", "payoff"}},
    "Sangan": {"val": 0, "tags": {"dark"}},
    "Clear Vice Dragon": {"val": 0, "tags": {"dark", "dragon", "level 8", "payoff"}},


    "Trade-In": {"val": 0, "tags": set()},
    "Cards of Consonance": {"val": 0, "tags": set()},
    "Super Rejuvenation": {"val": 0, "tags": set()},
    "Upstart Goblin": {"val": 0, "tags": set()},
    "Allure of Darkness": {"val": 0, "tags": set()},
    "Instant Fusion": {"val": 0, "tags": {"starter"}},
    "Giant Trunade": {"val": 0, "tags": {"sweeper"}},
    "Heavy Storm": {"val": 0, "tags": {"sweeper"}},
    "Pot of Avarice": {"val": 0, "tags": set()},
    "Card Destruction": {"val": 0, "tags": set()},
    "Future Fusion": {"val": 0, "tags": set()},
    "Foolish Burial": {"val": 0, "tags": set()},
    "Magical Stone Excavation": {"val": 0, "tags": set()},
    "Dark World Dealings": {"val": 0, "tags": set()},
    "D.D.R. - Different Dimension Reincarnation": {"val": 0, "tags": set()},

    "Reckless Greed": {"val": 0, "tags": set()},
    "Torrential Tribute": {"val": 0, "tags": {"defense"}},
    "Mirror Force": {"val": 0, "tags": {"defense"}},
    "Legacy of Yata-Garasu": {"val": 0, "tags": set()},
    "Jar of Greed": {"val": 0, "tags": set()},
    "Trap Dustshoot": {"val": 0, "tags": set()},

}

# Define your specific hard-coded combinations
# We use frozenset so order doesn't matter: ("A","B") == ("B","A")
TRIPLE_COMBOS = {
    frozenset(["Wizard", "Mana Crystal", "Fireball"]): 15,
    frozenset(["Dragon", "Dragon", "Dragon"]): 20
}

# --- 2. THE MULTI-PASS EVALUATOR ---
def evaluate_hand(hand_names):
    # Map names to their full data dictionary
    hand_data = [CARD_LIBRARY[name] for name in hand_names]
    score = 0

    # PASS 1: Base Quality
    # Summing the "val" of every card in hand
    score += sum(card["val"] for card in hand_data)

    # PASS 2: Tag-Based Pair Synergy
    # We check every unique pair for specific tag interactions
    for c1, c2 in combinations(hand_data, 2):
        t1, t2 = c1["tags"], c2["tags"]
        
        if "dark" in t1 and c2 == "Allure of Darkness": score += 0
        if "dark" in t2 and c1 == "Allure of Darkness": score += 0

        if "level 8" in t1 and c2 == "Trade-In": score += 0
        if "level 8" in t2 and c1 == "Trade-In": score += 0

        if "tuner" in t1 and c2 == "Cards of Consonance": score += 0
        if "tuner" in t2 and c1 == "Cards of Consonance": score += 0

        if "starter" in t1 and c2 == "Red-Eyes Darkness Metal Dragon": score += 0
        if "starter" in t2 and c1 == "Red-Eyes Darkness Metal Dragon": score += 0

        if "debris target" in t1 and c2 == "Debris Dragon": score += 0
        if "debris target" in t2 and c1 == "Debris Dragon": score += 0

        if "tuner" in t1 and c2 == "Instant Fusion": score += 0
        if "tuner" in t2 and c1 == "Instant Fusion": score += 0
        
        # Example: Fire + Ice anti-synergy (penalty)
        if "fire" in t1 and "ice" in t2: score -= 1
        if "fire" in t2 and "ice" in t1: score -= 1

    # PASS 3: Hard-Coded Combinations & Tag Thresholds
    # A) Check specific hard-coded triples
    for triple in combinations(hand_names, 3):
        if frozenset(triple) in TRIPLE_COMBOS:
            score += TRIPLE_COMBOS[frozenset(triple)]

    # B) Check Tag "Critical Mass" (e.g., a "Fire" deck bonus)
    all_tags_in_hand = [tag for card in hand_data for tag in card["tags"]]
    if all_tags_in_hand.count("fire") >= 3:
        score += 10  # "Blaze" bonus for having 3+ fire tags
        
    return score

# --- 3. MONTE CARLO SIMULATION ENGINE ---
def run_simulation(deck_list, hand_size=5, iterations=10000):
    total_score = 0
    results = []

    for _ in range(iterations):
        # Draw a random hand without replacement
        hand = random.sample(deck_list, hand_size)
        
        # Evaluate the hand
        h_score = evaluate_hand(hand)
        
        results.append(h_score)
        total_score += h_score

    # Summary Statistics
    avg = total_score / iterations
    print(f"--- Simulation Results ({iterations} trials) ---")
    print(f"Average Hand Value: {avg:.2f}")
    print(f"Highest Quality Hand: {max(results)}")
    print(f"Lowest Quality Hand:  {min(results)}")

# --- 4. EXECUTION ---
# Create a sample deck of 40 cards
my_deck = (["Fireball"] * 8 + ["Wizard"] * 8 + ["Mana Crystal"] * 8 + 
           ["Ice Shield"] * 8 + ["Dragon"] * 8)

run_simulation(my_deck)