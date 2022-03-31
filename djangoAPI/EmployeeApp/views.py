from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Departments,Employees
from EmployeeApp.serializers import DepartmentSerializer, EmployeeSerializer

@csrf_exempt
def departmentApi(request,id=0):
    if request.method=='GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(deepartments_serializer.data, safe=False)
    elif request.method=='POST':
        department_data=JSONParser().parse(request)
        department_serlializer = DepartmentSerializer(data=department_data)
        if department_serlializer.is_valid():
            department_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method=="PUT":
        department_data = JSONParser().parse(request)
        department=Department.objects.get(DepartmentId=department_data['DepartmentId'])
        department_serializer=DepartmentSerializer(department,data=department_data)
        if department_serlializer.is_valid():
            department_serlializer.save()
            return JsonResponse("Updated Successfully!", safe=False)
        return JsonResponse("Failed to update.", safe=False)

    elif request.method=='DELETE':
        department=Departments.objects.get(DepartmentId=id)
        departments.delete()
        return JsonResponse('Deleted Successfully!', safe=False)

