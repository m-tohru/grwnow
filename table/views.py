from django.views import View
from django.shortcuts import render
from django.http import HttpResponseRedirect
from table.models import ReservationStatus
from table.validator import Validation



# Create an Spotipy instance
validation = Validation()


class LandingView(View):

    def get_status(self, floor, table):
        res = ReservationStatus.objects.filter(floor_table_no = str(floor) + "f_" + str(table))
        for data in res: return data.status


    def get(self, request):

        contents = {
            '1f_1': self.get_status(1, 1),
            '1f_2': self.get_status(1, 2),
            '1f_3': self.get_status(1, 3),
            '1f_4': self.get_status(1, 4),
            '1f_5': self.get_status(1, 5),
            '1f_6': self.get_status(1, 6),
            '1f_7': self.get_status(1, 7),
            '1f_8': self.get_status(1, 8),
            '2f_1': self.get_status(2, 1),
            '2f_2': self.get_status(2, 2),
            '2f_3': self.get_status(2, 3),
            '3f_1': self.get_status(3, 1),
            '3f_2': self.get_status(3, 2),
            '3f_3': self.get_status(3, 3),
        }

        
        return render(request, 'index.html', contents)
        


    def post(self, request):

        """ Post variables """
        floor = request.POST['floor']
        table_no = request.POST['table_no']

        if str(self.get_status(floor, table_no)) == "None":
            table_info = ReservationStatus(
                floor_table_no = str(floor) + "f_" + str(table_no),
                status = "In Use",
            )
            table_info.save()
        else:
            if str(self.get_status(floor, table_no)) == "In Use":
                status = "Vacant"
            else:
                status = "In Use"

            table_info = ReservationStatus.objects.filter(floor_table_no = str(floor) + "f_" + str(table_no)).first()
            table_info.status = status
            table_info.save()

        #table_info = ReservationStatus(
        #            floor_table_no = str(floor) + "f_" + str(table_no),
        #            status = status,
        #)
        #table_info.save()
       

        contents = {
            '1f_1': self.get_status(1, 1),
            '1f_2': self.get_status(1, 2),
            '1f_3': self.get_status(1, 3),
            '1f_4': self.get_status(1, 4),
            '1f_5': self.get_status(1, 5),
            '1f_6': self.get_status(1, 6),
            '1f_7': self.get_status(1, 7),
            '1f_8': self.get_status(1, 8),
            '2f_1': self.get_status(2, 1),
            '2f_2': self.get_status(2, 2),
            '2f_3': self.get_status(2, 3),
            '3f_1': self.get_status(3, 1),
            '3f_2': self.get_status(3, 2),
            '3f_3': self.get_status(3, 3),
        }

        return render(request, 'index.html', contents)
