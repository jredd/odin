from django.conf.urls import patterns, url
from views import ProjectList, ProjectDetail


urlpatterns = patterns('',
    url(r'^project-list/$', ProjectList.as_view(), name='project_list'),
    url(r'^project-detail/(?P<pk>[0-9]+)/$', ProjectDetail.as_view(), name='project_list'),
    #url(r'blast-requests-list/$', BlastRequestsList.as_view(), name='job_list'),

)