from django.contrib import admin

from measurements import models as measurement_model

from .models import Recipe, RecipeVersion


class IngredientMeasurementInline(admin.TabularInline):
    model = measurement_model.IngredientMeasurement


class RecipeVersionAdmin(admin.ModelAdmin):
    inlines = [IngredientMeasurementInline]


admin.site.register(model_or_iterable=Recipe, admin_class=admin.ModelAdmin)
admin.site.register(model_or_iterable=RecipeVersion, admin_class=RecipeVersionAdmin)
