from django.shortcuts import render , redirect
from .forms import ReservationForm, RateCoachForm, PaymentForm
from .models import Client, Reservation, Training, Coach, Payment
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, "index.html")


@login_required
def Reservations(request):
    if request.method == "POST":
        Id = request.POST['id']
        r = Reservation.objects.filter(id=Id).first()
        r.delete()
        r.training.Coach.disagrate()
        r.training.Coach.save()
        r.client.Cancel()
        r.client.save()
        return redirect("Reservations")
    query = Reservation.objects.filter(client=Client.objects.filter(user=request.user).first())
    context = {"reservations": query, "form": ReservationForm}
    return render(request, "Reservations.html", context)


@login_required
def ReservationCreate(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        trainings = Reservation.objects.filter(client=Client.objects.filter(user=request.user).first())
        if form.is_valid():
            reservation = form.save(commit=False)
            client = Client.objects.filter(user=request.user).first()
            if trainings.filter(training=reservation.training):
                return redirect("Reservations")
            if trainings.filter(training__datetime=reservation.training.datetime):
                return redirect("Reservations")
            if client.allowed == client.enters:
                return redirect("Reservations")
            if client.remaining == 0:
                return redirect("Reservations")
            else:
                client.Enter()
                client.save()
                reservation.training.Coach.updateTrainings()
                reservation.training.Coach.save()
                reservation.client = Client.objects.filter(user=request.user).first()
                reservation.save()
            return redirect("Reservations")
    context = {"form": ReservationForm}
    return render(request, "ReservationCreate.html", context)


def Coaches(request):
    query = Coach.objects.filter()
    context = {"coaches": query}
    return render(request, "Coaches.html",context)


@login_required
def RateCoach(request):
    if request.method == "POST":
        rate = request.POST['rate']
        userr = request.POST['user']
        coach = Coach.objects.filter(user__username=userr).first()
        c_old_rate = coach.rate
        c_old_num = coach.rate_num
        coach.rate = float("{0:.2f}".format(((c_old_rate*c_old_num) + float(rate))/(c_old_num+1)))
        coach.rate_num = coach.rate_num+1
        coach.save()
        return redirect("Coaches")
    query = Coach.objects.filter()
    context = {"form": RateCoachForm, "coaches": query}
    return render(request, "RateCoach.html", context)


@login_required
def Clients(request):
    query = Client.objects.filter()
    context = {"clients": query}
    return render(request, "Clients.html", context)


@login_required
def ReservationEdit(request, pk):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            r = Reservation.objects.filter(id=pk).first()
            t_id = request.POST['t_id']
            t = Training.objects.filter(id=t_id).first()
            r.training = t
            r.save()
            return redirect("Reservations")
    query = Training.objects.filter()
    context = {"form": ReservationForm,"trainings": query}
    return render(request, "ReservationEdit.html", context)


@login_required
def PaymentCreate(request):
    if request.method == "POST":
        form = PaymentForm(request.POST)
        date = request.POST['date']
        payments = Payment.objects.filter(client=Client.objects.filter(user=request.user).first())
        if form.is_valid():
            payment = form.save(commit=False)
            for p in payments:
                month = str(p.date).split('-')[1]
                if month == str(date).split('-')[1]:
                    return redirect("Payments")
            payment.date = date
            payment.client = Client.objects.filter(user=request.user).first()
            payment.client.allowed = 4
            payment.client.remaining = 40
            payment.client.save()
            payment.save()
            return redirect("Payments")
    context = {"form": PaymentForm}
    return render(request, "PaymentCreate.html", context)


@login_required
def Payments(request):
    query = Payment.objects.filter(client=Client.objects.filter(user=request.user).first())
    context = {"payments": query}
    return render(request, "Payemnts.html", context)


def Trainings(request):
    query = Training.objects.filter()
    context = {"trainings": query}
    return render(request, "Trainings.html", context)


def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("index")
    return render(request, "login.html")
