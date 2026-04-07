import requests
# city=0
def fetchweather(city):
    # print("hello")
    url=f"https://api.weatherapi.com/v1/current.json?key=8de5549662704b358a8143323260704&q={city}"
    try:
        response=requests.get(url)
        data=response.json()
        if response.status_code==200:
            location=data['location']['name']   
            temp=data['current'] ['temp_c']
            humidity=data['current'] ['humidity']
            condition=data['current'] ['condition'] ['text']

            return location,temp,condition,humidity
        else:
            print("no city found!!!")
#     except requests.exceptions.ConnetionTimeout:
#         print("no internet")
#     except Exception as e:
#         print(f"the error is: {e}")




# fetchweather()
# def main():
    # ask=0
    # while ask != "quit":
        # city=input("Enter the city of your choice (or quit): ")        
        # result=fetchweather(city)
        # if result:
            # location,temp,condition,humidity =result
            # print(f"{location}: {temp}*C, {humidity}%, {condition}")
        # ask=input("do you want to do another weather search?(y/quit): ")
# 
# main()







# ```
# {
#   "Transfer-Encoding": "chunked",
#   "Connection": "keep-alive",
#   "Vary": "Accept-Encoding",
#   "CDN-PullZone": "93447",
#   "CDN-RequestCountryCode": "GB",
#   "Age": "0",
#   "x-weatherapi-qpm-left": "10000000",
#   "CDN-ProxyVer": "1.50",
#   "CDN-RequestPullSuccess": "True",
#   "CDN-RequestPullCode": "200",
#   "CDN-CachedAt": "04/07/2026 14:37:45",
#   "CDN-EdgeStorageId": "1318",
#   "CDN-RequestId": "48bb3d86dc6ac2595c8b39d688fe9240",
#   "CDN-Cache": "MISS",
#   "CDN-Status": "200",
#   "CDN-RequestTime": "0",
#   "Cache-Control": "public, max-age=180",
#   "Content-Type": "application/json",
#   "Date": "Tue, 07 Apr 2026 14:37:45 GMT",
#   "Server": "BunnyCDN-FR1-1320"
# }

# {
#     "location": {
#         "name": "Mumbai",
#         "region": "Maharashtra",
#         "country": "India",
#         "lat": 18.975,
#         "lon": 72.826,
#         "tz_id": "Asia/Kolkata",
#         "localtime_epoch": 1775572641,
#         "localtime": "2026-04-07 20:07"
#     },
#     "current": {
#         "last_updated_epoch": 1775572200,
#         "last_updated": "2026-04-07 20:00",
#         "temp_c": 28.2,
#         "temp_f": 82.8,
#         "is_day": 0,
#         "condition": {
#             "text": "Mist",
#             "icon": "//cdn.weatherapi.com/weather/64x64/night/143.png",
#             "code": 1030
#         },
#         "wind_mph": 8.3,
#         "wind_kph": 13.3,
#         "wind_degree": 284,
#         "wind_dir": "WNW",
#         "pressure_mb": 1011.0,
#         "pressure_in": 29.85,
#         "precip_mm": 0.0,
#         "precip_in": 0.0,
#         "humidity": 70,
#         "cloud": 50,
#         "feelslike_c": 31.4,
#         "feelslike_f": 88.4,
#         "windchill_c": 27.3,
#         "windchill_f": 81.2,
#         "heatindex_c": 29.8,
#         "heatindex_f": 85.6,
#         "dewpoint_c": 21.5,
#         "dewpoint_f": 70.7,
#         "vis_km": 5.0,
#         "vis_miles": 3.0,
#         "uv": 0.0,
#         "gust_mph": 11.6,
#         "gust_kph": 18.6,
#         "air_quality": {
#             "co": 158.85,
#             "no2": 4.55,
#             "o3": 150.0,
#             "so2": 22.25,
#             "pm2_5": 26.85,
#             "pm10": 44.95,
#             "us-epa-index": 2,
#             "gb-defra-index": 3
#         },
#         "short_rad": 0,
#         "diff_rad": 0,
#         "dni": 0,
#         "gti": 0
#     }
# }
# ```

# this is the json responce
