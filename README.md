# image-processing
Сервис, способный принимать **изображение**, сохранять его в различных форматах и разрешениях с определенной степенью сжатия.

## Содержание

- [Функциональность](#функциональность)
- [Установка и настройка](#установка-и-настройка)
  - [Используя poetry](#используя-poetry)
  - [Используя venv](#используя-venv)
- [Технологии](#технологии)



## Функциональность
1. **Загрузка изображения**

Сервис принимает на вход путь до файла с изображением. Параметр можно задать через терминал. Поддерживаемые расширения файлов указываются в переменных среды. При попытке загрузки файла с другим расширением пользователь получит сообщение об ошибке.

2. **Обработка изображения**

Изображение сохраняется в том же формате, в котором был исходник, с определенными разрешениями и степенью сжатия.

Стандартная конфигурация в шаблоне `.env.example` содержит несколько шаблонов разрешений:
```plain
Минимальное разрешение: 100x100 пикселей, качество сжатия 70%.
Низкое разрешение: 480x360 пикселей, качество сжатия 50%.
Среднее разрешение: 800x600 пикселей.
Высокое разрешение: 1280x720 пикселей.
Максимальное разрешение: 1920x1080 пикселей.
```
Файлы сохраняются в директории, указанной в конфигурации сервиса. Названия файлов состоят из имени исходного файла, размера исходного файла и его расширения.

## Установка и настройка
### Используя poetry
1. Склонируйте репозиторий и перейдите в него
```bash
cd image-processing
```
2. Установите зависимости проекта
```bash
poetry install
```
3. Активируйте виртуальное окружение
```bash
poetry shell
```
4. Создайте файл `.env` и наполните его по примеру файла `.env.example`
```python
ALLOWED_EXTENSIONS=jpeg,jpg,png,svg,webp # Разрешения для входных изображений
DIRECTORY_TO_SAVE=/path/to/directory/ # Путь для измененного изображения 

# Строки пресетов разрешений: каждый новый пресет имеет индекс выше прошлого на единицу. 
# Поля: name - название пресета, resW - ширина изображения, resH - высота изображения,
# index - вариант выбора для пользователя, quality - степень сжатия в процентах (без сжатия - null)
RESOLUTION_PRESETS_0={"name": "minimal", "resW": 100, "resH": 100, "index": 1, "quality": 70}
```
5. Перейдите в директорию `src`
```bash
cd src
```
6. Запустите сервис
```bash
python main.py
```

### Используя venv
1. Склонируйте репозиторий и перейдите в него
```bash
cd image-processing
```
2. Создайте виртуальное окружение:
```bash
python -m venv venv
Это создаст виртуальное окружение с именем venv в текущей директории.
```
3. Активируйте виртуальное окружение:

Для Windows:

```bash
venv\Scripts\activate
```
Для MacOS/Linux:
```bash
source venv/bin/activate
```
4. Установите зависимости проекта:

```bash
pip install -r requirements.txt
```
5. Создайте файл `.env` и наполните его по примеру файла `.env.example`
6. Перейдите в директорию src:
```bash
cd src
```
7. Запустите файл main.py:
```bash
python main.py
```

## Технологии
Проект выполнен с использованием следующих технологий:
- `Python 3.11`
- `Pillow 10.3.0`
- `Pydantic 2.6.4`
- `dotenv 1.0.1`