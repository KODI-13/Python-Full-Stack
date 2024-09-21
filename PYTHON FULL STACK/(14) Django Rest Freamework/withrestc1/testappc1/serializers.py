from rest_framework import serializers
from testappc1.models import Employee


# # validation using Validator Attributes
# def multiple_of_1000(value):
#     if value%1000 != 0:
#         raise serializers.ValidationError('Employee Salary should be multiple of 1000')
    
# class EmployeeSerializer(serializers.Serializer):
#     eno = serializers.IntegerField()
#     ename = serializers.CharField(max_length=200)
#     esal = serializers.FloatField(validators=[multiple_of_1000])
#     eaddr = serializers.CharField(max_length=200)

#     # Field level validations
#     def validate_esal(self, value):
#         if value < 5000:
#             raise serializers.ValidationError('Employee salary should be minimum 5000')
#         return value
    
#     # Object level validations
#     def validate(self, data):
#         ename = data.get('ename')
#         esal = data.get('esal')
#         if ename.lower() == 'sunny':
#             if esal < 50000:
#                 raise serializers.ValidationError('Sunny salary should be minimum 5000')
#         return data
    
#     def create(self, validated_data):
#         return Employee.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.eno = validated_data.get('eno',instance.eno)
#         instance.ename = validated_data.get('ename',instance.ename)
#         instance.esal = validated_data.get('esal',instance.esal)
#         instance.eaddr = validated_data.get('eaddr',instance.eaddr)
#         instance.save()
#         return instance


# # option for normal serializer defined above

# with the use of model serializer we dont have to explicitly explain all fields and also there is no need to override create and update method inside model Serializer


def multiple_of_1000(value):
    if value%1000 != 0:
        raise serializers.ValidationError('Employee Salary should be multiple of 1000')
    
class EmployeeSerializer(serializers.ModelSerializer):
    esal = serializers.FloatField(validators=[multiple_of_1000])

    class Meta:
        model = Employee
        fields = '__all__'


# go to 1_basic.txt Notes