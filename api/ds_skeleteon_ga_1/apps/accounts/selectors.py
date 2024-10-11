from ds_skeleteon_ga_1.apps.accounts.models import UserAccount


def get_all_users():
    return UserAccount.objects.active()
