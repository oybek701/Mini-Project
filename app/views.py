from django.shortcuts import render, get_object_or_404, redirect
from .forms import DataForm
from .models import Data


def data_list(req):
    groups = Data.objects.all()

    contex = {"groups": groups}

    return render(req, "data_list.html", contex)


def data_create(req):
    form = DataForm(req.POST or None)

    if form.is_valid():
        form.save()
        return redirect("data_list")

    context = {
        "form": form,
    }

    return render(req, "data_form.html", context)


def data_update(req, pk):
    group = get_object_or_404(Data, pk=pk)
    form = DataForm(req.POST or None, instance=group)

    if form.is_valid():
        form.save()
        return redirect("data_list")

    context = {
        "form": form,
    }

    return render(req, "data_form.html", context)


def data_delete(req, pk):
    group = get_object_or_404(Data, pk=pk)

    if req.method == "POST":
        group.delete()
        return redirect("data_list")

    context = {
        "group": group,
    }

    return render(req, "data_delete.html", context)
