from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, Boolean, Text, String, DateTime, ForeignKey, Float

from .. import db
Base = db.Model


class Payer(Base):
    __tablename__ = "payers"
    id = Column(Integer, primary_key=True)
    name = Column(String(length=150))
    mapped_id = Column(String(length=10))

    def __unicode__(self):
        return self.name


payer_group_payers = Table(
    'payer_group_payers',
    Base.metadata,
    Column('payer_id', Integer, ForeignKey('payers.id')),
    Column('payer_group_id', Integer, ForeignKey('payer_groups.id'))
)


class PayerGroup(Base):
    __tablename__ = "payer_groups"
    id = Column(Integer, primary_key=True)
    name = Column(String(length=150))
    payers = relationship("Payer", secondary=payer_group_payers)

    def __unicode__(self):
        return "PayerGroup: " + str(self.name)


class Procedure(Base):
    __tablename__ = "procedures"
    id = Column(Integer, primary_key=True)
    name = Column(String(length=250))
    cpt = Column(String(length=25))


class ProcedurePrice(Base):
    __tablename__ = "procedure_prices"
    id = Column(Integer, primary_key=True)
    procedure_id = Column(Integer, ForeignKey("procedures.id"))
    payer_id = Column(Integer, ForeignKey("payers.id"))
    payer_group_id = Column(Integer, ForeignKey("payer_groups.id"))
    price = Column(Float)