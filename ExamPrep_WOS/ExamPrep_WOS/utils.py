from ExamPrep_WOS.profiles.models import Profile


def get_user_obj():
    return Profile.objects.first()

