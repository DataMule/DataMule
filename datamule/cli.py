import click
from datamule.io.yaml_Parser import yamlParser
from datamule.core.data_mule import DataMule

@click.group()
def main():
    pass

@main.command()
def ps():
    """This prints all currently running process. """
    pass

@main.command()
@click.argument('dataset_name', type=click.STRING)
@click.argument('db_type', type=click.STRING)
def run(dataset_name, db_type):
    """This starts the datamule."""
    parser = yamlParser()
    dataset_dict = parser.parse(dataset_name + ".yml")
    protocol, connectors, auth, format_type = parser.getConstructorArguments(dataset_dict)
    API_ACCESS_TOKEN = None
    if auth:
        API_ACCESS_TOKEN = click.prompt('Authentication required, please enter API access token', type=str)
    dataMule = DataMule(protocol, connectors, auth, format_type, db_type, API_ACCESS_TOKEN)
    dataMule.run()

