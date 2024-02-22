from click import argument, option, Path, pass_obj
from time import sleep
from datetime import datetime
from tsp.tsp_client import TspClient
from tsp.response import ResponseStatus
from benchmark.commands import benchmark, log_output, log_benchmark, POLLING_TIME
from animation.waiting import start_waiting_animation, stop_waiting_animation


@benchmark.command(name="get-xy-tree")
@argument('UUID', type=str)
@argument('OUTPUT_ID', type=str)
@option('--body', type=Path(exists=True), help='JSON file that contain the body params for the request')
@option('--verbose', '-v', is_flag=True, default=False)
@pass_obj
def get_xy_tree_benchmark(tsp_client: TspClient, uuid: str, output_id: str, body: str, verbose: bool):
    print(f"Get XY Tree: ", end="")
    animation_event = start_waiting_animation()
    start = datetime.now()
    response = get_xy_tree(tsp_client, uuid, output_id)
    end = datetime.now()
    elapsed = end - start
    stop_waiting_animation(animation_event)
    print(f"{elapsed.total_seconds()}s")
    log_benchmark(tsp_client.base_url, "Get XY Tree", elapsed.total_seconds(), response.size)

    if verbose:
        log_output("Get XY Tree", response)



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
def get_xy_benchmark(tsp_client: TspClient, uuid: str, output_id: str, start: int, end: int, items: list, nb_times: int,  body: str, verbose: bool):
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

    print(f"Get XY: ", end="")
    animation_event = start_waiting_animation()
    start = datetime.now()
    response = get_xy(tsp_client, uuid, output_id, parameters)
    end = datetime.now()
    elapsed = end - start
    stop_waiting_animation(animation_event)
    print(f"{elapsed.total_seconds()}s")
    log_benchmark(tsp_client.base_url, "Get XY", elapsed.total_seconds(), response.size)

    if verbose:
        log_output("Get XY", response)


######################################## CONCRETE CASE ################################

@benchmark.command(name="concrete-get-xy")
@argument('UUID', type=str)
@argument('OUTPUT_ID', type=str)
@argument('START', type=int)
@argument('END', type=int)
@option('--nb-items', "-i", default=60)
@option('--nb-times', type=int)
@option('--body', type=Path(exists=True), help='JSON file that contain the body params for the request')
@option('--verbose', '-v', is_flag=True, default=False)
@pass_obj
def get_xy_concrete_benchmark(tsp_client: TspClient, uuid: str, output_id: str, start: int, end: int, items: list, nb_times: int,  body: str, verbose: bool):
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

    print(f"Get XY: ", end="")
    animation_event = start_waiting_animation()
    start = datetime.now()
    response = get_xy(tsp_client, uuid, output_id, parameters)
    end = datetime.now()
    elapsed = end - start
    stop_waiting_animation(animation_event)
    print(f"{elapsed.total_seconds()}s")
    log_benchmark(tsp_client.base_url, "Real Case - Get XY", elapsed.total_seconds(), response.size)

    if verbose:
        log_output("Get XY", response)


######################################## FUNCTION ################################

def get_xy_tree(tsp_client: TspClient, uuid: str, output_id: str, body: str, verbose: bool):
    response = tsp_client.fetch_xy_tree(uuid, output_id, None)
    while response.is_ok() and response.model.status != ResponseStatus.COMPLETED:
        sleep(POLLING_TIME)
        response = tsp_client.fetch_xy_tree(uuid, output_id, None)    
    
    return response

def get_xy(tsp_client: TspClient, uuid: str, output_id: str, parameters):
    response = tsp_client.fetch_xy(uuid, output_id, parameters)
    while response.is_ok() and response.model.status != ResponseStatus.COMPLETED:
        sleep(POLLING_TIME) 
        response = tsp_client.fetch_xy(uuid, output_id, parameters)    
    
    return response
