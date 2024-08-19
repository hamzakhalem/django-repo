from django.contrib.auth.models import User
from rest_framework import serializers



class UserSerializers(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True, required=False)
    username = serializers.CharField(read_only=True)
    old_password = serializers.CharField(write_only=True, required= False)

    def validate(self, data):
        reqmeth = self.context['request'].method
        password = data.get('password', None)

        if reqmeth == 'POST':
            if password == None:
                raise serializers.ValidationError({"info":"Please Provide Password"})
        elif reqmeth == 'PUT' or reqmeth == 'PATCH':   
            old_password = data.get('old_password', None)
            if password == None:
                raise serializers.ValidationError({"info":"Please Provide Password"})
            if password != None and old_password == None:
                raise serializers.ValidationError({"info":"Please Provide Old Password"})
        return data

    def create(self, validated_data):
        password = validated_data.pop['passowrd']
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
    def update(self, instance, validated_data):
        try:
            user = instance
            password = validated_data['password']
            old_password = validated_data['old_password']
            if(user.check_password(old_password)):
                user.set_password(password)
            else:
                raise Exception("Old password wrong")
            user.save()
        except Exception as err:
            raise serializers.ValidationError(err)
        return super(UserSerializers, self).update(instance, validated_data)
    class  Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'first_name', 'last_name', 'password', 'old_password']
