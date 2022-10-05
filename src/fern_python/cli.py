import typer

from fern_python.generated import ir_types
from fern_python.generators import PydanticModelGenerator
from generator_exec.resources.config import GeneratorConfig


def main(path_to_config_json: str) -> None:
    config = GeneratorConfig.parse_file(path_to_config_json)
    ir = ir_types.IntermediateRepresentation.parse_file(config.ir_filepath)
    generator = PydanticModelGenerator(intermediate_representation=ir, output_filepath=config.output.path)
    generator.run()


if __name__ == "__main__":
    typer.run(main)
