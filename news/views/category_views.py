from rest_framework.generics import ListAPIView
from rest_framework import exceptions
from news.models.flatform import FlatForm
from news.models.category import Category

from news.serializers.category_sz import CategoryListSZ


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSZ

    def get_queryset(self):
        flat_form_name = self.kwargs.get('flatform')
        flat_form_qs = FlatForm.objects.filter(title=flat_form_name)
        if not flat_form_qs.exists():
            raise exceptions.NotFound(detail='flatform not exists')

        return self.queryset.filter(flat_form__title=flat_form_name)
