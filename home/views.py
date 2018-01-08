from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from about.models import Organization_abstract, Human_resource, Report, Audit_report
from home.models import Slider, Collage, We_offer, Ticker
from logistic.models import Servicetype, Subtitle, Tool
from works.models import Major_work, Upcoming, Work_progress
from offer.models import Slider, Training, Gallery
from detail.models import Survey_detail, Gallery, Publication_link

# Create your views here.

class IndexView(ListView):
    context_object_name = 'home'
    template_name = 'index.html'
    queryset = We_offer.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['slider'] = Slider.objects.all()
        context['collage'] = Collage.objects.all()[:5]
        context['offer'] = We_offer.objects.all()
        context['ticker'] = Ticker.objects.all()[:1]
        # And so on for more models
        return context

def organization(request):
    gallery = Organization_abstract.objects.all()
    context = {
        'gallery' : gallery,
    }
    return render(request, "organization-abstract.html", context)

class LogisticView(ListView):
    context_object_name = 'service'
    template_name = 'logistic.html'
    queryset = Servicetype.objects.all()

    def get_context_data(self, **kwargs):
        context = super(LogisticView, self).get_context_data(**kwargs)
        context['maintitle'] = Servicetype.objects.all()
        context['subtitle'] = Subtitle.objects.all()
        context['facility'] = Tool.objects.all()
        # And so on for more models
        return context

def human_res(request):
    human = Human_resource.objects.all()
    filter = Human_resource.objects.all().order_by('name')
    context = {
        'human' : human,
        'filter' : filter,
    }
    return render(request, "human-resource.html", context)

class ReportsView(ListView):
    context_object_name = 'report'
    template_name = 'reports.html'
    queryset = Report.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ReportsView, self).get_context_data(**kwargs)
        context['latest'] = Report.objects.all()
        context['reports'] = Audit_report.objects.all()
        # And so on for more models
        return context

def major_works(request):
    # pagination_per_page = request.GET.get('per_page', 3)
    major = Major_work.objects.all()
    # try:
    #     per_page = int(request.REQUEST['p'])
    # except:
    #     per_page = 25  # default value
    #
    # paginator = Paginator(objects, per_page)

    # query = request.GET.get("q")
    # if query:
    #     major = major.filter(
    #         Q(project_name__icontains=query) |
    #         Q(project_type__icontains=query) |
    #         Q(funding_agency__icontains=query) |
    #         Q(year__icontains=query)
    #     ).distinct()
    # # paginator = Paginator(major, pagination_per_page)  # Show 25 contacts per page
    # try:
    #     per_page = int(request.REQUEST['p'])
    # except:
    #     per_page = 1  # default value
    #
    # paginator = Paginator(major, per_page)
    # page_request_var = "page"
    # page = request.GET.get(page_request_var)
    # try:
    #     major = paginator.page(page)
    # except PageNotAnInteger:
    #     # If page is not an integer, deliver first page.
    #     major = paginator.page(1)
    # except EmptyPage:
    #     # If page is out of range (e.g. 9999), deliver last page of results.
    #     major = paginator.page(paginator.num_pages)


    context = {
        "major": major,
        # "page_request_var": page_request_var,
        # "pagination_per_page": pagination_per_page,
    }
    return render(request, "major-works.html", context)

def process_ajax(request):

    draw = request.GET['draw']
    start = int(request.GET['start'])
    length = int(request.GET['length'])
    order_column = int(request.GET['order[0][column]'])
    order_direction = '' if request.GET['order[0][dir]'] == 'desc' else '-'
    column = [i.name for n, i in enumerate(Major_work._meta.get_fields()) if n == order_column][0]
    global_search = request.GET['search[value]']
    all_objects = Major_work.objects.all()

    columns = [i.name for i in Major_work._meta.get_fields()][1:]
    objects = []
    for i in all_objects.order_by(order_direction + column)[start:start + length].values():
        ret = [i[j] for j in columns]
        objects.append(ret)
    filtered_count = all_objects.count()
    total_count = Major_work.objects.count()
    return JsonResponse({
        "sEcho": draw,
        "iTotalRecords": total_count,
        "iTotalDisplayRecords": filtered_count,
        "aaData": objects,

})




def upworking_works(request):
    upcoming = Upcoming.objects.all()
    context = {
        'upcoming' : upcoming,
    }
    return render(request, "upworking-works.html", context)

def ongoing_works(request):
    ongoing = Work_progress.objects.all()
    context = {
        'ongoing' : ongoing,
    }
    return render(request, "ongoing-works.html", context)

class we_offerView(ListView):
    context_object_name = 'we_offer'
    template_name = 'we-offer.html'
    queryset = Training.objects.all()

    def get_context_data(self, **kwargs):
        context = super(we_offerView, self).get_context_data(**kwargs)
        context['slider'] = Slider.objects.all()[:3]
        context['training'] = Training.objects.all()[:1]
        context['gallery'] = Gallery.objects.all()[:5]
        # And so on for more models
        return context

class survey_detailView(ListView):
    context_object_name = 'detail'
    template_name = 'survey-details.html'
    queryset = Survey_detail.objects.all()

    def get_context_data(self, **kwargs):
        context = super(survey_detailView, self).get_context_data(**kwargs)
        context['detail'] = Survey_detail.objects.all()
        context['gallery'] = Gallery.objects.all()
        context['publication'] = Publication_link.objects.all()
        # And so on for more models
        return context
