from django.shortcuts import render
from .sniffer import start_sniffing

def sniff_traffic(request):
    if request.method == 'POST':
        interface = request.POST.get('interface', 'eth0')
        count = int(request.POST.get('count', 10))
        start_sniffing(interface=interface, count=count)
    return render(request, 'sniffer/index.html')

from django.shortcuts import render
from .sniffer import start_sniffing
from .models import Packet

def sniff_traffic(request):
    if request.method == 'POST':
        interface = request.POST.get('interface', 'eth0')
        count = int(request.POST.get('count', 10))
        start_sniffing(interface=interface, count=count)
    
    # Fetch all captured packets from the database
    packets = Packet.objects.all().order_by('-timestamp')
    return render(request, 'sniffer/index.html', {'packets': packets})