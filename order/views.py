from django.shortcuts import render, get_object_or_404, redirect

from store.models import Product
from order.models import Cart, Order

from coupon.forms import CouponCodeForm
from coupon.models import Coupon

from django.utils import timezone


def add_to_cart(request, pk):
    if request.user.is_authenticated:
        item = get_object_or_404(Product, pk=pk)
        order_item = Cart.objects.get_or_create(item=item, user=request.user, purchased=False)
        order_qs = Order.objects.filter(user=request.user, ordered=False)
        if order_qs.exists():
            order = order_qs[0]
            if order.orderitems.filter(item=item).exists():
                size = request.POST.get('size')
                color = request.POST.get('color')
                quantity = request.POST.get('quantity')
                if quantity:
                    order_item[0].quantity += int(quantity)
                else:
                    order_item[0].quantity += 1
                order_item[0].size = size
                order_item[0].color = color
                order_item[0].save()
                return redirect('store:index')
            else:
                size = request.POST.get('size')
                color = request.POST.get('color')
                order_item[0].size = size
                order_item[0].color = color
                order.orderitems.add(order_item[0])
                return redirect('store:index')
        else:
            order = Order(user=request.user)
            order.save()
            order.orderitems.add(order_item[0])
            return redirect('store:index')
    else:
        return redirect('account:login')


def cart_view(request):
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, purchased=False)
        orders = Order.objects.filter(user=request.user, ordered=False)
        if carts.exists() and orders.exists():
            order = orders[0]
            coupon_form = CouponCodeForm(request.POST)
            if coupon_form.is_valid():
                current_time = timezone.now()
                code = coupon_form.cleaned_data.get('code')
                coupon_obj = Coupon.objects.get(code=code, active=True)
                if coupon_obj.valid_to >= current_time:
                    get_discount = (coupon_obj.discount / 100) * order.get_totals()
                    total_price_after_discount = order.get_totals() - get_discount
                    request.session['discount_total'] = total_price_after_discount
                    request.session['coupon_code'] = code
                    return redirect('order:cart')
                else:
                    coupon_obj.active = False
                    coupon_obj.save()
                    return redirect('order:cart')

            total_price_after_discount = request.session.get('discount_total')
            coupon_code = request.session.get('coupon_code')
            context = {
                'carts': carts,
                'order': order,
                'coupon_form': coupon_form,
                'coupon_code': coupon_code,
                'total_price_after_discount': total_price_after_discount
            }
            return  render(request, 'store/cart.html', context)
    else:
        return redirect('account:login')


def remove_item_from_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    orders = Order.objects.filter(user=request.user, ordered=False)
    if orders.exists():
        order = orders[0]
        if order.orderitems.filter(item=item).exists():
            order_item = Cart.objects.filter(item=item, user=request.user, purchased=False)[0]
            order.orderitems.remove(order_item)
            order_item.delete()
            return redirect('order:cart')
        else:
            return redirect('order:cart')
    else:
        return redirect('order:cart')



def increase_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item = Cart.objects.filter(item=item, user=request.user, purchased=False)[0]
            if order_item.quantity >= 1:
                order_item.quantity += 1
                order_item.save()
                return redirect('order:cart')
        else:
            return redirect('store:index')
    else:
        return redirect('store:index')


def decrease_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item = Cart.objects.filter(item=item, user=request.user, purchased=False)[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
                return redirect("order:cart")
            else:
                order.orderitems.remove(order_item)
                order_item.delete()
                return redirect('store:index')
        else:
            return redirect('store:index')
    else:
        return redirect('store:index')









