from click import CommandCollection
from generate_config.commands import config_cli
from benchmark.commands import benchmark_cli


cli = CommandCollection(sources=[benchmark_cli, config_cli])

if __name__ == '__main__':
    cli()