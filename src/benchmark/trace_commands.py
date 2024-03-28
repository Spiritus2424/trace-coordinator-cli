from click import argument, option, Path, pass_obj
from datetime import datetime
from tsp.tsp_client import TspClient
from benchmark.commands import benchmark, log_benchmark, log_output
from animation.waiting import start_waiting_animation, stop_waiting_animation
from tsp.trace_set import TraceSetEncoder

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
    print(f"Open Trace: ", end="")
    animation_event = start_waiting_animation()
    start = datetime.now()
    response = tsp_client.open_traces(trace_path, trace_name, max_depth, regex_filter)
    end = datetime.now()
    elapsed = end - start
    stop_waiting_animation(animation_event)
    print(f"{elapsed.total_seconds()}s")
    log_benchmark(tsp_client.base_url, "Open Trace", elapsed.total_seconds())

    if verbose:
        print(f"Number of trace: {len(response.model.traces)}")
        for trace in response.model.traces:
            print(trace.UUID)
        log_output("Open Trace", response.model, TraceSetEncoder)




@benchmark.command(name="get-traces")
@option('--uuid', type=str, help='UUID of opened trace')
@pass_obj
def get_trace(tsp_client: TspClient, uuid: str):
    print(f"Get Traces: ", end="")
    animation_event = start_waiting_animation()
    start = datetime.now()
    if uuid == None:
        tsp_client.fetch_traces()
        end = datetime.now()
    else:
        tsp_client.fetch_trace(uuid)
    end = datetime.now()
    elapsed = end - start
    stop_waiting_animation(animation_event)
    print(f"{elapsed.total_seconds()}s")
    log_benchmark(tsp_client.base_url, "Get Traces", elapsed.total_seconds())

@benchmark.command(name="delete-trace")
@option('--uuid', type=str)
@pass_obj
def delete_trace(tsp_client: TspClient, uuid: str):
    print(f"Delete Trace: ", end="")
    animation_event = start_waiting_animation()
    start = datetime.now()
    tsp_client.delete_trace(uuid)
    end = datetime.now()
    elapsed = end - start
    stop_waiting_animation(animation_event)
    print(f"{elapsed.total_seconds()}s")
    log_benchmark(tsp_client.base_url, "Delete Trace", elapsed.total_seconds())
