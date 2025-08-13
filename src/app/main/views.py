from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'main/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'Home',
            'description': 'Furniture Store - Home',
        })
        return context


class AboutView(TemplateView):
    template_name = 'main/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'About Us',
            'description': (
                'Welcome to our premium furniture store! We are dedicated to '
                'providing high-quality, stylish furniture that transforms your '
                'house into a home. With years of experience in the furniture '
                'industry, we carefully curate each piece to ensure it meets our '
                'standards of quality, comfort, and design.'
            )
        })
        return context


class DeliveryPaymentView(TemplateView):
    template_name = 'main/delivery_payment.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'Delivery and Payment',
            'description': 'Learn about our delivery options and payment methods.'
        })
        return context


class ContactInfoView(TemplateView):
    template_name = 'main/contact_info.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'Contact Information',
            'description': 'Get in touch with us for any questions or support.'
        })
        return context