from django.views.generic import TemplateView


class UserProfileView(TemplateView):
    template_name = 'user_profile.html'