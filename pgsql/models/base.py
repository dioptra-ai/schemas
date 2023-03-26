from copy import deepcopy

from sqlalchemy import MetaData, inspect
from sqlalchemy.orm import declarative_base

Base = declarative_base(metadata=MetaData(naming_convention={
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_`%(constraint_name)s`",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}))


def _asdict(self):
    return deepcopy({
        'metadata' if c.key == 'metadata_' else c.key: getattr(self, c.key) 
            for c in inspect(self).mapper.column_attrs
    })

setattr(Base, '_asdict', _asdict)
