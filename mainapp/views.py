from django.shortcuts import render

def home(response):
    return render(response, "index.html", {})

def about(response):
    return render(response, "about.html", {})

def skills(response):
    return render(response, "skills.html", {})

def projects(response):
    return render(response, "projects.html", {})

def contact(response):
    return render(response, "contact.html", {})
