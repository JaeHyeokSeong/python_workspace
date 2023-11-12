# https://anweh.tistory.com/42

from geopy.geocoders import Nominatim
from __init__ import address_list, tags
import osmnx as ox

geolocator = Nominatim(user_agent='South Korea')


def get_address(address):
    geo = geolocator.geocode(address)
    crd = (geo.latitude, geo.longitude)
    # tuple 형태로 반환함
    return crd


if __name__ == '__main__':
    results = {}

    for address in address_list:
        crd = get_address(address)
        # dist 는 현재 주워진 crd 에서 반경 100m 의 모든 편의 시설을 찾는다
        pois = ox.features_from_point(crd, tags=tags, dist=100)
        pois_count = pois['amenity'].value_counts()
        results[address] = pois

    # 결과물 excel 파일에 저장 하기
    for key, value in results.items():
        value.to_excel(f'{key}_output.xlsx')
