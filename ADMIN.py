from django.contrib import admin

# Register your models here.
from .models import physics_note
from .models import chemistry_note
from .models import Math1_note
from .models import Math2_note
from .models import electronics_note
from .models import basic_electrical_note
from .models import mechanical_note
from .models import Soft_skill_note
from .models import AI_note
from .models import Emerging_Technology_note
from .models import PPS_note


admin.site.register(physics_note)
admin.site.register(chemistry_note)
admin.site.register(Math1_note)
admin.site.register(Math2_note)
admin.site.register(electronics_note)
admin.site.register(basic_electrical_note)
admin.site.register(mechanical_note)
admin.site.register(AI_note)
admin.site.register(Emerging_Technology_note)
admin.site.register(PPS_note)
admin.site.register(Soft_skill_note)
