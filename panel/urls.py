from django.urls import path
from .views import (
    home_view,
    reboot,
    shut_down,
    restart_service,
    stop_service,
    start_service,
    enable_service,
    disable_service,
    info_service,
    data_disks_space,
    data_temp_sensors,
    data_resource_usage,
    login_view,
    logout_view,
)

app_name = 'panel'

urlpatterns = [
    path("", home_view, name="home-view"),
    path("reboot/", reboot, name="reboot"),
    path("shut_down/", shut_down, name="shut-down"),
    path("restart_service/<str:name>/", restart_service, name="restart-service"),
    path("stop_service/<str:name>/", stop_service, name="stop-service"),
    path("start_service/<str:name>/", start_service, name="start-service"),
    path("enable_service/<str:name>/", enable_service, name="enable-service"),
    path("disable_service/<str:name>/", disable_service, name="disable-service"),
    path("info_service/<str:name>/", info_service, name="info-service"),
    
    path("_data_disks_space/", data_disks_space, name="data-disk-space"),
    path("_data_temp_sensors/", data_temp_sensors, name="data-temp-sensors"),
    path("_data_resource_usage/", data_resource_usage, name="data-resource-usage"),
    
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
]
