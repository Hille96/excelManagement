import json
import pandas as pd
from django.shortcuts import render
from django.views import View
from django.views.generic.edit import FormView

from .models import ExcelData
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import auth


class HomeView (View):
    template_name = 'excelmanagement/home.html'

    @method_decorator(login_required(login_url="/login/"))
    def get(self, request):
        return render(request, self.template_name)


class UploadFileView(FormView):
    template_name = 'excelmanagement/upload.html'

    @method_decorator(login_required(login_url="/login/"))
    def get(self, request):
        return render(request, self.template_name)

    @method_decorator(login_required(login_url="/login/"))
    def post(self, request, *args, **kwargs):
        file = request.FILES['myfile']

        if file.name.endswith('.xlsx'):
            self._handle_xlsx(file)
        elif file.name.endswith('.csv'):
            self._handle_csv(file)
        return render(request, self.template_name)

    def _handle_xlsx(self, file):
        ExcelData.objects.create(
            title=file.name,
            data=pd.read_excel(file).to_json(),
        )

    def _handle_csv(self, file):
        data = pd.read_csv(file, error_bad_lines=False).to_json()
        ExcelData.objects.create(
            title=file.name,
            data = data
        )

        
class FilterView(View):
    template_name = 'excelmanagement/filter.html'

    @method_decorator(login_required(login_url="/login/"))
    def get(self, request):
        return render(request, self.template_name)


class ViewView(View):
    template_name = 'excelmanagement/view.html'
    selection = ExcelData.objects.all()

    @method_decorator(login_required(login_url="/login/"))
    def get(self, request):
        return render(request, self.template_name, {"selection":self.selection})

    @method_decorator(login_required(login_url="/login/"))
    def post(self, request):

        try:
            if request.POST["selection_id"]:
                test = ExcelData.objects.get(pk=request.POST["selection_id"])
                objects = json.loads(ExcelData.objects.get(pk=request.POST["selection_id"]).data)
                request.session['last_selection_id'] = request.POST["selection_id"]

        except:
            objects = json.loads(ExcelData.objects.get(pk=request.session['last_selection_id']).data)
            for key, values in objects.items():
                for key, value in values.items():
                    if key == request.POST["rownumber"]:
                        valuesOfRow = value.split(";")
                        newString = ""
                        for word in valuesOfRow:
                            if word == request.POST['value']:
                                word = request.POST['newword']
                                newString += word + ";"
                            else:
                                newString += word + ";"
                        values[key] = newString
            ExcelData.objects.filter(pk=request.session['last_selection_id']).update(data=json.dumps(objects))

        titlevalue = list(objects.keys())[0]
        titlevalue = titlevalue.split(";")

        titleDict = {"title": titlevalue}
        objects["data"] = objects.pop(list(objects.keys())[0])
        for key, value in objects["data"].items():
            objects["data"][key] = value.split(";")
        objects["title"] = titleDict
        objects["selection"] = self.selection

        return render(request, self.template_name, objects)


class LoginView(View):
     template_login = 'excelmanagement/login.html'
     template_home = 'excelmanagement/home.html'

     def get(self, request):
         return render(request, self.template_login)

     def post(self, request):
         username = request.POST.get('username', '')
         password = request.POST.get('password', '')
         user = auth.authenticate(username=username, password=password)

         if user is not None:
             auth.login(request, user)
             return render(request, self.template_home)

         else:
             message = " Sorry! Username or Password didn't match, Please try again ! "
             return render(request,self.template_login, {"message": message})

class LogoutView(View):
    template_login = 'excelmanagement/login.html'

    def get(self, request):
        auth.logout(request)
        message = "Successfully logged out."
        return render(request, self.template_login, {"message": message})