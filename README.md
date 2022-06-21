На просторах сети нашёл задачу из тестового задания. Было интересно реализовать.



# Подбор похожих доменов
## Использование
python main.py [-h] -kw KEYWORD [KEYWORD ...] [-dz DOMAIN-ZONE [DOMAIN-ZONE ...]]

## Задача
Для оперативного поиска фишинговых ресурсов может применяться следующая
логика:
- составляется первичный набор ключевых слов, ассоциирующихся с целевой
компанией
- при помощи набора стратегий (например, одна из них — подстановка схожих
по написанию символов) формируется расширенный набор ключевых слов
- полученное на предыдущем шаге множество перемножается на некоторое
множество доменных зон (ru, com, net, org, biz и т. п.)
- отправляются dns-запросы с целью получить IP-адрес по каждому из
элементов списка
- домены, по которым удалось определить ip, попадают в отчет

В рамках задания необходимо разработать консольное приложение, решающее
описанную выше задачу. Входные данные — набор ключевых слов, результат —
список доменов с ip-адресом. Стратегии формирования набора ключевых слов
описаны в табл.1. Список доменных зон для подстановки представлен ниже.
DNS-запросы должны отправляться параллельно.

|                         Стратегия                            | Входное слово |                                Выходные слова                               |
| ------------------------------------------------------------ | ------------- | --------------------------------------------------------------------------- |
| Добавление одного символа <br />в конец строки               |   group-ib    | group-iba <br />group-ibb <br />group-ibc <br />...                         |
| Подстановка символа, <br />схожего по написанию (homoglyph)  |   group-ib    | gr0up-ib <br />group-1b <br />gr0up-1b                                      |
| Выделение поддомена, <br />т. е. добавление точки            |   group-ib    | group-i.b <br />grou.p-ib <br />gro.up-ib <br />gr.oup-ib <br />g.roup-ib   |
| Удаление одного символа                                      |   group-ib    | group-i <br />group-b <br />groupib <br />grou-ib <br />...                 |

Список доменных зон: <br />
com, ru, net, org, info, cn, es, top, au, pl, it, uk, tk, ml, ga, cf, us, xyz, top, site, win, bid
