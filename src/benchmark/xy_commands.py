from click import argument, option, Path, pass_obj
from tsp.tsp_client import TspClient
from tsp.response import ResponseStatus
from time import sleep
from datetime import datetime
from commands import benchmark, log_output, log_benchmark, POLLING_TIME


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