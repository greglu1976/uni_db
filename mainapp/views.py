from django.shortcuts import render
from django.http import HttpResponse

from .models import Cabinets, Terminals, PhDLDconnections, LogicDevices, LogicNodesTypes, DataObjects, LDLNconnections, \
    LogicNodeInstantiated, LNobject, LNtypeObjConnections
from .wordprocessor import word_report
from .dxfprocessor import dxf_report

def index(request):
    return render(request, 'mainapp/main.html', {'activeMain': 'active', 'activeHelp': '', 'title': 'Главная'})

def reports(request):
    cabinets = Cabinets.objects.all()
    cabinets = cabinets.order_by('name')
    cabinets1 = list() # шкафы 1 архитектуры
    cabinets2 = list() # шкафы 2 архитектуры
    
    for cabinet in cabinets:
        if cabinet.name[-1] =='1':
            cabinets1.append(cabinet)
        else:
            cabinets2.append(cabinet)
    return render(request, 'mainapp/reports.html', {'cabinets1': cabinets1, 'cabinets2': cabinets2, 'activeMain': '', 'activeHelp': '', 'title': 'Перечень шкафов / отсеков'})

def get_report(request):
    cab = request.GET.get('name')
    type = request.GET.get('type')
    if type == 'cabinet':
        return word_report(request, cab)
    if type == 'dxf':
        return dxf_report(request, cab)


# показываем шкаф
def cabinet(request):
    cab = request.GET.get('name')
    type = request.GET.get('type')
    cabinet= Cabinets.objects.get(name=cab)
    print('OK', cabinet.terminal1)
    return render(request, 'mainapp/cabinet.html', {'cabinet': cabinet, 'title': 'Отчеты по шкафу: '+cabinet.name})



def show(request):
    name = request.GET.get('name')
    type = request.GET.get('type')

# -------------------------------обработка ied------------------------------
    if type == 'ied':
        ied = Terminals.objects.get(name=name)
        conns = PhDLDconnections.objects.all().filter(ied_id=ied.id)
        conns = conns.order_by('ld')
        lds = list()
        for item in conns.iterator():
            obj = LogicDevices.objects.get(name=item.ld)
            #print(obj)
            lds.append(obj)
        lds.sort(key=lambda x: x.name)
        return render(request, 'mainapp/showld.html', {'ied': ied, 'lds': lds, 'title': 'Логические устройства в составе ИЭУ '+str(ied)})

# -------------------------------обработка ld------------------------------
    if type == 'ld':
        ld = LogicDevices.objects.get(name=name)
        lns_conns = LDLNconnections.objects.all().filter(ld_id=ld.id)
        lns_conns = lns_conns.order_by('ld')

        lns = list()
        for item in lns_conns.iterator():
            print('------------>', item.ln)
            ln = LogicNodeInstantiated.objects.get(short_name=item.ln)
            #print(ln)
            lns.append(ln)
        lns.sort(key=lambda x: x.class_name)
        return render(request, 'mainapp/showldobj.html', {'ld':ld, 'lns': lns, 'title': 'Экземпляры ЛУ в составе лог. устройства '+str(ld)})

    # -------------------------------обработка ln------------------------------
    if type == 'ln':
        lntype = LogicNodesTypes.objects.get(name=name)
        #print('++++++++++++++', lntype.id)
        #fb = LogicNodeInstantiated.objects.filter(ln_type=lntype.id).first()
        #print(fb.short_name)
        #fb_desc = LogicNodeInstantiated.objects.get(short_name=fb)
        #fb_desc = LogicNodeInstantiated.objects.all().filter(ln_type=lntype)
        objects = LNtypeObjConnections.objects.all().filter(ln_type=lntype.id)

        objs = list()
        for item in objects.iterator():
            print('------------>', item.ln_obj)
            object_id = DataObjects.objects.get(name=item.ln_obj)
            object = LNobject.objects.get(data_object=object_id)
            objs.append(object)
            print('------------>', objs)
        objs.sort(key=lambda x: (str(x.dataset), str(x.func_group), str(x.cdc), str(x.data_object))) #, str(x.cdc)[0]
        return render(request, 'mainapp/showlnobj.html', {'objs': objs, 'lntype':lntype, 'title': 'Объекты в составе типа ЛУ '+str(lntype) })

def lntypes(request):
    lntypes = LogicNodesTypes.objects.all()
    return render(request, 'mainapp/lntypes.html', {'lntypes':lntypes, 'title': 'Список типов логических узлов'})

def connslntype(request):
    name = request.GET.get('name')
    type = request.GET.get('type')
    if type == 'ln_type':
        lntype = LogicNodesTypes.objects.get(name=name)
        ln_inst = LogicNodeInstantiated.objects.all().filter(ln_type=lntype.id)
        for inst in ln_inst:
            print(inst.short_name)
        return render(request, 'mainapp/conns.html', {'ln_type': name, 'ln_inst':ln_inst, 'title': 'Потомки типа ЛУ '+str(name)})
    if type == 'inst_ln':
        lntype = request.GET.get('lntype')
        ln_id = LogicNodeInstantiated.objects.get(short_name=name)
        print('>', ln_id.id)
        lds = LDLNconnections.objects.all().filter(ln=ln_id.id)
        objs = list()
        for ld in lds:
            print('>>>>>>', ld.ld)
            #objs.append(ld)
            ldevice = LogicDevices.objects.get(name=ld.ld)
            print('>>>>>+', ldevice.fb_name)
            objs.append(ldevice)
        return render(request, 'mainapp/connsfb.html', {'fb': name, 'lntype':lntype, 'objs': objs, 'title': 'Состав лог. устройств для экземпляра типа ЛУ '+str(name)})
        
        # проверим ИЭУ в которые входит данное лог устройство
    if type == 'inst_ld':
        print('try ld...')
        ld = LogicDevices.objects.get(name=name)
        ld_conns = PhDLDconnections.objects.all().filter(ld=ld.id)
        ied = list()
        for ld_conn in ld_conns:
            terminal1_ieds = Cabinets.objects.all().filter(terminal1=ld_conn.ied)
            for terminal1_ied in terminal1_ieds:
                ied.append({'name':'ИЭУ1', 'ied':str(ld_conn.ied), 'cab':terminal1_ied.name})
            terminal2_ieds = Cabinets.objects.all().filter(terminal2=ld_conn.ied)
            for terminal2_ied in terminal2_ieds:
                ied.append({'name':'ИЭУ2', 'ied':str(ld_conn.ied), 'cab':terminal2_ied.name})
            terminal3_ieds = Cabinets.objects.all().filter(terminal3=ld_conn.ied)
            for terminal3_ied in terminal3_ieds:
                ied.append({'name':'ИЭУ3', 'ied':str(ld_conn.ied), 'cab':terminal3_ied.name})
            ied = sorted(ied, key= lambda x: x['cab'] )
        return render(request, 'mainapp/connsied.html', {'ld': ld, 'ied': ied, 'title': 'Перечень ИЭУ, НКУ для лог. устройства '+str(ld)})

    return HttpResponse('error')

def help(request):
    page = request.GET.get('page')
    if page=='model':
        return render(request, 'mainapp/model.html', {'title': 'Документация', 'activeMain': '', 'activeHelp': 'active'})
    else:
        return render(request, 'mainapp/help.html', {'title': 'Документация', 'activeMain': '', 'activeHelp': 'active'})

