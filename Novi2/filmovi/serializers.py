from django.shortcuts import render
from rest_framework import serializers
from filmovi.models import Filmovi, Produkcija, Bioskopi


# class FilmoviProdukcijaSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Produkcija
#         fields = ('produkcijske_kuce', ' filmovi_set')


class ProdukcijaFilmoviSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filmovi
        fields = ('naslovi',)


# class FilmoviBioskopiSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Bioskopi
#         fields = ('bioskop', 'filmovi_set')


class BioskopiFilmoviSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filmovi
        fields = ('naslovi',)


class ProdukcijaSerializer(serializers.ModelSerializer):
    filmovi = ProdukcijaFilmoviSerializer(many=True, read_only=True)

    class Meta:
        model = Produkcija
        fields = ('produkcijske_kuce', 'filmovi')


class BioskopiSerializer(serializers.ModelSerializer):
    filmovi = BioskopiFilmoviSerializer(many=True, read_only=True)

    class Meta:
        model = Bioskopi
        fields = ('bioskop', 'filmovi')


class FilmoviSerializer(serializers.ModelSerializer):
    # produkcija = FilmoviProdukcijaSerializer()
    # # produkcija = serializers.CharField(source="produkcija.produkcijske_kuce")
    # bioskopi = FilmoviBioskopiSerializer()

    class Meta:
        model = Filmovi
        fields = ('produkcija', 'biskis', 'naslovi',
                  'zanrovi', 'rezija', 'glumci', 'ocene')


class FilmoviProdukcijaSerializer(serializers.ModelSerializer):
    filmovi_set = FilmoviSerializer(many=True)

    class Meta:
        model = Produkcija
        fields = '__all__'

    def create(self, validated_data):
        filmovi_validated_data = validated_data.pop('filmovi_set')
        produkcija = Produkcija.objects.create(**validated_data)
        filmovi_set_serializer = self.fields['filmovi_set']
        for each in filmovi_validated_data:
            each['produkcija'] = produkcija
        filmovi = filmovi_set_serializer.create(filmovi_validated_data)
        return produkcija


class FilmoviBioskopiSerializer(serializers.ModelSerializer):
    # filmovi = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    filmovi_set = FilmoviSerializer(many=True)

    class Meta:
        model = Bioskopi
        fields = '__all__'

    def create(self, validated_data):
        filmovi_validated_data = validated_data.pop('filmovi_set')
        bioskop = Bioskopi.objects.create(**validated_data)
        filmovi_set_serializer = self.fields['filmovi_set']
        for each in filmovi_validated_data:
            each['bioskop'] = bioskop
        filmovi = filmovi_set_serializer.create(filmovi_validated_data)
        return bioskop



