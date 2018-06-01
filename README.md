# python-test-profi

Задача состоит из двух подчастей. Необходимо самостоятельно формализовать задачу, придумать структуры данных, форматы, модульность, интерфейс (без деталей) и всё остальное, что может понадобиться для реального применения вашего решения этой вполне реальной задачи. Итак:
 
С типовой формы заказа (такой как на главной странице repetitors.info) в базу данных поступают заполненные бланки, содержащие, в частности, графу «номер телефона». Содержимое этой графы — строка, полнейший user input, никак не структурированный, не отфильтрованный и способный содержать всё что угодно в каком угодно виде, но где-то там в этой строке пользователь наверняка указал в том числе и свой номер телефона (или несколько).
Необходимо аккуратно распарсить этот user input, чтобы вытащить оттуда все номера телефонов и привести их к каноническому виду:
8KKKNNNNNNN (например, 89031110022)
Все номера по формату российские. Код города по умолчанию (для прямых номеров) считать заданным (например, пусть будет 495). 
 
При поступлении нового заказа менеджеру нужно знать, есть ли в базе другие заказы от этого же клиента. Это могут быть дубликаты того же заказа, предыдущие старые заказы этого клиента и пр. — не важно. Важно то, что будем для простоты считать, что клиент идентифицируется только по номерам телефона. Нужно придумать и описать (словами) механизм поиска заказов от того же клиента, что прислал заданный заказ. В описании должны присутствовать: общая идея решения, структура БД, характерные запросы.
Сразу уточним, что задача хоть и небольшая (рассчитана на пару часов работы и пару страниц кода), но весьма непростая, т.к. требует самостоятельного нахождения всех возможных подвохов (особенно в первой части) и создания оптимальных универсальных структур данных и кода. Предполагаем, что база данных большая, обращений к скрипту много, и вообще всё живёт в условиях почти high load. 
 
UPD: «Пара страниц» — это буквально пара страниц. Решения в 100 файлов суммарным объёмом 500 кб невозможно проверить. Решения, использующие разные мудрёные фреймворки, также невозможно проверить. Чистый код, стандартные библиотеки — для задачки на пару страниц этого более чем достаточно.