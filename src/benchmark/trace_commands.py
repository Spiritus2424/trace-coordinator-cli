from click import argument, option, Path, pass_obj
from tsp.tsp_client import TspClient
from datetime import datetime
from pprint import pprint
from commands import benchmark, log_benchmark
import json

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

