from abc import ABC, abstractmethod
from typing import List, Tuple

import fern.ir.pydantic as ir_types
from fern.generator_exec.sdk.resources import GeneratorConfig

from fern_python.codegen import ExportStrategy, Filepath

EMPTY_DIRECTORIES: Tuple[Filepath.DirectoryFilepathPart, ...] = ()


class FernFilepathCreator(ABC):
    def __init__(self, ir: ir_types.IntermediateRepresentation, generator_config: GeneratorConfig):
        self._ir = ir
        self._generator_config = generator_config

    def generate_filepath_prefix(self) -> Tuple[Filepath.DirectoryFilepathPart, ...]:
        return self._generator_config.output.mode.visit(
            download_files=lambda: EMPTY_DIRECTORIES,
            publish=lambda x: (
                (
                    Filepath.DirectoryFilepathPart(
                        module_name=self._ir.api_name.snake_case.unsafe_name,
                        export_strategy=ExportStrategy(export_all=True),
                    ),
                )
                + tuple(
                    Filepath.DirectoryFilepathPart(
                        module_name=folder_name,
                        export_strategy=ExportStrategy(export_all=True),
                    )
                    for folder_name in self._get_folders_inside_src()
                )
            ),
        )

    @abstractmethod
    def _get_folders_inside_src(self) -> List[str]:
        ...
