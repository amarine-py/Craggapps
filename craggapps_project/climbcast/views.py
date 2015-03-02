from django.shortcuts import render
from django.http import HttpResponse
from climbcast.models import CraggUser, CraggArea
from climbcast.forms import CraggUserForm, CraggAreaForm

# Create your views here.

def index(request):
    # Query the database for a list of ALL users currently stored.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    user_list = CraggUser.objects.all()[:5]
    context_dict = {'users': user_list}

    area_list = CraggArea.objects.all()[:5]
    context_dict['areas'] = area_list

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'climbcast/index.html', context_dict)

def about(request):
    return HttpResponse("This is the default about view for CraggApps\ClimbCast")

def cragguser(request, user_name_slug):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a username slug with the given username?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        users = CraggUser.objects.get(slug=user_name_slug)
        context_dict['user_name'] = users.username

        # Retrieve THE ASSOCIATED AREAS IN THE FUTRE. For now, attributes.
        user_area_list = users.craggarea_set.all()

        # Note that filter returns >= 1 model instance.
        u_e = users.user_email
        f_n = users.first_name
        l_n = users.last_name

        # Add the variables into the context dictionary.
        context_dict['email_address'] = u_e
        context_dict['first_name'] = f_n
        context_dict['last_name'] = l_n
        context_dict['user_areas'] = user_area_list
        
        # Also add the user object from the database.
        # We will use this in the template to verify that the user exists.
        context_dict['cragguser'] = users

    except CraggUser.DoesNotExist:
        # If user doesn't exist...
        # Don't do anything - the template displays the "no user" message for us.
        pass

    return render(request, 'climbcast/cragguser.html', context_dict)

def craggarea(request, area_name_slug):

    #Create a context dictionary that we can pass to template rendering engine
    context_dict = {}

    try:
        # Can we find a username slug with the given area name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        areas = CraggArea.objects.get(slug=area_name_slug)
        context_dict['area_name'] = areas.area_name

        # Note that filter returns >= 1 model instance.
        a_c = areas.area_city
        a_s = areas.area_state

        # Add variables into context dictionary.
        context_dict['area_city'] = a_c
        context_dict['area_state'] = a_s
        # Also add the area object from the database.
        # We will use this in teh template to verify that the user exists.
        context_dict['craggarea'] = areas

    except CraggArea.DoesNotExist:
        # If area doesn't exist...
        # Let the template handle it with a "no area" message.
        pass

    return render (request, 'climbcast/craggarea.html', context_dict)

def add_cragg_user(request):
    # An HTTP POST?
    if request.method == 'POST':
        form = CraggUserForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to database.
            form.save(commit=True)
            

            #Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained erros - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = CraggUserForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'climbcast/add_cragg_user.html', {'form': form})
