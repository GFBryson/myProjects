import datetime
import strugDB
import re
import calendar

DATE_RE=re.compile("^(20)+(1[8-9]|[2-9][0-9])+(-)+(0[1-9]|1[0-2])+(-)+([0-2][0-9]|3[0-1])$")
TIME_RE=re.compile("^([0-9]|1[0-2])+(:)+([0-5][0-9])$")
STRIPPER="%Y-%m-%d %H:%M:%S"

db=strugDB.sdb()
class strugEvents():
    def makeEvent(command,channel):
        print("in event maker")
        split=command.split("&gt;&gt;")
        parsed=(split[1].strip()).split(" ")
        description=None
        if(len(split)>=3):
            description=split[2]
        else:
            description=" "
        #print("\nparsed")
        #print(parsed)
  #     print()

        if(len(parsed)>=4):
            response=None
            if not(DATE_RE.match(parsed[0])):#check date Syntax
                response="Please check your date formatting\nYYYY-DD-MM :slightly_smiling_face:"
            elif not(TIME_RE.match(parsed[1])):#check time syntax
                response="Please check your time formatting\nHH:MM :slightly_smiling_face:"
            elif not((parsed[2]=='p')or(parsed[2]=='a')):#check for a or p
                response='I\'m not sure what you mean by "{res}"\n Please use \'p\' for PM and \'a\' for AM'
                response=response.format(res=parsed[2])
            else:
                if(len(parsed)>4):
                    for x in range(4,len(parsed)):
                        parsed[3]=parsed[3]+" "+parsed[x]
                print("TITLE: "+parsed[3])
                split_date=parsed[0].split('-')
                split_time=parsed[1].split(':')
                for d in range(0,len(split_date)):
                    split_date[d]=int(split_date[d].lstrip('0'))
                for t in range(0,len(split_time)):
                    split_time[t]=int(split_time[t].lstrip('0'))
                if (parsed[2]=='a') and (split_time[0]==12):
                        split_time[0]=0
                if(parsed[2]=='p') and (split_time[0]<12):
                    split_time[0]=split_time[0]+12
                new_date=datetime.datetime(split_date[0],split_date[1],split_date[2],split_time[0],split_time[1])
                db.add_event(new_date,channel,parsed[3])
                db.print_events()
                response="event "+parsed[3]+" created for "+parsed[1]+" "+parsed[2]+"m on "+parsed[0]
        else:
            response="I'm sorry, you are missing some arguments\nPlease use the format YYYY-MM-DD HH:MM a/p EVENT_NAME"
        return response
    def print_week(channel):
            now=datetime.datetime.now()
            events=db.get_events()
            response=""
            for e in events:
                time=datetime.datetime.strptime(e[1],STRIPPER)
                #print(time.day)
                if(((time-now).days)<8) and (((time-now).days)>0) and (e[2]==channel):
                        response+=e[3]+" at "+time.strftime("%I:%M %p")+" on "
                        response+=""+calendar.day_name[time.weekday()]+" "+calendar.month_name[time.month]+" "+str(time.day)+" "+str(time.year)+"\n"
            if response=="":
                    response="There are no upcomming events for this channel this week"
            return response
