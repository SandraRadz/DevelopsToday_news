from django.contrib import admin

from news.models import Comment, NewPost


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


class NewPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_name', 'creation_date')
    list_filter = ('creation_date',)
    readonly_fields = ('upvotes_amount',)
    inlines = [CommentInline]


admin.site.register(NewPost, NewPostAdmin)

