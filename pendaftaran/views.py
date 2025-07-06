from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Hotel
from .forms import HotelForm

# ======== AUTHENTICATION ========

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        if user:
            login(request, user)
            return redirect('/dashboard/')
        else:
            return render(request, 'login.html', {'error': 'Username atau password salah'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('/')

# ======== HALAMAN UTAMA ========

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def tentang(request):
    return render(request, 'tentang.html')

@login_required
def chat(request):
    return render(request, 'chat.html')

# ======== FITUR CRUD HOTEL ========

@login_required
def index(request):
    q = request.GET.get('q', '')
    sort = request.GET.get('sort', 'nama')
    hotels = Hotel.objects.all()

    if q:
        hotels = hotels.filter(nama__icontains=q)

    valid_sort_fields = ['nama', 'kamar', 'harga', 'lama_inap']
    if sort.replace('-', '') in valid_sort_fields:
        hotels = hotels.order_by(sort)

    paginator = Paginator(hotels, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    columns = [
        ('nama', 'Nama'),
        ('kamar', 'Kamar'),
        ('harga', 'Harga'),
        ('lama_inap', 'Lama')
    ]

    return render(request, 'hotel/index.html', {
        'hotels': page_obj,
        'q': q,
        'sort': sort,
        'columns': columns,
        'page_obj': page_obj,
    })

@login_required
def tambah(request):
    form = HotelForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('/hotel/')
    return render(request, 'hotel/form.html', {'form': form, 'judul': 'Tambah Data'})

@login_required
def edit(request, id):
    hotel = get_object_or_404(Hotel, pk=id)
    form = HotelForm(request.POST or None, instance=hotel)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('/hotel/')
    return render(request, 'hotel/form.html', {'form': form, 'judul': 'Edit Data'})

@login_required
def hapus(request, id):
    hotel = get_object_or_404(Hotel, pk=id)
    hotel.delete()
    return redirect('/hotel/')
