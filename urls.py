# Copyright 2014 Rackspace
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.conf.urls import patterns
from django.conf.urls import url

from hotbuilder_horizon import views
import hotbuilder_horizon.api as hotui_api
from hotbuilder_horizon.api import template_validate
from hotbuilder_horizon.api import json_to_yaml
from hotbuilder_horizon.api import yaml_to_json
from hotbuilder_horizon.api import url_to_json

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^api/resource_type_show/'
        r'(?P<region>\w+)/'
        r'(?P<resource_types>(?:\w+::\w+::\w+,?)+)/$',
        hotui_api.resource_type_show, name='resource_type_show'),
    url(r'^api/template_validate/$', hotui_api.template_validate,
        name='template_validate'),
    url(r'^api/json_to_yaml/$', json_to_yaml, name='json_to_yaml'),
    url(r'^api/yaml_to_json/$', yaml_to_json, name='yaml_to_json'),
    url(r'^api/url_to_json/$', url_to_json, name='url_to_json'),
)
