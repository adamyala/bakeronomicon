from django.contrib import admin

from .models import DryIngredient, FatIngredient, Ingredient, WetIngredient


class FatIngredientInline(admin.StackedInline):
    model = FatIngredient
    extra = 0


class WetIngredientInline(admin.StackedInline):
    model = WetIngredient
    extra = 0


class DryIngredientInline(admin.StackedInline):
    model = DryIngredient
    extra = 0


class IngredientAdmin(admin.ModelAdmin):
    inlines = [WetIngredientInline, FatIngredientInline, DryIngredientInline]


admin.site.register(Ingredient, IngredientAdmin)
