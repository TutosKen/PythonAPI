from django.db import models
from .merchant import Merchant

# Create your models here.


class MerchantToken(models.Model):
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expiration_time = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'merchant_token'

    # Validates if token is active and not expired
    # Otherwise it'll set the active status to false
    def check_token(self) -> bool:
        valid_token = False
        if self.active:
            from datetime import datetime, timedelta
            import pytz

            expire_time = self.updated_at + \
                timedelta(minutes=self.expiration_time)

            now = datetime.now(tz=pytz.UTC)
            if expire_time > now:
                valid_token = True
            else:
                self.active = False
                self.save()

        return valid_token
