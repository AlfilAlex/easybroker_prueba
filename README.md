# Prueba técnica EasyBroker

El siguiente proyecto es el resultado de la prueba técnica de EasyBroker que consiste en una página que consume \n
los recursos mediante su API.

De tal forma, se construye una página web para la venta, renta y compra de propiedades utilizando 2 páginas principales:

1. Properties List (HomePage): Página con estilo vintage (como si fuera de los 2000), donde se presentan cartas de cada propiedad obtenida a partir de una petición a la API de EasyBroker. Cada carta incluye información básica de la propiedad y un botón de ver más que te lleva a la página _property_.
   Se utiliza una paginación y se muestran 15 resultados por página.

2. Property profile: Página con estilo sencillo que incluye una mayor cantidad de información e imagenes de la propiedad. Adicionalmente incluye una sección de contacto. En la cual el usuario registra los datos cuando se encuentre interesado en una propiedad. Estos datos son enviados a EasyBroker, junto con el ID de esta propiedad.

## Implementación

La implementación de la API se realizó utilizando Flask para el backend y el motor de renderizado Jinja2 para el frontend. Se tomó esta elección debido a la agilidad que proporciona Flask para contruir aplicaciones sencillas y confiables. A pesar de poder escalar bien a proyectos de dimensiones mayores, en dicho caso combendrí migrar a frameworks más robustos como Django.

### Alzado del proyecto

El proyecto en cuention tiene la siguiente estructura:

```
    .
    ├── app
    │ ├── home
    │ │ ├── static
    │ │ ├── template
    │ │ └── home.py
    │ ├── property
    │ │ ├── static
    │ │ ├── template
    │ │ └── property_profile.py
    │ └── **init**.py
    ├── tests
    │ ├── functional
    │ │ ├── **init**.py
    │ │ ├── test_home.py
    │ │ └── test_property_page.py
    │ ├── unit
    │ │ ├── **init**.py
    │ │ └── test_properties_home_page.py
    │ ├── conftest.py
    │ └── \_init\_\_.py
    ├── config.py
    ├── README.md
    ├── requirements.txt
    └── wsgi.py
```

Los paquetes utilizados para el proyecto se encuentran en el archivo requirements.txt que pueden ser instalados mediante el siguente comando:

    pip install -r /path/to/requirements.txt
