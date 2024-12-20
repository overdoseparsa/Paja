from django.db import models
from django.utils.timezone import now
from django.contrib.auth import get_user_model

def check_valid_ammount(amount):
    assert 5000  < amount < 10**10 , "Not ; vaild amount"
    return amount



class Tarakonsh(
    models.Model
):
    time = models.DateTimeField(
        null=False , blank=True , 
    )
    
    description = models.TextField(
        null= True  , 
    )
    
    amount = models.PositiveBigIntegerField(
        blank=False , null= False  , unique_for_date='time' , validators=[check_valid_ammount]
    )
    # add title or description 

    author  = models.ForeignKey(
        get_user_model() , on_delete=models.CASCADE , blank=False  , null= False  , 
    )
    test_image = models.ImageField(
       blank=False , null= True , 
    )

    
    def __str__(self):
        return f'{self.author.username} -> {self.amount} <- '
    
    