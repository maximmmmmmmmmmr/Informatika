# TODO Напишите функцию для поиска индекса товара
def find_article(items_list,find_item):
    if find_item in items_list:      # Проверяем находится ли искомый товар в спсике товаров
        return items_list.index(find_item)  #Возвращаем индекс товара

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_article(items_list,find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
