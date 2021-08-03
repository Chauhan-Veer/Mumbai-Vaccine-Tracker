import requests
from datetime import datetime, time, timedelta
from time import sleep

import telegram




my_token = " "
chat_id = " "


today = datetime.today()


num_days = 1

global district
#Mumbai District Number 
district = ['395']


all_dates = []


for i in range(num_days):
    all_dates.append(today+timedelta(i))


final_dates = []

def main():
    for i in all_dates:
        final_dates.append(i.strftime("%d/%m/%y"))

        for dis in district:
            for d in final_dates:
                url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}'.format(dis, d)
                
                result = requests.get(url)

            json_result = result.json()
            

            if json_result['centers']:
                for center in json_result["centers"]:
                    for sessions in center["sessions"]:
                        

                            
                            # bot = telegram.Bot(token=my_token)

                            if int(sessions['available_capacity']) != 0:
                                global no_of_vacc
                                no_of_vacc = str(sessions['available_capacity'])

                            


                            
                            print("\n")
                            pins = "Pincode:  " + str(center["pincode"])
                            diss = "District:  " + "Mumbai"
                            Date = "Date:  " + d
                            center_name = "Center name:  " + center["name"]
                            center_address = "Centeer Address:  " + center["address"]
                            no_of_vacc = "Number of Vaccine:  " + str(sessions['available_capacity'])
                            age = "Age:  " + str(sessions["min_age_limit"])
                            Dose_1 = "Dose 1:  " + str(sessions['available_capacity_dose1'])
                            Dose_2 = "Dose 2:  " + str(sessions['available_capacity_dose2'])
                            vacc_type = "Vaccine Type:  " + str(sessions["vaccine"])
                            fee = f"Vaccine Fee: {str(center['fee_type'])}"
                            

                            link = "Resgiter Here 👇 \nhttps://selfregistration.cowin.gov.in/"
                            

                            main_message = f"{pins}\n\n{diss}\n\n{Date}\n\n{center_name}\n\n{center_address}\n\n{no_of_vacc}\n\n{age}\n\n{Dose_1}\n\n{Dose_2}\n\n{vacc_type}\n\n{fee}\n\n\n{link}\n"
                            print(main_message)# sleep(60)
                            # bot.sendMessage(chat_id=chat_id, text=main_message)
                            
                        

if __name__ == '__main__':
    main()