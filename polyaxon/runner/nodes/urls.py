from rest_framework.urlpatterns import format_suffix_patterns

from django.urls import re_path

from libs.urls import INDEX_PATTERN, SEQUENCE_PATTERN
from runner.nodes import views

cluster_nodes_urlpatterns = [
    re_path(r'^cluster/nodes/?$',
            views.ClusterNodeListView.as_view()),
    re_path(r'^nodes/{}/?$'.format(SEQUENCE_PATTERN),
            views.ClusterNodeDetailView.as_view()),
    re_path(r'^nodes/{}/gpus/?$'.format(SEQUENCE_PATTERN),
            views.ClusterNodeGPUListView.as_view()),
    re_path(r'^nodes/{}/gpus/{}/?$'.format(SEQUENCE_PATTERN, INDEX_PATTERN),
            views.ClusterNodeGPUDetailView.as_view()),
]

urlpatterns = format_suffix_patterns(cluster_nodes_urlpatterns)
