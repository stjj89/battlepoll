from django.http import HttpResponse
from voting.models import *

# Admin login page
def admin_view(request):
	# render admin login page
	return HttpResponse("Admin page")

# Homepage for voting
def homepage_view(request):
	# Check if a battle is going on

	# If battle is going on, render links with names of each side, along with
	# a text box to fill in voting string

	# Otherwise, render page saying that no battle is going on

	return HttpResponse("Home page")