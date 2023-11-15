from click import command, argument, option, Path, group, version_option
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ruamel.yaml import YAML

from generate_config.trace_server import TraceServer
from generate_config.experiment import Experiment


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@group(context_settings=CONTEXT_SETTINGS)
@version_option(version='1.0.0')
def coordinator():
    """Create Cordinator Configuration file"""
    pass


@coordinator.command(name="generate")
@argument('hosts-files', type=Path(exists=True), nargs=-1)
@option('--trace-path', type=str, prompt=True)
@option('--filter', type=str)
@option('--output-directory', type=Path(exists=True, dir_okay=True),  help='output directory')
@option('--output-file-name', type=str, default='.trace.coordinator.yml', help='output file name')
@option('--port', '-p', type=int, default=8080)
@option('--groups', type=str,  multiple=True, default=['workers'])
def generate_config(hosts_files: list, trace_path: str, filter: str, output_directory: str, output_file_name: str, port: int, groups: list):
    manager = InventoryManager(loader=DataLoader(), sources=hosts_files)
    trace_servers: list = []
    for group in groups:
        for host in manager.get_groups_dict().get(group): 
            trace_servers.append(TraceServer(host, port, [trace_path], filter))

    config = {}
    config["trace-servers"] = trace_servers
 

    with open(output_file_name, 'w') as output_file:
        yaml=YAML(typ='safe')
        yaml.register_class(TraceServer)
        yaml.preserve_quotes = True
        yaml.default_flow_style = False
        yaml.dump(config, output_file)

    print(f"'{output_file_name}' generated successfully.")


@coordinator.command(name="add-experiment")
@argument('config-file', type=Path(exists=True))
@option('--experiment-name', type=str, prompt=True)
@option('--trace-path', type=str, prompt=True)
@option('--filter', type=str)
def add_experiment(config_file, experiment_name, trace_path, filter):

    config = {}
    config["experiments"] = [Experiment(experiment_name, [trace_path], filter)]

    with open(config_file, 'a') as file:
        yaml=YAML(typ='safe')
        yaml.register_class(TraceServer)
        yaml.register_class(Experiment)
        yaml.preserve_quotes = True
        yaml.default_flow_style = False
        yaml.allow_duplicate_keys = True
        data = list(yaml.load_all(file))
        print(data)