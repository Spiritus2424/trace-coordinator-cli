from click import argument, option, Path, pass_obj
from time import sleep
from datetime import datetime
from tsp.tsp_client import TspClient, GenericResponse, ModelType
from tsp.response import ResponseStatus, GenericResponseEncoder
from benchmark.commands import benchmark, log_output, log_benchmark, POLLING_TIME
from animation.waiting import start_waiting_animation, stop_waiting_animation
import json

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
    log_benchmark(tsp_client.base_url, "Get XY Tree", elapsed.total_seconds())

    if verbose:
        log_output("Get XY Tree", response.model, GenericResponseEncoder)



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
    log_benchmark(tsp_client.base_url, "Get XY", elapsed.total_seconds())

    if verbose:
        log_output("Get XY", response.model, GenericResponseEncoder)


######################################## CONCRETE CASE ################################

@benchmark.command(name="concrete-get-xy")
@argument('UUID', type=str)
@argument('OUTPUT_ID', type=str)
@argument('START', type=int)
@argument('END', type=int)
@option('--tree', type=Path(exists=True), help='JSON file that contain the tree that the Get XY tree returned')
@option('--process', default="")
@option('--nb-items', "-i", type=int, default=60)
@option('--nb-times', type=int)
@option('--verbose', '-v', is_flag=True, default=False)
@pass_obj
def get_xy_concrete_benchmark(tsp_client: TspClient, uuid: str, output_id: str, start: int, end: int, tree: str, process: str, nb_items: int, nb_times: int, verbose: bool):
    xy_tree = None
    with open(tree, 'r') as file:
        xy_tree = GenericResponse(json.load(file), ModelType.XY_TREE)
        

    parameters = {
        "parameters": {
            "requested_timerange": {
                "start": start,
                "end": end,
                "nbTimes": nb_times
            },
            "requested_items": sample_xy_tree(xy_tree.model.entries, nb_items, process)
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
    log_benchmark(tsp_client.base_url, "Get XY", elapsed.total_seconds())

    if verbose:
        log_output("Get XY", response.model, GenericResponseEncoder)


######################################## FUNCTION ################################

def get_xy_tree(tsp_client: TspClient, uuid: str, output_id: str):
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


def sample_xy_tree(entries: list, nb_items: int, process: str):
    id_items = []
    for entry in entries:
        if entry.labels[0] == process:
            id_items.append(entry.id)
        if nb_items != 0 and len(id_items) > nb_items:
            break

    return id_items