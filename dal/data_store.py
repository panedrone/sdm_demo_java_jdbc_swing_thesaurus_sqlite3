"""
    This file is a part of SQL DAL Maker project: https://sqldalmaker.sourceforge.net
    It demonstrates how to implement an interface DataStore in Python + sqlite3|psycopg2|mysql|cx_oracle|django.db.
    More about DataStore: https://sqldalmaker.sourceforge.net/data_store.html
    Recent version: https://github.com/panedrone/sqldalmaker/blob/master/src/resources/data_store.py

    Successfully tested with both "no-django" and django.db:

    - 'django.db.backends.sqlite3' ---------------- built-in
    - 'django.db.backends.postgresql_psycopg2' ---- pip install psycopg2
    - 'mysql.connector.django' -------------------- pip install mysql-connector-python
       ^^ instead of built-in 'django.db.backends.mysql' to enable cursor.stored_results().
       MySQL SP returning result-sets --> http://www.mysqltutorial.org/calling-mysql-stored-procedures-python/
       MySQL Connector/Python as Django Engine? -->
       https://stackoverflow.com/questions/26573984/django-how-to-install-mysql-connector-python-with-pip3)
    - 'django.db.backends.oracle' ------------------pip install cx_oracle

    Copy-paste it to your project and change it for your needs.
    Improvements are welcome: sqldalmaker@gmail.com

"""

# uncomment one of the imports below for "no-django"

import sqlite3
# import psycopg2
# import mysql.connector
# import cx_oracle

# uncomment the imports and code below while using django.db:

# import django.db
# from django.apps import AppConfig
# from django.db import transaction
# from django.db.backends.base.base import BaseDatabaseWrapper
#
#
# class MyDjangoAppConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     # default_auto_field = 'django.db.models.AutoField'
#     name = 'dal'  # python package containing generated django models


# # there should be "settings.py" in the project root
# # Google --> django settings.py location
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings') # call it in __main__

# django.setup() should be called before importing/using generated django models -->
# AppRegistryNotReady("Apps aren't loaded yet.")
# django.setup() # ----------- call it before calling of factory create_ds() -> DataStore:


class OutParam:
    def __init__(self):
        self.value = None


class DataStore:

    def begin(self): pass

    def commit(self): pass

    def rollback(self): pass

    # ORM-based raw-SQL helpers

    def get_one_raw(self, cls, params=None):
        """
        :param cls: a model class containing static field SQL
        :param params: a tuple of SQL params
        :return: a model object
        """
        pass

    def get_all_raw(self, cls, params=None) -> []:
        """
        :param cls: a model class containing static field SQL
        :param params: a tuple of SQL params
        :return: an array of model objects
        """
        pass

    # ORM-based helpers

    def filter(self, cls, params: dict):
        """
        :param cls: a model class
        :param params: dict of named filter params
        :return: a QuerySet
        """
        pass

    def delete_by_filter(self, cls, params: dict) -> int:
        """
        :param cls: a model class
        :param params: dict of named filter params
        :return: amount of rows affected
        """
        pass

    def update_by_filter(self, cls, data: dict, params: dict) -> int:
        """
        :param cls: a model class
        :param data: dict of column-value to update
        :param params: dict of filter params
        :return: amount of rows affected
        """
        pass

    # ORM-based CRUD methods

    def create_one(self, obj) -> None:
        """
        :param obj: a model object or serializer object
        :return: None
        """
        pass

    def read_all(self, cls):
        """
        :param cls: a model class
        :return: a QuerySet
        """
        pass

    def read_one(self, cls, pk: dict):
        """
        :param cls: a model class
        :param pk: primary key as a dict of column-value pairs
        :return: a model object
        """
        pass

    def update_one(self, cls, data: dict, pk: dict) -> int:
        """
        :param cls: model class
        :param data: dict of column-value to update
        :param pk: primary key as a dict of column-value pairs
        :return: int, amount of rows affected
        """
        pass

    def delete_one(self, cls, pk: dict) -> int:
        """
        :param cls: model class
        :param pk: primary key as a dict of column-value pairs
        :return: int, amount of rows affected
        """
        pass

    # Raw-SQL methods

    def insert_row(self, sql, params, ai_values):
        """
        :param sql: str
        :param params: array, values of SQL parameters
        :param ai_values: an array like [["o_id", 1], ...] to specify and obtain auto-incremented values
        :return: None
        :raise Exception if no rows inserted.
        """
        pass

    def exec_dml(self, sql, params):
        """
        :param sql: str
        :param params: array, values of SQL parameters
        :return: int, amount of rows affected
        """
        pass

    def query_scalar(self, sql, params):
        """
        :param sql: str
        :param params: array, values of SQL parameters
        :return single scalar value
        :raise Exception if amount of fetched rows != 1
        """
        pass

    def query_all_scalars(self, sql, params) -> []:
        """
        :param sql: str
        :param params: array, values of SQL parameters
        :return array of scalar values
        """
        pass

    def query_row(self, sql, params):
        """
        :param sql: str
        :param params: array, values of SQL parameters
        :return single fetched row
        :raise Exception if amount of rows != 1
        """
        pass

    def query_all_rows(self, sql, params, callback):
        """
        :param sql: str
        :param params: array, values of SQL parameters.
        :param callback: Ð° function delivering fetched rows to caller
        :return: None
        """
        pass


