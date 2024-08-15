# for the frontend


from django.shortcuts import render
from django.views.generic import TemplateView,View
from .forms import UserRegisterForm
from django.contrib.auth import authenticate,login,logout
from .forms import UserRegisterForm
from django.shortcuts import redirect
from .models import Product

class Index(TemplateView):
    template_name = "index.html"

class Dashboard(View):
    def get(self,request):
        items=Product.objects.filter(user=self.request.user.id).order_by('id')
        return render(request,'dashboard.html',{'items': items})

class SignUpView(View):
    def get(self,request):
        form =UserRegisterForm()
        return render(request,'signup.html',{'form':form})
    
    def post(self,request):
        form=UserRegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            user=authenticate(
                
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
            )
            login(request,user)
            return redirect('index')
        return render(request,'signup.html',{'form':form})

def logout_user(request):
    logout(request)
    
    return render(request,'logout.html',{})


    



        
 #for api   
from .models import Category,Product
from .serializers import CategorySerializer,ProductSerializer
from django_filters import rest_framework as filters
from .pagination import CustomPagination
from rest_framework.viewsets import (ModelViewSet, ReadOnlyModelViewSet,)
from .filters import ProductFilter
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from .permissions import IsAdmin


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes=(IsAuthenticatedOrReadOnly,)
    
class ProductViewSet(ModelViewSet):
    pagination_class=CustomPagination
    queryset= Product.objects.select_related('category').all()
    serializer_class=ProductSerializer
    filter_backends=(filters.DjangoFilterBackend,)
    filterset_class=ProductFilter
    permission_classes=(IsAuthenticatedOrReadOnly,IsAdmin,)
    

