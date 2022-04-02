- [Кен Томпсон](#orgcb2db97)
  - [ ](#org015b86f)
  - [Томпсон](#org99d93e8)
- [print](#orga665f0e)
- [Чуть лучше чем принт](#org7ddc253)
- [PDB](#orga51c438)
  - [myobj.py](#orga662a13)
  - [\_](#org360f7af)
- [PDB](#org24a02b6)
- [PDB](#org4f01f3c)
- [PDB](#org67b43e2)
- [PDB](#orgdda4469)
- [PDB](#org59c5cc4)
- [PuDB](#orgff4e16b)
- [runserver\_plus](#orge68f16c)



<a id="orgcb2db97"></a>

# Кен Томпсон


<a id="org015b86f"></a>

##       :B_block:BMCOL:

<span class="underline"><span class="underline">[Wiki](https://ru.wikipedia.org/wiki/%25D0%25A2%25D0%25BE%25D0%25BC%25D0%25BF%25D1%2581%25D0%25BE%25D0%25BD,_%25D0%259A%25D0%25B5%25D0%25BD)</span></span>


<a id="org99d93e8"></a>

## Томпсон     :B_block:BMCOL:

![img](Thompson.jpg)


<a id="orga665f0e"></a>

# print

> Сейбел: Какие инструменты вы используете при отладке?
>
> Томпсон: В основном вывод на печать. При разработке программы я размещаю очень много операторов вывода на печать.


<a id="org7ddc253"></a>

# Чуть лучше чем принт

<span class="underline"><span class="underline">[logging](https://docs.python.org/3/library/logging.html)</span></span>

-   Во время разработки можно выводить сообщения на экран
-   В продакшене, пишем сообщения уже в логгер (syslog, просто в файл)
-   Можем настраивать режими отладки


<a id="orga51c438"></a>

# PDB


<a id="orga662a13"></a>

## myobj.py     :B_block:

```python
from dataclasses import dataclass
@dataclass
class MyObj:
    n: int
    def go(self):
        for i in range(self.n):
            print(i)
if __name__ == "__main__":
    MyObj(5).go()
```


<a id="org360f7af"></a>

## \_     :B_ignoreheading:

```shell
python -m pdb ./myobj.py
```


<a id="org24a02b6"></a>

# PDB

Можно вызвать в рамках Python-сессии

```python
import pdb
from myobj import MyObj

pdb.run("MyObj(5).go()")
```


<a id="org4f01f3c"></a>

# PDB

Чаще всего может потребоваться перейти в режим отладки в определённом месте программы

```python
# тут какой-то код
def main(request):
    import pdb # ipdb
    pdb.set_trace() # ipdb.set_trace()
    data = request.GET
# дальше много кода
```


<a id="org67b43e2"></a>

# PDB

```python
try:
    some_code()
except:
    import sys
    import ipdb
    tb = sys.exc_info()[2]
    ipdb.post_mortem(tb)
```


<a id="orgdda4469"></a>

# PDB

-   **h(elp) [command]:** выведет подсказку по доступным командам
-   **a(rgs):** напечать аргументы текущей функции (текущего стека вызовов)
-   **p <expression>:** напечатать содержимое переменной или результат вызова
-   **pp <expression>:** красиво напечатать
-   **w(here):** покажет стектрейс как вы очутились в текущем месте кода
-   **l(ist) [start [end]]:** выведет по 5 строк вокруг текущей или вокруг заданной, либо выведет строки со start по end
-   **u(p) / d(own):** перемещение по стеку вызовов


<a id="org59c5cc4"></a>

# PDB

-   **! выражение:** выполнить выражение, например переопределить значение переменной
-   **s(tep):** зайти внутрь вызова
-   **n(ext):** следующая строка кода
-   **b(reak) [ ([filename:]lineno | function) [, condition] ]:** добавить точку останова
-   **disable N:** отключить точку останова
-   **enable N:** включить точку останова
-   **cl(ear) (filename:lineno | bpnumber):**


<a id="orgff4e16b"></a>

# PuDB

```shell
python -m pudb myobj.py
```

![img](pudb.png)


<a id="orge68f16c"></a>

# runserver\_plus

<span class="underline"><span class="underline">[installation instruction](https://django-extensions.readthedocs.io/en/latest/installation_instructions.html)</span></span>

```shell
WERKZEUG_DEBUG_PIN=1234 \
    python manage.py runserver_plus
```
