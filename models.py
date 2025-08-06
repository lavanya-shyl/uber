from django.db import models



class Ride(models.Model):
    SOURCE_DESTINATION_CHOICES = [
        ('kayamkulam', 'Kayamkulam'),
        ('alappuzha', 'alappuzha'),
        ('ernakulam', 'Ernakulam'),
        ('thrissur', 'thrissur'),
    ]

    destination_source = models.CharField(max_length=100, choices=SOURCE_DESTINATION_CHOICES)
    destination = models.CharField(max_length=100, choices=SOURCE_DESTINATION_CHOICES)
    ride_date = models.DateTimeField()
    # distance = models.FloatField(null=True, blank=True)
    # fare = models.FloatField(default=0)

    def calculate_distance(self):
        if (self.destination_source == 'kayamkulam' and self.destination == 'alappuzha') or \
           (self.destination_source == 'alappuzha' and self.destination == 'kayamkulam'):
            return 10
        elif (self.destination_source == 'kayamkulam' and self.destination == 'ernakulam') or \
             (self.destination_source == 'ernakulam' and self.destination == 'kayamkulam'):
            return 15
        elif (self.destination_source == 'kayamkulam' and self.destination == 'thrissur') or \
             (self.destination_source == 'thrissur' and self.destination == 'kayamkulam'):
            return 8
        else:
            return 0

    def calculate_fare(self):
        base_fare = 50
        per_km_rate = 10
        distance = self.calculate_distance()
        self.distance = distance
        self.fare = base_fare + (distance * per_km_rate)
        if self.fare is None:
            self.fare = 0
