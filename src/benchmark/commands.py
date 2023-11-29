from click import argument, option, Path, group, version_option, pass_context, pass_obj
from tsp.tsp_client import TspClient
from tsp.tsp_client_response import TspClientResponseEncoder
from tsp.indexing_status import IndexingStatus 
from tsp.response import ResponseStatus
from time import time, sleep
from datetime import datetime
from pprint import pprint
import json
import csv


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
tsp_client_cached = None



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


@benchmark.command(name="open-trace")
@argument('TRACE_PATH')
@option('--trace-name', type=str, default=None, help='If max deth is 0, it will be the name of the trace at the path. Otherwise it will be a prefix')
@option('--max-depth', type=int, default=0)
@option('--regex-filter', type=str, default=None)
@option('--body', type=Path(exists=True), help='JSON file that contain the body params for the request')
@option('--debug', '-d', is_flag=True, default=False)
@option('--verbose', '-v', is_flag=True, default=False)
@pass_obj
def open_trace(tsp_client: TspClient, trace_path: str, trace_name: str, max_depth: int, regex_filter: str, body: str, debug: bool, verbose: bool):
    start = datetime.now()
    response = tsp_client.open_traces(trace_path, trace_name, max_depth, regex_filter)
    end = datetime.now()
    elapsed = end - start

    if debug:
        print("Response:")
        pprint(json.dumps(response.__dict__, default=vars))

    if verbose:
        print("Number of trace: ", len(response.model))
        for trace in response.model:
            print(trace.UUID)

    print(f"Open Trace: {elapsed.total_seconds()}s")
    log_benchmark(tsp_client.base_url, "Open Trace", elapsed.total_seconds(), response.size)



@benchmark.command(name="get-traces")
@option('--uuid', type=str, help='UUID of opened trace')
@pass_obj
def get_trace(tsp_client: TspClient, uuid: str):
    start = datetime.now()
    if uuid == None:
        tsp_client.fetch_traces()
        end = datetime.now()
    else:
        tsp_client.fetch_trace(uuid)
    end = datetime.now()
    elapsed = end - start
    print(f"Get Traces: {elapsed.total_seconds()}s")
    log_benchmark(tsp_client.base_url, "Get Traces", elapsed.total_seconds())

@benchmark.command(name="delete-trace")
@option('--uuid', type=str)
@pass_obj
def delete_trace(tsp_client: TspClient, uuid: str):
    start = datetime.now()
    tsp_client.delete_trace(uuid)
    end = datetime.now()
    elapsed = end - start
    print(f"Delete Trace: {elapsed.total_seconds()}s")
    log_benchmark(tsp_client.base_url, "Delete Trace", elapsed.total_seconds())


@benchmark.command(name="create-experiment")
@argument('EXPERIMENT_NAME', type=str)
@option('--uuids', type=str, multiple=True, help='List of traces UUID')
@option('--body', type=Path(exists=True), help='JSON file that contain the body params for the request')
@option('--debug', '-d', is_flag=True, default=False)
@option('--verbose', '-v', is_flag=True, default=False)
@pass_obj
def open_experiment(tsp_client: TspClient, experiment_name: str, uuids: list, body: str, debug: bool, verbose: bool):
    start = datetime.now()
    response = tsp_client.open_experiment(experiment_name, uuids)
    while response.is_ok() and response.model.indexing_status != IndexingStatus.COMPLETED:
        sleep(0.2) # 200ms
        response = tsp_client.fetch_experiment(response.model.UUID)
    end = datetime.now()
    elapsed = end - start

    if verbose:
        print(f"{response.model.name}:{response.model.UUID}:[{response.model.start},{response.model.end}]" )

    print(f"Create Experiment: {elapsed.total_seconds()}s")
    log_benchmark(tsp_client.base_url, "Create Experiment", elapsed.total_seconds())

