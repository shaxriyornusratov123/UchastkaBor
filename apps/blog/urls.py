from django.urls import path

from apps.blog.views import BlogListView, BlogSingleView
# from apps.blog.apis import BlogPostListAPIView, BlogPostDetailAPIView


urlpatterns = [
    path("posts/", BlogListView.as_view(), name="blogs"),
    path("posts/<slug:slug>/", BlogSingleView.as_view(), name="blog-single"),

    # path("api/posts/", BlogPostListAPIView.as_view(), name="api-blogs"),
    # path("api/post/<int:pk>/", BlogPostDetailAPIView.as_view(), name="api-blog-single"),
]