from django.db import models

from apps.users.models import User


class Company(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    number = models.IntegerField(max_length=12)
    user = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE)


class Question(models.Model):
    question_type = models.CharField(max_length=100)
    documents = models.CharField


class Section(models.Model):
    name = models.CharField(max_length=200)
    question = models.ForeignKey(Question, related_name='questions', on_delete=models.CASCADE)
    company = models.ForeignKey(Company, related_name='company', on_delete=models.CASCADE)


class Job(models.Model):
    job_role = models.CharField(max_length=200)
    company = models.ForeignKey(Company, related_name='company', on_delete=models.CASCADE)
    section = models.ForeignKey(Section, related_name='section', on_delete=models.CASCADE)


class Assessor(models.Model):
    name = models.CharField(max_length=200)
    documents = models.CharField(max_length=200)


class Interview(models.Model):
    assessor = models.ForeignKey(Assessor, related_name='assessor', on_delete=models.CASCADE)


class Candidate(models.Model):
    name = models.CharField(max_length=100)
    nic = models.IntegerField(max_length=15)
    contact_number = models.IntegerField(max_length=12)


class Experience(models.Model):
    placed_work = models.CharField(max_length=100)
    time_period = models.DateTimeField
    role = models.CharField(max_length=100)
    candidate = models.ForeignKey(Candidate, related_name='candidate', on_delete=models.CASCADE)




