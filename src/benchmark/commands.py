from click import option, group, version_option, pass_context
from tsp.tsp_client import TspClient
from tsp.tsp_client_response import TspClientResponseEncoder
import json
import csv


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
POLLING_TIME = 0.5


@group(context_settings=CONTEXT_SETTINGS)
@version_option(version='1.0.0')
@option('--ip', type=str, default='localhost', help='IP address of trace server', envvar="TSP_CLI_BENCHMARK_IP")
@option('--port', '-p', type=int, default=8080, help='Port of trace server', envvar="TSP_CLI_BENCHMARK_PORT")
@option('--debug', '-d', is_flag=True, default=False)
@pass_context
def benchmark(ctx, ip: str, port: int, debug: bool):
    """Benchmark commands."""
    ctx.obj = TspClient(f'http://{ip}:{port}/tsp/api/')
    if debug:
        print(f"Target: {ctx.obj.base_url}")

def log_benchmark(target, endpoint, elapsed_time, response_size = None):
    with open('benchmark-tsp.csv', '+a', encoding='utf-8') as benchmark_file:
        writer = csv.writer(benchmark_file)
        writer.writerow([target, endpoint, elapsed_time, response_size])

def log_output(endpoint, data):
    with open(f'{endpoint}.json', '+w', encoding='utf-8') as log_file:
        json.dump(data, log_file, indent=4, cls= TspClientResponseEncoder)


if __name__ == '__main__':
    benchmark()
    # benchmark.add_command(open_trace)