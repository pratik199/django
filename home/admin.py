from django.contrib import admin
from home.models import Student
from home.models import Teacher
from home.models import Library
from home.models import Parents
from home.models import Section,Book

# Register your models here.

'''admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Library)
admin.site.register(Parents)
admin.site.register(Section)
admin.site.register(Book)'''

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    search_fields=('student_name','id')
    list_filter=('student_name','id')
    fields=('student_name','department')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    search_fields=('teacher_name','id')
    list_filter=('teacher_name','id')
    fields=('teacher_name',)

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    pass

@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    pass   

@admin.register(Parents)
class ParentsAdmine(admin.ModelAdmin):
    pass
    