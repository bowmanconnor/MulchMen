from django.shortcuts import render, redirect, get_object_or_404
from .models import Appointment, Expense
from .forms import NewAppointmentStaffForm, NewAppointmentUserForm, NewExpenseForm
from django.views.generic import UpdateView, DetailView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.urls import reverse_lazy


from .methods import new_appointment, add_appointment_sms, appointment_confirmed, complete_appointment_email




def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

@login_required
def orders(request):
    user = request.user
    appointments = Appointment.objects.filter(user=user)
    return render(request, 'your_orders.html', {'appointments' : appointments, 'user' : user })








@login_required
def schedule(request):
    if request.method == 'POST':
        form = NewAppointmentUserForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.name = request.user.first_name + " " + request.user.last_name
            appointment.email = request.user.email
            appointment.user = request.user
            appointment.save()
            new_appointment(appointment)
            return redirect('profile')
    else:
        form = NewAppointmentUserForm()
    return render(request, 'schedule.html', {'form': form})

@staff_member_required(login_url='home')
def schedule_staff(request):
    if request.method == 'POST':
        form = NewAppointmentStaffForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.save()
            return redirect('view_appointments')
    else:
        form = NewAppointmentStaffForm()
    return render(request, 'schedule_staff.html', {'form': form})

@staff_member_required(login_url='home')
def view_appointments(request):
    appointments = Appointment.objects.order_by("-date")
    return render(request, 'view_appointments.html', {'appointments' : appointments})
    
@method_decorator(staff_member_required(login_url='home') , name='dispatch')
class AppointmentUpdateView(UpdateView):
    model = Appointment
    fields = ('name', 'email', 'phone', 'address', 'address', 'weeding', 'edging', 'delivery', 'date', 'status', 'cost', 'hear_about_us', 'additional_comments',)

    template_name = 'edit_appointment.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'appointment'

    def form_valid(self, form):
        appointment = form.save(commit=False)
        appointment.save()
        return redirect('view_appointments')

@method_decorator(staff_member_required(login_url='home') , name='dispatch')
class AppointmentDetailView(DetailView):
    model = Appointment
    template_name = 'view_appointment.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'appointment'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

@method_decorator(staff_member_required(login_url='home') , name='dispatch')
class AppointmentDeleteView(DeleteView):
    model = Appointment
    success_url = reverse_lazy('view_appointments')
    template_name = 'view_appointment.html'

def confirm_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    appointment.status = 'S'
    appointment.save()
    appointment_confirmed(appointment)

    #Add google cal stuff 
    return redirect('view_appointments')

def complete_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    appointment.status = 'C'
    appointment.save()
    complete_appointment_email(appointment)
    return redirect('view_appointments')







@staff_member_required(login_url='home')
def view_expenses(request):
    expenses = Expense.objects.all()
    return render(request, 'view_expenses.html', {'expenses' : expenses})

@staff_member_required(login_url='home')
def new_expense(request):
    if request.method == 'POST':
        form = NewExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.save()
            return redirect('view_expenses')
    else:
        form = NewExpenseForm()
    return render(request, 'new_expense.html', {'form': form})

@method_decorator(staff_member_required(login_url='home') , name='dispatch')
class ExpenseUpdateView(UpdateView):
    model = Expense
    fields = ('expense', 'amount', 'purchaser', 'paid', )

    template_name = 'edit_expense.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'expense'

    def form_valid(self, form):
        expense = form.save(commit=False)
        expense.save()
        return redirect('view_expenses')

@method_decorator(staff_member_required(login_url='home') , name='dispatch')
class ExpenseDetailView(DetailView):
    model = Expense
    template_name = 'view_expense.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'expense'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

@method_decorator(staff_member_required(login_url='home') , name='dispatch')
class ExpenseDeleteView(DeleteView):
    model = Expense
    success_url = reverse_lazy('view_exspenses')
    template_name = 'view_expense.html'

def pay_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    expense.paid = True
    expense.save()
    return redirect('view_expenses')
