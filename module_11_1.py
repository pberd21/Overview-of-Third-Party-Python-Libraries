import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts')

if response.status_code == 200:
    posts = response.json()
    print(posts[:5])
else:
    print("Ошибка при запросе:", response.status_code)
#Методы/функции:
#requests .get (): отправляет GET-запрос.
#response. status_code: проверяет статус код ответа.
#response. json(): преобразует ответ в формат JSON.