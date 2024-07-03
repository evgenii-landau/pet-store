from django import template

register = template.Library()


@register.inclusion_tag("users/inclusion/right-column-welcome.html")
def show_welcome():
    return {}


@register.inclusion_tag("users/inclusion/right-column-details.html")
def show_details(form):
    return {"form": form}


@register.inclusion_tag("users/inclusion/right-column-change-password.html")
def show_change_password(form):
    return {
        "form": form,
    }
