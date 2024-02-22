from click import argument, option, Path, pass_obj
from tsp.tsp_client import TspClient
from tsp.response import ResponseStatus
from time import sleep
from datetime import datetime
from commands import benchmark, POLLING_TIME, log_benchmark, log_output


@benchmark.command(name="get-timegraph-tree")
@argument('UUID', type=str)
@argument('OUTPUT_ID', type=str)
@option('--body', type=Path(exists=True), help='JSON file that contain the body params for the request')
@option('--verbose', '-v', is_flag=True, default=False)
@pass_obj
def get_timegraph_tree(tsp_client: TspClient, uuid: str, output_id: str, body: str, verbose: bool):
    start = datetime.now()
    response = tsp_client.fetch_timegraph_tree(uuid, output_id, None)

    while response.is_ok() and response.model.status != ResponseStatus.COMPLETED:
        sleep(POLLING_TIME) 
        response = tsp_client.fetch_timegraph_tree(uuid, output_id, None)    
    
    end = datetime.now()
    elapsed = end - start

    if verbose:
        log_output("Get Timegraph Tree", response)

    print(f"Get TimeGraph Tree: {elapsed.total_seconds()}s")
    log_benchmark(tsp_client.base_url, "Get TimeGraph Tree", elapsed.total_seconds(), response.size)

@benchmark.command(name="get-timegraph-states")
@argument('UUID', type=str)
@argument('OUTPUT_ID', type=str)
@argument('START', type=int)
@argument('END', type=int)
@option('--items', "-i" , multiple=True, default=[])
@option('--nb-times', type=int)
@option('--body', type=Path(exists=True), help='JSON file that contain the body params for the request')
@option('--verbose', '-v', is_flag=True, default=False)
@pass_obj
def get_timegraph_states(tsp_client: TspClient, uuid: str, output_id: str, start: int, end: int, items: list, nb_times: int,  body: str, verbose: bool):
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
    response = tsp_client.fetch_timegraph_states(uuid, output_id, parameters)
    while response.is_ok() and response.model.status != ResponseStatus.COMPLETED:
        sleep(POLLING_TIME) 
        response = tsp_client.fetch_timegraph_states(uuid, output_id, parameters)
    
    end = datetime.now()
    elapsed = end - start
    if verbose:
        log_output("Get Timegraph States", response)

    print(f"Get TimeGraph States: {elapsed.total_seconds()}s")
    log_benchmark(tsp_client.base_url, "Get TimeGraph States", elapsed.total_seconds(), response.size)
    
@benchmark.command(name="get-timegraph-arrows")
@argument('UUID', type=str)
@argument('OUTPUT_ID', type=str)
@argument('START', type=int)
@argument('END', type=int)
@option('--nb-times', type=int)
@option('--body', type=Path(exists=True), help='JSON file that contain the body params for the request')
@option('--verbose', '-v', is_flag=True, default=False)
@pass_obj
def get_timegraph_arrows(tsp_client: TspClient, uuid: str, output_id: str, start: int, end: int, nb_times: int, body: str, verbose: bool):
    parameters = {
        "parameters": {
            "requested_timerange": {
                "start": start,
                "end": end,
                "nbTimes": nb_times
            }
        }
    }
    start = datetime.now()
    response = tsp_client.fetch_timegraph_arrows(uuid, output_id, parameters)
    while response.is_ok() and response.model.status != ResponseStatus.COMPLETED:
        sleep(POLLING_TIME) 
        response = tsp_client.fetch_timegraph_arrows(uuid, output_id, parameters)
    
    end = datetime.now()
    elapsed = end - start
    if verbose:
        log_output("Get Timegraph Arrows", response)

    print(f"Get TimeGraph Arrows: {elapsed.total_seconds()}s")
    log_benchmark(tsp_client.base_url, "Get TimeGraph Arrows", elapsed.total_seconds(), response.size)




######################################## REAL CASE ################################

@benchmark.command(name="get-timegraph-states")
@argument('UUID', type=str)
@argument('OUTPUT_ID', type=str)
@argument('START', type=int)
@argument('END', type=int)
@option('--items', "-i" , multiple=True, default=[])
@option('--nb-times', type=int)
@option('--body', type=Path(exists=True), help='JSON file that contain the body params for the request')
@option('--verbose', '-v', is_flag=True, default=False)
@pass_obj
def get_timegraph_states(tsp_client: TspClient, uuid: str, output_id: str, start: int, end: int, items: list, nb_times: int,  body: str, verbose: bool):
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
    response = tsp_client.fetch_timegraph_states(uuid, output_id, parameters)
    while response.is_ok() and response.model.status != ResponseStatus.COMPLETED:
        sleep(POLLING_TIME) 
        response = tsp_client.fetch_timegraph_states(uuid, output_id, parameters)
    
    end = datetime.now()
    elapsed = end - start
    if verbose:
        log_output("Get Timegraph States", response)

    print(f"Get TimeGraph States: {elapsed.total_seconds()}s")
    log_benchmark(tsp_client.base_url, "Get TimeGraph States", elapsed.total_seconds(), response.size)
    

@benchmark.command(name="get-timegraph-arrows")
@argument('UUID', type=str)
@argument('OUTPUT_ID', type=str)
@argument('START', type=int)
@argument('END', type=int)
@option('--nb-times', type=int)
@option('--body', type=Path(exists=True), help='JSON file that contain the body params for the request')
@option('--verbose', '-v', is_flag=True, default=False)
@pass_obj
def get_timegraph_arrows(tsp_client: TspClient, uuid: str, output_id: str, start: int, end: int, nb_times: int, body: str, verbose: bool):
    parameters = {
        "parameters": {
            "requested_timerange": {
                "start": start,
                "end": end,
                "nbTimes": nb_times
            }
        }
    }
    start = datetime.now()
    response = tsp_client.fetch_timegraph_arrows(uuid, output_id, parameters)
    while response.is_ok() and response.model.status != ResponseStatus.COMPLETED:
        sleep(POLLING_TIME) 
        response = tsp_client.fetch_timegraph_arrows(uuid, output_id, parameters)
    
    end = datetime.now()
    elapsed = end - start
    if verbose:
        log_output("Get Timegraph Arrows", response)

    print(f"Get TimeGraph Arrows: {elapsed.total_seconds()}s")
    log_benchmark(tsp_client.base_url, "Get TimeGraph Arrows", elapsed.total_seconds(), response.size)