# DT Simulation Class Structure

from abc import ABC, abstractmethod
from enum import Enum

from enum import Enum

class GameEvent(Enum):

    # Summons
    MONSTER_NORMAL_SUMMONED = 1
    MONSTER_SPECIAL_SUMMONED = 2
    MONSTER_FLIP_SUMMONED = 3
    MONSTER_GEMINI_SUMMONED = 4
    MONSTER_RITUAL_SUMMONED = 5
    MONSTER_FUSION_SUMMONED = 6
    MONSTER_SYNCHRO_SUMMONED = 7

    # Card movement
    CARD_MOVED_TO_HAND = 8
    CARD_DRAWN =
    CARD_MOVED_TO_DECK = 9
    CARD_MOVED_TO_EXTRA_DECK = 10
    CARD_MOVED_TO_GY = 11
    CARD_MOVED_TO_FIELD = 12
    CARD_SET_TO_FIELD = 
    CARD_MOVED_TO_BANISHED = 13

    MONSTER_BATTLE_POSITION_CHANGED = 14
    MONSTER_FLIPPED_FACEUP = 15
    MONSTER_FLIPPED_FACEDOWN = 16
    MONSTER_DECLARE_ATTACK = 17
    MONSTER_TARGETED_BY_ATTACK = 
    MONSTER_TARGETED_BY_EFFECT = 
    MONSTER_DESTROYED_BY_BATTLE = 14
    MONSTER_DESTROYED_BY_EFFECT = 15
    MONSTER_WAS_TRIBUTED = 
    MONSTER_WAS_DISCARDED = 

    ATTACK_MODIFIED = 16
    DEFENSE_MODIFIED = 17
    LEVEL_MODIFIED = 18

    LIFE_POINTS_GAINED = 19
    LIFE_POINTS_LOST = 20
    BATTLE_DAMAGE_INFLICTED = 
    EFFECT_DAMAGE_INFLICTED = 
    CARD_ACTIVATED = 21
    
    # Phase transitions
    ENTER_DRAW_PHASE = 22
    ENTER_STANDBY_PHASE = 23
    ENTER_MAIN_PHASE_1 = 24
    ENTER_BATTLE_PHASE = 25
    ENTER_MAIN_PHASE_2 = 26
    ENTER_END_PHASE = 27

    EXIT_DRAW_PHASE = 28
    EXIT_STANDBY_PHASE = 29
    EXIT_MAIN_PHASE_1 = 30
    EXIT_BATTLE_PHASE = 31
    EXIT_MAIN_PHASE_2 = 32
    EXIT_END_PHASE = 33

    ENTER_BATTLE_STARTSTEP = 34
    ENTER_BATTLE_ENDSTEP = 35

    EXIT_BATTLE_STARTSTEP = 36
    EXIT_BATTLE_ENDSTEP = 37

    ENTER_BATTLESTEP_1 = 38 # Attack Declaration
    ENTER_BATTLESTEP_2 = 39 # Before the Damage Step

    ENTER_DAMAGE_1 = 40
    ENTER_DAMAGE_2 = 41
    ENTER_DAMAGE_3 = 42
    ENTER_DAMAGE_4 = 43
    ENTER_DAMAGE_5 = 44
    ENTER_DAMAGE_6 = 45
    ENTER_DAMAGE_7 = 46

    EXIT_DAMAGE_1 = 47
    EXIT_DAMAGE_2 = 48
    EXIT_DAMAGE_3 = 49
    EXIT_DAMAGE_4 = 50
    EXIT_DAMAGE_5 = 51
    EXIT_DAMAGE_6 = 52
    EXIT_DAMAGE_7 = 53

    BATTLE_WAS_CONDUCTED = 

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




