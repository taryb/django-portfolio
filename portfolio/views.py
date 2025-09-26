from django.shortcuts import render

def home(request):
    return render(request, "portfolio/home.html")

def projects(request):
    # Later this will pull from a database model
    demo_projects = [
        {"title": "PyQt Lab Automation", "desc": "Simulated 4-camera lab tool with measurement & SNR."},
        {"title": "Expense Tracker", "desc": "CLI tool with CSV persistence and summaries."},
        {"title": "Expense Dashboard", "desc": "Streamlit app for visualizing spending patterns."},
    ]
    return render(request, "portfolio/projects.html", {"projects": demo_projects})
