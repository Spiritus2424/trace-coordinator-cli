from click import command, argument, option, Path, prompt
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from generate_config.trace_server import TraceServer
from ruamel.yaml import YAML

@command(name="generate")
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
        yaml.dump(config, output_file)

    print(f"'{output_file_name}' generated successfully.")
