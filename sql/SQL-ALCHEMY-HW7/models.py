from datetime import datetime
from sqlalchemy import Column,Integer, String,Boolean
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, relationship


engine = create_engine("sqlite:///college.db")
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Students(Base):
    __tablename__ = "students"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(40))
    group_id = Column(Integer(), ForeignKey("ggroups.id"))

class Groups(Base):
    __tablename__ = "ggroups"
    id = Column(Integer(),primary_key=True, autoincrement=True)
    name = Column(String(25))

class Teachers(Base):
    __tablename__ = "teachers"
    id = Column(Integer(), primary_key= True, autoincrement= True)
    name = Column(String(40))

class Subjects(Base):
    __tablename__ = "subjects"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(30))
    teacher_id = Column(Integer(), ForeignKey("teachers.id"))

class Grades(Base):
    __tablename__ = "grades"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    subject_id = Column(Integer(),ForeignKey("subjects.id"))
    student_id = Column(Integer(),ForeignKey("students.id"))
    grade = Column(Integer())
    date = Column(DateTime())
