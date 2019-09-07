from api.models import Match, Sport, Market, Selection
from rest_framework import serializers


class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = ('id', 'name')


class SelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = ('id', 'name', 'odds')


class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = ('id', 'name', 'selections')


class MatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ('id', 'url', 'name', 'start_time')


class MatchDetailSerializer(serializers.ModelSerializer):
    sport = SportSerializer()
    market = MarketSerializer()

    class Meta:
        model = Match
        fields = ('id', 'url', 'name', 'start_time', 'sport', 'market')
