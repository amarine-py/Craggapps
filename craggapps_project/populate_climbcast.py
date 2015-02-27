import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'craggapps_project.settings')
import django
django.setup()

from climbcast.models import User

def populate():
    jabba_user = User.objects.get_or_create(username='jabba', first_name='Jack',
                          last_name='Johnson', user_email='jabba@fake.net',
                          user_password='jabbajohn')[0]
    jabba_user.save()

    luke_user = User.objects.get_or_create(username='luke', first_name='Luke',
                         last_name='Skywalker', user_email='theforce@astro.com',
                         user_password='lukeboyee')[0]
    luke_user.save()

    chewy_user = User.objects.get_or_create(username='chewy', first_name='Chewbacca',
                          last_name='Bigfoot', user_email='chewy@falcon.org',
                          user_password='chewyloveshan')[0]
    chewy_user.save()

    boba_user = User.objects.get_or_create(username='boba', first_name='Boba',
                         last_name='Fett', user_email='bobafett@lasergun.net',
                         user_password='murderbydeath')[0]
    boba_user.save()

    for u in User.objects.all():
        for attr, value in u.__dict__.iteritems():
            print "{}: {}".format(str(attr), str(value))

if __name__ == '__main__':
    print "Starting ClimbCast population script..."
    populate()


            
            
    
