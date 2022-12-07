from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Callable, Optional, Set, Tuple

import fern.ir.pydantic as ir_types

from fern_python.codegen import AST, Filepath


class PydanticGeneratorContext(ABC):
    