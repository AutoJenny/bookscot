from django.db import models

class Template(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    template_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class DataSet(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Script(models.Model):
    name = models.CharField(max_length=200)
    generated_script = models.TextField()
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    data_set = models.ForeignKey(DataSet, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Directory(models.Model):
    title = models.CharField(max_length=200)
    level = models.IntegerField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
