from django.shortcuts import render, redirect, get_object_or_404
from main.forms import Item_Form
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
import datetime, json
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
import requests

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")
    if filter_type == "all":
        item_list = Product.objects.all()
    else:
        item_list = Product.objects.filter(user=request.user)
    
    context = {
        'npm' : '2406496126',
        'name': request.user.username,
        'class': 'PBP D',
        'item_list': item_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)

@login_required(login_url='/login')
def create_item(request):
    form = Item_Form(request.POST or None, request.FILES or None)
    
    if form.is_valid() and request.method == "POST":
        item_entry = form.save(commit = False)
        item_entry.user = request.user
        item_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_item.html", context)

def show_items(request, id):
    item = get_object_or_404(Product, pk=id)
    item.increment_views()

    context = {
        'item': item
    }

    return render(request, "item_detail.html", context)

#File Type
def show_xml(request):
     item_list = Product.objects.all()
     xml_data = serializers.serialize("xml", item_list)
     return HttpResponse(xml_data, content_type="application/xml")
 
def show_xml_by_id(request, item_id):
    try:
        item_parts = Product.objects.filter(pk=item_id)
        xml_data = serializers.serialize("xml", item_parts)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
       return HttpResponse(status=404)
 
def show_json(request):
    filter_type = request.GET.get("filter", "all")

    if filter_type == "my":
        if request.user.is_authenticated:
            item_list = Product.objects.filter(user=request.user)
        else:
            return JsonResponse({'error': 'User not logged in'}, status=403)
    else:
        item_list = Product.objects.all()

    data = [
        {
            'id': str(item.id),
            'name': item.name,
            'price': item.price,
            'description': item.description,
            'thumbnail': item.thumbnail if item.thumbnail else "",
            'thumbnail_custom': item.thumbnail_custom.url if item.thumbnail_custom else "",
            'created_at': item.created_at.isoformat() if item.created_at else None,
            'updated_at': item.updated_at.isoformat() if item.updated_at else None,
            'category': item.category,
            'category_display': dict(Product.CATEGORY_CHOICES).get(item.category, item.category),
            'is_featured': item.is_featured,
            'is_item_hot': item.is_item_hot,
            'item_views': item.item_views,
            'user': item.user.username if item.user else None,
            'user_id': item.user.id if item.user else None,
        }
        for item in item_list
    ]

    return JsonResponse(data, safe=False)
    
def show_json_by_id(request, item_id):
    try:
        item = Product.objects.select_related('user').get(pk=item_id)
        data = {
            'id': str(item.id),
            'name': item.name,
            'price': item.price,
            'description': item.description,
            'thumbnail': item.thumbnail if item.thumbnail else "",
            'thumbnail_custom': item.thumbnail_custom.url if item.thumbnail_custom else "",
            'created_at': item.created_at.isoformat() if item.created_at else None,
            'updated_at': item.updated_at.isoformat() if item.updated_at else None,
            'category': item.category,
            'category_display': dict(Product.CATEGORY_CHOICES).get(item.category, item.category),
            'is_featured': item.is_featured,
            'is_item_hot': item.is_item_hot,
            'item_views': item.item_views,
            'user_username': item.user.username if item.user else None,
            'user_id': item.user.id if item.user else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)

#Register, login, logout
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created! Welcome customers!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/login')
def edit_item(request, id):
    item = get_object_or_404(Product, pk=id)
    form = Item_Form(request.POST or None, request.FILES or None, instance=item)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_item.html", context)

@login_required(login_url='/login')
def delete_item(request, id):
    item = get_object_or_404(Product, pk=id)
    item.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_item_ajax(request):
    name = strip_tags(request.POST.get("title"))
    price = strip_tags(request.POST.get("price"))
    description = strip_tags(request.POST.get("content"))
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    thumbnail_custom = request.FILES.get("thumbnail_custom")
    is_featured = request.POST.get("is_featured") == 'on'
    user = request.user

    new_item = Product(
        name=name,
        price=price,
        description=description,
        category=category,
        thumbnail=thumbnail if thumbnail else None,
        thumbnail_custom=thumbnail_custom if thumbnail_custom else None,
        is_featured=is_featured,
        user=user
    )
    new_item.save()
    return HttpResponse(b"CREATED", status=201)

@login_required
@require_POST
def update_item_ajax(request, id):
    """
    Menangani update item melalui AJAX dengan aman menggunakan Django Forms.
    """
    try:
        item = Product.objects.get(pk=id, user=request.user)
    except Product.DoesNotExist:
        return JsonResponse({
            'status': 'error', 
            'message': 'Item not found or you are not authorized.'
        }, status=404)
    
    print("POST data:", request.POST)
    print("FILES data:", request.FILES)
    
    name = strip_tags(request.POST.get("title", ""))
    price = request.POST.get("price", "")
    description = strip_tags(request.POST.get("content", ""))
    category = request.POST.get("category", "")
    thumbnail = request.POST.get("thumbnail", "")
    is_featured = request.POST.get("is_featured") == 'on'
    item.name = name if name else item.name
    item.price = price if price else item.price
    item.description = description if description else item.description
    item.category = category if category else item.category
    item.is_featured = is_featured
    
    if thumbnail:
        item.thumbnail = thumbnail
    if 'thumbnail_custom' in request.FILES:
        item.thumbnail_custom = request.FILES['thumbnail_custom']
    
    try:
        item.save()
        return JsonResponse({
            'status': 'success', 
            'message': 'Item updated successfully!'
        })
    except Exception as e:
        print("Error saving item:", str(e))
        return JsonResponse({
            'status': 'error', 
            'message': f'Error saving item: {str(e)}'
        }, status=400)

def login_ajax(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            
            response_data = {
                'status': 'success',
                'message': 'Login successful!',
                'redirect_url': reverse('main:show_main')
            }
            response = JsonResponse(response_data)
            response.set_cookie('last_login', str(datetime.datetime.now()))
            
            return response
        else:
            return JsonResponse({
                'status': 'error',
                'message': 'Invalid username or password. Please try again.'
            }, status=401)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

def register_ajax(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        form = UserCreationForm(data)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'status': 'success',
                'message': 'Account created! You can now log in.',
                'redirect_url': reverse('main:login')
            })
        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

def proxy_image(request):
    image_url = request.GET.get('url')
    if not image_url:
        return HttpResponse('No URL provided', status=400)
    
    try:
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        
        return HttpResponse(
            response.content,
            content_type=response.headers.get('Content-Type', 'image/jpeg')
        )
    except requests.RequestException as e:
        return HttpResponse(f'Error fetching image: {str(e)}', status=500)
    
@csrf_exempt
def create_item_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        name = strip_tags(data.get("name", ""))
        description = strip_tags(data.get("description", ""))
        price = data.get("price", 0)
        category = data.get("category", "")
        thumbnail = data.get("thumbnail", "")
        is_featured = data.get("is_featured", False)

        user = request.user

        new_product = Product(
            name=name,
            description=description,
            price=price,
            category=category,
            thumbnail=thumbnail,
            is_featured=is_featured,
            user=user,
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)

    return JsonResponse({"status": "error"}, status=401)
