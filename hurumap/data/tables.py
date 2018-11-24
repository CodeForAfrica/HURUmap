from wazimap.data.tables import FieldTable as FieldTableWazimap, SimpleTable as SimpleTableWazimap, get_model_for_db_table, Base, Table

class SimpleTable(SimpleTableWazimap):
  def _build_model(self, db_table):
        # does it already exist?
        model = get_model_for_db_table(db_table)
        if model:
            return model

        columns = self._build_model_columns()

        class Model(Base):
            __table__ = Table(db_table, Base.metadata, *columns, autoload=False, extend_existing=True)

        return Model

class FieldTable(FieldTableWazimap):
  def _build_model(self, db_table):
        # does it already exist?
        model = get_model_for_db_table(db_table)
        if model:
            return model

        columns = self._build_model_columns()

        class Model(Base):
            __table__ = Table(db_table, Base.metadata, *columns, autoload=False, extend_existing=True)

        return Model

