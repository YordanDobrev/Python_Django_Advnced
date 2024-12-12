from Artonia_v2.accounts.models import ArtoniaUser


def get_user_obj():
    return ArtoniaUser.objects.first()
