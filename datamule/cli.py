import click
from datamule.io.yaml_parser import yamlParser
from datamule.core.data_mule import DataMule
from datamule.core.data_process import DataProcess

@click.group()
def main():
    pass

@main.command()
def ps():
    """This prints all currently running processes in the database. """
    data_process = DataProcess()
    click.echo(data_process.get_processes())

@main.command()
@click.argument('dataset_name', type=click.STRING)
@click.argument('db_type', type=click.STRING)
def run(dataset_name, db_type):
    """Starts the datamule."""
    parser = yamlParser()
    dataset_dict = parser.parse(dataset_name + ".yml")
    protocol, connectors, auth, format_type = parser.getConstructorArguments(dataset_dict)
    API_ACCESS_TOKEN = None
    if auth:
        API_ACCESS_TOKEN = click.prompt('Authentication required, please enter API access token', type=str)
    dataMule = DataMule(protocol, connectors, auth, format_type, db_type, API_ACCESS_TOKEN)
    dataMule.run()