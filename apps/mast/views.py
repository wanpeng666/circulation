import copy

from django.http import JsonResponse, QueryDict, HttpResponse
from django.views import View

from apps.mast.models import incidents
from apps.utils.loginRequired import LoginRequiredMixin


class incidentsView(View):
    # 获取所有的事件工单
    def get(self, request):
        allIncidents = [incident for incident in incidents.objects.all() if incident.islastest is True]
        incidentList = []
        # 可在循环前分页,暂不做
        for incident in allIncidents:
            incidentDict = {}
            incidentDict['reporter'] = incident.reporter.username
            incidentDict['status'] = incident.get_status_display()
            incidentDict['title'] = incident.title
            incidentDict['level'] = incident.get_level_display()
            incidentDict['degree'] = incident.get_degree_display()
            incidentDict['assigned_to'] = incident.assigned_to.username
            incidentDict['Time'] = incident.Time
            incidentList.append(incidentDict)
        content = {
            'success': True,
            'message': '获取事件工单成功',
            'data': incidentList,
        }
        return JsonResponse(content)

    def post(self, request):
        user = request.user
        res = request.POST
        title = res.get('title', '')
        level = res.get('level', '')
        degree = res.get('degree', '')
        assigned_to = res.get('assigned_to', '')
        obj = incidents.objects.create(title=title, level=level, degree=degree, assigned_to_id=assigned_to,
                                       reporter=user)
        obj.status = '2'
        obj.save()
        obj.sId = obj.id
        obj.fId = ''
        obj.save()
        content = {
            'success': True,
            'message': '创建事件工单成功',
        }
        return JsonResponse(content)


class incidentDetailView(View):
    def get(self, request, id):
        try:
            incident = incidents.objects.get(id=id)
        except Exception as e:
            content = {
                'success': False,
                'message': '未查询到此工单',
            }
            return JsonResponse(content)
        infoDict = {
            'title': incident.title,
            'status': incident.get_status_display(),
            'reporter': incident.reporter.username,
            'level': incident.get_level_display(),
            'degree': incident.get_degree_display(),
            'assigned_to': incident.assigned_to.username,
        }
        content = {
            'success': True,
            'message': 'ok',
            'data': infoDict,
        }
        return JsonResponse(content)

    def put(self, request, id):
        res = QueryDict(request.body)
        try:
            incident = incidents.objects.get(id=id)
        except Exception as e:
            content = {
                'success': False,
                'message': '未查询到此工单',
            }
            return JsonResponse(content)
        title = res.get('title', '')
        print(title)
        level = res.get('level', '')
        degree = res.get('degree', '')
        assigned_to = res.get('assigned_to', '')
        newIncident = copy.deepcopy(incident)
        newIncident.pk = None
        if title:
            newIncident.title = title
        if level:
            newIncident.level = level
        if degree:
            newIncident.degree = degree
        if assigned_to:
            newIncident.assigned_to_id = assigned_to
        newIncident.fId_id = id
        newIncident.save()
        incident.islastest = False
        incident.save()
        content = {
            'success': True,
            'message': '修改工单成功',
        }
        return JsonResponse(content)