from django.contrib import admin
from .models import Post

# モデルをAdminページ（管理画面）上で見えるようにするため、admin.site.register(Post)でモデルを登録する必要があります。
admin.site.register(Post)
