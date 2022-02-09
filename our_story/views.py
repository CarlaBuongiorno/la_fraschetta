from django.shortcuts import render


def our_story(request):
    """ A view to return the about page """
    return render(request, 'our_story/our_story.html')
