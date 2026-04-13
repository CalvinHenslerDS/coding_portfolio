import random
import matplotlib.pyplot as plt
from itertools import combinations
import math

CARD_LIBRARY = {

    "Red-Eyes Darkness Metal Dragon": {"val": 0, "tags": {"dragon", "dark"}},
    "Blue-Eyes White Dragon": {"val": 0, "tags": {"light", "dragon", "level 8", "payoff"}},
    "White Stone of Legend": {"val": 10, "tags": {"light", "tuner", "dragon", "debris target", "starter"}},
    "Debris Dragon": {"val": 30, "tags": {"tuner", "dragon", "starter"}},
    "Tragoedia": {"val": 90, "tags": {"dark", "hand trap"}},
    "Vortex Trooper": {"val": 85, "tags": {"debris target"}},
    "Gorz the Emissary of Darkness": {"val": 85, "tags": {"dark", "hand trap"}},
    "Morphing Jar": {"val": 90, "tags": set()},
    "Flamvell Guard": {"val": 30, "tags": {"tuner", "dragon", "debris target", "starter"}},
    "Tri-Horned Dragon": {"val": 0, "tags": {"dark", "dragon", "level 8", "payoff"}},
    "Koa'ki Meiru Drago": {"val": 60, "tags": {"dragon", "payoff"}},
    "Prime Material Dragon": {"val": 0, "tags": {"light", "dragon", "payoff"}},
    "Battle Fader": {"val": 30, "tags": {"dark", "hand trap"}},
    "Exodius the Ultimate Forbidden Lord": {"val": 0, "tags": {"dark"}},
    "Card Trooper": {"val": 70, "tags": {"debris target"}},
    "Snipe Hunter": {"val": 40, "tags": {"dark"}},
    "Frost and Flame Dragon": {"val": 0, "tags": {"dragon", "water"}},
    "Tyrant Dragon": {"val": 0, "tags": {"fire", "dragon", "level 8", "payoff"}},
    "Chaos Sorcerer": {"val": 0, "tags": {"dark"}},
    "Dark Armed Dragon": {"val": 0, "tags": {"dark", "dragon"}},
    "Dragon Ice": {"val": 0, "tags": {"water", "dragon"}},
    "White Night Dragon": {"val": 0, "tags": {"water", "dragon", "level 8", "payoff"}},
    "Sangan": {"val": 50, "tags": {"dark"}},
    "Clear Vice Dragon": {"val": 0, "tags": {"dark", "dragon", "level 8", "payoff"}},


    "Trade-In": {"val": 0, "tags": set()},
    "Cards of Consonance": {"val": 0, "tags": set()},
    "Super Rejuvenation": {"val": 0, "tags": set()},
    "Upstart Goblin": {"val": 5, "tags": set()},
    "Allure of Darkness": {"val": 0, "tags": set()},
    "Instant Fusion": {"val": 0, "tags": {"starter"}},
    "Giant Trunade": {"val": 30, "tags": {"sweeper"}},
    "Heavy Storm": {"val": 60, "tags": {"sweeper"}},
    "Pot of Avarice": {"val": 0, "tags": set()},
    "Card Destruction": {"val": 50, "tags": set()},
    "Future Fusion": {"val": 20, "tags": set()},
    "Foolish Burial": {"val": 4, "tags": set()},
    "Magical Stone Excavation": {"val": 0, "tags": set()},
    "Dark World Dealings": {"val": 3, "tags": set()},
    "D.D.R. - Different Dimension Reincarnation": {"val": 0, "tags": set()},

    "Reckless Greed": {"val": 70, "tags": set()},
    "Torrential Tribute": {"val": 90, "tags": {"defense"}},
    "Mirror Force": {"val": 75, "tags": {"defense"}},
    "Legacy of Yata-Garasu": {"val": 3, "tags": set()},
    "Jar of Greed": {"val": 3, "tags": set()},
    "Trap Dustshoot": {"val": 90, "tags": set()},

}

