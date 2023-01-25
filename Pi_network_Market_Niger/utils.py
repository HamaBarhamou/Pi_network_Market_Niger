from functools import wraps
from django.http import HttpResponseRedirect


def authors_vendor(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):
        """ accepter la vue uniquement pour les vendeurs """
        print("request.user.fonction: ",request.user.fonction)
        if request.user.fonction == 2 or request.user.fonction is None:
             return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/')

  return wrap
