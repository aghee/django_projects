from django.contrib import admin
from .models import Category,Product,ProductLine,ProductImage,ProductType,Attribute,AttributeValue,SeasonalEvent


class ChildCategoryInline(admin.TabularInline):
    model=Category
    fk_name="parent"
    extra=1

class ParentCategoryAdmin(admin.ModelAdmin):
    inlines=[ChildCategoryInline]
    list_display=["name","parent_name"]

    def parent_name(self,obj):
        return obj.parent.name if obj.parent else None

admin.site.register(Category,ParentCategoryAdmin)

class ChildTypeInline(admin.TabularInline):
    model=ProductType
    fk_name="parent"
    extra=1

class ParentTypeAdmin(admin.ModelAdmin):
    inlines=[ChildTypeInline]

admin.site.register(ProductType,ParentTypeAdmin)

class AttributeValueInline(admin.TabularInline):
    model=AttributeValue
    extra=1

class AttributeAdmin(admin.ModelAdmin):
    inlines=[AttributeValueInline]

admin.site.register(Attribute,AttributeAdmin)

class SeasonalEventAdmin(admin.ModelAdmin):
    list_display=("name","start_date","end_date")

admin.site.register(SeasonalEvent,SeasonalEventAdmin)


class ProductImageInline(admin.StackedInline):
    model=ProductImage
    extra=1

class ProductLineInline(admin.StackedInline):
    model=ProductLine
    inlines=[ProductImageInline]
    extra=1

class ProductAdmin(admin.ModelAdmin):
    inlines=[ProductLineInline]
    list_display=("name","category","stock_status","is_active",)
    list_filter=("category","stock_status","is_active",)
    search_fields=("name",)

admin.site.register(Product,ProductAdmin)
admin.site.register(ProductLine)



























# Register your models here.
'''
#extend features of admin site
class  CategoryAdmin(admin.ModelAdmin):
#     prepopulated_fields={'slug':("name",)}
    list_display=["id","name","is_active"]
    search_fields=["name","slug"]#provide a search feature in the category area in django admin
    list_display_links=("id",)
    list_editable=("name",)

class  ProductAdmin(admin.ModelAdmin):
    list_filter=("stock_status",)

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(ProductLine)
admin.site.register(ProductImage)
admin.site.register(ProductType)

'''




