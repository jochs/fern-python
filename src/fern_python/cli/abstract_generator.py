from abc import ABC, abstractmethod

from generator_exec.resources.config import GeneratorConfig

from fern_python.codegen.project import Project, PyProjectTomlConfig
from fern_python.generated.ir_types import IntermediateRepresentation
from fern_python.generator_exec_wrapper import GeneratorExecWrapper


class AbstractGenerator(ABC):
    def generate(
        self,
        *,
        generator_exec_wrapper: GeneratorExecWrapper,
        ir: IntermediateRepresentation,
        generator_config: GeneratorConfig,
    ) -> None:
        pyproject_toml_config = generator_config.output.mode.visit(
            download_files=lambda: None,
            publish=lambda publish: PyProjectTomlConfig(
                package_name=publish.registries_v_2.pypi.package_name, package_version=publish.version
            ),
        )
        with Project(
            filepath=generator_config.output.path,
            project_name=ir.api_name,
            pyproject_toml_config=pyproject_toml_config,
        ) as project:
            self.run(
                generator_exec_wrapper=generator_exec_wrapper,
                ir=ir,
                generator_config=generator_config,
                project=project,
            )

    @abstractmethod
    def run(
        self,
        *,
        generator_exec_wrapper: GeneratorExecWrapper,
        ir: IntermediateRepresentation,
        generator_config: GeneratorConfig,
        project: Project,
    ) -> None:
        pass
