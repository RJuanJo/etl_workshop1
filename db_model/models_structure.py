""" Declare the SQL classes for the database """

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Date, CheckConstraint

BASE = declarative_base()


class Candidates(BASE):
    """This class is to create the table candidates in the database from the csv."""

    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(100))
    applicant_date = Column(String(20))
    country = Column(String(100))
    experience_year = Column(String(40))
    seniority = Column(String(40))
    technology = Column(String(40))
    code_challenge_score = Column(String(40))
    technical_interview_score = Column(String(40))


class BestCandidates(BASE):
    """This table is to store the data from the candidates after the ETL process."""

    __tablename__ = "aspirant"

    id = Column(Integer, primary_key=True)
    applicant_date = Column(Date())
    code_challenge_score = Column(Integer())
    country = Column(String(100))
    email = Column(String(100))
    experience_year = Column(Integer())
    first_name = Column(String(50))
    is_hire = Column(Integer())
    last_name = Column(String(50))
    seniority = Column(String(40))
    technical_interview_score = Column(Integer())
    technology = Column(String(40))
    technology_category = Column(String(40))

    __table_args__ = (CheckConstraint("is_hire >= 0 AND is_hire <= 1"),)
