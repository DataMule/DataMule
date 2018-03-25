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
    template = """    {0:5}    |{1:20}|{2:20}|{3:20}|{4:22}|{5:14}""".format \
        ("id", "name", "local_or_container", "table_name", "created_date", "datasource_type")

    click.echo(template)
    for process in data_process.get_processes():
        click.echo(process)
        click.echo('\n')

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
    user_name, password = dataMule.run()
    click.echo("you database username is {} and password is {}".format(user_name, password))