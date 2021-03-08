from django.contrib import admin

from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    save_as = True
    print(1)


admin.site.register(Post, PostAdmin)
