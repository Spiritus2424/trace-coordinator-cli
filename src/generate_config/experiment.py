from ruamel.yaml import Representer

class Experiment:
    def __init__(self, name: str, traces_path: list, filter: str):
        self.name = name
        self.traces_path = traces_path
        self.filter = filter
    

    @classmethod
    def to_yaml(cls, representer: Representer, node):
        return representer.represent_dict({
            "name": node.name,
            "traces-path": node.traces_path,
            "filter": node.filter
        })
   

    