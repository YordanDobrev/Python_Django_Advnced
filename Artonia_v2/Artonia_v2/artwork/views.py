from django.contrib.auth import get_user_model
from django.views.generic import ListView
from Artonia_v2.art_painting.models import ArtPainting
from Artonia_v2.macrame.models import Macrame

UserModel = get_user_model()


class PublicArtworkListView(ListView):
    model = Macrame, ArtPainting
    template_name = 'artwork/public_artwork_list.html'
    context_object_name = 'macrames'
    paginate_by = 12

    def get_queryset(self):
        queryset = Macrame.objects.filter(is_public=True).order_by('-created_at')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        public_macrames = Macrame.objects.select_related('user').filter(is_public=True).order_by('-created_at')
        public_arts = ArtPainting.objects.select_related('user').filter(is_public=True).order_by('-created_at')

        macrames_by_creator = {}
        arts_by_creator = {}

        for macrame in public_macrames:
            creator_username = macrame.user.username
            if creator_username not in macrames_by_creator:
                macrames_by_creator[creator_username] = []
            macrames_by_creator[creator_username].append(macrame)
        context['macrames_by_creator'] = macrames_by_creator

        for art in public_arts:
            creator_username = art.user.username
            if creator_username not in arts_by_creator:
                arts_by_creator[creator_username] = []
            arts_by_creator[creator_username].append(art)
        context['arts_by_creator'] = arts_by_creator

        return context
