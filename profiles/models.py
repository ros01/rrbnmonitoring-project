from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    ROLE = (
	('Monitoring', 'Monitoring'),
	('ZonalOffices', 'ZonalOffices'),
	('Registrar', 'Registrar'),
	('Finance', 'Finance'),
	)


    MODULE_NAME = (
	('Monitoring HQ', 'MonitoringHq'),
	('Enugu Office', 'EnuguOffice'),
	('Registrars Office', 'CEO'),
	('Accounts HQ', 'FAH'),
	)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    module_name = models.CharField (max_length=20, choices=MODULE_NAME)
    role = models.CharField (max_length=20, choices=ROLE)