def resolve_future_fusion(hand, deck, grave):
    priority_pool = [
        "White Stone of Legend", "White Stone of Legend", "White Stone of Legend",
        "Koa'ki Meiru Drago",
        "Prime Material Dragon",
        "Flamvell Guard",
    ]

    mill_count = 0
    stones_sent = 0
    has_debris = "Debris Dragon" in hand
    has_redeyes = "Red-Eyes Darkness Metal Dragon" in hand

    for card_name in priority_pool:
        if mill_count < 5 and card_name in deck:
            deck.remove(card_name)
            grave.append(card_name)
            mill_count += 1
            if card_name == "White Stone of Legend":
                stones_sent += 1
    
    while mill_count < 5:

        if not has_debris and "Debris Dragon" in deck:
            target = "Debris Dragon"
        elif not has_redeyes and "Red-Eyes Darkness Metal Dragon" in deck:
            target = "Red-Eyes Darkness Metal Dragon"
        elif "Debris Dragon" in deck:
            target = "Debris Dragon"
        elif "Red-Eyes Darkness Metal Dragon" in deck:
            target = "Red-Eyes Darkness Metal Dragon"
        elif "Blue-Eyes White Dragon" in deck:
            target = "Blue-Eyes White Dragon"
        else:
            break
        
        deck.remove(target)
        grave.append(target)
        mill_count += 1
    
    for i in range(stones_sent):
        if "Blue-Eyes White Dragon" in deck:
            deck.remove("Blue-Eyes White Dragon")
            hand.append("Blue-Eyes White Dragon")
    
    return hand, deck, grave

# Implement expected value of drawing into rejuv for non-rejuv hands

def get_dynamic_weight(card_name, hand, deck, grave, discard_count):
    tags = CARD_LIBRARY[card_name]["tags"]
    count_in_hand = hand.count(card_name)
    
#     "Red-Eyes Darkness Metal Dragon": {"val": 0, "tags": {"dragon", "dark"}},
#     "Tragoedia": {"val": 90, "tags": {"dark", "hand trap"}},
#     "Gorz the Emissary of Darkness": {"val": 85, "tags": {"dark", "hand trap"}},
#     "Debris Dragon"
#     "White Stone of Legend"
#     "Flamvell Guard": {"val": 30, "tags": {"tuner", "dragon", "debris target", "starter"}},
#     "Tri-Horned Dragon": {"val": 0, "tags": {"dark", "dragon", "level 8", "payoff"}},
#     "Koa'ki Meiru Drago": {"val": 60, "tags": {"dragon", "payoff"}},
#     "Prime Material Dragon": {"val": 0, "tags": {"light", "dragon", "payoff"}},
#     "Snipe Hunter": {"val": 40, "tags": {"dark"}},

#     "Super Rejuvenation": {"val": 0, "tags": set()},
#     "Pot of Avarice": {"val": 0, "tags": set()},
#     "Card Destruction": {"val": 50, "tags": set()},
#     "Future Fusion": {"val": 20, "tags": set()},
#     "Foolish Burial"
#     "Dark World Dealings": {"val": 3, "tags": set()},


    if card_name in [
        "Reckless Greed",
        "Trap Dustshoot"
    ]:
        return 100
    
    if card_name in [
        "Pot of Avarice", 
        "Heavy Storm", 
        "Giant Trunade",
        "Instant Fusion",
        "Vortex Trooper",
        "Morphing Jar",
        "Card Trooper",
        "Sangan",
        "Snipe Hunter"
    ]:
        return -100
    
    if card_name in [
        "Torrential Tribute",
    ]:
        return 50
    if card_name in [
        "Mirror Force"
    ]:
        return 45

    if card_name in ["Magical Stone Excavation"]:
        if "Super Rejuvenation" not in hand:
            return -100
        else:
            dragons_in_hand =  sum(1 for c in hand if "dragon" in CARD_LIBRARY[c]["tags"])
            return 5 + ((min(2,dragons_in_hand) + discard_count) * 50)

    if "level 8" in tags:
        tradeins_in_deck = deck.count("Trade-In")
        # Weight scales: 0 Trade-Ins = 5 pts, 3 Trade-Ins = 50 pts
        return 5 + (tradeins_in_deck * 10)

    if "tuner" in tags:
        coc_in_deck = deck.count("Cards of Consonance")
        return 5 + (coc_in_deck * 10)

    if card_name == "Trade-In":
        targets_in_deck = sum(1 for c in deck if "level 8" in CARD_LIBRARY[c]["tags"])
        return 5 + (targets_in_deck * 10)

    if card_name == "Cards of Consonance":
        targets_in_deck = sum(1 for c in deck if "tuner" in CARD_LIBRARY[c]["tags"])
        return 5 + (targets_in_deck * 10)

    if card_name == "Allure of Darkness":
        targets_in_deck = sum(1 for c in deck if "dark" in CARD_LIBRARY[c]["tags"])

    if count_in_hand > 1:
        weight -= 50

    # Default to the library's base value
    return CARD_LIBRARY[card_name].get("val", 40)

