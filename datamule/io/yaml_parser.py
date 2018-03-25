import os
import yaml
from collections import defaultdict


class yamlParser():
    def __init__(self):
        self.yamlFileDirectory = 'data_mule_hub'

    def parse(self, filename):
        cur_path = os.getcwd()
        yamlFilePath = os.path.join(cur_path, 'datamule', self.yamlFileDirectory, filename)
        with open(yamlFilePath,'r') as stream:
            try:
                parse_dict = yaml.load(stream)
                return parse_dict['get_data']
            except yaml.YAMLError as exc:
                print(exc)

    def getConstructorArguments(self, mydict):
        protocol = mydict['protocol']
        connectors = mydict['connectors']
        auth = mydict['auth']
        format_type = mydict['format_type']
        
        return protocol, connectors, auth, format_type
