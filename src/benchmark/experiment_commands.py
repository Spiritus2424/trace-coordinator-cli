from click import argument, option, Path, pass_obj
from time import sleep
from datetime import datetime
from tsp.tsp_client import TspClient
from tsp.indexing_status import IndexingStatus
from benchmark.commands import benchmark, log_benchmark, log_output, POLLING_TIME
from animation.waiting import start_waiting_animation, stop_waiting_animation

@benchmark.command(name="create-experiment")
@argument('EXPERIMENT_NAME', type=str)
@option('--uuids', type=str, multiple=True, help='List of traces UUID')
@option('--body', type=Path(exists=True), help='JSON file that contain the body params for the request')
@option('--debug', '-d', is_flag=True, default=False)
@option('--verbose', '-v', is_flag=True, default=False)
@pass_obj
def open_experiment(tsp_client: TspClient, experiment_name: str, uuids: list, body: str, debug: bool, verbose: bool):
    print(f"Create Experiment: ", end="")
    animation_event = start_waiting_animation()
    start = datetime.now()
    response = tsp_client.open_experiment(experiment_name, uuids)
    while response.is_ok() and response.model.indexing_status != IndexingStatus.COMPLETED:
        sleep(POLLING_TIME)
        response = tsp_client.fetch_experiment(response.model.UUID)
    end = datetime.now()
    elapsed = end - start
    stop_waiting_animation(animation_event)
    print(f"{elapsed.total_seconds()}s")
    log_benchmark(tsp_client.base_url, "Create Experiment", elapsed.total_seconds())


    if verbose:
        print(f"{response.model.name}:{response.model.UUID}:[{response.model.start},{response.model.end}]" )


@benchmark.command(name="get-experiments")
@option('--uuid', type=str, help='UUID of an experiment')
@option('--verbose', '-v', is_flag=True, default=False)
@pass_obj
def get_experiment(tsp_client: TspClient, uuid: str, verbose: bool):
    print(f"Get Experiments: ", end="")
    animation_event = start_waiting_animation()
    start = datetime.now()
    if uuid == None:
        response = tsp_client.fetch_experiments()
        while response.is_ok() and response.model.indexing_status != IndexingStatus.COMPLETED:
            sleep(POLLING_TIME)
            response = tsp_client.fetch_experiments()
    else:
        response = tsp_client.fetch_experiment(uuid)
        while response.is_ok() and response.model.indexing_status != IndexingStatus.COMPLETED.value:
            sleep(POLLING_TIME) 
            response = tsp_client.fetch_experiments(response.model.UUID)
    end = datetime.now()
    elapsed = end - start
    stop_waiting_animation(animation_event)
    print(f"{elapsed.total_seconds()}s")
    log_benchmark(tsp_client.base_url, "Get Experiments", elapsed.total_seconds())
    
    if verbose:
        print("Experiments: ", len(response.model))
        for experiment in response.model:
            print(f"{experiment.name}:{experiment.UUID}:[{experiment.start},{experiment.end}]")


@benchmark.command(name="get-outputs")
@argument('UUID', type=str)
@option('--output-id', type=str, default=None)
@option('--verbose', '-v', is_flag=True, default=False)
@pass_obj
def get_outputs_descriptors(tsp_client: TspClient, uuid: str, output_id: str, verbose: bool):

    print(f"Get Outputs Descriptors: ", end="")
    animation_event = start_waiting_animation()
    start = datetime.now()
    response = None
    if output_id == None:
        response = tsp_client.fetch_experiment_outputs(uuid)
    else:
        response = tsp_client.fetch_experiment_output(uuid, output_id)
    end = datetime.now()
    elapsed = end - start
    stop_waiting_animation(animation_event)
    print(f"{elapsed.total_seconds()}s")
    log_benchmark(tsp_client.base_url, "Get Outputs Descriptors", elapsed.total_seconds())

    if verbose:
        log_output("Get Outputs Descriptors", response)
        # print("Descriptors: ", len(response.model.descriptors))
        # pprint(json.dumps(response.__dict__,  default=vars))
