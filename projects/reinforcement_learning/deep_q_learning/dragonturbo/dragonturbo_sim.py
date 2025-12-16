# DT Simulation Class Structure

from abc import ABC, abstractmethod
from enum import Enum



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

class Effect(ABC):
    def __init__(self, speed: Speed):
        self.speed = speed
    
    @abstractmethod
    def resolve(self, game_state, source_card):
        pass


class Card(ABC):
   
    def __init__(self, card_name: str, card_legality: CardLegality):
        self.card_name = card_name
        self.card_legality = card_legality
        self.effects: list[Effect] = []

class Spell(Card):

    def __init__(self, card_name: str, card_legality: CardLegality, spell_type: SpellType):
        super().__init__(card_name, card_legality)
        self.spell_type = spell_type


class Trap(Card):
    def __init__(self, card_name: str, card_legality: CardLegality, trap_type: TrapType):
        super().__init__(card_name, card_legality)
        self.trap_type = trap_type

class Monster(Card):
    def __init__(self, card_name: str, card_legality: CardLegality, level: int, monster_type: MonsterType, monster_attribute: MonsterAttribute, monster_category: MonsterCategory, effects: list[Effect] = None):
        super().__init__(card_name, card_legality)
        self.effects = effects or []
        self.level = level
        self.monster_type = monster_type
        self.monster_attribute = monster_attribute
        self.monster_category = monster_category


