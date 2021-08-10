# catanddog-microservice
 catanddog-microservice
 

1. Микросервис, разработанный на FastAPI, представляет собой фреймворк, работающий с RestAPI. FastAPI-это современная, быстрая (высокопроизводительная) веб-платформа для создания API с Python 3.6+ на основе стандартных подсказок типа Python. Чтобы запустить приложение, напишите команду uvicorn app. main:app --reload, и у вас будет Api с адресом 127.0.0.1:8000, Еще тут есть SwaggerUI, /docs - также можете увидеть структуру методов
2. В качестве классификатора я взял готовую модель с github, которая примерно хорошо определяет. И модель работает на фреймворке Tensorflow.Keras. Чтобы делать прогнозы, вам нужно ввести json данные по этой ссылке /classifier/{photos}
3. Структура ввода:
{
  "photos": [
    {
      "ID": "string",
      "img_code": "string"
    }
  ]
}
4. А вывод:
{
  "results": [
    {
      "ID": "string",
      "cat_prob": float,
      "dog_prob": float
    }
  ]
}
5. После этого модель была оценена, и было сделано несколько визуализаций, показывающих инсайты из выборки данных.
![image](https://user-images.githubusercontent.com/54392243/128825010-27e8d571-dce1-457a-a917-b02b8ec319d7.png)
![image](https://user-images.githubusercontent.com/54392243/128825090-07b6b025-8f83-467b-9e17-978ab841b60d.png)
![image](https://user-images.githubusercontent.com/54392243/128825114-0a02b8f4-f4d9-4937-b139-b075f50e82c0.png)
![image](https://user-images.githubusercontent.com/54392243/128825152-e3560e19-6b84-410f-98d2-c419a827bbe8.png)
![image](https://user-images.githubusercontent.com/54392243/128825188-83af4c5c-17c7-44c9-bbb2-c7a94eb29fa8.png)
![image](https://user-images.githubusercontent.com/54392243/128825217-f8e87788-ed5f-411b-bc43-d0a02a1268d5.png)

 
Микро-сервис «Котопёс»
Задача:
1. Скачать из open-source ресурсов 500 изображении кошек и 500 изображении собак.
2. Написать микро-сервис на любом удобном фреймворке, который будет принимать на вход JSON с массивом из изображении в формате BASE64
3. Применить любую open-source классификационную модель, которая умеет определять животное на фотографии (cat or dog)
4. На выходе получить JSON с id фотографии и вероятностью классификационной модели
5. Полученный результат экспортировать в excel файл и проанализировать точность модели. Результаты показать в виде сводных и диаграмм.
6. Загрузить проект в GitHub.

INPUT:

![image](https://user-images.githubusercontent.com/54392243/128649189-876dc065-104f-465f-bd29-cc6327ab241a.png)

OUTPUT:

![image](https://user-images.githubusercontent.com/54392243/128649195-9d227abc-4c18-40ed-afce-95246984c724.png)


