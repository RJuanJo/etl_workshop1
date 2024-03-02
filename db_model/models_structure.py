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
    email = Column(String(60))
    applicant_date = Column(String(20))
    country = Column(String(40))
    experience_year = Column(String(40))
    seniority = Column(String(40))
    technology = Column(String(40))
    code_challenge_score = Column(String(40))
    technical_interview_score = Column(String(40))
