from django.contrib import admin
from .models import MyInfo
from .models import Education
from .models import Experience
from .models import Interest
from .models import Skills
from .models import Awards

# Register your models here.
admin.site.register(MyInfo)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Interest)
admin.site.register(Skills)
admin.site.register(Awards)