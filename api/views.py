import json
from django.http import JsonResponse

def ping(request):
    return JsonResponse({
        "ok": True,
        "service": "demo-b (django)",
        "ts": __import__("datetime").datetime.utcnow().isoformat() + "Z",
        "remote": request.META.get("REMOTE_ADDR"),
        "headers": {
            "host": request.META.get("HTTP_HOST"),
            "xff": request.META.get("HTTP_X_FORWARDED_FOR"),
        }
    })

def echo(request):
    try:
        data = json.loads(request.body.decode("utf-8") or "{}")
    except Exception:
        data = None
    return JsonResponse({
        "ok": True,
        "service": "demo-b (django)",
        "received": data,
        "ts": __import__("datetime").datetime.utcnow().isoformat() + "Z"
    })
