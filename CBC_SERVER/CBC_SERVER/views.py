from django.http import JsonResponse

response_data = {}
response_data['result'] = 'error'


def test(resuest):
    print("test")
    return JsonResponse({'Hello': 'CBC'})
