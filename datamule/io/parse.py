import yaml
from datatmule.core.data_set import DataSet
from collections import defaultdict


class Parser():
    def parse(self,filename):
        d = defaultdict(dict)
        with open(filename,'r') as stream:
            try:
                parse_dict = yaml.load(stream)
                return parse_dict['get_data']
            except yaml.YAMLError as exc:
                print(exc)
    def getConstructorArguments(self,mydict):
        protocol = mydict['protocol']
        connectors = mydict['connectors']
        delta = mydict['delta']
        auth = mydict['auth']
        schema =mydict['schema']
        format_type = mydcit['format_type']
        return protocol,connectors,auth,schema,delta,format_type
                


