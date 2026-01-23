# DT Simulation Class Structure

from abc import ABC, abstractmethod

from enum import Enum, IntEnum

class GameEvent(IntEnum):

    # --- 100: SUMMONS ---
    MONSTER_NORMAL_SUMMONED = 101
    MONSTER_SPECIAL_SUMMONED = 102
    MONSTER_FLIP_SUMMONED = 103
    MONSTER_GEMINI_SUMMONED = 104
    MONSTER_RITUAL_SUMMONED = 105
    MONSTER_FUSION_SUMMONED = 106
    MONSTER_SYNCHRO_SUMMONED = 107

    # --- 200: CARD MOVEMENT ---
    CARD_MOVED_TO_HAND = 201
    CARD_DRAWN = 202
    CARD_MOVED_TO_DECK = 203
    CARD_MOVED_TO_EXTRA_DECK = 204
    CARD_MOVED_TO_GY = 205
    CARD_MOVED_TO_FIELD = 206
    CARD_SET_TO_FIELD = 207
    CARD_MOVED_TO_BANISHED = 208
    CARD_DISCARDED_FOR_COST = 209
    CARD_DISCARDED_BY_EFFECT = 210
    MONSTER_TRIBUTED = 211

    # --- 300: STATE CHANGES & ATTACK ---
    MONSTER_BATTLE_POSITION_CHANGED = 301
    MONSTER_FLIPPED_FACEUP = 302
    MONSTER_FLIPPED_FACEDOWN = 303
    MONSTER_DECLARE_ATTACK = 304
    MONSTER_ATTACK_STOPPED = 305
    MONSTER_REPLAY_ATTACK = 306
    MONSTER_ATTACK_NEGATED = 307
    MONSTER_TARGETED_BY_ATTACK = 308
    MONSTER_TARGETED_BY_EFFECT = 309
    MONSTER_DESTROYED_BY_BATTLE = 310
    MONSTER_DESTROYED_BY_EFFECT = 311

    
    # --- 400: STAT MODIFICATIONS ---
    ATTACK_MODIFIED = 401
    DEFENSE_MODIFIED = 402
    LEVEL_MODIFIED = 403

    # --- 500: LIFE POINTS & DAMAGE ---
    LIFE_POINTS_GAINED = 501
    LIFE_POINTS_LOST = 502
    BATTLE_DAMAGE_INFLICTED = 503
    EFFECT_DAMAGE_INFLICTED = 504

    # --- 600: ACTIVATIONS ---
    CARD_ACTIVATED = 601
    EFFECT_ACTIVATED = 602
    ACTIVATION_NEGATED = 603
    EFFECT_NEGATED = 604

    # --- 1000: PHASE TRANSITIONS ---
    ENTER_DRAW_PHASE = 1001
    ENTER_STANDBY_PHASE = 1002
    ENTER_MAIN_PHASE_1 = 1003
    ENTER_BATTLE_PHASE = 1004
    ENTER_MAIN_PHASE_2 = 1005
    ENTER_END_PHASE = 1006

    EXIT_DRAW_PHASE = 1011
    EXIT_STANDBY_PHASE = 1012
    EXIT_MAIN_PHASE_1 = 1013
    EXIT_BATTLE_PHASE = 1014
    EXIT_MAIN_PHASE_2 = 1015
    EXIT_END_PHASE = 1016

    # --- 1100: BATTLE STEP DETAILS ---
    ENTER_BATTLE_STARTSTEP = 1101
    ENTER_BATTLE_ENDSTEP = 1102
    EXIT_BATTLE_STARTSTEP = 1103
    EXIT_BATTLE_ENDSTEP = 1104
    ENTER_BATTLESTEP_1 = 1105 # Attack Declaration
    ENTER_BATTLESTEP_2 = 1106 # Before the Damage Step
    

    # --- 1200: DAMAGE STEP (Sub-steps 1-7) ---
    ENTER_DAMAGE_1 = 1201
    ENTER_DAMAGE_2 = 1202
    ENTER_DAMAGE_3 = 1203
    ENTER_DAMAGE_4 = 1204
    ENTER_DAMAGE_5 = 1205
    ENTER_DAMAGE_6 = 1206
    ENTER_DAMAGE_7 = 1207

    EXIT_DAMAGE_1 = 1211
    EXIT_DAMAGE_2 = 1212
    EXIT_DAMAGE_3 = 1213
    EXIT_DAMAGE_4 = 1214
    EXIT_DAMAGE_5 = 1215
    EXIT_DAMAGE_6 = 1216
    EXIT_DAMAGE_7 = 1217

    # --- 1300: END OF BATTLE PHASE ---
    BATTLE_WAS_CONDUCTED = 1301

