from django.http import HttpResponse
from voting.models import *
from django.shortcuts import render

# Admin login page
def admin_view(request):
	# render admin login page
	values = request.META.items()
	values.sort()
	html = []
	for k, v in values:
		html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
	return HttpResponse('<table>%s</table>' % '\n'.join(html))

# Homepage for voting
def homepage_view(request):
    return render(request, 'search_form.html')

	# Check if a battle is going on

	# If battle is going on, render links with names of each side, along with
	# a text box to fill in voting string

	# Otherwise, render page saying that no battle is going on

	# return HttpResponse("Home page")