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

import yaml
import json

from django.views.generic import TemplateView
import openstack_dashboard.api.heat as heat_api
from openstack_dashboard.api import base


#from heat.common.region import get_regions

class IndexView(TemplateView):
    template_name = 'hotui.html'

    def get_context_data(self, **kwargs):
        resource_names = [r.resource_type for r in
                          heat_api.resource_types_list(self.request)]
        context = {}
        context['resource_names'] = json.dumps(resource_names)
        context['region_value'] = 'region'

        return context
