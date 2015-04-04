import re
from django import template
from django.utils.translation import ugettext_lazy as _
from apps.jalali import *


register = template.Library()

JALALI = 0
ARABIC = 1
ENGLISH = 2

CALENDAR = {
    'fa': JALALI,
    'ar': ARABIC,
    'en': ENGLISH,
}

@register.tag
def transdate(parser, token):
    bits = token.split_contents()
    if len(bits) < 2:
        raise template.TemplateSyntaxError('"transdate" takes one argument.')
    return TransDateNode(bits[1])

class TransDateNode(template.Node):

    def __init__(self, date):
        self.date = template.Variable(date)

    def render(self, context):
        language = context['LANGUAGE_CODE']
        date = self.date.resolve(context)
        # now = datetime.datetime.now()
        # if (now - date) == datetime.timedelta(days=1):
        #     return _('Yesterday')
        trans_date = (date.year, date.month, date.day)
        if CALENDAR[language] == JALALI:
            jalali_date_obj = GregorianToJalali(date.year, date.month, date.day)
            trans_date = jalali_date_obj.getJalaliList()

        try:
            time = (date.hour, date.minute)
            date_time = '%s/%s/%s' % trans_date + ' --  %s:%s' % time
        except AttributeError:
            date_time = '%s/%s/%s' % trans_date
        return date_time


# create Dom for pagination
# ------ {% pagination  [object_list] %} --------- #
@register.tag
def pagination(parser, token):
    bits = token.split_contents()
    if len(bits) < 2:
        raise template.TemplateSyntaxError('"pagination" takes at least one argument.')
    return Pagination(bits[1], bits[2:])


class Pagination(template.Node):
    def __init__(self, object_list, args):
        self.object_list = template.Variable(object_list)
        self.args = [template.Variable(arg) for arg in args]

    def render(self, context):
        dom = ''
        object_list = self.object_list.resolve(context)
        slice = self.args[0].resolve(context)
        request = self.args[1].resolve(context)
        next_string = self.args[2].resolve(context)
        previous_string = self.args[3].resolve(context)

        last = object_list.paginator.num_pages
        current = object_list.number

        if last > 1:

            if not next_string: next_string = ' > '
            if not previous_string: previous_string = ' < '

            parameter_string = ''
            if request.GET:
                query_string = request.META['QUERY_STRING']

                if 'page' in query_string:
                    parameter_string = re.sub("&?page=\d+", '', query_string)
                else:
                    parameter_string = '&%s' %(query_string)


            list = []
            dom = '<ul class="pagination">'
            GAP = 2
            start_gap = 0
            end_gap = 0
            if current - slice == GAP:
                start_gap = GAP
            if last - current == slice + GAP:
                end_gap = GAP

            if last > 10:
                if current <= start_gap + slice:
                    i = current - 1
                    while i > 0:
                        list.append(current - i)
                        i -= 1

                else:
                    i = slice - 1
                    while (i < slice) and (i > 0) and (current - i) > 0:
                        list.append(current - i)
                        i -= 1

                if last - current <= slice + end_gap + 1:
                    j = 0
                    while j < last - current + 1:
                        list.append(current + j)
                        j += 1
                else:
                    j = 0
                    while (j <= slice) and (current + j) < last + 1:
                        list.append(current + j)
                        j += 1

                if object_list.has_previous():
                    dom = '%s <li class="first-page"><a href="?page=%d%s">%s</a></li>' % (dom,current - 1, parameter_string, previous_string)
                if 1 not in list:
                    dom = '%s <li><a href="?page=1%s"> 1 </a></li>' % (dom, parameter_string)
                if current - slice > GAP :
                    dom = '%s  <li><span> ... </span></li>' % (dom)

                for page in list:
                    if page != current:
                        dom = '%s <li><a href="?page=%d%s"> %d </a></li>' % (dom, page, parameter_string,page)
                    else:
                        dom = '%s  <li><a href="#" class="active">%d</a></li>' % (dom, page)
                #end_gap or GAP?
                if last - current > slice + end_gap + 1:
                    dom = '%s  <li><span> ... </span></li>' % (dom)

                if last not in list:
                    dom = '%s <li><a href="?page=%d%s" > %d </a></li>' % (dom, last, parameter_string,last)
                if object_list.has_next():
                    dom = '%s <li class="last-page"><a href="?page=%d%s" >%s</a></li>' % (dom, current + 1, parameter_string, next_string)

            else:
                list = object_list.paginator.page_range
                for page in list:
                    if page != current:
                        dom = '%s  <li><a href="?page=%d%s">%d</a></li>' % (dom, page, parameter_string, page)
                    else:
                        dom = '%s  <li class="active"><a href="#">%d</a></li>' % (dom, page)

            dom = '%s </ul>' % (dom)
        return dom
