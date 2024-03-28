from click import option, group, version_option, pass_context
from tsp.tsp_client import TspClient
import json
import csv
import logging, logging.config

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
POLLING_TIME = 0.5


@group(context_settings=CONTEXT_SETTINGS)
@version_option(version='1.0.0')
@option('--ip', type=str, default='localhost', help='IP address of trace server', envvar="TSP_CLI_BENCHMARK_IP")
@option('--port', '-p', type=int, default=8080, help='Port of trace server', envvar="TSP_CLI_BENCHMARK_PORT")
@option('--debug', '-d', is_flag=True, default=False)
@option('--logging-config', type=str, default='logging.ini')
@pass_context
def benchmark(ctx, ip: str, port: int, debug: bool, logging_config: str):
    """Benchmark commands."""
    ctx.obj = TspClient(f'http://{ip}:{port}/tsp/api/')

    if debug:
        logging.config.fileConfig(fname=logging_config)
        logging.debug(f"Target: {ctx.obj.base_url}")


def log_benchmark(target, endpoint, elapsed_time):
    with open('benchmark-tsp.csv', '+a', encoding='utf-8') as benchmark_file:
        writer = csv.writer(benchmark_file)
        writer.writerow([target, endpoint, elapsed_time])

def log_output(endpoint, data, cls = None):
    with open(f'{endpoint}.json', '+w', encoding='utf-8') as log_file:
        json.dump(data, log_file, indent=4, cls=cls)


def get_logger():
    return logging.getLogger("benchmark")

if __name__ == '__main__':
    benchmark()