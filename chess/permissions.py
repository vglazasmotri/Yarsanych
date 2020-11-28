from django.http import Http404


class BuyersPermissionsMixin:
    def has_permission(self):
        return self.request.user in self.get_object().buyers.all()

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permission():
            raise Http404()
        return super().dispatch(request, *args, **kwargs)
