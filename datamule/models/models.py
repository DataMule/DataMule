from sqlalchemy import Column, Table, Integer, ForeignKey, create_engine, String, Boolean, Numeric, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///data_mule.db')
Session = sessionmaker(bind=engine)
Base = declarative_base()


class TimestampMixin(object):
    created_date = Column(DateTime, default=func.now())


class DataProcessModel(Base, TimestampMixin):
    """DataProcess object"""
    __tablename__ = 'data_process'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    local_or_container = Column(String)
    delta = Column(String)
    table_name = Column(String)
    datasource_type = Column(String)


    def __str__(self):
        return 'id  name     local_or_container   delta    table_name   created_date   datasource_type \n' \
               '{}  {}       {}                   {}       {}           {}             {}'.format\
            (self.id, self.name, self.local_or_container, self.delta, self.table_name,
             self.created_date, self.datasource_type)

    def __repr__(self):
        return 'id  name     local_or_container   delta    table_name   created_date   datasource_type \n' \
               '{}  {}       {}                   {}       {}           {}             {}'.format\
            (self.id, self.name, self.local_or_container, self.delta, self.table_name,
             self.created_date, self.datasource_type)


Base.metadata.create_all(engine)