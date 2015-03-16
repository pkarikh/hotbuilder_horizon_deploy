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

import httplib2
import json
import yaml

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import openstack_dashboard.api.heat as heat_api
import hotbuilder_horizon.common.api.heat_api as hotui_api


def get_template_from_url(url):
    '''Helper function to retrieve heat template content from a given url.'''

    h = httplib2.Http(disable_ssl_certificate_validation=True)
    resp, content = h.request(
        uri=url,
        method='GET',
    )

    return content

def template_validate(request):
    endpoint = request.POST.get("endpoint")

    kwargs = {}

    template_url = request.POST.get("url")
    template = request.POST.get("template")

    if template_url is not None:
        kwargs["template_url"] = template_url

    if template is not None:
        kwargs["template"] = json.loads(template)

    try:
        validate = hotui_api.template_validate(request, endpoint, **kwargs)
        return HttpResponse(json.dumps(validate),
                            content_type="application/json")
    except Exception as e:
        return HttpResponse(str(e),
                            content_type="text/html")

def resource_type_show(request, region, resource_types):
    type_show_info = {t: heat_api.resource_type_get(request, t) for t in
                      resource_types.split(',')}
    return HttpResponse(json.dumps(type_show_info),
                        content_type="application/json")

@csrf_exempt
def json_to_yaml(request):
    print "asdf"
    return HttpResponse(hotui_api.json_to_yaml(request.POST['json']),
                        content_type="text/html") 

@csrf_exempt
def yaml_to_json(request):
    return HttpResponse(hotui_api.yaml_to_json(request.POST['yaml']),
                        content_type="application/json")

def url_to_json(request):
    try:
        template = get_template_from_url(request.GET.get('url'))
        return HttpResponse(hotui_api.yaml_to_json(template),
                            content_type="application/json")
    except Exception as e:
        return HttpResponse(str(e), content_type="text/html")
