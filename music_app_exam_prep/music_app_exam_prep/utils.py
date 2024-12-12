from music_app_exam_prep.profiles.models import Profile


def get_user_obj():
    return Profile.objects.first()
