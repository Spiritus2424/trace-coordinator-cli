from click import argument, option, Path, group, version_option, pass_context, pass_obj
from tsp.tsp_client import TspClient
from tsp.response import ResponseStatus 
from time import time, sleep
from datetime import datetime

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
tsp_client_cached = None


@group(context_settings=CONTEXT_SETTINGS)
@version_option(version='1.0.0')
@option('--ip', type=str, default='localhost', help='IP address of trace server', envvar="TSP_CLI_BENCHMARK_IP")
@option('--port', '-p', type=int, default=8080, help='Port of trace server', envvar="TSP_CLI_BENCHMARK_PORT")
@option('--debug', '-d', type=bool, default=False)
@pass_context
def benchmark(ctx, ip: str, port: int, debug: bool):
    """Benchmark commands."""
    ctx.obj = TspClient(f'http://{ip}:{port}/tsp/api/')
    if debug:
        print(ctx.obj.base_url)


@benchmark.command(name="open-trace")
@argument('TRACE_PATH', type=Path(exists=True))
@option('--trace-name', type=str, help='If max deth is 0, it will be the name of the trace at the path. Otherwise it will be a prefix')
@option('--max-depth', type=int, default=0)
@option('--regex-filter', type=str, default=None)
@option('--body', type=Path(exists=True), help='JSON file that contain the body params for the request')
@pass_obj
def open_trace(tsp_client: TspClient, trace_path: str, trace_name: str, max_depth: int, regex_filter: str, body_file: str):
    start = datetime.now()
    tsp_client.open_trace(trace_name, trace_path, max_depth, regex_filter)
    end = datetime.now()
    elapsed = end - start
    print(f"Open Trace: {elapsed.total_seconds()}s")


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

@benchmark.command(name="delete-trace")
@option('--uuid', type=str)
@pass_obj
def delete_trace(tsp_client: TspClient, uuid: str):
    start = datetime.now()
    tsp_client.delete_trace(uuid)
    end = datetime.now()
    elapsed = end - start
    print(f"Delete Trace: {elapsed.total_seconds()}s")


@benchmark.command(name="create-experiment")
@argument('EXPERIENCE_NAME', type=str)
@option('--uuids', type=list, help='List of traces UUID')
@option('--body', type=Path(exists=True), help='JSON file that contain the body params for the request')
@pass_obj
def open_experiment(tsp_client: TspClient, experiment_name: str, uuids: list, body_file: str):
    start = datetime.now()
    response = tsp_client.open_experiment(experiment_name, uuids)
    while response.is_ok() and response.model.indexin_status != ResponseStatus.COMPLETED:
        sleep(0.2) # 200ms
        response = tsp_client.fetch_experiment(response.model.UUID)
    end = datetime.now()
    elapsed = end - start
    print(f"Create Experiment: {elapsed.total_seconds()}s")

@benchmark.command(name="get-experiments")
@option('--uuid', type=str, help='UUID of an experiment')
@pass_obj
def get_experiment(tsp_client: TspClient, uuid: str):
    start = datetime.now()
    if uuid == None:
        response = tsp_client.fetch_experiments()
        while response.is_ok() and response.model.indexin_status != ResponseStatus.COMPLETED:
            sleep(0.2) # 200ms
            response = tsp_client.fetch_experiments()
    else:
        response = tsp_client.fetch_experiment(uuid)
        while response.is_ok() and response.model.indexin_status != ResponseStatus.COMPLETED:
            sleep(0.2) # 200ms
            response = tsp_client.fetch_experiments(response.model.UUID)
    end = datetime.now()
    elapsed = end - start
    print(f"Get Experiments: {elapsed.total_seconds()}s")

@benchmark.command(name="get-timegraph-tree")
@option('--uuid', type=str, help='UUID of an experiment')
@option('--output-id')
@option('--body', type=Path(exists=True), help='JSON file that contain the body params for the request')
@pass_obj
def get_timegraph_tree(tsp_client: TspClient, uuid: str, body_file: str):
    tsp_client.fetch_timegraph_tree(uuid, )
    pass

@benchmark.command(name="get-timegraph-state")
@option('--body', type=Path(exists=True), help='JSON file that contain the body params for the request')
@pass_obj
def get_timegraph_state(tsp_client: TspClient, body_file: str):
    pass

@benchmark.command(name="get-timegraph-arrow")
@option('--body', type=Path(exists=True), help='JSON file that contain the body params for the request')
@pass_obj
def get_timegraph_arrow(tsp_client: TspClient, body_file: str):
    pass

@benchmark.command(name="get-xy-tree")
@option('--body', type=Path(exists=True), help='JSON file that contain the body params for the request')
@pass_obj
def get_xy_tree(tsp_client: TspClient, body_file: str):
    pass

@benchmark.command(name="get-xy")
@option('--body', type=Path(exists=True), help='JSON file that contain the body params for the request')
@pass_obj
def get_xy(tsp_client: TspClient, body_file: str):
    pass
