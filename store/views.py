from django.shortcuts import render

from django.views.generic import ListView, DetailView, TemplateView

# product models
from store.models import Category, Product, ProductImages, Banner


class HomeListView(TemplateView):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all().order_by('-id')
        banners = Banner.objects.filter(is_active=True).order_by('-id')[0:3]

        context = {
            'products': products,
            'banners': banners
        }
        return render(request, 'store/index.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == 'post' or request.method == 'POST':
            search_product = request.POST.get('search_product')
            products = Product.objects.filter(name__icontains=search_product).order_by('-id')

            context = {
                'products': products
            }
            return render(request, 'store/index.html', context)



class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/product.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_images'] = ProductImages.objects.filter(product=self.object.id)
        return context


    # item.get_product_url

# def product_details(request, pk):
#     item = Product.objects.get(id=pk)
#     photos = ProductImages.objects.filter(product=item).order_by('-created')
#     context = {
#         'item': item,
#         'photos': photos,
#     }
#     return render(request, 'store/product.html', context)

