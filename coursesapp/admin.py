from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline, GenericTabularInline
from django.contrib.contenttypes.models import ContentType

from coursesapp.models import Content, Course, Module, Subject


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ["title", "slug"]
    prepopulated_fields = {"slug": ("title",)}  # TODO: Сделать чтобы в менеджере слаг автоматически подключался


class ModuleInline(admin.StackedInline):
    model = Module
    extra = 2


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "subject", "created")
    list_filter = ("created", "subject")
    search_fields = ("title", "overview")
    prepopulated_fields = {"slug": ("title",)}
    inlines = (ModuleInline,)


class ContentInline(GenericStackedInline):
    model = Content
    extra = 2


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ("content_view",)
    # inlines = (ContentInline,)

    def content_view(self, obj):
        models = ContentType.objects.get_for_model(obj)
        res = Content.objects.filter(content_type__pk=models.pk, object_id=obj.pk)
        print(res[0].item.title if len(res) > 0 else "-")
        return res[0].item.title if len(res) > 0 else "-"
