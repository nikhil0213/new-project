from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import FirstTable
from .serializers import FirstTableSerializer
from rest_framework import status
from testapp.forms import FirstTableForm
from testapp.models import FirstTable
from django.http import HttpResponse

import mysql.connector
from mysql.connector import Error
# Create your views here.
'''def std(request):
    if request.method=="POST":
        form=FirstTableForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/view')
            except:
                pass
    else:
        form=FirstTableForm()
    return render(request,'index.html',{'form':form})'''

def std(request):
    connection = mysql.connector.connect(host='localhost',
                                         database='amandata',
                                         user='root',
                                         password='',
                                         port='3308')
    cursor=connection.cursor()
    val=('shashank','cs2','bihar',87)
    sql="insert into testapp_firsttable(name,branch,address,marks) values(%s,%s,%s,%s)"
    cursor.execute(sql,val)
    connection.commit()
    s="<h1>data has been inserted</h1>"
    return HttpResponse(s)


@api_view(['GET'])
def FirstList(request):
    if request.method=='GET':
        obj=FirstTable.objects.all()
        serializer=FirstTableSerializer(obj,many=True)
        return Response(serializer.data)
