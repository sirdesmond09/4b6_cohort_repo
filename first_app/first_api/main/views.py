from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import BookSerializer, StudentSerializer
from .models import Book, Student
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(methods=['POST'], request_body=StudentSerializer())
@api_view(['GET', 'POST'])
def students(request):
    
    if request.method == 'GET':
        all_students = Student.objects.order_by('-date_joined') #get the data
        
        serializer = StudentSerializer(all_students,many=True) #serialize the data
        
        data = {
            "message":"success",
            "data" : serializer.data
        } #prepare the response data
        
        
        return Response(data, status=status.HTTP_200_OK) #send the response
    
    
    elif request.method == 'POST':
        
        serializer = StudentSerializer(data=request.data)  #get and deserialize the data
        
        if serializer.is_valid(): #check if data is valid
            serializer.save() #save the data
            data = {
            "message":"success",
            "data" : serializer.data
            }
            return Response(data, status=status.HTTP_201_CREATED)
        
        
        else:
            error = {
                'message':'failed',
                "errors":serializer.errors
            }
    
            return Response(error, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(methods=['PUT', 'DELETE'], request_body=StudentSerializer())
@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, student_id):
    """
    Takes in a student id and returns the http response depending on the http method.
    
    Args:
    student_id: Interger
    
    Allowed methods:
    GET- Get the detail of a single student
    PUT- Aloows the student detail to be edited
    DELETE- This logic delets the student record from the data base
    """
    
    try:
        student = Student.objects.get(id=student_id) #get the data from the model
    except Student.DoesNotExist:
        error = {
                'message':'failed',
                "errors": f"Student with id {student_id} does not exist"
            }
    
        return Response(error, status=status.HTTP_404_NOT_FOUND)
    
    
    
    if request.method == "GET":
        serializer = StudentSerializer(student) 
        data = {
            "message":"success",
            "data" : serializer.data
        } #prepare the response data
        
        
        return Response(data, status=status.HTTP_200_OK) #send the response
    
    elif request.method == "PUT":
        serializer = StudentSerializer(student, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            data = {
            "message":"success",
            "data" : serializer.data
            }
            return Response(data, status=status.HTTP_202_ACCEPTED)
        
        
        else:
            error = {
                'message':'failed',
                "errors":serializer.errors
            }
    
            return Response(error, status=status.HTTP_400_BAD_REQUEST) 
        
    elif request.method == 'DELETE':
        student.delete()
        
        return Response({"message":"success"}, status=status.HTTP_204_NO_CONTENT)
    
    
    
@swagger_auto_schema(methods=['POST'], request_body=BookSerializer())  
@api_view(['GET', 'POST'])
def books(request):
    
    if request.method == 'GET':
        all_books = Book.objects.order_by('-created_at') #get the data
        
        serializer = BookSerializer(all_books,many=True) #serialize the data
        
        data = {
            "message":"success",
            "data" : serializer.data
        } #prepare the response data
        
        
        return Response(data, status=status.HTTP_200_OK) #send the response
    
    
    elif request.method == 'POST':
        
        serializer = BookSerializer(data=request.data)  #get and deserialize the data
        
        if serializer.is_valid(): #check if data is valid
            serializer.save() #save the data
            data = {
            "message":"success",
            "data" : serializer.data
            }
            return Response(data, status=status.HTTP_201_CREATED)
        
        
        else:
            error = {
                'message':'failed',
                "errors":serializer.errors
            }
    
            return Response(error, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(methods=['PUT', 'DELETE'], request_body=BookSerializer())
@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, book_id):
    """
    Takes in a book id and returns the http response depending on the http method.
    
    Args:
    book_id: Interger
    
    Allowed methods:
    GET- Get the detail of a single book
    PUT- Aloows the book detail to be edited
    DELETE- This logic delets the book record from the data base
    """
    
    try:
        book = Book.objects.get(id=book_id) #get the data from the model
    except Book.DoesNotExist:
        error = {
                'message':'failed',
                "errors": f"Book with id {book_id} does not exist"
            }
    
        return Response(error, status=status.HTTP_404_NOT_FOUND)
    
    
    
    if request.method == "GET":
        serializer = BookSerializer(book) 
        data = {
            "message":"success",
            "data" : serializer.data
        } #prepare the response data
        
        
        return Response(data, status=status.HTTP_200_OK) #send the response
    
    elif request.method == "PUT":
        serializer = BookSerializer(book, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            data = {
            "message":"success",
            "data" : serializer.data
            }
            return Response(data, status=status.HTTP_202_ACCEPTED)
        
        
        else:
            error = {
                'message':'failed',
                "errors":serializer.errors
            }
    
            return Response(error, status=status.HTTP_400_BAD_REQUEST) 
        
    elif request.method == 'DELETE':
        book.delete()
        
        return Response({"message":"success"}, status=status.HTTP_204_NO_CONTENT)
    
    
@api_view(['GET'])
def cohort_list(request):
    if request.method=='GET':
        cohorts = Student.objects.values_list('cohort', flat=True).distinct()
        
        data = {cohort:{
            "count":Student.objects.filter(cohort=cohort).count(),
            "data":Student.objects.filter(cohort=cohort).values()
            } 
                
                for cohort in cohorts}
        
        return Response(data, status=status.HTTP_200_OK)