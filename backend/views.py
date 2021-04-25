from django.shortcuts import render

from django.http import JsonResponse

import os
import random

import json
import excel2json
import pandas
import shortuuid


# Create your views here.

def randommatch(request):
    # BASE_DIR = Path(__file__).resolve().parent.parent
    file = random.choice(os.listdir("JSON"))
    print(file)
    with open("JSON/" + file) as f:
        data = json.load(f)
    return JsonResponse(data, safe=False)


def getcredit(request):
    excel_data_df = pandas.read_excel(
        'Excel/IPL_Data.xlsx', sheet_name='players')
    json_str = excel_data_df.to_json()
    data = eval(json_str)
    arr = []
    for key in data["Players"]:
        arr.append({"name": data["Players"][key],
                    "credit": data["Credit Value"][key],
                    "id": shortuuid.uuid(),
                    "points": 0
                    })
    print(arr)
    print("Excel to Json", arr)
    return JsonResponse(arr, safe=False)
