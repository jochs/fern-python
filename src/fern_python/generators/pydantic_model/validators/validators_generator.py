from abc import ABC, abstractmethod
from typing import Sequence

from fern_python.codegen import AST
from fern_python.pydantic_codegen import PydanticModel

from .validator_generators import ValidatorGenerator


class ValidatorsGenerator(ABC):
    _VALIDATOR_CLASS_NAME = "Validators"

    def __init__(self, model: PydanticModel):
        self._model = model

    def add_validators(self) -> None:
        for generator in self._get_validator_generators():
            generator.add_validator_to_model()

        validators_class = AST.ClassDeclaration(
            name=ValidatorsGenerator._VALIDATOR_CLASS_NAME,
        )
        self._populate_validators_class(validators_class=validators_class)
        self._model.add_inner_class(inner_class=validators_class)

    def _get_reference_to_validators_class(self) -> AST.ClassReference:
        return AST.ClassReference(
            qualified_name_excluding_import=(self._model.name, ValidatorsGenerator._VALIDATOR_CLASS_NAME)
        )

    @abstractmethod
    def _populate_validators_class(self, validators_class: AST.ClassDeclaration) -> None:
        ...

    @abstractmethod
    def _get_validator_generators(self) -> Sequence[ValidatorGenerator]:
        ...
