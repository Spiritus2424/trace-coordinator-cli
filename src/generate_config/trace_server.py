from ruamel.yaml import Representer

class TraceServer:
    def __init__(self, host: str, port: int, traces_path: list, filter: str):
        self.host = host
        self.port = port
        self.traces_path = traces_path
        self.filter = filter
    

    @classmethod
    def to_yaml(cls, representer: Representer, node):
        return representer.represent_dict({
            "host": node.host,
            "port": node.port,
            "traces-path": node.traces_path,
            "filter": node.filter
        })
   

    