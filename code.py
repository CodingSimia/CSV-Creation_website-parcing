from bs4 import BeautifulSoup

# HTML-код страницы сохраненный в переменной html
html = """
<div class="employee-card svelte-1ala9v1">
    <div class="title svelte-1ala9v1">
        <a href="/agent/joan-kagan">Joan <em>Kagan</em></a>
    </div>
    <div class="contact svelte-1ala9v1">
        <a href="mailto:joan@theagencyre.com">joan@theagencyre.com</a>
        <a href="tel:+19179929433" title="+1 917 992 9433">(917) 992-9433</a>
    </div>
</div>

<div class="employee-card svelte-1ala9v1">
    <div class="title svelte-1ala9v1">
        <a href="/agent/john-doe">John <em>Doe</em></a>
    </div>
    <div class="contact svelte-1ala9v1">
        <a href="mailto:john@example.com">john@example.com</a>
        <a href="tel:+123456789" title="+1 234 567 89">(123) 456-789</a>
    </div>
</div>
"""

# Создаем объект BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Используем метод find_all для поиска всех блоков с классом "employee-card"
employee_cards = soup.find_all("div", {"class": "employee-card"})

# Теперь у вас есть список всех блоков с этим классом
for card in employee_cards:
    # Извлекаем имя из блока
    name_element = card.select_one('.title a')
    if name_element:
        name = name_element.get_text()

    # Извлекаем номер телефона из блока
    phone_element = card.select_one('.contact a[href^="tel:"]')
    if phone_element:
        phone = phone_element['title']

    # Извлекаем адрес электронной почты из блока
    email_element = card.select_one('.contact a[href^="mailto:"]')
    if email_element:
        email = email_element['href'][7:]

    print("Имя:", name)
    print("Номер телефона:", phone)
    print("Адрес электронной почты:", email)
