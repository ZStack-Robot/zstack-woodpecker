'''

@author: Frank
'''

import os
import zstackwoodpecker.setup_actions as setup_actions
import zstackwoodpecker.operations.deploy_operations as deploy_operations
import zstackwoodpecker.operations.config_operations as config_operations
import zstackwoodpecker.test_lib as test_lib
import zstackwoodpecker.test_util as test_util

USER_PATH = os.path.expanduser('~')
EXTRA_SUITE_SETUP_SCRIPT = '%s/.zstackwoodpecker/extra_suite_setup_config.sh' % USER_PATH
def test():
    setup = setup_actions.SetupAction()
    setup.plan = test_lib.all_config
    setup.run()

    if os.path.exists(EXTRA_SUITE_SETUP_SCRIPT):
        os.system("bash %s" % EXTRA_SUITE_SETUP_SCRIPT)
    deploy_operations.deploy_initial_database(test_lib.deploy_config)
    delete_policy = test_lib.lib_set_delete_policy('vm', 'Direct')
    delete_policy = test_lib.lib_set_delete_policy('volume', 'Direct')
    delete_policy = test_lib.lib_set_delete_policy('image', 'Direct')
    if test_lib.lib_get_ha_selffencer_maxattempts() != None:
	test_lib.lib_set_ha_selffencer_maxattempts('60')
	test_lib.lib_set_ha_selffencer_storagechecker_timeout('60')
    test_lib.lib_set_primary_storage_imagecache_gc_interval(1)
    test_util.test_pass('Suite Setup Success')

