from wazimap.models import DBTable
from wazimap.data.base import Base
from wazimap.data.utils import get_session, get_datatable


def get_table_data(table_name, session, geo_code, geo_level):
    table = get_datatable(table_name)
    if table:
        description = table.description
        data = session.query(Base.metadata.tables[table_name]).filter(Base.metadata.tables[table_name].c.geo_level == geo_level).filter(Base.metadata.tables[table_name].c.geo_code == geo_code).all()

        return {
            'description': description,
            'raw_data': data,
            'columns': Base.metadata.tables[table_name].columns.keys()
        }

def raw_data_for_geography(geo_code, geo_level):
    Base.metadata.reflect()
    session = get_session()
    tables = DBTable.objects.all()

    final_data = []
    for table in tables:
        data = get_table_data(table.name, session, geo_code, geo_level)
        final_data.append(data)

    return final_data






