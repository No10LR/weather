#coding=utf-8
from urllib2 import urlopen
from urllib2 import Request
import re
import json
import time

xttime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def getweather():
    apicity=raw_input('输入查询的城市')
    weatherapi = 'https://free-api.heweather.com/v5/weather?city=yourcity&key=yourkey'
    # 天气的原始api
    kwapi=weatherapi.replace('yourkey','c40da344f3714ed28819c02d8b3485ae')
    # 使用replace替代，接口的key
    cityinfo = re.compile('yourcity')
    cwapi = cityinfo.sub(apicity,kwapi)
    # 使用正则表达式替代，查询城市
    # print cwapi
    req = Request(cwapi)
    #发送请求
    resp = urlopen(req).read()
    # print resp
    return resp
fwapi =getweather()

def getjson():
    json_data = json.loads(fwapi)
    # print json_data
    data = json_data['HeWeather5'][0]
    # print data
    return data
weatherdata = getjson()

def alldata():
    try:
       pm25 = weatherdata['aqi']['city']['pm25']
       qlty = weatherdata['aqi']['city']['qlty']
       #空气质量
       # print pm25
       # print qlty
    except:
        pm25 = 'null'
        qlty = 'null'
    city = weatherdata['basic']['city']
    updatetime = weatherdata['basic']['update']['loc']

    #当天
    daily_forecast =weatherdata['daily_forecast'][0]
    sr1 = daily_forecast['astro']['sr']
    ss1 = daily_forecast['astro']['ss']
    #日出日落
    datetime1 = daily_forecast['date']
    hum1 = daily_forecast['hum']
    #相对湿度
    pop1 = daily_forecast['pop']
    #降水概率
    tmpmax1 = daily_forecast['tmp']['max']
    tmpmin1 = daily_forecast['tmp']['min']
    #温度
    uv1 = daily_forecast['uv']
    #紫外线
    vis1 = daily_forecast['vis']
    #能见度
    winddir1 = daily_forecast['wind']['dir']
    windsc1 = daily_forecast['wind']['sc']
    windspd1 = daily_forecast['wind']['spd']
    #风向，风速，风级

    #明天
    daily_forecast =weatherdata['daily_forecast'][1]
    sr2 = daily_forecast['astro']['sr']
    ss2 = daily_forecast['astro']['ss']
    #日出日落
    datetime2 = daily_forecast['date']
    hum2 = daily_forecast['hum']
    #相对湿度
    pop2 = daily_forecast['pop']
    #降水概率
    tmpmax2 = daily_forecast['tmp']['max']
    tmpmin2 = daily_forecast['tmp']['min']
    #温度
    uv2 = daily_forecast['uv']
    #紫外线
    vis2 = daily_forecast['vis']
    #能见度
    winddir2 = daily_forecast['wind']['dir']
    windsc2 = daily_forecast['wind']['sc']
    windspd2 = daily_forecast['wind']['spd']
    #风向，风速，风级

    #后天
    daily_forecast =weatherdata['daily_forecast'][2]
    sr3 = daily_forecast['astro']['sr']
    ss3 = daily_forecast['astro']['ss']
    #日出日落
    datetime3 = daily_forecast['date']
    hum3 = daily_forecast['hum']
    #相对湿度
    pop3 = daily_forecast['pop']
    #降水概率
    tmpmax3 = daily_forecast['tmp']['max']
    tmpmin3 = daily_forecast['tmp']['min']
    #温度
    uv3 = daily_forecast['uv']
    #紫外线
    vis3 = daily_forecast['vis']
    #能见度
    winddir3 = daily_forecast['wind']['dir']
    windsc3 = daily_forecast['wind']['sc']
    windspd3 = daily_forecast['wind']['spd']
    #风向，风速，风级

    #小时预报
    hourly_forecast = weatherdata['hourly_forecast'][0]
    condtxt = hourly_forecast['cond']['txt']
    hourly_forecastdate = hourly_forecast['date']
    hourly_forecasthum = hourly_forecast['hum']
    hourly_forecastpop = hourly_forecast['pop']
    hourly_forecasttmp = hourly_forecast['tmp']
    hourly_forecastwinddir = hourly_forecast['wind']['dir']
    hourly_forecastwindsc = hourly_forecast['wind']['sc']
    hourly_forecastwindspd = hourly_forecast['wind']['spd']

    nowcondtxt = weatherdata['now']['cond']['txt']
    #天气状况 ：多云
    nowfl = weatherdata['now']['fl']
    #体感
    nowhum =weatherdata['now']['hum']
    nowtmp = weatherdata['now']['tmp']
    nowwinddir = weatherdata['now']['wind']['dir']
    nowwindsc = weatherdata['now']['wind']['sc']
    nowwindspd = weatherdata['now']['wind']['spd']

    status = weatherdata['status']
    #获取信息状态
    return pm25,qlty,city,updatetime,sr1,sr2,sr3,ss1,ss2,ss3,datetime1,datetime2,datetime3,hum1,hum2,hum3,pop1,pop2,pop3,tmpmax1,tmpmax2,tmpmax3,tmpmin1,tmpmin2,tmpmin3,uv1,uv2,uv3,vis1,vis2,vis3,winddir1,winddir2,winddir3,windsc1,windsc2,windsc3,windspd1,windspd2,windspd3,condtxt,hourly_forecastdate,hourly_forecasthum,hourly_forecastpop,hourly_forecasttmp,hourly_forecastwinddir,hourly_forecastwindsc,hourly_forecastwindspd,nowcondtxt,nowfl,nowhum,nowtmp,nowwinddir,nowwindsc,nowwindspd,status

