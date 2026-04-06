import random
from itertools import combinations

# --- 1. DATA CONFIGURATION ---
# Using sets {} for tags allows for faster lookups and set math
CARD_LIBRARY = {

    "Red-Eyes Darkness Metal Dragon": {"val": 0, "tags": {"dragon", "dark"}},
    "Blue-Eyes White Dragon": {"val": 0, "tags": {"light", "dragon", "level 8", "payoff"}},
    "White Stone of Legend": {"val": 0, "tags": {"light", "tuner", "dragon", "debris target", "starter"}},
    "Debris Dragon": {"val": 0, "tags": {"tuner", "dragon", "starter"}},
    "Tragoedia": {"val": 0, "tags": {"dark", "hand trap"}},
    "Vortex Trooper": {"val": 0, "tags": {"debris target"}},
    "Gorz the Emissary of Darkness": {"val": 0, "tags": {"dark", "hand trap"}},
    "Morphing Jar": {"val": 0, "tags": set()},
    "Flamvell Guard": {"val": 0, "tags": {"tuner", "dragon", "debris target", "starter"}},
    "Tri-Horned Dragon": {"val": 0, "tags": {"dark", "dragon", "level 8", "payoff"}},
    "Koa'ki Meiru Drago": {"val": 0, "tags": {"dragon", "payoff"}},
    "Prime Material Dragon": {"val": 0, "tags": {"light", "dragon", "payoff"}},
    "Battle Fader": {"val": 0, "tags": {"dark", "hand trap"}},
    "Exodius the Ultimate Forbidden Lord": {"val": 0, "tags": {"dark"}},
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

def evaluate_dynamic_synergies(hand_names, hand_data):
    bonus = 0
    discard_count = 0
    added_bewd_count = 0
    
    reckless_count = hand_names.count("Reckless Greed")
    bewd_count = hand_names.count("Blue-Eyes White Dragon")
    wsol_count = hand_names.count("White Stone of Legend")
    tradein_count = hand_names.count("Trade-In")
    coc_count = hand_names.count("Cards of Consonance")
    rejuvenation_count = hand_names.count("Super Rejuvenation")
    mse_count = hand_names.count("Magical Stone Excavation")
    debris_count = hand_names.count("Debris Dragon")
    guard_count = hand_names.count("Flamvell Guard")

    wsol_in_grave = False

    rejuvenation_resolutions = rejuvenation_count

    tuner_count = sum(1 for card in hand_data if "tuner" in card["tags"])
    level8_count = sum(1 for card in hand_data if "level 8" in card["tags"])
    dragon_count = sum(1 for card in hand_data if "dragon" in card["tags"])

    if "Future Fusion" in hand_names:
        added_bewd_count += min(3 - bewd_count, 3 - wsol_count)
        wsol_in_grave = True

    if "Foolish Burial" in hand_names:
        if bewd_count + added_bewd_count < 3:
            wsol_in_grave = True
            added_bewd_count += 1

    wsolcoc_resolutions = min(coc_count, wsol_count)
    if wsolcoc_resolutions > 0:
        wsol_in_grave = True
        coc_count -= wsolcoc_resolutions
        tuner_count -= wsolcoc_resolutions
        wsol_count -= wsolcoc_resolutions
        dragon_count -= wsolcoc_resolutions
        discard_count += wsolcoc_resolutions
        added_bewd_count += min(3 - bewd_count - added_bewd_count, wsolcoc_resolutions)

    nonwsolcoc_resolutions = min(coc_count, tuner_count)
    if nonwsolcoc_resolutions > 0:
        debris_count -= nonwsolcoc_resolutions - guard_count
        tuner_count -= nonwsolcoc_resolutions
        dragon_count -= nonwsolcoc_resolutions
        discard_count += nonwsolcoc_resolutions

    if {"Instant Fusion", "Trade-In"}.issubset(set(hand_names)) and bewd_count + added_bewd_count == 0:
        if wsol_count > 0 or (debris_count > 0 and wsol_in_grave):
            dragon_count -= 1
            added_bewd_count += 1

    level8_count += added_bewd_count

    tradein_resolutions = min(tradein_count, level8_count)
    dragon_count -= tradein_resolutions

    bonus += tradein_resolutions * 0
    bonus += wsolcoc_resolutions * 0
    bonus += nonwsolcoc_resolutions * 0

    dragon_count += added_bewd_count

    if reckless_count == 2:
        bonus += 0
    if reckless_count == 3:
        bonus += 0
    
    if "Allure of Darkness" in hand_names:
        if any("dark" in card["tags"] for card in hand_data):
            bonus += 0

    if "Red-Eyes Darkness Metal Dragon" in hand_names:
        if any("starter" in card["tags"] for card in hand_data):
            if any("payoff" in card["tags"] for card in hand_data):
                bonus+= 0
    
    if debris_count > 0:
        if any("debris target" in card["tags"] for card in hand_data):
            bonus += 0
    
    if "Instant Fusion" in hand_names:
        if "Prime Material Dragon" in hand_names:
            bonus += 0
        if tuner_count > 0:
            bonus += 0

    if rejuvenation_count > 0:
        if mse_count > 0:
            rejuvenation_resolutions += mse_count
            discard_count += min(dragon_count, 2 * mse_count)
            dragon_count -= min(dragon_count, 2 * mse_count)
    
    if "Card Destruction" in hand_names:
        discard_count += dragon_count
    
    if {"Future Fusion", "Pot of Avarice"}.issubset(set(hand_names)):
        bonus += 0
    
    if "Morphing Jar" in hand_names:
        bonus += 0 * dragon_count

    bonus += rejuvenation_resolutions * discard_count * 0

    return bonus

# --- 2. THE MULTI-PASS EVALUATOR ---
def evaluate_hand(hand_names):
    # Map names to their full data dictionary
    hand_data = [CARD_LIBRARY[name] for name in hand_names]
    score = 0

    # PASS 1: Base Quality
    # Summing the "val" of every card in hand
    score += sum(card["val"] for card in hand_data)

    score += evaluate_dynamic_synergies(hand_names, hand_data)
        
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