from click import argument, option, Path, pass_obj
from time import sleep
from datetime import datetime
from tsp.tsp_client import TspClient
from tsp.response import ResponseStatus
from benchmark.commands import benchmark, POLLING_TIME, log_benchmark, log_output
from animation.waiting import start_waiting_animation, stop_waiting_animation

@benchmark.command(name="get-timegraph-tree")
@argument('UUID', type=str)
@argument('OUTPUT_ID', type=str)
@option('--body', type=Path(exists=True), help='JSON file that contain the body params for the request')
@option('--verbose', '-v', is_flag=True, default=False)
@pass_obj
def get_timegraph_tree_command(tsp_client: TspClient, uuid: str, output_id: str, body: str, verbose: bool): 
    print(f"Get TimeGraph Tree: ", end="")
    animation_event = start_waiting_animation()
    start = datetime.now()
    response = get_timegraph_tree(tsp_client, uuid, output_id)
    end = datetime.now()
    elapsed = end - start
    stop_waiting_animation(animation_event)
    print(f"{elapsed.total_seconds()}")
    log_benchmark(tsp_client.base_url, "Get TimeGraph Tree", elapsed.total_seconds(), response.size)

    if verbose:
        log_output("Get Timegraph Tree", response)



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
def get_timegraph_states_command(tsp_client: TspClient, uuid: str, output_id: str, start: int, end: int, items: list, nb_times: int,  body: str, verbose: bool):
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
    print(f"Get TimeGraph States: ", end="")
    animation_event = start_waiting_animation()
    start = datetime.now()
    response = get_timegraph_states(tsp_client, uuid, output_id, parameters)
    end = datetime.now()
    elapsed = end - start
    stop_waiting_animation(animation_event)
    print(f"{elapsed.total_seconds()}s")
    log_benchmark(tsp_client.base_url, "Get TimeGraph States", elapsed.total_seconds(), response.size)
    
    if verbose:
        log_output("Get Timegraph States", response)


 
@benchmark.command(name="get-timegraph-arrows")
@argument('UUID', type=str)
@argument('OUTPUT_ID', type=str)
@argument('START', type=int)
@argument('END', type=int)
@option('--nb-times', type=int)
@option('--body', type=Path(exists=True), help='JSON file that contain the body params for the request')
@option('--verbose', '-v', is_flag=True, default=False)
@pass_obj
def get_timegraph_arrows_command(tsp_client: TspClient, uuid: str, output_id: str, start: int, end: int, nb_times: int, body: str, verbose: bool):
    parameters = {
        "parameters": {
            "requested_timerange": {
                "start": start,
                "end": end,
                "nbTimes": nb_times
            }
        }
    }

    print(f"Get TimeGraph Arrows: ", end="")
    animation_event = start_waiting_animation()
    start = datetime.now()
    response = get_timegraph_arrows(tsp_client, uuid, output_id, parameters)
    end = datetime.now()
    elapsed = end - start
    stop_waiting_animation(animation_event)
    print(f"{elapsed.total_seconds()}s")
    log_benchmark(tsp_client.base_url, "Get TimeGraph Arrows", elapsed.total_seconds(), response.size)

    if verbose:
        log_output("Get Timegraph Arrows", response)



######################################## CONCRETE CASE ################################

@benchmark.command(name="concrete-get-timegraph-states")
@argument('UUID', type=str)
@argument('OUTPUT_ID', type=str)
@argument('START', type=int)
@argument('END', type=int)
@option('--nb-items', "-i", default=60)
@option('--nb-times', type=int)
@option('--verbose', '-v', is_flag=True, default=False)
@pass_obj
def get_timegraph_states_concrete_command(tsp_client: TspClient, uuid: str, output_id: str, start: int, end: int, items: list, nb_times: int,  body: str, verbose: bool):
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
    # Get Tree
    response = get_timegraph_tree(tsp_client, uuid, output_id)

    

    print(f"Get TimeGraph States: ", end="")
    animation_event = start_waiting_animation()
    start = datetime.now()
    response = get_timegraph_states(tsp_client, uuid, output_id, parameters)
    end = datetime.now()
    elapsed = end - start
    stop_waiting_animation(animation_event)
    print(f"{elapsed.total_seconds()}s")
    log_benchmark(tsp_client.base_url, "Real Case - Get TimeGraph States", elapsed.total_seconds(), response.size)
    
    if verbose:
        log_output("Get Timegraph States", response)


@benchmark.command(name="concrete-get-timegraph-arrows")
@argument('UUID', type=str)
@argument('OUTPUT_ID', type=str)
@argument('START', type=int)
@argument('END', type=int)
@option('--nb-times', type=int)
@option('--body', type=Path(exists=True), help='JSON file that contain the body params for the request')
@option('--verbose', '-v', is_flag=True, default=False)
@pass_obj
def get_timegraph_arrows_concrete_command(tsp_client: TspClient, uuid: str, output_id: str, start: int, end: int, nb_times: int, body: str, verbose: bool):
    parameters = {
        "parameters": {
            "requested_timerange": {
                "start": start,
                "end": end,
                "nbTimes": nb_times
            }
        }
    }

    print(f"Get TimeGraph Arrows: ", end="")
    animation_event = start_waiting_animation()
    start = datetime.now()
    response = get_timegraph_arrows(tsp_client, uuid, output_id, parameters)
    end = datetime.now()
    elapsed = end - start
    stop_waiting_animation(animation_event)
    print(f"{elapsed.total_seconds()}s")
    log_benchmark(tsp_client.base_url, "Real Case - Get TimeGraph Arrows", elapsed.total_seconds(), response.size)

    if verbose:
        log_output("Get Timegraph Arrows", response)




######################################## FUNCTION ################################

def get_timegraph_tree(tsp_client: TspClient, uuid: str, output_id: str):
    response = tsp_client.fetch_timegraph_tree(uuid, output_id, None)
    while response.is_ok() and response.model.status != ResponseStatus.COMPLETED:
        sleep(POLLING_TIME)
        response = tsp_client.fetch_timegraph_tree(uuid, output_id, None)
    
    return response


def get_timegraph_states(tsp_client: TspClient, uuid: str, output_id: str, parameters):
    response = tsp_client.fetch_timegraph_states(uuid, output_id, parameters)
    while response.is_ok() and response.model.status != ResponseStatus.COMPLETED:
        sleep(POLLING_TIME)
        response = tsp_client.fetch_timegraph_states(uuid, output_id, parameters)

    return response


def get_timegraph_arrows(tsp_client: TspClient, uuid: str, output_id: str, parameters):
    response = tsp_client.fetch_timegraph_arrows(uuid, output_id, parameters)
    while response.is_ok() and response.model.status != ResponseStatus.COMPLETED:
        sleep(POLLING_TIME)
        response = tsp_client.fetch_timegraph_arrows(uuid, output_id, parameters)

    return response