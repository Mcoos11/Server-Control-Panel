from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
from  control_panel.settings import BASE_DIR
import subprocess, os

@login_required(login_url='panel:login')
def home_view(request):
  services_file_path = os.path.join(BASE_DIR, "services.txt")
  services_file = open(services_file_path, 'r')
  services = services_file.readlines()
  services = [service.strip() for service in services]
  services_file.close()
  statusing = []
  enabling = []
  for service in services:
      status = subprocess.run(['sudo', 'systemctl', 'is-active', str(service)], stdout=subprocess.PIPE)
      status = status.stdout.decode('utf-8').strip()
      if status == 'active':
        statusing.append(1)
      elif status == 'inactive':
        statusing.append(0)
  
      enable = subprocess.run(['sudo', 'systemctl', 'is-enabled', str(service)], stdout=subprocess.PIPE)
      enable = enable.stdout.decode('utf-8').strip()
      if enable == 'enabled':
        enabling.append(1)
      elif enable == 'disabled':
        enabling.append(0)
  
  obj = zip(services, statusing, enabling)
  return render(request, "panel/home.html", {'services': obj})      

def reboot(request):
  output = os.system(f'sudo reboot')
  if output:
    messages.info(request, f'{output}')
  return redirect("panel:home-view")

def shut_down(request):
  output = os.system(f'sudo shutdown now')
  if output:
    messages.info(request, f'{output}')
  return redirect("panel:home-view")
  
def restart_service(request, name):
  output = os.system(f'sudo systemctl restart {name}')
  if output:
    messages.info(request, f'{output}')
  return redirect("panel:home-view")

def stop_service(request, name):
  output = os.system(f'sudo systemctl stop {name}')
  if output:
    messages.info(request, f'{output}')
  return redirect("panel:home-view")

def start_service(request, name):
  output = os.system(f'sudo systemctl start {name}')
  if output:
    messages.info(request, f'{output}')
  return redirect("panel:home-view")

def enable_service(request, name):
  output = os.system(f'sudo systemctl enable {name}')
  if output:
    messages.info(request, f'{output}')
  return redirect("panel:home-view")

def disable_service(request, name):
  output = os.system(f'sudo systemctl disable {name}')
  if output:
    messages.info(request, f'{output}')
  return redirect("panel:home-view")

def info_service(request, name):
  output = subprocess.run(['sudo', 'journalctl', '-u', str(name), '-b'], stdout=subprocess.PIPE)
  output = output.stdout.decode("utf-8").strip()
  return JsonResponse({'info': output})

def data_disks_space(request):
  pass

def data_temp_sensors(request):
  pass

def data_resource_usage(request):
  pass

# LOGIN
@user_passes_test(lambda user: not user.is_authenticated, redirect_field_name=None)
def login_view(request):
  if request.method == "POST":
    password = request.POST['pass']
    user = authenticate(request, username="admin", password=password)
    if user is not None and user.is_active:
      login(request, user)
      return redirect('panel:home-view')
    else:
      messages.error(request, ("Błędne hasło!"))
      return redirect('panel:login')
  else:
    return render(request, 'panel/login.html')
   
def logout_view(request):
    if request.user.is_authenticated:
        messages.success(request, ("Wylogowano."))
    logout(request)
    return redirect('panel:login')
