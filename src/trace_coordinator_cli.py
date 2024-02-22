from click import group
from generate_config.commands import coordinator
from benchmark.commands import benchmark
from benchmark.trace_commands import open_trace, get_trace, delete_trace

@group()
def cli():
    pass

cli.add_command(coordinator)
cli.add_command(benchmark)

if __name__ == '__main__':
    cli()