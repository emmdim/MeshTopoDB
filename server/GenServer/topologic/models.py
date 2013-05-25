from django.db import models

# Create your models. here.
class Node(models.Model):
    #sliver name or hostname of the devide
    name = models.CharField(max_length=200)
    #mac of the node
    ethname = models.CharField(max_length=200)
    ethip = models.CharField(max_length=15)
    ethmac = models.CharField(max_length=17)

    def __unicode__(self):
        return self.name

# Do I need a switch structure?
# I actually need the switch
class Switch(models.Model):
    #What would be a UID for the virtual switches?
    name = models.CharField(max_length=200)
    eth1name = models.CharField(max_length=200)
    eth2name = models.CharField(max_length=200, default="none")
    eth3name = models.CharField(max_length=200, default="none")
    eth1mac = models.CharField(max_length=17)
    eth2mac = models.CharField(max_length=17, default="none")
    eth3mac = models.CharField(max_length=17, default="none")
    eth1ip = models.CharField(max_length=15, default="none")
    eth2ip = models.CharField(max_length=15, default="none")
    eth3ip = models.CharField(max_length=15, default="none")
    
    def __unicode__(self):
        return self.name

