# (c) 2017, Ansible by Red Hat, inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#
import os
import re
import copy
import json
import collections
import q

from ansible import constants as C
from ansible.plugins.action import ActionBase
from ansible.module_utils.network.common.utils import to_list
from ansible.module_utils.six import iteritems, string_types
from ansible.module_utils._text import to_bytes, to_text
from ansible.errors import AnsibleError, AnsibleUndefinedVariable, AnsibleFileNotFound

try:
    from __main__ import display
except ImportError:
    from ansible.utils.display import Display
    display = Display()

def warning(msg):
    if C.ACTION_WARNINGS:
        display.warning(msg)


class ActionModule(ActionBase):

    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = dict()

        result = super(ActionModule, self).run(tmp, task_vars)

        try:
            src = self._task.args.get('src')
            output_file = self._task.args.get('output')
        except KeyError as exc:
            return {'failed': True, 'msg': 'missing required argument: %s' % exc}

        self.facts = {}

        if not os.path.exists(src) and not os.path.isfile(src):
            raise AnsibleError("src is either missing or invalid")

        json_config = self._loader.load_from_file(src)

        #self.ds.update(task_vars)
        
        q(json_config)
        result['ansible_facts'] = self.facts
        return result
