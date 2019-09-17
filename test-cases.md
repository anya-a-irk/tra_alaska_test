## Предварительные условия для каждого тест-кейса:

docker azshoo/alaska с сервисом развернут и корректно функционирует (```docker run -p 8091:8091 -it azshoo/alaska:1.0```), база пуста.

## Тест-кейсы
### Тест-кейс № 1. Обратиться к /info

**Шаги:**


1. Отправить GET запрос (```curl -X GET -i 'http://172.17.0.1:8091/info'```)



**Ожидаемый результат**

```status code 200; Welcome to Alaska! This is CRUD service for bears in alaska. CRUD routes presented with REST naming notation: POST /bear - create GET /bear - read all bears GET /bear/:id - read specific bear PUT /bear/:id - update specific bear DELETE /bear - delete all bears DELETE /bear/:id - delete specific bear Example of ber json: {"bear_type":"BLACK","bear_name":"mikhail","bear_age":17.5}. Available types for bears are: POLAR, BROWN, BLACK and GUMMY.```

### Тест-кейс № 2. Cоздать медведя одного из типов со всеми заполненными полями

**Шаги:**

1. Отправить POST запрос с данными медведя (см "Ожидаемый результат")
2. Отправить GET запрос (```curl -X GET -i 'http://172.17.0.1:8091/bear'```)



**Ожидаемый результат**

|Вводимое значение | Ожидаемый результат | Полученный результат | Status |
| --- | --- | --- | --- |
| ```curl -X POST -i 'http://172.17.0.1:8091/bear' --data '{"bear_type":"POLAR","bear_name":"MISHA","bear_age":13}'```| ```status code 200; 1;  [{"bear_id":1,"bear_type":"POLAR","bear_name":"MISHA","bear_age":13}]```| ```status code 200; 1;  [{"bear_id":1,"bear_type":"POLAR","bear_name":"MISHA","bear_age":13.0}]```| PASS |
| ```curl -X POST -i 'http://172.17.0.1:8091/bear' --data '{"bear_type":"BROWN","bear_name":"MISHA","bear_age":13}'``` | ```status code 200; 1; [{"bear_id":1,"bear_type":"BROWN","bear_name":"MISHA","bear_age":13}]``` | ```status code 200; 1; [{"bear_id":1,"bear_type":"BROWN","bear_name":"MISHA","bear_age":13.0}]``` |  PASS |
| ```curl -X POST -i 'http://172.17.0.1:8091/bear' --data '{"bear_type":"BLACK","bear_name":"MISHA","bear_age":13}'``` | ```status code 200; 1; [{"bear_id":1,"bear_type":"BLACK","bear_name":"MISHA","bear_age":13}]``` | ```status code 200; 1; [{"bear_id":1,"bear_type":"BLACK","bear_name":"MISHA","bear_age":13.0}]``` | PASS |
| ```curl -X POST -i 'http://172.17.0.1:8091/bear' --data '{"bear_type":"GUMMY","bear_name":"MISHA","bear_age":13}'``` | ```status code 200; 1; [{"bear_id":1,"bear_type":"GUMMY","bear_name":"MISHA","bear_age":13}]``` | ```status code 200; 1; [{"bear_id":1,"bear_type":"UNKNOWN","bear_name":"EMPTY_NAME","bear_age":0.0}]```  | <mark> FAILED <mark> |

### Тест-кейс № 3. Cоздать медведя с незаполненными полями

**Шаги:**


1. Отправить POST запрос с данными медведя (см "Ожидаемый результат")



**Ожидаемый результат**

