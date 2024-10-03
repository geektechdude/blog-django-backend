from django.contrib import admin
from blog.models import Post, Profile, Tag

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag

@admin.register(Post)
class PostAdmin(admin.Model.Admin):
    model = Post

    list_display = (
        "id",
        "title",
        "subitle",
        "slug",
        "publish_date",
        "published",
    )
    list_filter = (
        "published",
        "publish_date",
    )
    list_editable = (
        "title",
        "subtitle",
        "slug",
        "publish_date",
        "published",
    )
    search_fields = (
        "title",
        "subtitle",
        "slug",
        "publish_date",
        "published",
    )
    prepopulated_fields = {
        "slug": {
            "title",
            "subtitle",
        }
    }
    date_hierachy = "publish_date"
    save_on_top = True