class CardLegality(Enum):
    FORBIDDEN = 0
    LIMITED = 1
    SEMI_LIMITED = 2
    UNLIMITED = 3

class Speed(Enum):
    SPEED_1 = 1
    SPEED_2 = 2
    SPEED_3 = 3

class SpellType(Enum):
    NORMAL = "normal"
    QUICK_PLAY = "quick-play"
    CONTINUOUS = "continuous"
    FIELD = "field"
    EQUIP = "equip"
    RITUAL = "ritual"

class TrapType(Enum):
    NORMAL = "normal"
    COUNTER = "counter"
    CONTINUOUS = "continuous"

class MonsterType(Enum):
    BEAST = "beast"
    DIVINE_BEAST = "divine-beast"
    DRAGON = "dragon"
    WINGED_BEAST = "winged-beast"
    BEAST_WARRIOR = "beast-warrior"
    WARRIOR = "warrior"
    ZOMBIE = "zombie"
    AQUA = "aqua"
    MACHINE = "machine"
    FISH = "fish"
    INSECT = "insect"
    FIEND = "fiend"
    PYRO = "pyro"
    FAIRY = "fairy"
    DINOSAUR = "dinosaur"
    PLANT = "plant"
    PSYCHIC = "psychic"
    REPTILE = "reptile"
    ROCK = "rock"
    SEA_SERPENT = "sea-serpent"
    SPELLCASTER = "spellcaster"
    THUNDER = "thunder"

class MonsterAttribute(Enum):
    WATER = "water"
    FIRE = "fire"
    EARTH = "earth"
    WIND = "wind"
    DARK = "dark"
    LIGHT = "light"
    DIVINE = "divine"

class MonsterCategory(Enum):
    NORMAL = "normal"
    EFFECT = "effect"
    FUSION = "fusion"
    RITUAL = "ritual"
    SYNCHRO = "synchro"

class MonsterCategory2(Enum):
    TUNER = "tuner"
    FLIP = "flip"
    GEMINI = "gemini"
    SPIRIT = "spirit"
    TOON = "toon"
    UNION = "union"

class Position(Enum):
    ATTACK_FACE_UP = 1
    DEFENSE_FACE_UP = 2
    DEFENSE_FACE_DOWN = 3

class Effect(ABC):
    def __init__(self, speed: Speed):
        self.speed = speed
    
    @abstractmethod
    def resolve(self, game_state, source_card):
        pass


class Card(ABC):
   
    def __init__(self, card_name: str, card_legality: CardLegality, card_text: str):
        self.card_name = card_name
        self.card_legality = card_legality
        self.card_text = card_text
        self.effects: list[Effect] = []

class Spell(Card):

    def __init__(self, card_name: str, card_legality: CardLegality, card_text: str, spell_type: SpellType):
        super().__init__(card_name, card_legality, card_text)
        self.spell_type = spell_type


class Trap(Card):
    def __init__(self, card_name: str, card_legality: CardLegality, card_text: str, trap_type: TrapType):
        super().__init__(card_name, card_legality, card_text)
        self.trap_type = trap_type

class Monster(Card):
    def __init__(
            self, 
            card_name: str,
            card_legality: CardLegality,
            card_text: str,
            level: int,
            attack: int,
            defense: int,
            monster_type: MonsterType,
            monster_attribute: MonsterAttribute,
            monster_category: MonsterCategory,
            monster_category_2: list[MonsterCategory2] = None,
            effects: list[Effect] = None
        ):

        super().__init__(card_name, card_legality, card_text)

        self.original_level = level
        self.original_attack = attack
        self.original_defense = defense

        self.level = level
        self.attack = attack
        self.defense = defense

        self.position: Position = None
        self.is_face_up: bool = False

        self.monster_type = monster_type
        self.monster_attribute = monster_attribute
        self.monster_category = monster_category
        self.monster_category_2 = monster_category_2 or []
        self.effects = effects or []




