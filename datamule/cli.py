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
@click.argument('datasetname', type=click.STRING)
def run(datasetname):
    """This starts the datamule."""
    parser = yamlParser()
    d = parser.parse(datasetname + ".yml")
    protocol, connectors, auth, format_type, db_type = parser.getConstructorArguments(d)
    API_ACCESS_TOKEN = None
    if auth:
        API_ACCESS_TOKEN = click.prompt('Authentication required, please enter API access token', type=str)
    dataMule = DataMule(protocol, connectors, auth, format_type, db_type, API_ACCESS_TOKEN)
    dataMule.run()

