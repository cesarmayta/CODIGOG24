# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'
        
    def __str__(self):
        return self.name

class Kind(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kind'
        
    def __str__(self):
        return self.name

class Person(models.Model):
    code = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=60, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    kind = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person'
    
    def __str__(self):
        return self.name


class Priority(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'priority'
    
    def __str__(self):
        return self.name
        


class Project(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project'

    def __str__(self):
        return self.name
    
class Status(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'status'

    def __str__(self):
        return self.name
    
class Subkind(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    kind = models.ForeignKey(Kind, models.RESTRICT)

    class Meta:
        managed = False
        db_table = 'subkind'

    def __str__(self):
        return self.name

class Ticket(models.Model):
    code = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    file = models.CharField(max_length=255, blank=True, null=True)
    file2 = models.CharField(max_length=255, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True,auto_now=True)
    created_at = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    kind = models.ForeignKey(Kind, models.RESTRICT)
    subkind = models.ForeignKey(Subkind, models.RESTRICT, blank=True, null=True)
    user = models.ForeignKey(User, models.RESTRICT, blank=True, null=True)
    person = models.ForeignKey(Person, models.RESTRICT, blank=True, null=True)
    asigned = models.ForeignKey(User, models.RESTRICT, related_name='ticket_asigned_set', blank=True, null=True)
    project = models.ForeignKey(Project, models.RESTRICT, blank=True, null=True)
    category = models.ForeignKey(Category, models.RESTRICT, blank=True, null=True)
    priority = models.ForeignKey(Priority, models.RESTRICT)
    status = models.ForeignKey(Status, models.RESTRICT, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ticket'
        
    def __str__(self):
        return self.title
        
class Answer(models.Model):
    description = models.TextField(blank=True, null=True)
    file = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, models.RESTRICT, blank=True, null=True)
    person = models.ForeignKey(Person, models.RESTRICT, blank=True, null=True)
    status = models.ForeignKey(Status, models.RESTRICT, blank=True, null=True)
    ticket = models.ForeignKey(Ticket, models.RESTRICT)
    kind = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'answer'
        
    def __str__(self):
        return self.ticket.title
        
class History(models.Model):
    code = models.CharField(max_length=50, blank=True, null=True)
    date_at = models.DateField(blank=True, null=True,auto_now=True)
    description = models.TextField()
    status = models.ForeignKey(Status, models.RESTRICT, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, models.RESTRICT, blank=True, null=True)
    asigned = models.ForeignKey(User, models.RESTRICT, related_name='history_asigned_set', blank=True, null=True)
    ticket = models.ForeignKey(Ticket, models.RESTRICT)

    class Meta:
        managed = False
        db_table = 'history'
        
    def __str__(self):
        return self.ticket.title
        
class Notification(models.Model):
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(User, models.RESTRICT, blank=True, null=True)
    receptor = models.ForeignKey(User, models.RESTRICT, related_name='notification_receptor_set', blank=True, null=True)
    ticket = models.ForeignKey(Ticket, models.RESTRICT)
    status = models.ForeignKey(Status, models.RESTRICT, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notification'
        
    def __str__(self):
        return self.ticket.title