from django.shortcuts import render
from django.contrib.auth.models import User
from .models import rahul
import openpyxl
# import csv


def new_user(request):
	users = User.objects.all()
	return render(request, 'new_user.html',{'users':users})


def excel_data(request):
	wb = openpyxl.load_workbook('/home/user/Downloads/pizza.xlsx')
	worksheet = wb["Sheet1"]
	excel_data = list()
	for row in worksheet.iter_rows():
		row_data = list()
		for cell in row:
			row_data.append(str(cell.value))
		excel_data.append(row_data)
	return render(request, 'includes/excel.html', {"excel_data":excel_data})