|Вводимое значение | Ожидаемый результат |
| --- | --- |
| ```curl -X POST -i 'http://172.17.0.1:8091/bear' --data '{"bear_name":"MISHA","bear_age":13}'```| ```status code 200; Error. Pls fill all parameters```
| ```curl -X POST -i 'http://172.17.0.1:8091/bear'  --data '{"bear_type":"POLAR","bear_age":13}'``` | ```status code 200; Error. Pls fill all parameters``` |
| ```curl -X POST -i 'http://172.17.0.1:8091/bear'  --data '{"bear_type":"BROWN","bear_age":13}'``` | ```status code 200; Error. Pls fill all parameters``` |
| ```curl -X POST -i 'http://172.17.0.1:8091/bear' --data '{"bear_type":"BLACK","bear_age":13}'``` | ```status code 200; Error. Pls fill all parameters``` |
| ```curl -X POST -i 'http://172.17.0.1:8091/bear' --data '{"bear_type":"GUMMY","bear_age":13}'``` | ```status code 200; Error. Pls fill all parameters```|
| ```curl -X POST -i 'http://172.17.0.1:8091/bear' --data '{"bear_type":"POLAR","bear_name":"MISHA"}'``` | ```status code 200; Error. Pls fill all parameters```|
| ```curl -X POST -i 'http://172.17.0.1:8091/bear' --data '{"bear_type":"BROWN","bear_name":"MISHA"}'``` | ```status code 200; Error. Pls fill all parameters```|
| ```curl -X POST -i 'http://172.17.0.1:8091/bear' --data '{"bear_type":"BLACK","bear_name":"MISHA"}'``` | ```status code 200; Error. Pls fill all parameters```|
| ```curl -X POST -i 'http://172.17.0.1:8091/bear' --data '{"bear_type":"GUMMY","bear_name":"MISHA"}'``` | ```status code 200; Error. Pls fill all parameters```|

### Тест-кейс № 4. Cоздать медведя с типом не пренадлежащим POLAR, BROWN, BLACK или GUMMY

**Шаги:**


1. Отправить POST запрос с данными медведя (```curl -X POST -i 'http://172.17.0.1:8091/bear' --data '{"bear_type":"RED","bear_name":"misha","bear_age":20}'```)



**Ожидаемый результат**

```status code 500 ```


### Тест-кейс № 5. Удалить всех медведей

**Шаги:**

