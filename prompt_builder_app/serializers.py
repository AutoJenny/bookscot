from rest_framework import serializers
from .models import DataSet, Template, Script

class DataSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSet
        fields = '__all__'

class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = '__all__'

class ScriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Script
        fields = '__all__'
from rest_framework import serializers
from .models import DataSet, Template, Script

class DataSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSet
        fields = '__all__'

class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = '__all__'

class ScriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Script
        fields = '__all__'
