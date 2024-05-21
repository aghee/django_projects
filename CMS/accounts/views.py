from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import Order,Product,Customer
from .forms import OrderForm,CustomerForm
from .filters import OrderFilter


# Create your views here.
def home(request):
    customers=Customer.objects.order_by('-id')[:5]
    # customers=Customer.objects.all()
    orders=Order.objects.order_by('-id')[:5]
    orders1=Order.objects.all()
    delivered=orders1.filter(status="Delivered").count()
    pending=orders1.filter(status="Pending").count()
    total_orders=orders1.count()
    
    # no_of_orders=orders.filter(customer=customers.id)

    context={
        "customers1":customers,
        "orders":orders,
        "total_customers":customers.count(),
        "delivered":delivered,
        "pending":pending,
        "total_orders":total_orders

        # "latest_five_items":orders[:5]
    }
    # count=0
    # for cust in customers:
    #     count+=1
    # context={
    #     "count":count
    # }
    return render(request,"accounts/dashboard.html",context)
    

def product(request):
    product1=Product.objects.all()
    context={
        "products":product1
    }
    return render(request,"accounts/products.html",context)

def customer(request,pk):
    customer=Customer.objects.get(id=pk)
    orders=customer.order_set.all()
    total_cust_orders=orders.count()
    myFilter=OrderFilter(request.GET,queryset=orders)
    orders=myFilter.qs

    context={
        "customer":customer,
        "orders":orders,
        "total_cust_orders":total_cust_orders,
        "myFilter":myFilter
    }
    return render(request,"accounts/customers.html",context)

def status_count(request):
    total_orders=Order.objects.filter(status="Pending")
    total_orders1=Order.objects.filter(status="Delivered")
    total_orders2=Order.objects.all()
    
    # count=0
    # for ord in total_orders:
    #     count+=1
    final_count={
        "orders_count":total_orders.count(),
        "orders_count1":total_orders1.count(),
        "orders_count2":total_orders2.count()
    }

    # item_list={}

    # for item in total_orders:
    #     if item in item_list:
    #         item_list[item]+=1
    #     else:
    #         item_list[item]=1
    # print(item_list)


    return render(request,"accounts/status.html",final_count)

def create_order(request,pk):
    OrderFormSet=inlineformset_factory(Customer,Order,fields=('product','status'),extra=5)#form accepting multiple items/orders
    customer=Customer.objects.get(id=pk)
    formset=OrderFormSet(queryset=Order.objects.none(),instance=customer)
    # form=OrderForm(initial={"customer":customer})
    # form=OrderForm()
    if request.method=="POST":
        # print("PRINTING",request.POST)
        # form=OrderForm(request.POST)
        formset=OrderFormSet(request.POST,instance=customer) #bound form coz it has arguments passed in it
        if formset.is_valid():
            formset.save()
            return redirect("/")

    context={
        "formset":formset,
             }
    return render(request,"accounts/order_form.html",context)

def update_order(request,pk):
    # if request.method=="POST":
        # print("PRINTING",request.POST)
    order=Order.objects.get(id=pk)
    form=OrderForm(instance=order) #bound form coz it has arguments passed in it
    if request.method=="POST":
        form=OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect("/")
    context={
        "form":form
    }
    return render (request,"accounts/order_form.html",context)

def delete_order(request,pk):
    order=Order.objects.get(id=pk)
    # prod_name=order.product
    if request.method =="POST":
        order.delete()
        return redirect ("/")
    context={
        "prod_name":order
    }

    return render (request,"accounts/delete_ord.html",context)

def create_customer(request):
    form=CustomerForm()
    if request.method =="POST":
        form=CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context={
        "form":form
    }
    return render(request,"accounts/customer_form.html",context)


def update_customer(request,pk):
    cust_to_update=Customer.objects.get(id=pk)
    # print(cust_to_update)
    form=CustomerForm(instance=cust_to_update)
    if request.method=="POST":
        form=CustomerForm(request.POST,instance=cust_to_update)
        if form.is_valid():
            form.save()
            return redirect("/")
    context={
        "form":form,
    }
    return render(request,"accounts/customer_form.html",context)


def delete_customer(request,pk):
    cust_to_delete=Customer.objects.get(id=pk)
    if request.method =="POST":
        cust_to_delete.delete()
        return redirect("/")
    context={
        "cust_to_delete":cust_to_delete
    }
    return render(request,"accounts/del_customer.html",context)

# def userpage(request):
#     context={

#     }
#     return render(request,"accounts/user.html",context)

def registerpage(request):
    context={

    }
    return render(request,"accounts/register.html",context)

def loginpage(request):
    context={

    }
    return render(request,"accounts/login.html",context)



