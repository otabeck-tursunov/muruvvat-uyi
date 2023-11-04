from django.db import models

class Yangilik(models.Model):
    sarlavha = models.CharField(max_length=100)
    qisqa_matn = models.CharField(max_length=200)
    batafsil = models.TextField()
    rasm = models.FileField(upload_to='yangilik', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sarlavha}"


