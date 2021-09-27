from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=200)
    user_password = models.CharField(max_length=100)


class Company(models.Model):
    company_name = models.CharField(max_length=200)
    company_location = models.CharField(max_length=200)
    company_number = models.IntegerField(max_length=12)
    user = models.ForeignKey(User, related_name='user', on_delete=models.PROTECT)


class Job(models.Model):
    job_role = models.CharField(max_length=200)
    company = models.ForeignKey(Company, related_name='company', on_delete=models.CASCADE)


class Accesssor(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.PROTECT)
    job = models.ForeignKey(Job, related_name='job', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)


class Interview(models.Model):
    accessor = models.ForeignKey(Accesssor, related_name='accessor', on_delete=models.CASCADE)


class Candidate(models.Model):
    name = models.CharField(max_length=100)
    nic_number = models.IntegerField(max_length=15)
    contact_number = models.IntegerField(max_length=12)


class Question(models.Model):
    question_type = models.CharField(max_length=100)
    documents = models.CharField


class Section(models.Model):
    section_name = models.CharField(max_length=200)
    question = models.ForeignKey(Question, related_name='questions', on_delete=models.CASCADE)
    company = models.ForeignKey(Company, related_name='company', on_delete=models.CASCADE)


class Experience(models.Model):
    placed_work = models.CharField(max_length=100)
    time_period = models.DateTimeField
    role = models.CharField(max_length=100)
    candidate = models.ForeignKey(Candidate, related_name='candidate', on_delete=models.CASCADE)




