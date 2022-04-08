from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from .models import Employee, Passport, WorkProject, Membership, Client, VIPClient
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
