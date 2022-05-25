# meta.py

def add_metadata(meta_type, object_id, meta_key, meta_value, unique = False):
    pass

def update_metadata(meta_type, object_id, meta_key, meta_value, prev_value = ''):
    pass

def get_metadata(meta_type, object_id, meta_key = '', single = False):
    pass

def get_metadata_raw(meta_type, object_id, meta_key = '', single = False):
    pass

def get_metadata_default(meta_type, object_id, meta_key, single = False):
    pass

def metadata_exists(meta_type, object_id, meta_key):
    pass

def get_metadata_by_mid(meta_type, meta_id):
    pass

def update_metadata_by_mid(meta_type, meta_id, meta_value, meta_key = False):
    pass

def delete_metadata_by_mid(meta_type, meta_id):
    pass

def update_meta_cache(meta_type, object_ids):
    pass

def wp_metadata_lazyloader():
    pass

def get_meta_sql(meta_query, _type, primary_table, primary_id_column, context = None):
    pass

def _get_meta_table(_type):
    pass

def is_protected_meta(meta_key, meta_type = ''):
    pass

def sanitize_meta(meta_key, meta_value, object_type, object_subtype = ''):
    pass

def register_meta(object_type, meta_key, args, deprecated = None):
    pass

def filter_default_metadata(value, object_id, meta_key, single, meta_type):
    pass

def registered_meta_key_exists(object_type, meta_key, object_subtype = ''):
    pass

def unregister_meta_key(object_type, meta_key, object_subtype = ''):
    pass

def get_registered_meta_keys(object_type, object_subtype = ''):
    pass

def get_registered_metadata(object_type, object_id, meta_key = ''):
    pass

def _wp_register_meta_args_allowed_list(args, default_args):
    pass

def get_object_subtype(object_type, object_id):
    pass