@benchmark.command(name="get-experiments")
@option('--uuid', type=str, help='UUID of an experiment')
@option('--verbose', '-v', is_flag=True, default=False)
@pass_obj
def get_experiment(tsp_client: TspClient, uuid: str, verbose: bool):
    start = datetime.now()
    if uuid == None:
        response = tsp_client.fetch_experiments()
        while response.is_ok() and response.model.indexing_status != IndexingStatus.COMPLETED:
            sleep(0.2) # 200ms
            response = tsp_client.fetch_experiments()
    else:
        response = tsp_client.fetch_experiment(uuid)
        while response.is_ok() and response.model.indexing_status != IndexingStatus.COMPLETED.value:
            sleep(0.2) # 200ms
            response = tsp_client.fetch_experiments(response.model.UUID)
    end = datetime.now()
    elapsed = end - start
    
    if verbose:
        print("Experiments: ", len(response.model))
        for experiment in response.model:
            print(f"{experiment.name}:{experiment.UUID}:[{experiment.start},{experiment.end}]")

    print(f"Get Experiments: {elapsed.total_seconds()}s")
    log_benchmark(tsp_client.base_url, "Get Experiments", elapsed.total_seconds())

@benchmark.command(name="get-outputs")
@argument('UUID', type=str)
@option('--output-id', type=str, default=None)
@option('--verbose', '-v', is_flag=True, default=False)
@pass_obj
def get_outputs_descriptors(tsp_client: TspClient, uuid: str, output_id: str, verbose: bool):
    start = datetime.now()
    response = None
    if output_id == None:
        response = tsp_client.fetch_experiment_outputs(uuid)
    else:
        response = tsp_client.fetch_experiment_output(uuid, output_id)
    end = datetime.now()
    elapsed = end - start

    if verbose:
        log_output("Get Outputs Descriptors", response)
        # print("Descriptors: ", len(response.model.descriptors))
        # pprint(json.dumps(response.__dict__,  default=vars))
        
    print(f"Get Outputs Descriptors: {elapsed.total_seconds()}s")
    log_benchmark(tsp_client.base_url, "Get Outputs Descriptors", elapsed.total_seconds())


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
        sleep(0.2) # 200ms
        response = tsp_client.fetch_timegraph_tree(uuid, output_id)    
    
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
@option('--nb-times', type=int)
@option('--body', type=Path(exists=True), help='JSON file that contain the body params for the request')
@option('--verbose', '-v', is_flag=True, default=False)
@pass_obj
def get_timegraph_states(tsp_client: TspClient, uuid: str, output_id: str, start: int, end: int, nb_times: int,  body: str, verbose: bool):
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
    response = tsp_client.fetch_timegraph_states(uuid, output_id, parameters)
    while response.is_ok() and response.model.status != ResponseStatus.COMPLETED:
        sleep(0.2) # 200ms
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
        sleep(0.2) # 200ms
        response = tsp_client.fetch_timegraph_arrows(uuid, output_id, parameters)
    
    end = datetime.now()
    elapsed = end - start
    if verbose:
        log_output("Get Timegraph Arrows", response)

    print(f"Get TimeGraph Arrows: {elapsed.total_seconds()}s")
    log_benchmark(tsp_client.base_url, "Get TimeGraph Arrows", elapsed.total_seconds(), response.size)


@benchmark.command(name="get-xy-tree")
@argument('UUID', type=str)
@argument('OUTPUT_ID', type=str)
@option('--body', type=Path(exists=True), help='JSON file that contain the body params for the request')
@pass_obj
def get_xy_tree(tsp_client: TspClient, body: str):
    pass

@benchmark.command(name="get-xy")
@argument('UUID', type=str)
@argument('OUTPUT_ID', type=str)
@option('--body', type=Path(exists=True), help='JSON file that contain the body params for the request')
@pass_obj
def get_xy(tsp_client: TspClient, body: str):
    pass


def log_benchmark(target, endpoint, elapsed_time, response_size = None):
    with open('benchmark-tsp.csv', '+a', encoding='utf-8') as benchmark_file:
        writer = csv.writer(benchmark_file)
        writer.writerow([target, endpoint, elapsed_time, response_size])

def log_output(endpoint, data):
    with open(f'{endpoint}.json', '+w', encoding='utf-8') as log_file:
        json.dump(data, log_file, indent=4, cls= TspClientResponseEncoder)
        
