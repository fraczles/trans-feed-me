from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.contrib import messages
import datetime, sqlite3



def home(request):
    return render(request, "base.html")

def fn(request,num):
    
    time_list_late = []
    time_list_early = []
    time_list_zero = []
    conn = sqlite3.connect("gtfs_rt/gtfsrdb/c.db")
    c = conn.cursor()
    b = conn.cursor()
    c.execute("select arrival_delay from stop_time_updates")
    b.execute("select trip_id from trip_updates")
    for i in range(int(num)):
        a = c.fetchone()
        d = b.fetchone()
        trip_id = d[0]
        mins = int(a[0])/60
        
        
        if mins > 0:
            time_list_late.append({'id': trip_id, 'mins': mins})
        elif mins < 0:
            
            time_list_early.append({'id': trip_id, 'mins': mins})
        else:
            
            time_list_zero.append({'id': trip_id, 'mins': mins})
            
        
        
    
    
    
    
    
    
    
    

    
    
    return render(request, 'result.html', {'num': int(num),'time_list_early':time_list_early, 'time_list_late':time_list_late, 'time_list_zero':time_list_zero })
    