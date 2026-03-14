from django.db import models

class Assetowner(models.Model):
    ownerid = models.AutoField(db_column='OwnerID', primary_key=True)
    ownername = models.CharField(db_column='OwnerName', max_length=100)
    department = models.CharField(db_column='Department', max_length=100, blank=True, null=True)
    contactemail = models.CharField(db_column='ContactEmail', max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'AssetOwner'

    def __str__(self):
        return self.ownername


class Asset(models.Model):
    assetid = models.AutoField(db_column='AssetID', primary_key=True)
    hostname = models.CharField(db_column='Hostname', max_length=255)
    ipaddress = models.CharField(db_column='IPAddress', max_length=45, blank=True, null=True)
    operatingsystem = models.CharField(db_column='OperatingSystem', max_length=100, blank=True, null=True)
    isactive = models.IntegerField(db_column='IsActive', blank=True, null=True)
    ownerid = models.ForeignKey(Assetowner, models.CASCADE, db_column='OwnerID')

    class Meta:
        db_table = 'Asset'

    def __str__(self):
        return self.hostname


class Scan(models.Model):
    scanid = models.AutoField(db_column='ScanID', primary_key=True)
    scandate = models.DateTimeField(db_column='ScanDate')
    scannername = models.CharField(db_column='ScannerName', max_length=100, blank=True, null=True)
    scantype = models.CharField(db_column='ScanType', max_length=50, blank=True, null=True)
    scope = models.CharField(db_column='Scope', max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'Scan'

    def __str__(self):
        return f"Scan: {self.scandate.strftime('%Y-%m-%d')}"


class Vulnerabilitydefinition(models.Model):
    vuldefid = models.AutoField(db_column='VulDefID', primary_key=True)
    name = models.CharField(db_column='Name', max_length=255)
    cve_id = models.CharField(db_column='CVE_ID', unique=True, max_length=20, blank=True, null=True)
    basescore = models.DecimalField(db_column='BaseScore', max_digits=3, decimal_places=1, blank=True, null=True)
    description = models.TextField(db_column='Description', blank=True, null=True)

    class Meta:
        db_table = 'VulnerabilityDefinition'

    def __str__(self):
        return f"{self.cve_id} - {self.name}"


class Finding(models.Model):
    findingid = models.AutoField(db_column='FindingID', primary_key=True)
    discoverydate = models.DateField(db_column='DiscoveryDate', blank=True, null=True)
    assetid = models.ForeignKey(Asset, models.CASCADE, db_column='AssetID')
    vuldefid = models.ForeignKey(Vulnerabilitydefinition, models.CASCADE, db_column='VulDefID')
    scanid = models.ForeignKey(Scan, models.CASCADE, db_column='ScanID')
    status = models.CharField(db_column='Status', max_length=14, blank=True, null=True)

    class Meta:
        db_table = 'Finding'

    def __str__(self):
        return f"Finding {self.findingid}: {self.status}"


class Mitigationaction(models.Model):
    mactionid = models.AutoField(db_column='MActionID', primary_key=True)
    findingid = models.ForeignKey(Finding, models.CASCADE, db_column='FindingID')
    actiondate = models.DateTimeField(db_column='ActionDate', blank=True, null=True)
    actiontaken = models.TextField(db_column='ActionTaken', blank=True, null=True)
    operatorname = models.CharField(db_column='OperatorName', max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'MitigationAction'

    def __str__(self):
        return f"Action on Finding {self.findingid.findingid}"