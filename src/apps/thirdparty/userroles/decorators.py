from django.contrib.auth.decorators import user_passes_test
import pdb

def role_required(*roles):
    """
    Decorator for views that checks whether a user has a particular role,
    redirecting to the log-in page if neccesary.
    Follows same style as django.contrib.auth.decorators.login_required,
    and django.contrib.auth.decorators.permission_required.
    """
    def check_role(user):
        #        pdb.set_trace()
        #return getattr(user, 'role', None) in roles
        #return True
        #return user.role in roles
        if user.role in roles:
            pdb.set_trace()
            return True
        else:
            print user.roles
            pdb.set_trace()
            return False


    return user_passes_test(check_role)
    
