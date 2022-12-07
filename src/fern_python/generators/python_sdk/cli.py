import typer

from fern_python.cli.generator_cli import GeneratorCli

from .python_sdk_generator import PythonSdkGenerator


def main(path_to_config_json: str) -> None:
    python_sdk_generator = PythonSdkGenerator()
    cli = GeneratorCli(python_sdk_generator, path_to_config_json)
    cli.run()


if __name__ == "__main__":
    typer.run(main)
