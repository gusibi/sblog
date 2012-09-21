from django.shortcuts import render_to_response
from django.http import Http404
from django.http import HttpResponseRedirect
# from django.core.context_processors import csrf
from django.template import RequestContext
# from django.http import HttpResponse
from django.contrib.comments import get_delete_url
from simpleblog.forms import BlogForm
from simpleblog.forms import TagForm
from simpleblog.models import Blog
from simpleblog.models import Author
from simpleblog.models import Tag


def blog_list(request):
    blogs = Blog.objects.order_by('-id')
    return render_to_response("blog_list.html", {"blogs": blogs})


def blog_show(request, id=''):
    try:
        blog = Blog.objects.get(id=id)
        tags = blog.tags.all()
    except Blog.DoesNotExist:
        raise Http404
    return render_to_response("blog_show.html",
        {"blog": blog, "tags": tags},
        context_instance=RequestContext(request))


def blog_add_comment(request, id=''):
    blog = Blog.objects.get(id=id)
    return render_to_response('blog_add_comments.html',
            {"blog": blog},
            context_instance=RequestContext(request))


def blog_show_comment(request, id=''):
    blog = Blog.objects.get(id=id)
    de = get_delete_url
    return render_to_response('blog_comments_show.html', {"blog": blog, "de": de})


def blog_del(request, id=""):
    try:
        blog = Blog.objects.get(id=id)
    except Exception:
        raise Http404
    if blog:
        blog.delete()
        return HttpResponseRedirect("/simpleblog/bloglist/")
    blogs = Blog.objects.all()
    return render_to_response("blog_list.html", {"blogs": blogs})


def blog_add(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        tag = TagForm(request.POST)
        if form.is_valid() and tag.is_valid():
            cd = form.cleaned_data
            cdtag = tag.cleaned_data
            tagname = cdtag['tag_name']
            for taglist in tagname.split():
                Tag.objects.get_or_create(tag_name=taglist.strip())
            title = cd['caption']
            author = Author.objects.get(id=1)
            content = cd['content']
            blog = Blog(caption=title, author=author, content=content)
            blog.save()
            for taglist in tagname.split():
                blog.tags.add(Tag.objects.get(tag_name=taglist.strip()))
                blog.save()
            id = Blog.objects.order_by('-id')[0].id
            return HttpResponseRedirect('/simpleblog/blog/%s' % id)
    else:
        form = BlogForm()
        tag = TagForm()
    return render_to_response('blog_add.html', {'form': form, 'tag': tag}, context_instance=RequestContext(request))


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
            return HttpResponseRedirect('/simpleblog/blog/%s' % id)
    else:
        try:
            blog = Blog.objects.get(id=id)
        except Exception:
            raise Http404
        form = BlogForm(initial={'caption': blog.caption, 'content': blog.content}, auto_id=False)
    return render_to_response('blog_add.html', {'blog': blog, 'form': form, 'id': id}, context_instance=RequestContext(request))
