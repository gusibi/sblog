from django.shortcuts import render_to_response
from django.http import Http404
from django.http import HttpResponseRedirect
# from django.core.context_processors import csrf
from django.template import RequestContext
# from django.http import HttpResponse
from simpleblog.forms import BlogForm
from simpleblog.models import Blog
from simpleblog.models import Author


def blog_list(request):
    blogs = Blog.objects.order_by('-id')
    return render_to_response("blog_list.html", {"blogs": blogs})


def blog_show(request, id=''):
    try:
        blog = Blog.objects.get(id=id)
        tags = blog.tags.all()
    except Blog.DoesNotExist:
        raise Http404
    url = request.META.get("PATH_INFO")
    return render_to_response("blog_show.html", {"blog": blog, "tags": tags, "url": url}, context_instance=RequestContext(request))


def blog_del(request, id=""):
    try:
        blog = Blog.objects.get(id=id)
    except Exception:
        raise Http404
    if blog:
        blog.delete()
        return HttpResponseRedirect("/smallblog/bloglist/")
    blogs = Blog.objects.all()
    return render_to_response("blog_list.html", {"blogs": blogs})


def blog_add(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            title = cd['caption']
            author = Author.objects.get(id=1)
            content = cd['content']
            blog = Blog(caption=title, author=author, content=content)
            blog.save()
            id = Blog.objects.order_by('-id')[0].id
            return HttpResponseRedirect('/smallblog/blog/%s' % id)
    else:
        form = BlogForm()
    return render_to_response('blog_add.html', {'form': form}, context_instance=RequestContext(request))


def blog_update(request, id=""):
    id = id
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            title = cd['caption']
            content = cd['content']
            blog = Blog.objects.get(id=id)
            if blog:
                blog.caption = title
                blog.content = content
                blog.save()
            else:
                blog = Blog(caption=blog.caption, content=blog.content)
                blog.save()
            return HttpResponseRedirect('/smallblog/blog/%s' % id)
    else:
        try:
            blog = Blog.objects.get(id=id)
        except Exception:
            raise Http404
        form = BlogForm(initial={'caption': blog.caption, 'content': blog.content}, auto_id=False)
    return render_to_response('blog_add.html', {'blog': blog, 'form': form, 'id': id}, context_instance=RequestContext(request))
