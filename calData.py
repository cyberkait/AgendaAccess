import datetime
import win32com.client


# Get todays date
start_date=datetime.datetime.now()

#get a day after today
end_date=start_date+ datetime.timedelta(days=1)

def timeString(dt):
    return dt.strftime("%I:%M %p")


outlook = win32com.client.Dispatch('Outlook.Application').GetNamespace('MAPI')
calendar = outlook.getDefaultFolder(9).Items
calendar.IncludeRecurrences = True
calendar.Sort('[Start]')
restriction = "[Start] >= '" + start_date.strftime('%m/%d/%Y') + "' AND [End] <= '" + end_date.strftime('%m/%d/%Y') + "'"
calendar = calendar.Restrict(restriction)
am = [app for app in calendar]

app_subjects = [app.subject for app in am]
app_start =[app.start for app in am]
app_end =[app.end for app in am]


all_apps = []
for i in range(len(app_subjects)):
    all_apps.append(f"{app_subjects[i]} ({timeString(app_start[i])} - {timeString(app_end[i])})\n")