def simulate_hand_resolution(starting_hand, starting_deck, starting_grave):
    hand = list(starting_hand)
    deck = list(starting_deck)
    # We track 'actions' to see how much the hand 'moved'
    actions_taken = []
    
    # We use a while loop because one action (like Trade-In) 
    # might enable another action (like Cards of Consonance)
    still_moving = True
    while still_moving:
        still_moving = False
        
        # 1. PRIORITY: DECK THINNING (Searchers/Millers)
        # Future Fusion: Massive thinning (e.g., 5-8 cards)
        if "Future Fusion" in hand:
            # Example: Send 3 Stone, 2 BEWD to Grave
            targets = ["White Stone of Legend", "White Stone of Legend", "White Stone of Legend", "Blue-Eyes White Dragon", "Blue-Eyes White Dragon"]
            for t in targets:
                if t in deck: deck.remove(t)
            # Stone's effect: Add BEWD from deck to hand
            for _ in range(3):
                if "Blue-Eyes White Dragon" in deck:
                    deck.remove("Blue-Eyes White Dragon")
                    hand.append("Blue-Eyes White Dragon")
            
            hand.remove("Future Fusion")
            actions_taken.append("Future Fusion")
            still_moving = True
            continue # Re-start loop to check new hand state

        # 2. PRIORITY: DISCARD DRAWS (Trade-In, CoC)
        # Check for Cards of Consonance + White Stone specifically (High Value)
        if "Cards of Consonance" in hand and "White Stone of Legend" in hand:
            hand.remove("Cards of Consonance")
            hand.remove("White Stone of Legend")
            # Draw 2
            for _ in range(2): 
                if deck: hand.append(deck.pop())
            # Stone Search
            if "Blue-Eyes White Dragon" in deck:
                deck.remove("Blue-Eyes White Dragon")
                hand.append("Blue-Eyes White Dragon")
            
            actions_taken.append("CoC-Stone")
            still_moving = True
            continue

        # Trade-In: Requires Level 8 in hand
        lvl8_in_hand = [c for c in hand if "level 8" in CARD_LIBRARY[c]["tags"]]
        if "Trade-In" in hand and lvl8_in_hand:
            hand.remove("Trade-In")
            hand.remove(lvl8_in_hand[0]) # Discard first available Lvl 8
            for _ in range(2):
                if deck: hand.append(deck.pop())
            
            actions_taken.append("Trade-In")
            still_moving = True
            continue

        # 3. PRIORITY: HAND REFRESH (The "Bridge" cards)
        if "Vortex Trooper" in hand:
            # Logic: Shuffle back 2 worst cards (e.g., duplicate Dragons)
            # For simplicity, we'll shuffle back 2 random cards or specific payoffs
            hand.remove("Vortex Trooper")
            # Draw 2
            for _ in range(2):
                if deck: hand.append(deck.pop())
            
            actions_taken.append("Vortex Trooper")
            still_moving = True
            continue

    return hand, actions_taken

# --- Integration into your Monte Carlo ---
# results = []
# for _ in range(iterations):
#     initial_hand = draw_hand(6)
#     remaining_deck = [c for c in my_deck if c not in initial_hand] # simplified
#     final_hand, actions = simulate_hand_resolution(initial_hand, remaining_deck)
#     score = evaluate_final_state(final_hand, actions

