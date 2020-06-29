from django.db import models


class JoinRequest(models.Model):
    TITLES =(
        ('Mr', 'Mr'),
        ('Ms', 'Ms')
    )
    STATUS =(
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('confirmed', 'Confirmed'),
        ('rejected', 'Rejected')
    )
    PROVINCES =(
        ('cp', 'Central Province'),
        ('ep', 'Eastern Province'),
        ('np', 'Northern Province'),
        ('sp', 'Southern Province'),
        ('wp', 'Western Province'),
        ('nwp', 'North Western Province'),
        ('ncp', 'North Central Province'),
        ('up', 'Uva Province'),
        ('sgp', 'Sabaragamuwa Province'),
    )
    title = models.CharField(null=False, choices=TITLES, max_length=36)
    first_name = models.CharField(null=False, max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(null=False,max_length=100)
    nic = models.CharField(null=False, max_length=12,default=None)

    email = models.EmailField(null=False, default=None)
    address_line_one = models.CharField(null=False,max_length=100, default=None)
    address_line_two = models.CharField(null=False,max_length=100, default=None)
    city = models.CharField(null=False, max_length=150,default=None)
    province = models.CharField(null=False,choices=PROVINCES, max_length=50, default=None)

    vehicle_reg = models.CharField(null=False, max_length=20,default=None)
    photo = models.ImageField(default=None)

    applied_date = models.DateField(auto_now=True)
    status = models.CharField(null=False, default='pending', choices=STATUS, max_length=20)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name
