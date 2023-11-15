from click import command, argument, option, Path, group, version_option
from tsp.tsp_client import TspClient

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@group(context_settings=CONTEXT_SETTINGS)
@version_option(version='1.0.0')
@option('--ip', type=str, default='localhost', help='IP address of trace server')
@option('--port', '-p', type=int, default=8080, help='Port of trace server')
def benchmark_cli():
    pass


@benchmark_cli.command(name="open-trace")
@argument('TRACE_PATH', type=Path(exists=True), prompt=True)
@option('--trace-name', type=str, help='If max deth is 0, it will be the name of the trace at the path. Otherwise it will be a prefix')
@option('--max-depth', type=int, default=0)
@option('--body', type=Path(exists=True), help='JSON file that contain the body params for the request')
def open_trace():
    pass


@benchmark_cli.command(name="get-traces")
@option('--uuid', type=str, help='UUID of opened trace')
def get_trace():
    pass

@benchmark_cli.command(name="delete-trace")
@option('--uuid', type=str)
def delete_trace():
    pass


@benchmark_cli.command(name="open-experiment")
@argument('EXPERIENCE_NAME', type=str, prompt=True)
@option('--uuids', type=list, help='List of trace uuids')
@option('--body', type=Path(exists=True), help='JSON file that contain the body params for the request')
def open_experiment():
    pass

@benchmark_cli.command(name="get-experiments")
@option('--uuid', type=str, help='UUID of created experiment')
def get_experiment():
    pass

@benchmark_cli.command(name="get-timegraph-tree")
@option('--body', type=Path(exists=True), help='JSON file that contain the body params for the request')
def get_timegraph_tree():
    pass

@benchmark_cli.command(name="get-timegraph-state")
@option('--body', type=Path(exists=True), help='JSON file that contain the body params for the request')
def get_timegraph_state():
    pass

@benchmark_cli.command(name="get-timegraph-arrow")
@option('--body', type=Path(exists=True), help='JSON file that contain the body params for the request')
def get_timegraph_arrow():
    pass

@benchmark_cli.command(name="get-xy-tree")
@option('--body', type=Path(exists=True), help='JSON file that contain the body params for the request')
def get_xy_tree():
    pass

@benchmark_cli.command(name="get-xy")
@option('--body', type=Path(exists=True), help='JSON file that contain the body params for the request')
def get_xy():
    pass


def init_tsp_client(ip_address, port):
    API_URL_BASE = 'http://{0}:{1}/tsp/api/'.format(ip_address, port)
    tsp_client = TspClient(API_URL_BASE) 