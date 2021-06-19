from rest_framework.generics import ListAPIView

from news.models.flatform import FlatForm

from news.serializers.flatform_sz import FlatformListSZ


class FlatFormListView(ListAPIView):
    queryset = FlatForm.objects.all()
    serializer_class = FlatformListSZ
