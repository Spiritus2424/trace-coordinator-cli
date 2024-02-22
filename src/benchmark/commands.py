from click import argument, option, Path, group, version_option, pass_context, pass_obj
from tsp.tsp_client import TspClient
from tsp.tsp_client_response import TspClientResponseEncoder
from tsp.response import ResponseStatus
from time import sleep
from datetime import datetime
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

@benchmark.command(name="get-xy-tree")
@argument('UUID', type=str)
@argument('OUTPUT_ID', type=str)
@option('--body', type=Path(exists=True), help='JSON file that contain the body params for the request')
@option('--verbose', '-v', is_flag=True, default=False)
@pass_obj
def get_xy_tree(tsp_client: TspClient, uuid: str, output_id: str, body: str, verbose: bool):
    start = datetime.now()
    response = tsp_client.fetch_xy_tree(uuid, output_id, None)

    while response.is_ok() and response.model.status != ResponseStatus.COMPLETED:
        sleep(POLLING_TIME)
        response = tsp_client.fetch_xy_tree(uuid, output_id, None)    
    
    end = datetime.now()
    elapsed = end - start

    if verbose:
        log_output("Get XY Tree", response)

    print(f"Get XY Tree: {elapsed.total_seconds()}s")
    log_benchmark(tsp_client.base_url, "Get XY Tree", elapsed.total_seconds(), response.size)


@benchmark.command(name="get-xy")
@argument('UUID', type=str)
@argument('OUTPUT_ID', type=str)
@argument('START', type=int)
@argument('END', type=int)
@option('--items', "-i" , multiple=True, default=[])
@option('--nb-times', type=int)
@option('--body', type=Path(exists=True), help='JSON file that contain the body params for the request')
@option('--verbose', '-v', is_flag=True, default=False)
@pass_obj
def get_xy(tsp_client: TspClient, uuid: str, output_id: str, start: int, end: int, items: list, nb_times: int,  body: str, verbose: bool):
    parameters = {
        "parameters": {
            "requested_timerange": {
                "start": start,
                "end": end,
                "nbTimes": nb_times
            },
            "requested_items": items
        }
    }
    start = datetime.now()
    response = tsp_client.fetch_xy(uuid, output_id, parameters)
    while response.is_ok() and response.model.status != ResponseStatus.COMPLETED:
        sleep(POLLING_TIME) 
        response = tsp_client.fetch_xy(uuid, output_id, parameters)    
    
    end = datetime.now()
    elapsed = end - start

    if verbose:
        log_output("Get XY", response)

    print(f"Get XY: {elapsed.total_seconds()}s")
    log_benchmark(tsp_client.base_url, "Get XY", elapsed.total_seconds(), response.size)


@benchmark.command(name="get-xy")
@argument('UUID', type=str)
@argument('OUTPUT_ID', type=str)
@argument('START', type=int)
@argument('END', type=int)
@option('--nb-times', type=int)
@option('--verbose', '-v', is_flag=True, default=False)
@pass_obj
def get_xy(tsp_client: TspClient, uuid: str, output_id: str, start: int, end: int, items: list, nb_times: int,  body: str, verbose: bool):
    parameters = {
        "parameters": {
            "requested_timerange": {
                "start": start,
                "end": end,
                "nbTimes": nb_times
            },
            "requested_items": items
        }
    }
    start = datetime.now()
    response = tsp_client.fetch_xy(uuid, output_id, parameters)
    while response.is_ok() and response.model.status != ResponseStatus.COMPLETED:
        sleep(POLLING_TIME) 
        response = tsp_client.fetch_xy(uuid, output_id, parameters)    
    
    end = datetime.now()
    elapsed = end - start

    if verbose:
        log_output("Get XY", response)

    print(f"Get XY: {elapsed.total_seconds()}s")
    log_benchmark(tsp_client.base_url, "Get XY", elapsed.total_seconds(), response.size)


def log_benchmark(target, endpoint, elapsed_time, response_size = None):
    with open('benchmark-tsp.csv', '+a', encoding='utf-8') as benchmark_file:
        writer = csv.writer(benchmark_file)
        writer.writerow([target, endpoint, elapsed_time, response_size])

def log_output(endpoint, data):
    with open(f'{endpoint}.json', '+w', encoding='utf-8') as log_file:
        json.dump(data, log_file, indent=4, cls= TspClientResponseEncoder)
        
