# -*- coding:utf-8 -*-
'''
# Author: li zi hao
'''
from rest_framework import serializers
from booktest.models import BookInfo

class BookInfoSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True,label='书籍编号')
    btitle = serializers.CharField(max_length=20,min_length=3,label='名称')
    bpub_date = serializers.DateField(label='发布日期')     # 必填字段如果没有的话，系统会报错
    bread = serializers.IntegerField(default=0,min_value=0,label='阅读量')
    bcomment = serializers.IntegerField(default=0,max_value=50,label='评论量')
    is_delete = serializers.BooleanField(default=False,label='逻辑删除')
    heros = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    def create(self, validated_data):
        book = BookInfo.objects.create(**validated_data)
        return book
    
    def update(self, instance, validated_data):
        instance.btitle = validated_data['btitle']
        instance.bcomment = validated_data['bcomment']
        instance.bpub_date = validated_data['bpub_date']
        instance.bread = validated_data['bread']
        instance.is_delete = validated_data['is_delete']
        return instance
    
    # def validate_btitle(self, value):
    #     if 'test' not in value:
    #         raise serializers.ValidationError('书名错误')
    #     return value

    # def create(self, validated_data):
    #     book = BookInfo.objects.create(**validated_data)
    #     return book
    
    # def update(self, instance, validated_data):
    #     instance.btitle = validated_data['btitle']
    #     instance.bpub_date = validated_data['bpub_date']
    #     instance.bread = validated_data['bread']
    #     instance.bcomment = validated_data['bcomment']
    #     instance.is_delete = validated_data['is_delete']
    #     instance.save()
    #     return instance

class HeroInfoSerializer(serializers.Serializer):
    GENDER = ((0, 'male'), (1, 'female'))
    id = serializers.IntegerField(label='ID',read_only=True)
    hname = serializers.CharField(max_length=20, label='名称')
    hgender = serializers.ChoiceField(choices=GENDER, label='性别', required=False)
    hcomment = serializers.CharField(max_length=200, label='描述信息', allow_null=True)
    # hbook = serializers.PrimaryKeyRelatedField(read_only=True)
    # hbook = serializers.StringRelatedField(read_only=True)
    hbook = BookInfoSerializer()