tupleweather=alldata()

def view():
    # pm25=tupleweather[0]
    # qlty=tupleweather[1]
    # city=tupleweather[2]
    # updatetime=tupleweather[3]
    # sr1=tupleweather[4]
    # sr2=tupleweather[5]
    # sr3=tupleweather[6]
    # ss1=tupleweather[7]
    # ss2=tupleweather[8]
    # ss3=tupleweather[9]
    # datetime1=tupleweather[10]
    # datetime2=tupleweather[11]
    # datetime3=tupleweather[12]
    # hum1=tupleweather[13]
    # hum2=tupleweather[14]
    # hum3=tupleweather[15]
    # pop1=tupleweather[16]
    # pop2=tupleweather[17]
    # pop3=tupleweather[18]
    # tmpmax1=tupleweather[19]
    # tmpmax2=tupleweather[20]
    # tmpmax3=tupleweather[21]
    # tmpmin1=tupleweather[22]
    # tmpmin2=tupleweather[23]
    # tmpmin3=tupleweather[24]
    # uv1=tupleweather[25]
    # uv2=tupleweather[26]
    # uv3=tupleweather[27]
    # vis1=tupleweather[28]
    # vis2=tupleweather[29]
    # vis3=tupleweather[30]
    # winddir1=tupleweather[31]
    # winddir2=tupleweather[32]
    # winddir3=tupleweather[33]
    # windsc1=tupleweather[34]
    # windsc2=tupleweather[35]
    # windsc3=tupleweather[36]
    # windspd1=tupleweather[37]
    # windspd2=tupleweather[38]
    # windspd3=tupleweather[39]
    # condtxt=tupleweather[40]
    # hourly_forecastdate=tupleweather[41]
    # hourly_forecasthum=tupleweather[42]
    # hourly_forecastpop=tupleweather[43]
    # hourly_forecasttmp=tupleweather[44]
    # hourly_forecastwinddir=tupleweather[45]
    # hourly_forecastwindsc=tupleweather[46]
    # hourly_forecastwindspd=tupleweather[47]
    # nowcondtxt=tupleweather[48]
    # nowfl=tupleweather[49]
    # nowhum=tupleweather[50]
    # nowtmp=tupleweather[51]
    # nowwinddir=tupleweather[52]
    # nowwindsc=tupleweather[53]
    # nowwindspd=tupleweather[54]
    # status=tupleweather[55]

    print tupleweather[54]

view()


