from dateutil.relativedelta import relativedelta
from django.http import Http404
from django.template.response import TemplateResponse
from django.utils import timezone
from django.views.decorators.http import require_GET

from counter import settings

@require_GET
def about(request):
    """more information about the instance"""
    # six_months_ago = timezone.now() - relativedelta(months=6)
    '''six_month_count = models.User.objects.filter(
        is_active=True, local=True, last_active_date__gt=six_months_ago
    ).count()'''
    data = {
        # "active_users": six_month_count,
        '''"status_count": models.Status.objects.filter(
            user__local=True, deleted=False
        ).count(),
        "admins": models.User.admins(),'''
        # "version": settings.VERSION,
        "version" : "0.1.0"
    }

    return TemplateResponse(request, "index.html", data)