from __future__ import annotations

from collections import ChainMap
from contextlib import contextmanager
from dataclasses import dataclass
from enum import Enum
import re
import shutil
import sys
from typing import (Any,
                    Dict,
                    IO,
                    Iterable,
                    List,
                    Optional,
                    NamedTuple,
                    overload,
                    Protocol,
                    runtime_checkable,
                    Union,)


from .default_styles import DEFAULT_STYLES
from . import errors
from .style import Style