def evaluate_dynamic_synergies(hand_names, hand_data, full_deck):
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

    bonus += tradein_resolutions * 100
    bonus += wsolcoc_resolutions * 150
    bonus += nonwsolcoc_resolutions * 100

    dragon_count += added_bewd_count

    if reckless_count == 2:
        bonus += 100
    if reckless_count == 3:
        bonus += 200
    
    if "Allure of Darkness" in hand_names:
        if any("dark" in card["tags"] for card in hand_data):
            bonus += 0

    if "Red-Eyes Darkness Metal Dragon" in hand_names:
        if any("starter" in card["tags"] for card in hand_data):
            if any("payoff" in card["tags"] for card in hand_data):
                bonus += 50
    
    if debris_count > 0:
        if any("debris target" in card["tags"] for card in hand_data):
            bonus += 50
    
    if "Instant Fusion" in hand_names:
        if "Prime Material Dragon" in hand_names:
            bonus += 50
        if tuner_count > 0:
            bonus += 50

    if rejuvenation_count > 0:
        if mse_count > 0:
            rejuvenation_resolutions += mse_count
            discard_count += min(dragon_count, 2 * mse_count)
            dragon_count -= min(dragon_count, 2 * mse_count)
    
    if "Card Destruction" in hand_names:
        discard_count += dragon_count
    
    if {"Future Fusion", "Pot of Avarice"}.issubset(set(hand_names)):
        bonus += 200
    
    if "Morphing Jar" in hand_names:
        bonus += 50 * dragon_count

    bonus += rejuvenation_resolutions * discard_count * 50

    potential_draws = 0

    if "Vortex Trooper" in hand_names: potential_draws += 2
    if "Upstart Goblin" in hand_names: potential_draws += 1
    if "Dark World Dealings" in hand_names: potential_draws += 1

    level8_count = sum(1 for card in hand_data if "level 8" in card["tags"]) + added_bewd_count


    return bonus

class MonteCarloSimulator:
    def __init__(self, deck_list, library):
        self.full_deck = deck_list
        self.library = library

    def draw_hand(self, size=5, forced_cards=None):
        deck = self.full_deck[:]
        hand = []
        
        # 1. Add forced cards first
        if forced_cards:
            for card in forced_cards:
                if card in deck:
                    deck.remove(card)
                    hand.append(card)
        
        # 2. Shuffle and fill the rest
        random.shuffle(deck)
        while len(hand) < size and deck:
            hand.append(deck.pop())
            
        return hand

    def run(self, iterations=1000, hand_size=5, forced_cards=None):
        results = []
        
        for _ in range(iterations):
            hand_names = self.draw_hand(hand_size, forced_cards)
            hand_data = [self.library[name] for name in hand_names]
            
            # Calculate Scores
            base_score = sum(card['val'] for card in hand_data)
            bonus_score = evaluate_dynamic_synergies(hand_names, hand_data)
            total_score = base_score + bonus_score
            
            results.append({
                "hand": hand_names,
                "base": base_score,
                "bonus": bonus_score,
                "total": total_score
            })
            
        return results

# --- 2. EXECUTION & REPORTING ---

# Define your 40-card deck
my_deck = [
    "Red-Eyes Darkness Metal Dragon", "Red-Eyes Darkness Metal Dragon", "Red-Eyes Darkness Metal Dragon",
    "Blue-Eyes White Dragon", "Blue-Eyes White Dragon", "Blue-Eyes White Dragon",
    "White Stone of Legend", "White Stone of Legend", "White Stone of Legend",
    "Debris Dragon", "Debris Dragon", "Debris Dragon",
    "Vortex Trooper", "Vortex Trooper", "Vortex Trooper",
    "Prime Material Dragon",
    "Koa'ki Meiru Drago",
    "Tragoedia", "Gorz the Emissary of Darkness",
    "Trade-In", "Trade-In", "Trade-In",
    "Cards of Consonance", "Cards of Consonance", "Cards of Consonance",
    "Super Rejuvenation", "Super Rejuvenation", "Super Rejuvenation",
    "Instant Fusion", "Instant Fusion",
    "Magical Stone Excavation", "Magical Stone Excavation",
    "Allure of Darkness",
    "Future Fusion", 
    "Card Destruction",
    "Pot of Avarice",
    "Heavy Storm",
    "Reckless Greed", "Reckless Greed", "Reckless Greed"
    # ... fill until 40
]

