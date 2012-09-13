from django.conf.urls.defaults import *
from notification.views import notices, mark_all_seen, single


urlpatterns = patterns('',
    url(r'^$', notices, name="notification_notices"),
    url(r'^(\d+)/$', single, name="notification_notice"),
    url(r'^mark_all_seen/$', mark_all_seen, name="notification_mark_all_seen"),
)
