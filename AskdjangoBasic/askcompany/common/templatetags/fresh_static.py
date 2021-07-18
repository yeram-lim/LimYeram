from time import time
from django import template
from django.conf import settings
from django.templatetags.static import StaticNode

register = template.Library()

class FreshStaticNode(StaticNode): 
    def url(self, context):
        url = super().url(context)
        if settings.DEBUG:
            url += '?_={}'.format(int(time())) #?:코드 수정/ _:의미x/ {}:들어갈 값, 여기서는 시간을 넣는다.
        return url

@register.tag('fresh_static')
def do_static(parser, token):
    return FreshStaticNode.handle_token(parser, token)