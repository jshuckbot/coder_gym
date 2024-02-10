from django.contrib import admin

from coursesapp.models import Course, Module, Subject


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ["title", "slug"]
    prepopulated_fields = {"slug": ("title",)}  # TODO: Сделать чтобы в менеджере слаг автоматически подключался


class ModuleInline(admin.StackedInline):
    model = Module


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "subject", "created")
    list_filter = ("created", "subject")
    search_fields = ("title", "overview")
    prepopulated_fields = {"slug": ("title",)}
    inlines = (ModuleInline,)
