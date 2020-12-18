from django.views.generic import ListView
from .models import Elf

class ElfListView(ListView):
  template_name = "elves/elf-list.html"
  model = Elf