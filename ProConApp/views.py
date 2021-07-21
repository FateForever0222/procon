import os
import math
import time
import zipfile

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from procon.myProCon.controller import ProCon
from ProConApp.models import Result, User
from django.utils import timezone


def index(request):
    return render(request, 'index\index.html')


def about(request):
    return render(request, 'about\\about.html')


def contact(request):
    return render(request, 'contact\contact.html')


def procon_web(request):
    return render(request, 'ProConWeb\ProConWeb.html')



def calculate(request):
    start = time.time()
    gap_percent = float(request.POST.get('input_gap'))
    pvalue1 = float(request.POST.get('input_p1'))
    pvalue2 = float(request.POST.get('input_p2'))
    groups = request.POST.get('groups')
    if groups is None:
        groups = '6 Groups'
    checked = request.POST.get('double_check')
    if checked is None:
        messages.error(request, 'Please double check!')
        return render(request, 'ProConWeb\ProConWeb.html')

    myFile = request.FILES.get("myfile", None)
    with open(os.path.join("upload", myFile.name), 'wb') as f:
        for i in myFile:
            f.write(i)
    pc = ProCon.ProCon("upload\\" + myFile.name, gap_percent, pvalue1, pvalue2)

    path = "ProConApp\static\result\\" + myFile.name + "\\"
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)
    pc.inf_to_file(path + "infResult.txt")
    pc.mut_to_file(path + "mutResult.txt")
    pc.tri_to_file(path + "triResult.txt")
    pc.graph_to_file(path + "Graph")

    z = zipfile.ZipFile("ProConApp\static\result\\" + myFile.name + "\result.zip", 'w', zipfile.ZIP_DEFLATED)
    filefullpath = os.path.join(path, 'infResult.txt')
    z.write(filefullpath, 'infResult.txt')
    filefullpath = os.path.join(path, 'triResult.txt')
    z.write(filefullpath, 'triResult.txt')
    filefullpath = os.path.join(path, 'mutResult.txt')
    z.write(filefullpath, 'mutResult.txt')
    filefullpath = os.path.join(path, 'Graph.png')
    z.write(filefullpath, 'Graph.png')
    z.close()

    dbin = Result(filename=myFile.name, inf=path + "infResult.txt", mut_inf=path + "mutResult.txt",
                  tri_inf=path + "triResult.txt", graph=path + "Graph.png", pub_date=timezone.now(),
                  creator_id=1, gap_percent=gap_percent, p1=pvalue1, p2=pvalue2)
    dbin.save()

    graph_path = path + "Graph.png"
    mut_obj = pc.get_mut_obj()
    gap_obj = pc.get_gap_lst()
    inf_obj = pc.get_inf()
    seq_obj = pc.get_seq()[0]
    inf_lst = []
    mut_inf_lst = []
    gap_lst = []
    seq_lst = []
    for i in range(0, pc.get_res_number()):
        tmplst = [mut_obj[i].get_site_1(), mut_obj[i].get_site_2(), mut_obj[i].get_mu_inf_12()]
        mut_inf_lst.append(tmplst)
        gap_lst.append(gap_obj[i][20] * 10000 // 1 / 10000)
    lst = []
    for i in range(1, pc.get_res_number() + 1):
        lst.append(i)

    for i in range(0, pc.get_res_number()):
        if gap_lst[i] > gap_percent:
            inf_lst.append(0.0)
        else:
            inf_lst.append(inf_obj[i])

    count = 1
    for i in range(0, pc.get_res_number()):
        seq_lst.append(str(count) + seq_obj[i])
        count += 1

    gap = pc.get_gap_lst()
    information_20 = pc.get_inf()
    seq = pc.get_seq()
    temp = list(enumerate(information_20))
    temp = sorted(temp, key=lambda x: x[1], reverse=True)
    sorted_origin_index = []
    for i in temp:
        sorted_origin_index.append(i[0])
    count = 1
    position_lst = []
    information_lst = []
    num_lst = []
    for i in sorted_origin_index:
        if gap[i][20] > gap_percent:
            continue
        else:
            num_lst.append(str(count))
            position_lst.append(str(i + 1) + str(seq[0][i]))
            information_lst.append(str(math.ceil(information_20[i] * 1000) / 1000))
            count = count + 1

    mut_num_lst = []
    mut_site1_lst = []
    mut_site2_lst = []
    mut_information_lst = []
    mul_list = []
    for i in range(len(pc.get_mut_inf())):
        pass
    for i in range(pc.get_res_number()):
        for j in range(pc.get_res_number()):
            mul_list.append([str(i + 1) + seq[0][i], str(j + 1) + seq[0][j], pc.get_mut_inf()[i][j]])
    temp = sorted(mul_list, key=lambda x: x[2], reverse=True)
    count = 1
    for i in temp:
        if i[2] > 10:
            mut_num_lst.append(str(count))
            mut_site1_lst.append(i[0])
            mut_site2_lst.append(i[1])
            mut_information_lst.append(str(math.ceil(i[2] * 100) / 100))
            count += 1
        else:
            break

    tri_num_lst = []
    tri_site1_lst = []
    tri_site2_lst = []
    tri_site3_lst = []
    count = 1
    for i in pc.get_triplets():
        tri_num_lst.append(str(count))
        tri_site1_lst.append(str(i.get_s1()) + seq[0][i.get_s1()])
        tri_site2_lst.append(str(i.get_s2()) + seq[0][i.get_s2()])
        tri_site3_lst.append(str(i.get_s3()) + seq[0][i.get_s3()])
        count += 1
    end = time.time()
    logtime = math.ceil((end - start) * 100) / 100

    return render(request, 'ProConWeb/ProConWebResult.html',
                  {'log_time': logtime, 'groups': groups, 'gap_percent': gap_percent, 'p1': pvalue1, 'p2': pvalue2,
                   'name': myFile.name, 'location': path,
                   'num_list': lst, 'inf_list': inf_lst, 'gap_list': gap_lst, 'seq': seq_lst,
                   'mut_inf_list': mut_inf_lst, 'filename': myFile.name,
                   'info_num_list': num_lst, 'position_list': position_lst, 'information_list': information_lst,

                   'mut_num_list': mut_num_lst, 'mut_site1_list': mut_site1_lst, 'mut_site2_list': mut_site2_lst,
                   'mut_information_list': mut_information_lst,
                   'tri_num_list': tri_num_lst, 'tri_site1_list': tri_site1_lst, 'tri_site2_list': tri_site2_lst,
                   'tri_site3_list': tri_site3_lst
                   })


def procon_java(request):
    return render(request, 'ProConJava\ProConJava.html')


def procon_python(request):
    return render(request, 'ProConPython\ProCon-python-userguide-V1.0.html')



def signin(request):
    first_name = request.POST.get('first_name')
    second_name = request.POST.get('second_name')
    user_name = request.POST.get('user_name')
    password = request.POST.get('password')
    email = request.POST.get('email')
    dbin = User(first_name=first_name, second_name=second_name, username=user_name,
                password=password, email=email, reg_date=timezone.now())
    try:
        dbin.save()
    except:
        return HttpResponse("Error")


def sign(request):
    return render(request, 'signin\sign.html')


def result(request):
    return render(request, 'ProConWeb\ProConWebResult.html')
