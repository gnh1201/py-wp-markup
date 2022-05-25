# plugin.py

def add_filter(hook_name, callback, priority = 10, accepted_args = 1):
    pass

def apply_filters(hook_name, value, *args):
    pass

def apply_filters_ref_array(hook_name, args):
    pass

def has_filter(hook_name, callback = False):
    pass

def remove_filter(hook_name, callback, priority = 10):
    pass

def remove_all_filters(hook_name, priority = False):
    pass

def current_filter():
    pass

def doing_filter(hook_name = null):
    pass

def add_action(hook_name, callback, priority = 10, accepted_args = 1):
    pass

def do_action(hook_name, *args):
    pass

def do_action_ref_array(hook_name, args):
    pass

def has_action(hook_name, callback = False):
    pass

def remove_action(hook_name, callback, priority = 10):
    pass

def remove_all_actions(hook_name, priority = False):
    pass

def current_action():
    pass

def doing_action(hook_name = null):
    pass

def did_action(hook_name):
    pass

def apply_filters_deprecated(hook_name, args, version, replacement = '', message = ''):
    pass

def do_action_deprecated(hook_name, args, version, replacement = '', message = ''):
    pass

def plugin_basename(file):
    pass

def wp_register_plugin_realpath(file):
    pass

def plugin_dir_path(file):
    pass

def plugin_dir_url(file):
    pass

def register_activation_hook(file, callback):
    pass

def register_deactivation_hook(file, callback):
    pass

def register_uninstall_hook(file, callback):
    pass
	
def _wp_call_all_hook(args):
    pass
	
def _wp_filter_build_unique_id(hook_name, callback, priority):
    pass
