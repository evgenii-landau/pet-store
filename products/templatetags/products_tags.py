from django import template

from static.vendor.data.footer import data

register = template.Library()


@register.inclusion_tag("products/footer.html")
def show_footer():
    footer_data = data
    return {"footer_data": footer_data}
