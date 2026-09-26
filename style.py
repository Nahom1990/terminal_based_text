import sys
from functools import lru_cache
from itertools import count
from operator import attrgetter
from pickle import dumps,loads
from random import getrandbits
from typing import Any,Dict, Iterable, List, Optional,Type,Union,cast

from . import errors
from .color import Color, ColorParseError, ColorSystem, blend_rgb
from .repr import Result, rich_repr
from .terminal_theme import DEFAULT_TERMINAL_THEME, TerminalTheme

_hash_getter=attrgetter(
    "_color", "_bgcolor", "_attributes", "_set_attributes", "_link", "_meta"

)