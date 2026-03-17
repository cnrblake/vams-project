from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Finding

# Create your views here.

@login_required(login_url='/accounts/login')
def dashboard(request):
    all_findings = Finding.objects.select_related('assetid', 'vuldefid').all()

    context = {
        'findings': all_findings
    }
    return render(request, 'vams_application/dashboard.html', context)