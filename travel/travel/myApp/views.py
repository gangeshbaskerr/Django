from django.shortcuts import render
from .forms import TicketForm
from .models import BusDetails


def book_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            bus = form.cleaned_data['Bus_No']
            destination = form.cleaned_data['Destination']
            persons = form.cleaned_data['No_of_Persons']

            try:
                bus_details = BusDetails.objects.get(Bus_No=bus)
                if bus_details.Seats_Available >= persons:
                    bus_details.Seats_Available -= persons
                    bus_details.save()
                    ticket_cost = calculate_ticket_cost(bus_details, destination, persons)
                    return render(request, 'booking_success.html', {'ticket_cost': ticket_cost})
                else:
                    return render(request, 'booking_failure.html')
            except BusDetails.DoesNotExist:
                return render(request, 'booking_failure.html')
    else:
        form = TicketForm()

    return render(request, 'book_ticket.html', {'form': form})


def calculate_ticket_cost(bus_details, destination, persons):
    destinations = bus_details.Destinations.split(',')
    ticket_costs = list(map(int, bus_details.TicketCosts.split(',')))

    index = destinations.index(destination)
    return ticket_costs[index] * persons

def show_front(request):
    return render(request, 'front_page.html')
