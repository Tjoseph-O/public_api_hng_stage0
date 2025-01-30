from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
from datetime import timezone

def get_info(request):
    utc_datetime = datetime.now(timezone.utc)  
    iso_format = utc_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ") 

    data = {
        "email": "mrtemitopejoseph@gmail.com",
        "current_datetime": iso_format,
        "github_url": "https://github.com/Tjoseph-O/public_api_hng_stage0"
    }
    return JsonResponse(data)