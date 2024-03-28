from click import group
from generate_config.commands import coordinator
from benchmark.commands import benchmark

@group()
def cli():
    pass

cli.add_command(coordinator)
cli.add_command(benchmark)

if __name__ == '__main__':
    cli()