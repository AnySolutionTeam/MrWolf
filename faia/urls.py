from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import landing.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", landing.views.index, name="index"),
    path("about/", landing.views.about, name="about"),
    path("contact/", landing.views.contact, name="contact"),
    path("facts/", landing.views.facts, name="facts"),
    path("feature/", landing.views.feature, name="feature"),
    path("project/", landing.views.project, name="project"),
    path("service/", landing.views.service, name="service"),
    path("team/", landing.views.team, name="team"),
    path("terms/", landing.views.terms, name="terms"),
    path("testimonial/", landing.views.testimonial, name="testimonial"),
    path("404/", landing.views.error_404, name="error_404"),
    path("support/", landing.views.support, name="support"),
    #path("db/", landing.views.db, name="db"),
    #path("admin/", admin.site.urls),
    path('', include('accounts.urls')),
]

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
