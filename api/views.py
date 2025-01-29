from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from datetime import datetime
from datetime import timezone

def get_info(request):
    data = {
        "email": "mrtemitopejoseph@gmail.com",
        "current_datetime": datetime.now(timezone.utc).isoformat(),
        "github_url": "https://github.com/Tjoseph-O/public_api_hng_stage0"
    }
    return JsonResponse(data)