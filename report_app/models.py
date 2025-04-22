

# Create your models here.
from django.db import models
from user_app.models import User
import uuid

# Create your models here.
road_severity=(
    (1,"mild"),
    (2,"moderate"),
    (3,"severe")
)

Category=(
    (1,"environmental & sanitation issues"),
    (2,"infrastructure issues"),
    (3,"public safety issue"),
    (4,"utilities & public service"),
    (5,"community and public service maintenance"),
    (6,"Health and emergency concern")
    
    
)
STATUS_TYPE_CHOICES = [
    ('active', 'Active'),
    ('inactive', 'Inactive'),
    ('pending', 'Pending'),
    ('completed', 'Completed'),
]


class Report(models.Model):
    id=models.UUIDField(unique=True,primary_key=True,default=uuid.uuid4)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True) 
    category_id=models.IntegerField(choices=Category,default=1)
    description=models.TextField()
    severity=models.IntegerField(choices=road_severity,default=1)
    latitude=models.DecimalField(max_digits=9, decimal_places=6)
    longitude=models.DecimalField(max_digits=9, decimal_places=6)
    image_url=models.ImageField(upload_to='report',null=True,blank=True)
    status=models.CharField(max_length=20,choices=STATUS_TYPE_CHOICES,default="pending")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.description
    
    

