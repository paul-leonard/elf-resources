from django.urls import path
from .views import ElfListView

urlpatterns = [
  path('', ElfListView.as_view(), name='elf_list')
]