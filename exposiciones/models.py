from django.db import models

from django.db import models

CATEGORIES = [
    ('Cuadros', 'Cuadros'),
    ('Obras de teatro', 'Obras de teatro'),
    ('Espacio', 'Espacio'),
    ('Otra', 'Otra'),
]

class Exposicion(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    categoria = models.CharField(max_length=50, choices=CATEGORIES)
    imagen = models.ImageField(upload_to='imagenes/', blank=True, null=True)
    audio = models.FileField(upload_to='audios/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} ({self.categoria})"

