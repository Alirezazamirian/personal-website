from django.contrib import admin
from django.contrib.admin.widgets import AdminDateWidget
from django.db import models
from django.contrib.auth.models import Group

from .models import Awards, Education, Experience, CommentBlog, MyBlog, MyOffer, CategoryBlog, Skills, User, \
    SiteSettings, Projects, Services


class AwardsAdmin(admin.ModelAdmin):
    earn_date = {
        models.DateField: {'widget': AdminDateWidget},
    }


admin.site.register(User)
admin.site.register(Awards, AwardsAdmin)
admin.site.unregister(Group)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(CategoryBlog)
admin.site.register(CommentBlog)
admin.site.register(MyBlog)
admin.site.register(MyOffer)
admin.site.register(Skills)
admin.site.register(SiteSettings)
admin.site.register(Projects)
admin.site.register(Services)
