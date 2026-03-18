from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Finding, Mitigationaction
from django.utils import timezone
from .forms import MitigationForm

# Create your views here.

@login_required(login_url='/accounts/login')
def dashboard(request):
    all_findings = Finding.objects.select_related('assetid', 'vuldefid').all()

    context = {
        'findings': all_findings
    }
    return render(request, 'vams_application/dashboard.html', context)


@login_required
def mitigate_finding(request, finding_id):
    # Retrieve the specific finding or throw 404
    finding = get_object_or_404(Finding, pk=finding_id)

    if request.method == 'POST':
        form = MitigationForm(request.POST)
        if form.is_valid():
            mitigation = form.save(commit=False)
            mitigation.findingid = finding
            mitigation.actiondate = timezone.now()
            mitigation.operatorname = request.user.username
            mitigation.save()

            finding.status = 'Fixed'
            finding.save()

            return redirect('dashboard')
    else:
        form = MitigationForm()

    return render(request, 'vams_application/mitigate.html', {'form': form, 'finding': finding})