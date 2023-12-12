from django.shortcuts import render
from .models import Edge


def display_sorted_edges(request):
    # Assuming the graph.txt file contains the correct data in the specified format
    Edge.objects.all().delete()
    with open('D:/S5/PYTHON LAB/graph.txt', 'r') as file:
        n = int(file.readline().strip())
        for _ in range(n):
            start_vertex, end_vertex, weight = map(int,file.readline().split(','))
            # Create and save an Edge instance
            Edge.objects.create(start_vertex=start_vertex, end_vertex=end_vertex, weight=weight)

    # Retrieve all edges from the database and order them by weight
    edges = Edge.objects.order_by('weight')

    return render(request, 'index.html', {'edges':edges})