from django.db import models
from datetime import date
from django.urls import reverse


class AbstractPerson(models.Model):
    name
    birth_date


class Employee(AbstractPerson):
    work_position
    experience


class Passport(models.Model):
    employee
    inn
    card_id


class WorkProject(models.Model):
    project_name
    employee


class Membership(models.Model):

