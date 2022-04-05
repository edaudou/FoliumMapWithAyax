from atexit import register
from calendar import c
from logging import PlaceHolder
from operator import ge
from pickletools import markobject
from statistics import geometric_mean
from tokenize import group
from turtle import color
from django.shortcuts import render
from django.http import HttpResponse
import folium
import datetime
import pandas as pd
import geopandas as gpd
from folium.plugins import MousePosition
import json
from .models import Group, Person

# Create your views here.
def index(request):
    template='index.html'
    return render(request,template)

def map(request):
    if request.method == 'POST':
        lng = request.POST.get('lng',None)
        lat = request.POST.get('lat',None)
        print("LA LATITUD ES ", lat, " Y LA LONGITUD ES ", lng)

    # Create map
    m=folium.Map(location=[42.4739, -2.4300],zoom_start=12 )

    # Una variable de la fecha actual
    now = datetime.datetime.now()

    #Variables con el tiempo de caducidad
    d1cad = datetime.datetime(2022, 3, 5)
    d2cad = datetime.datetime(2022, 2, 11)
    d3cad = datetime.datetime(2022, 5, 26)
    d4cad = datetime.datetime(2022, 5, 3)
    d5cad= datetime.datetime(2022, 3, 25)


    #Variables con fuciones para el click y posicion
    mposition=MousePosition()
    clickmarker=folium.ClickForMarker()
    
    #Listas para el dataframe
    listcad=[d1cad,d2cad,d3cad,d4cad,d5cad]
    long=[-2.4306285381317134,-2.4276190996170044,-2.4198567867279053,-2.4306285381317134,-2.4384]
    lat=[42.4677759035072,42.45435593416059,42.46366038267497,42.4877759035072, 42.4577]
    nombres=['Hospital San Pedro', 'Hospital San Lorenzo', "Hospital San Atilano", "Hospital Central", "Hospital San Marino"]

    #Dataframe con datos
    df=pd.DataFrame()
    df['Caducidad']=listcad
    df['Longitud']=long
    df['Latitud']=lat
    df['Nombre']=nombres
    #Contains long and lat on a variable
    geometry=gpd.points_from_xy(df.Longitud, df.Latitud)
    #Group it in the geoDataFrame
    geo_df = gpd.GeoDataFrame(df[['Caducidad','Nombre']],geometry=geometry)
    print(geo_df)
    # Create a geometry list from the GeoDataFrame
    geo_df_list = [[point.xy[1][0], point.xy[0][0]] for point in geo_df.geometry]

    
    # Iterate through list and add a marker for each, color-coded by its date.
    i = 0
    for coordinates in geo_df_list:
    #assign a color marker for the date 
        if geo_df.Caducidad[i] > now:
            type_color = "green"
        elif geo_df.Caducidad[i] < now:
            type_color = "red"
    # Place the markers with the popup labels and data
        m.add_child(folium.Marker(location = coordinates, popup =
        str(geo_df.Nombre[i]) +"<br>" +"Caducidad: " + str(geo_df.Caducidad[i]),tooltip="Click para mas detalles",
        icon = folium.Icon(color = type_color)))
    #Añadir las funciones (clickformarker,position)
        clickmarker.add_to(m)
        mposition.add_to(m)
        i = i + 1

    #Get html represetation of the map
    m=m._repr_html_()
    context={
        'm':m
    }
    template='map.html'
    return render(request,template,context)

def people(request):
    allperson=Person.objects.all()
    html=''
    groups=Person.objects.all().filter(group__name='Preparacion mapas')
    for person in allperson:
        html+="NAME= "+person.first_name+" "+person.last_name+" <br> DATE OF BIRTH= "+str(person.birth_date) +" <br>"+str(person.group)+"<br><br>"    
    template='people.html'
    print(allperson)
    context={
        'personas':allperson
    }
    return render(request,template,context)
