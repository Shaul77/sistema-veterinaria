from django.db.backends.base.base import BaseDatabaseWrapper
from django.db.backends.mysql.features import DatabaseFeatures

# Desactiva chequeo estricto de version
BaseDatabaseWrapper.check_database_version_supported = lambda self: None

# Desactiva la clausula RETURNING incompatible con MariaDB de XAMPP
DatabaseFeatures.can_return_columns_from_insert = property(lambda self: False)
DatabaseFeatures.can_return_rows_from_bulk_insert = property(lambda self: False)