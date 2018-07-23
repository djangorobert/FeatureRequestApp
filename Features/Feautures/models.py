# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class FeatureRequest(models.Model):


    CLIENT_A = 'A'
    CLIENT_B = 'B'
    CLIENT_C = 'C'


    HIGH = 'HIGH'
    MEDIUM = 'MEDIUM'
    LOW = 'LOW'


    POLICIES = 'POLICIES'
    BILLING = 'BILLING'
    CLAIMS = "CLAIMS"
    REPORTS = "REPORTS"

    PRIORITY = (
        (HIGH, 'HIGH'),
        (MEDIUM, 'MEDIUM'),
        (LOW, 'LOW'),
    )

    CLIENT = (
        (CLIENT_A, 'Client A'),
        (CLIENT_B, 'Client B'),
        (CLIENT_C, 'Client C'),
    )

    DEPARTMENT = (
        (POLICIES, 'Policies'),
        (BILLING, 'Billing'),
        (CLAIMS, 'Claims'),
        (REPORTS, 'Reports'),
    )


    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    client = models.CharField(
        max_length=9,
        choices=CLIENT)

    priority = models.CharField(
        max_length=8,
        choices=PRIORITY
    )

    target_date = models.DateTimeField('%m/%d/%y')
    department = models.CharField(
        max_length=12,
        choices=DEPARTMENT
    )

    def __unicode__(self):
        return self.title