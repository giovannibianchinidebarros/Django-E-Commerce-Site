# import_products.py
import os
import django
import requests
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SETTINGS_PATH = os.path.join(BASE_DIR, 'ecom_site', 'settings')
print(SETTINGS_PATH)


# Defina a variável de ambiente DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecom_site.settings')

# Carregue as configurações do Django
django.setup()


def import_products():
    from shop.models import Product
    try:
        # Faça a solicitação para obter a lista de produtos
        response = requests.get("https://dummyjson.com/products")
        response.raise_for_status()

        # Extrair a lista de produtos do JSON
        prod_list = response.json()['products']

        # Loop sobre cada produto na lista de produtos
        for product_data in prod_list:
            # Extraia os dados do produto
            title = product_data['title']
            price = product_data['price']
            rating = product_data['rating']
            brand = product_data['brand']
            category = product_data['category']
            description = product_data['description']
            thumbnail = product_data['thumbnail']
            image = product_data['images'][0]

            # Crie uma instância do modelo de Produto e preencha os campos
            product = Product.objects.create(
                title=title,
                price=price,
                rating=rating,
                brand=brand,
                category=category,
                description=description,
                thumbnail=thumbnail,
                image=image
            )

            print(f"Produto '{product.title}' adicionado com sucesso!")

        print("Todos os produtos foram importados com sucesso.")

    except Exception as e:
        print(f"Ocorreu um erro ao importar os produtos: {e}")


if __name__ == "__main__":
    import_products()
