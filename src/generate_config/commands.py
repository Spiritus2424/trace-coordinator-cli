from click import command, argument, option

@command(name="generate")
@argument('hosts-file', default='hosts')
@option('--output-directory', help='output directory')
@option('--output-file-name', default='.trace.coordinator.yml', help='output file name')
@option('--port', '-p', default=8080)
@option('--groups', multiple=True, default=['workers'])
def generate_config(hosts_file, output_directory, output_file_name, port, groups):
    print("Work")
    pass