from rest_framework import serializers
from scraping.models import News

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('title', 'link', 'created_at', 'source')