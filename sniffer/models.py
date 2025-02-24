from django.db import models

class Packet(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    src_ip = models.CharField(max_length=15)
    dst_ip = models.CharField(max_length=15)
    protocol = models.CharField(max_length=10)
    src_port = models.IntegerField(null=True, blank=True)
    dst_port = models.IntegerField(null=True, blank=True)
    payload = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.protocol} Packet: {self.src_ip}:{self.src_port} -> {self.dst_ip}:{self.dst_port}"