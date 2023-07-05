from datetime import timedelta


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "news",
        "PASSWORD": "a123",
        "HOST": "localhost",
        "USER": "arshia",
        "PORT": 5432,
    }
}

SECRET_KEY = "django-insecure-&jptp@f%1m3a^36i#9w-8fw9457f^m8dtrh%fbz$c!kzz-@r#m"


DEBUG = True


SIMPLE_JWT =  {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "JTI_CLAIM": "jti",
    "TOKEN_OBTAIN_SERIALIZER": "scraping.api.v1.serializer.MyTokenObtainPairSerializer",
}
