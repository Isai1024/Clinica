from django.db import models

# Create your models here.

class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    
    patient = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='doctor_appointments')
    office = models.ForeignKey('office.Office', on_delete=models.CASCADE)
    
    appointment_date = models.DateTimeField()
    reason = models.TextField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'appointments'
        ordering = ['appointment_date']
    
    def __str__(self):
        return f"Appointment {self.appointment_id} - {self.patient.first_name} with {self.doctor.first_name} on {self.appointment_date}"