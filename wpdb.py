# wpdb.py

class wpdb:
    def __get(name):
        pass
        
    def __set(name, value):
        pass

    def __isset(name):
        pass

    def __unset(name):
        pass
    
    def init_charset():
        pass
    
    def determine_charset(charset, collate):
        pass
    
    def set_charset(dbh, charset = None, collate = None):
        pass
    
    def set_sql_mode(modes = array()):
        pass
    
    def set_prefix(prefix, set_table_names = True):
        pass
    
    def set_blog_id(blog_id, network_id = 0):
        pass

    def get_blog_prefix(blog_id = None):
        pass

    def tables(scope = 'all', prefix = True, blog_id = 0):
        pass

    def select(db, dbh = None):
        pass

    def _weak_escape(string):
        pass

    def _real_escape(string):
        pass
    
    def _escape(data):
        pass

    def escape(data):
        pass

    def escape_by_ref(ref):
        pass

    def prepare(query, *args):
        pass

    def esc_like(text):
        pass
    
    def print_error(str = ''):
        pass
    
    def show_errors(show = True):
        pass
    
    def hide_errors():
        pass
    
    def suppress_errors(suppress = True):
        pass
    
    def flush():
        pass
    
    def db_connect(allow_bail = True):
        pass

    def parse_db_host(host):
        pass
    
    def check_connection(allow_bail = True):
        pass
    
    def query(query):
        pass
    
    def log_query(query, query_time, query_callstack, query_start, query_data):
        pass
    
    def placeholder_escape():
        pass
    
    def add_placeholder_escape(query):
        pass
    
    def remove_placeholder_escape(query):
        pass
    
    def insert(table, data, _format = None):
        pass
    
    def replace(table, data, _format = None):
        pass
    
    def _insert_replace_helper(table, data, _format = None, _type = 'INSERT'):
        pass

    def update(table, data, where, _format = None, where_format = None):
        pass

    def delete(table, where, where_format = None):
        pass
    
    def get_var(query = None, x = 0, y = 0):
        pass
    
    def get_row(query = None, output = OBJECT, y = 0):
        pass
    
    def get_col(query = None, x = 0):
        pass
    
    def get_results(query = None, output = OBJECT):
        pass
    
    def get_col_charset(table, column):
        pass
    
    def get_col_length(table, column):
        pass
    
    def strip_invalid_text_for_column(table, column, value):
        pass
    
    def get_col_info(info_type = 'name', col_offset = -1):
        pass
    
    def timer_start():
        pass

    def timer_stop():
        pass
    
    def bail(message, error_code = '500'):
        pass
    
    def close():
        pass
    
    def check_database_version():
        pass
    
    def supports_collation():
        pass

    def get_charset_collate():
        pass

    def has_cap(db_cap):
        pass

    def get_caller():
        pass
    
    def db_version():
        pass
    
    def db_server_info():
        pass