def create_ds() -> DataStore:
    return _DS()


class _DS(DataStore):
    class EngineType:
        sqlite3 = 1
        mysql = 2
        postgresql = 3
        oracle = 4

    def __init__(self):
        self.conn = sqlite3.connect('my-github.sqlite3')
        self.engine_type = self.EngineType.sqlite3

    # def __init__(self):
    #     self.conn = None
    #     self.engine_type = self.EngineType.sqlite3
    #     self.open()
    #
    # def open(self):
    #     # ===== uncomment to use without django.db:
    #
    #     # self.conn = sqlite3.connect('./task-tracker.sqlite')
    #     # self.engine_type = self.EngineType.sqlite3
    #
    #     # self.conn = mysql.connector.Connect(user='root', password='root', host='127.0.0.1', database='sakila')
    #     # self.engine_type = self.EngineType.mysql
    #
    #     # self.conn = psycopg2.connect(host="localhost", database="my-tests", user="postgres", password="sa")
    #     # self.engine_type = self.EngineType.postgresql
    #
    #     # print(self.conn.autocommit)
    #
    #     # ====== uncomment to use with django.db:
    #
    #     con = django.db.connections['default']
    #     engine = con.settings_dict["ENGINE"]
    #     if 'sqlite3' in engine:
    #         self.engine_type = self.EngineType.sqlite3
    #     elif 'mysql' in engine:
    #         self.engine_type = self.EngineType.mysql
    #     elif 'postgresql' in engine:
    #         self.engine_type = self.EngineType.postgresql
    #     elif 'oracle' in engine:
    #         self.engine_type = self.EngineType.oracle
    #     else:
    #         raise Exception('Unexpected: ' + engine)
    #     self.conn = con

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None

    # ORM-based raw-SQL helpers

    def get_all_raw(self, cls, params=None) -> []:
        if not params:
            params = ()
        raw_query_set = cls.objects.raw(cls.SQL, params)
        res = [r for r in raw_query_set]
        return res

    def get_one_raw(self, cls, params=None):
        rows = self.get_all_raw(cls, params)
        if len(rows) == 0:
            raise Exception('No rows')
        if len(rows) > 1:
            raise Exception('More than 1 row exists')
        return rows[0]

    # ORM-based helpers

    def filter(self, cls, params: dict):
        # Django Filter Model by Dictionary
        # https://stackoverflow.com/questions/16018497/django-filter-model-by-dictionary
        return cls.objects.filter(**params)

    def delete_by_filter(self, cls, params: dict) -> int:
        # Entry.objects.filter(blog=b).delete()
        # https://docs.djangoproject.com/en/4.1/ref/models/querysets/
        queryset = self.filter(cls, params)
        res_tuple = queryset.delete()  # (1, {'dal.Group': 1})
        return res_tuple[0]

    def update_by_filter(self, cls, data: dict, params: dict) -> int:
        # call update(), rather than loading the model object into memory.
        # Entry.objects.filter(id=10).update(comments_on=False)
        # https://docs.djangoproject.com/en/4.1/ref/models/querysets/
        queryset = self.filter(cls, params)
        rows_affected = queryset.update(**data)
        return rows_affected

    # ORM-based CRUD methods

    def create_one(self, obj):
        obj.save()

    def read_all(self, cls):
        return cls.objects.all()

    def read_one(self, cls, pk: dict):
        return cls.objects.get(**pk)

    def update_one(self, cls, data: dict, pk: dict) -> int:
        return self.update_by_filter(cls, data, pk)  # no fetch!

    def delete_one(self, cls, pk: dict) -> int:
        rc = self.delete_by_filter(cls, pk)  # no fetch!
        return rc

    # uncomment to use without django.db:

    def begin(self):
        self.conn.execute('begin')  # sqlite3
        # self.conn.start_transaction() # mysql
        # self.conn.begin() # psycopg2

    # uncomment to use without django.db:
    def commit(self):
        self.conn.execute('commit')  # sqlite3
        # self.conn.commit() # psycopg2, mysql

    # uncomment to use without django.db:
    def rollback(self):
        self.conn.execute("rollback")  # sqlite3
        # self.conn.rollback() # psycopg2, mysql

    # uncomment to use with django.db:

    # def begin(self):
    #     django.db.transaction.set_autocommit(False)
    #
    # def commit(self):
    #     django.db.transaction.commit()
    #
    # def rollback(self):
    #     django.db.transaction.rollback()

    def insert_row(self, sql, params, ai_values):
        sql = self._format_sql(sql)
        if len(ai_values) > 0:
            if self.engine_type == self.EngineType.postgresql:
                sql += ' RETURNING ' + ai_values[0][0]

        def do_insert(cursor):
            cursor.execute(sql, params)
            if len(ai_values) > 0:
                if self.engine_type == self.EngineType.postgresql:
                    ai_values[0][1] = cursor.fetchone()[0]
                else:
                    ai_values[0][1] = cursor.lastrowid
            if cursor.rowcount == 0:
                raise Exception('No rows inserted')

        self._exec(do_insert)

    @staticmethod
    def _exec_proc_pg(cursor, sql, params):
        out_params = []
        call_params = []
        for p in params:
            if isinstance(p, OutParam):
                call_params.append(p.value)
                out_params.append(p)
            else:
                call_params.append(p)
        cursor.execute(sql, call_params)
        if len(out_params) > 0:
            row0 = cursor.fetchone()
            i = 0
            for value in row0:
                out_params[i].value = value
                i += 1

    def _exec_proc_mysql(self, cursor, sp, params):
        call_params = self._get_call_params(params)
        # result_args: https://pynative.com/python-mysql-execute-stored-procedure/
        result_args = cursor.callproc(sp, call_params)
        for p in params:
            if isinstance(p, list) and callable(p[0]):
                i = 0
                for result in cursor.stored_results():
                    callback = p[i]
                    self._fetch_all(result, callback)
                    i += 1
                break
        self._assign_out_params(params, result_args)

    def _query_proc_mysql(self, cursor, sp, on_result, params):
        call_params = self._get_call_params(params)
        # result_args: https://pynative.com/python-mysql-execute-stored-procedure/
        result_args = cursor.callproc(sp, call_params)
        for result in cursor.stored_results():
            on_result(result)
        self._assign_out_params(params, result_args)

    def exec_dml(self, sql, params):
        sql = self._format_sql(sql)
        sp = self._get_sp_name(sql)

        def do_exec(cursor):
            if sp is None:
                cursor.execute(sql, params)
                return cursor.rowcount
            if self.engine_type == self.EngineType.postgresql:
                self._exec_proc_pg(cursor, sql, params)  # sql!
            elif self.engine_type == self.EngineType.mysql:
                self._exec_proc_mysql(cursor, sp, params)  # sp!
            else:
                raise Exception('Not supported for this engine')
            return 0

        self._exec(do_exec)

    def query_scalar(self, sql, params):
        rows = self.query_all_scalars(sql, params)
        if len(rows) == 0:
            raise Exception('No rows')
        if len(rows) > 1:
            raise Exception('More than 1 row exists')
        if isinstance(rows[0], list):
            return rows[0][0]
        else:
            return rows[0]  # 'select get_test_rating(?)' returns just scalar value, not array of arrays

    def query_all_scalars(self, sql, params):
        sql = self._format_sql(sql)
        res = []
        sp = self._get_sp_name(sql)

        def fetch_all(cursor):
            if sp is None:
                cursor.execute(sql, params)
                for row in cursor:
                    res.append(row[0])
                return res
            if self.engine_type != self.EngineType.mysql:
                raise Exception('Not supported for this engine')

            def on_result(result):
                for row_values in result:
                    res.append(row_values[0])

            self._query_proc_mysql(cursor, sp, on_result, params)

        self._exec(fetch_all)
        return res

    def query_row(self, sql, params):
        rows = []
        self.query_all_rows(sql, params, lambda row: rows.append(row))
        if len(rows) == 0:
            raise Exception('No rows')
        if len(rows) > 1:
            raise Exception('More than 1 row exists')
        return rows[0]

    def query_all_rows(self, sql, params, callback):
        sql = self._format_sql(sql)
        sp = self._get_sp_name(sql)

        def fetch_all(cursor):
            if sp is None:
                cursor.execute(sql, params)
                columns = [col[0] for col in cursor.description]
                for row in cursor:  # .fetchall():
                    # https://docs.djangoproject.com/en/3.2/topics/db/sql/
                    r = dict(zip(columns, row))
                    callback(r)
                return
            if self.engine_type != self.EngineType.mysql:
                raise Exception('Not supported for this engine')
            self._query_proc_mysql(cursor, sp, lambda result: self._fetch_all(result, callback), params)

        self._exec(fetch_all)

    def _exec(self, func: callable):
        # if isinstance(self.conn, BaseDatabaseWrapper):
        #     # https://stackoverflow.com/questions/8402898/how-can-i-access-the-low-level-psycopg2-connection-in-django
        #     with django.db.connection.cursor() as cursor:
        #         func(cursor)
        #     return
        # with self.conn.cursor() as cursor:  # sqlite3 error without django
        cursor = self.conn.cursor()
        try:
            func(cursor)
        finally:
            cursor.close()

    def _format_sql(self, sql):
        # if isinstance(self.conn, BaseDatabaseWrapper):
        #     return sql.replace("?", "%s")
        return sql

    @staticmethod
    def _fetch_all(result, callback):
        # https://stackoverflow.com/questions/34030020/mysql-python-connector-get-columns-names-from-select-statement-in-stored-procedu
        # https://kadler.github.io/2018/01/08/fetching-python-database-cursors-by-column-name.html#
        for row_values in result:
            row = {}
            i = 0
            for d in result.description:
                col_name = d[0]
                value = row_values[i]
                row[col_name] = value
                i = i + 1
            callback(row)

    @staticmethod
    def _get_sp_name(sql):
        parts = sql.split()
        if len(parts) >= 2 and parts[0].strip().lower() == "call":
            name = parts[1]
            end = name.find("(")
            if end == -1:
                return name
            else:
                return name[0:end]
        return None

    @staticmethod
    def _get_call_params(params):
        """
        COMMENT FROM SOURCES OF MySQL Connector => cursor.py:

        For OUT and INOUT parameters the user should provide the
        type of the parameter as well. The argument should be a
        tuple with first item as the value of the parameter to pass
        and second argument the type of the argument.
        """
        call_params = []
        for p in params:
            if isinstance(p, OutParam):
                call_params.append(p.value)
            elif isinstance(p, list) and callable(p[0]):
                pass  # MySQL SP returning result-sets
            else:
                call_params.append(p)
        return call_params

    @staticmethod
    def _assign_out_params(params, result_args):
        for i in range(len(params)):
            if isinstance(params[i], OutParam):
                params[i].value = result_args[i]
