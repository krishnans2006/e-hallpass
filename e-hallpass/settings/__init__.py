try:
    from secret import *
except ImportError:
    SECRET_KEY = "secure-secret"
    READY_PASSWORD = "iamready"
    ADMIN_PASSWORD = "iamadmin"
