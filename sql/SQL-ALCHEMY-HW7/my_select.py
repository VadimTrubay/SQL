from models import *
from pprint import pprint
from sqlalchemy import func,desc

def my_select1():
    select1 = session.query(Students.name, func.round(func.avg(Grades.grade),2).label("avg_grade"))\
        .select_from(Grades).join(Students).group_by(Students.id).order_by(desc("avg_grade")).limit(5).all()
    return select1



def my_select2():
    select2 = session.query(Students.name,Subjects.name, func.round(func.avg(Grades.grade),2).label("average_grade"))\
        .select_from(Grades).join(Students).join(Subjects)\
        .group_by(Students.id, Subjects.name).order_by(desc("average_grade")).where(Subjects.id == 5)\
        .first()
    return select2


def my_select3():
    select3 = session.query(Groups.name, Subjects.name, func.round(func.avg(Grades.grade)).label("average_grade"))\
        .select_from(Grades).join(Students).join(Subjects).join(Groups)\
        .group_by(Groups.name, Subjects.name).order_by(desc("average_grade")).where(Subjects.id==11).all()
    return select3

def my_select4():            
    select4= session.query(func.round(func.avg(Grades.grade),3).label("average_grade"))\
        .select_from(Grades).all()
    return select4


def my_select5():
    select5 = session.query(Subjects.name, Teachers.name)\
        .select_from(Subjects).join(Teachers).where(Teachers.id ==1).all()
    return select5

def my_select6():
    select6 = session.query(Students.name, Groups.name)\
        .select_from(Students).join(Groups).where(Groups.id ==1).all()
    return select6

def my_select7():
    select7 = session.query(Students.name, Grades.grade,Subjects.name, Groups.name)\
        .select_from(Grades).join(Students).join(Groups)\
        .group_by(Students.name).where(Subjects.id == 3,Groups.id ==3).all()
    return select7

def my_select8():
    select8 = session.query(Teachers.name, func.avg(Grades.grade), Subjects.name)\
        .select_from(Grades).join(Subjects).join(Teachers)\
        .where(Teachers.id == 4).group_by(Teachers.name,Subjects.name).all()
    return select8

def my_select9():
    select9 = session.query(Students.name, Subjects.name)\
    .select_from(Grades).join(Students).join(Subjects).group_by(Students.name,Subjects.name).where(Students.id ==25).all()
    return select9


def my_select10():
    select10 = session.query(Students.name, Subjects.name, Teachers.name)\
    .select_from(Grades).join(Students).join(Subjects).join(Teachers)\
    .group_by(Subjects.name).where(Students.id ==27,Teachers.id == 3).all()
    return select10