sim = MonteCarloSimulator(my_deck, CARD_LIBRARY)
# Example: Run 1000 trials, forcing 1 copy of Future Fusion to see how it performs
raw_data = sim.run(iterations=10000, hand_size=6, forced_cards=None)

# Sort by total score to find the "God Hands"
sorted_results = sorted(raw_data, key=lambda x: x['total'], reverse=True)

print(f"{'HAND':<80} | {'BASE':<5} | {'BONUS':<5} | {'TOTAL':<5}")
print("-" * 105)
for res in sorted_results[:100]: # Print top 10 hands
    hand_str = ", ".join(res['hand'])
    print(f"{hand_str:<80} | {res['base']:<5} | {res['bonus']:<5} | {res['total']:<5}")

    import statistics

def print_statistical_summary(results):
    scores = [res['total'] for res in results]
    
    # Core Metrics
    mean_score = statistics.mean(scores)
    median_score = statistics.median(scores)
    std_dev = statistics.stdev(scores)
    max_score = max(scores)
    min_score = min(scores)
    
    # Probability of "Playable" Hands
    # Assume a score of 150+ is a 'good' opening
    success_threshold = 150
    success_rate = (sum(1 for s in scores if s >= success_threshold) / len(scores)) * 100

    print("--- DECK PERFORMANCE SUMMARY ---")
    print(f"Total Iterations:  {len(results)}")
    print(f"Mean Score:        {mean_score:.2f}")
    print(f"Median Score:      {median_score:.2f} (50th Percentile)")
    print(f"Std Deviation:     {std_dev:.2f} (Lower is more consistent)")
    print(f"Score Range:       {min_score} - {max_score}")
    print(f"Consistency:       {success_rate:.2f}% of hands scored above {success_threshold}")
    print("--------------------------------")

print_statistical_summary(raw_data)

def print_percentiles(results):
    scores = sorted([res['total'] for res in results])
    count = len(scores)
    
    p90 = scores[int(count * 0.90)] # The "God Hand" threshold
    p10 = scores[int(count * 0.10)] # The "Brick" threshold
    
    print(f"Top 10% (P90):    {p90}")
    print(f"Bottom 10% (P10): {p10}")
    print(f"Power Gap (P90-P10): {p90 - p10}")

print_percentiles(raw_data)



def plot_score_distribution(results):
    scores = [res['total'] for res in results]
    
    plt.hist(scores, bins=30, color='skyblue', edgecolor='black')
    plt.axvline(sum(scores)/len(scores), color='red', linestyle='dashed', linewidth=1, label='Mean')
    
    plt.title('Opening Hand Quality Distribution')
    plt.xlabel('Hand Score')
    plt.ylabel('Frequency (Number of Hands)')
    plt.legend()
    plt.grid(axis='y', alpha=0.3)
    
    #plt.savefig('hand_distribution.png')
    #print("Plot saved as hand_distribution.png")

    plt.show()

plot_score_distribution(raw_data)

import csv

def export_results_to_csv(results, filename="simulation_results.csv"):
    # 1. Define the headers based on your dictionary keys
    # We join the 'hand' list into a single string so it fits in one CSV cell
    keys = ["hand", "base", "bonus", "total"]

    with open(filename, mode='w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        
        dict_writer.writeheader()
        
        # 2. Process and write the rows
        for res in results:
            # Create a copy so we don't modify the original raw_data
            row = res.copy()
            # Convert the list of card names into one string separated by semicolons
            row['hand'] = "; ".join(row['hand'])
            dict_writer.writerow(row)

    print(f"Successfully exported {len(results)} trials to {filename}")

# Call the function
#export_results_to_csv(raw_data)