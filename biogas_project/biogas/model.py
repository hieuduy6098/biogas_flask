
from sqlalchemy import Integer, String, Column, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from biogas import db



class users(db.Model):
    id = Column(Integer , autoincrement=True, nullable=False)
    userName = Column(String(50), nullable=False, unique=True)
    passWord = Column(String(50), nullable=False, unique=True)
    idMachine = Column(String(50), primary_key=True, nullable=False)
    dataSensors = relationship('dataSensors', backref='user', lazy=True)
    active = Column(Boolean, default=True)

class dataSensors(db.Model):
    id = Column(Integer,primary_key=True , autoincrement=True, nullable=False)
    typeData = Column(String(10), nullable=False)
    idMachine_id = Column(String(50), ForeignKey(users.idMachine), nullable=False)


if __name__ == '__main__':
    db.create_all()
