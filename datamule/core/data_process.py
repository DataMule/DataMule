from datamule.models.models import Session
from datamule.models.models import DataProcessModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DataProcess():

    engine = create_engine('sqlite:///data_mule.db')

    def __init__(self):
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def insert_process(self, name, local_or_container, delta, table_name, datasource_type):
        session = Session()
        data_process = DataProcessModel(name=name, local_or_container=local_or_container,
                                        delta=delta, table_name=table_name, datasource_type=datasource_type)
        session.add(data_process)
        session.commit()

    def get_processes(self):
        data_processes = self.session.query(DataProcessModel).all()
        return data_processes

    def remove_process(self, name):
        self.session.query(DataProcessModel).filter(DataProcessModel.name == name).delete()