1. Создать несколько медведей (отправить POST запросы с данными каждого медведя 
+ ```curl -X POST -i 'http://172.17.0.1:8091/bear' --data '{"bear_type":"POLAR","bear_name":"MISHA","bear_age":13}'```
+ ```curl -X POST -i 'http://172.17.0.1:8091/bear' --data '{"bear_type":"BROWN","bear_name":"MISHA","bear_age":13}'```
+ ```curl -X POST -i 'http://172.17.0.1:8091/bear' --data '{"bear_type":"BLACK","bear_name":"MISHA","bear_age":13}'```
2. Отправить DELETE запрос на удаление медведей (```curl -X DELETE -i 'http://172.17.0.1:8091/bear'```)
3. Отправить GET запрос (```curl -X GET -i 'http://172.17.0.1:8091/bear'```)



**Ожидаемый результат**

```status code 200; [] ```

### Тест-кейс № 6. Удалить существующего медведя

**Шаги:**


1. Создать медведя (отправить POST запрос с данными медведя 
```curl -X POST -i 'http://172.17.0.1:8091/bear' --data '{"bear_type":"POLAR","bear_name":"MISHA","bear_age":13}'```
2. Отправить DELETE запрос на удаление медведя с существующим id(```curl -X DELETE -i 'http://172.17.0.1:8091/bear/1'```)
3. Отправить GET запрос (```curl -X GET -i 'http://172.17.0.1:8091/bear'```)

**Ожидаемый результат**

```status code 200; [] ```

### Тест-кейс № 7. Удалить несуществующего медведя

**Шаги:**


1. Отправить DELETE запрос на удаление медведя с несуществующим (```curl -X DELETE -i 'http://172.17.0.1:8091/bear/150'```)

**Ожидаемый результат**

```status code 404; 'Such bear not found'```

### Тест-кейс № 8. Получить список всех медведей

**Шаги:**


1. Создать несколько медведей (отправить POST запрос с данными медведя 
+ ```curl -X POST -i 'http://172.17.0.1:8091/bear' --data '{"bear_type":"POLAR","bear_name":"MISHA","bear_age":13}'```
+ ```curl -X POST -i 'http://172.17.0.1:8091/bear' --data '{"bear_type":"BROWN","bear_name":"MISHA","bear_age":13}'```
+ ```curl -X POST -i 'http://172.17.0.1:8091/bear' --data '{"bear_type":"BLACK","bear_name":"MISHA","bear_age":13}'```
2. Отправить GET запрос (```curl -X GET -i 'http://172.17.0.1:8091/bear'```)



**Ожидаемый результат**

```[{"bear_id":1,"bear_type":"POLAR","bear_name":"MISHA","bear_age":13.0},{"bear_id":2,"bear_type":"BROWN","bear_name":"MISHA","bear_age":13.0},{"bear_id":3,"bear_type":"BLACK","bear_name":"MISHA","bear_age":13.0}]```


### Тест-кейс № 9. Получить информацию о существующем медведе

**Шаги:**


1. Создать медведя (отправить POST запрос с данными медведя 
```curl -X POST -i 'http://172.17.0.1:8091/bear' --data '{"bear_type":"POLAR","bear_name":"MISHA","bear_age":13}'```
2. Отправить GET запрос (```curl -X GET -i 'http://172.17.0.1:8091/bear/1'```)

**Ожидаемый результат**

```[{"bear_id":1,"bear_type":"POLAR","bear_name":"MISHA","bear_age":13}]```

### Тест-кейс № 10. Получить информацию о несуществующем медведе

**Шаги:**


1. Отправить GET запрос (```curl -X GET -i 'http://172.17.0.1:8091/bear/120'```)

**Ожидаемый результат**

```status code 200; EMPTY```

### Тест-кейс № 11. Получить информацию об удаленном медведе

**Шаги:**


1. Создать медведя (отправить POST запрос с данными медведя 
```curl -X POST -i 'http://172.17.0.1:8091/bear' --data '{"bear_type":"POLAR","bear_name":"MISHA","bear_age":13}'```
2. Удалить медведя (отправить DELETE запрос с данными медведя 
```curl -X DELETE -i 'http://172.17.0.1:8091/bear/1'```
3. Отправить GET запрос (```curl -X GET -i 'http://172.17.0.1:8091/bear/1'```)

**Ожидаемый результат**

```status code 200; EMPTY```

### Тест-кейс № 12. Обновить информацию о существующем медведе

**Шаги:**


1. Создать медведя (отправить POST запрос с данными медведя 
```curl -X POST -i 'http://172.17.0.1:8091/bear' --data '{"bear_type":"POLAR","bear_name":"MISHA","bear_age":13}'```)
2. Обновить информацию о медведе (отправить PUT запрос с новыми данными медведя 
```curl -X PUT -i 'http://172.17.0.1:8091/bear/1' --data '{"bear_type":"BLACK","bear_name":"mikhail","bear_age":17.5}' ```)
3. Отправить GET запрос (```curl -X GET -i 'http://172.17.0.1:8091/bear/1'```)

**Ожидаемый результат**

```status code 200; [{"bear_id":1,"bear_type":"BLACK","bear_name":"mikhail","bear_age":17.5}]```

**Полученный результат**

```status code 200; [{"bear_id":1,"bear_type":"POLAR","bear_name":"mikhail","bear_age":13.0}]```

**STATUS** : <span style="background-color: #FF0000">FAILED</span>

### Тест-кейс № 13. Обновить информацию о несуществующем медведе

**Шаги:**


1. Обновить информацию о несуществующем медведе (отправить PUT запрос с новыми данными медведя 
```curl -X PUT -i 'http://172.17.0.1:8091/bear/20' --data '{"bear_type":"BLACK","bear_name":"mikhail","bear_age":17.5}' ```)


**Ожидаемый результат**

```status code 200; []```

### Тест-кейс № 14. Отправить запрос по адресу, не указанному в /info

**Шаги:**


1. Отправить запрос по адресу, неуказанному в /info
```curl -X PUT -i 'http://172.17.0.1:8091/bear_info```


**Ожидаемый результат**

```404 Not Found```
