
from sqlalchemy import Integer, String, Column, Boolean, ForeignKey, Float, BigInteger
from sqlalchemy.orm import relationship
from biogas import db



class user(db.Model):
    __tablename__ = 'user'
    idMachine = Column(String(50), primary_key=True, nullable=False)
    userName = Column(String(50), nullable=False, unique=True)
    passWord = Column(String(50), nullable=False, unique=True)
    electricals = relationship('electrical', backref='user', lazy=True)
    environments = relationship('environment', backref='user', lazy=True)
    operations = relationship('operation', backref='user', lazy=True)

class electrical(db.Model):
    __tablename__ = 'electrical'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idMachine_id = Column(String(50), ForeignKey(user.idMachine), nullable=False)
    time = Column(BigInteger, nullable=False)
    eles = Column(Float, nullable=True)
    eleva = Column(Float, nullable=True)
    elevb = Column(Float, nullable=True)
    elevc = Column(Float, nullable=True)
    elevna = Column(Float, nullable=True)
    elevab = Column(Float, nullable=True)
    elevbc = Column(Float, nullable=True)
    elevca = Column(Float, nullable=True)
    elevla = Column(Float, nullable=True)
    eleia = Column(Float, nullable=True)
    eleib = Column(Float, nullable=True)
    eleic = Column(Float, nullable=True)
    eleiav = Column(Float, nullable=True)
    elepwa = Column(Float, nullable=True)
    elepwb = Column(Float, nullable=True)
    elepwc = Column(Float, nullable=True)
    elepwt = Column(Float, nullable=True)
    elepfa = Column(Float, nullable=True)
    elepfb = Column(Float, nullable=True)
    elepfc = Column(Float, nullable=True)
    elepft = Column(Float, nullable=True)
    elef = Column(Float, nullable=True)
    eleewh = Column(Float, nullable=True)
    eleevah = Column(Float, nullable=True)
    eletop = Column(Float, nullable=True)
    elethdva = Column(Float, nullable=True)
    elethdvb = Column(Float, nullable=True)
    elethdvc = Column(Float, nullable=True)
    elethdia = Column(Float, nullable=True)
    elethdib = Column(Float, nullable=True)
    elethdic = Column(Float, nullable=True)

class environment(db.Model):
    __tablename__ = 'environment'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idMachine_id = Column(String(50), ForeignKey(user.idMachine), nullable=False)
    time = Column(BigInteger, nullable=False)
    envtw = Column(Float, nullable=True)
    envpo = Column(Float, nullable=True)
    envo2 = Column(Float, nullable=True)
    envh2s = Column(Float, nullable=True)

class operation(db.Model):
    __tablename__ = 'operation'
    id = Column(Integer, primary_key=True , autoincrement=True, nullable=False)
    idMachine_id = Column(String(50), ForeignKey(user.idMachine), nullable=False)
    time = Column(BigInteger, nullable=False)
    opete = Column(Float, nullable=True)
    opetb = Column(Float, nullable=True)
    opepidsp = Column(Float, nullable=True)
    opepidout = Column(Float, nullable=True)
    opevpb = Column(Float, nullable=True)
    opepb = Column(Float, nullable=True)
    opevsfb = Column(Float, nullable=True)
def inserUser():
    for i in range(11,20):
        data = user(idMachine='g'+str(i), userName='user'+str(i), passWord='machine'+str(i))
        db.session.add(data)
        db.session.commit()


if __name__ == '__main__':
    #db.create_all()
    #inserUser()
    '''
    u1 = user(idMachine='g01', userName='user1', passWord='machine1')
    u2 = user(idMachine='g02', userName='user2', passWord='machine2')
    e1 = electrical(idMachine_id='g01', time = 1502135756)
    e2 = electrical(idMachine_id='g02', time=1502135756)
    db.session.add(e1)
    db.session.add(e2)
    db.session.commit()
    '''
