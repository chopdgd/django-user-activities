# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from model_utils import Choices


ACTIVITY_TYPES = Choices(
    (0, 'favorite', _('favorite')),
    (1, 'like', _('like')),
    (2, 'up_vote', _('up_vote')),
    (3, 'down_vote', _('down_vote')),
)
