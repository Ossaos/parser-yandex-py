# Парсинг маршрутов яндекса с помощью python и HAR

## Получение данных по маршрутам

На данный момент поиск маршрутов производится в полуавтоматическом режиме. Это значит что необходима ручная подготовка информации для парсинга, производится она подбором определенного набора маршрутов с помощью сторонних сайтов, например:

1. wikroutes.info
2. кондуктор24.рф
3. eway24.ru

Когда мы знаем о существовании маршрута, нам нужно удостовериться в его наличии в базе яндекс карт.
Данные же мы будем получать с помощью анализа запросов,исходящих с сайта карт к базе данных яндекса. Посмотреть эти запросы можно на вкладке **сеть** инструментов разработчика.
Открыть панель инструментов разработчика можно с помощью F12.
