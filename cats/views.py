from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets
from django.shortcuts import get_object_or_404


from .models import Cat
from .serializers import CatSerializer


@api_view(['GET', 'POST'])
def cat_list(request):
    """Представление обрабатывает методы POST и GET (Все объекты)."""
    if request.method == 'POST':
        serializer = CatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    cats = Cat.objects.all()
    serializer = CatSerializer(cats, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PATCH', 'PUT', 'DELETE'])
def cat_detail(request, pk):
    """Представление обрабатывает методы:

    PUT,
    PATCH,
    DELETE,
    GET (Один объект).
    """
    cat = get_object_or_404(Cat, id=pk)
    if request.method == 'PUT' or request.method == 'PATCH':
        serializer = CatSerializer(cat, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    serializer = CatSerializer(cat)
    return Response(serializer.data)


class CatAPIView(APIView):
    """Класс реализует методы POST и GET (Все объекты)."""

    def get(self, request):
        cats = Cat.objects.all()
        serializer = CatSerializer(cats, many=True)
        return Response(serializer.data)

    def post(self, request):
        serialize = CatSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)


class CatAPIDetail(APIView):
    """Класс реализует методы PUT, PATCH, DELETE и GET (Один объект)."""

    def get(self,request, pk):
        """"""
        cat = get_object_or_404(Cat, id=pk)
        serializer = CatSerializer(cat)
        return Response(serializer.data)

    def put(self, request, pk):
        """"""
        cat = get_object_or_404(Cat, id=pk)
        serializer = CatSerializer(cat, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        """"""
        cat = get_object_or_404(Cat, id=pk)
        serializer = CatSerializer(cat, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """"""
        cat = get_object_or_404(Cat, id=pk)
        cat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CatList(generics.ListCreateAPIView):
    """Класс реализует методы POST и GET (Все объекты)."""
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class CatDetail(generics.RetrieveUpdateDestroyAPIView):
    """Класс реализует методы PUT, PATCH, DELETE и GET (Один объект)."""
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class CatViewSet(viewsets.ModelViewSet):
    """Класс реализует полный CRUD."""

    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class CatReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    """Класс реализует только доступ к данным.

    Изменять данные не может
    """

    queryset = Cat.objects.all()
    serializer_class = CatSerializer



