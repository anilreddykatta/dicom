# -*- coding: utf-8 -*-
from django.db import models

class Document(models.Model):
    docid = models.AutoField(primary_key=True)
    docfile = models.FileField(upload_to='')
    date_time = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.docfile.name
