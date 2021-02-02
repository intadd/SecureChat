from django.db import models

class PubKeyWithServer(models.Model):
    pubKey = models.CharField(max_length=300)
    serverNameHash = models.CharField(max_length=512)
    
    def __str__(self):
        return self.serverNameHash
