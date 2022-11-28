from django.db import models

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    imag = models.TextField(max_length=350)

    # new code below
    def __str__(self):
        return self.name



class Feeding(models.Model):
    date = models.DateField()
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    )
    # Create a finch_id ForeignKey
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def  __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
    
    class Meta:
       ordering = ['-date']

        