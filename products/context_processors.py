def current_url(request):
    return {"current_url": request.path}


def current_category(request):
    """Контекстный процессор, добавляющий переменную в контекст,
    которая показывает содержит ли URL определенное слово
    """
    return {
        "url_contains_details": "details" in request.path,
        "url_contains_change_password": "change_password" in request.path,
    }
