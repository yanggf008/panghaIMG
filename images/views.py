from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Image, Comment
from django.template import loader
from django.urls import reverse
from django.views import generic

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'images/index.html'
    context_object_name = 'latest_image_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Image.objects.order_by('-pub_date')[:15]


class DetailView(generic.DetailView):
    model = Image
    template_name = 'images/detail.html'


class ResultsView(generic.DetailView):
    model = Image
    template_name = 'images/result.html'

def add(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    try:
        new_comment = Comment(image=image, comment_text = request.POST['comment_text'])
        print(request.POST["comment_text"] + "....")
    except (KeyError, Comment.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'image': image,
            'error_message': "You didn't select a choice.",
        })
    else:
        new_comment.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('images:detail', args=(image.id,)))


