from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """
    Admin setting to display line of items for each order
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """
    Admin setting to display order information with
    inline display for Order Line
    """
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'order_date',
                       'delivery_cost', 'subtotal',
                       'grand_total', 'original_bag',
                       'stripe_pid')

    fields = ('order_number', 'user_profile', 'order_date', 'full_name',
              'email', 'delivery_country', 'delivery_postcode',
              'delivery_town_or_city', 'delivery_street_address1',
              'delivery_street_address2', 'delivery_cost', 'subtotal',
              'grand_total', 'original_bag', 'stripe_pid')

    list_display = ('order_number', 'order_date', 'full_name',
                    'subtotal', 'delivery_cost',
                    'grand_total',)

    ordering = ('-order_date',)


admin.site.register(Order, OrderAdmin)
