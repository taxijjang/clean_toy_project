from django.urls import path

from news.views.flatform_views import FlatFormListView
from news.views.category_views import CategoryListView

from news.views.story_views import StoryListView

urlpatterns = [
    # flat_form
    path('flatforms', FlatFormListView.as_view()),

    # category
    path('<flatform>/categories', CategoryListView.as_view()),

    # story
    path('<flatform>/<category>/stories', StoryListView.as_view()),

]