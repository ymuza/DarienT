# **tu_credito**
# -----------------


##  Stack tecnológico

### Backend
- Python **3.12**
- Django **5.2**
- Django REST Framework
- PostgreSQL **15**
- JWT Authentication (`djangorestframework-simplejwt`)
- Documentación API: **drf-spectacular**

### Testing
- pytest
- pytest-django

### Infraestructura
- Docker
- Docker Compose

---

##  Modelo de dominio

### Banco
- nombre (único)
- tipo (PRIVADO / GOBIERNO)
- dirección

### Cliente
- dni (**único**)
- nombre_completo
- fecha_nacimiento
- edad
- email
- tipo_persona (NATURAL / JURIDICO)
- banco (FK → Banco)

### Crédito
- cliente (FK → Cliente)
- banco (FK → Banco)
- descripción
- pago_minimo
- pago_maximo
- plazo_meses
- tipo_credito (AUTOMOTRIZ / HIPOTECARIO / COMERCIAL)
- fecha_registro

#### Reglas de negocio clave
- El DNI del cliente es único.
- `pago_minimo` no puede ser mayor que `pago_maximo`.
- El banco del crédito debe coincidir con el banco del cliente.
- No se puede eliminar un banco si tiene clientes asociados (`PROTECT`).

Estas reglas están implementadas **a nivel de modelo**, garantizando consistencia desde cualquier punto de entrada (API, Admin, Backoffice).

---

##  Autenticación y permisos

La API REST está protegida con **JWT**.

- Lecturas: usuarios autenticados
- Escrituras (POST / PUT / DELETE): solo usuarios **staff**

Endpoints principales:
- `POST /api/auth/token/`
- `POST /api/auth/token/refresh/`

---

## Backoffice web

Rutas principales:

- `/backoffice/bancos/`
- `/backoffice/clientes/`
- `/backoffice/creditos/`

Características:
- CRUD básico
- Formularios simples
- Eliminaciones con confirmación
- Mensajes de éxito/error
- Acceso restringido a usuarios autenticados

---

## Documentación de la API

La documentación Swagger está disponible en:

- `/api/schema/`
- `/api/docs/`

Permite explorar y probar los endpoints autenticándose con JWT.

---

## Tests automatizados

Se incluyen tests para:

- Validaciones de modelos
- Reglas de negocio
- Permisos de la API
- Eliminación de entidades (incluyendo `PROTECT` y `CASCADE`)

Ejecutar tests localmente:

```bash
pytest
```

---

##Ejecución con Docker 

### Requisitos
- Docker
- Docker Compose

### Variables de entorno (`.env`)

```env
DEBUG=True
SECRET_KEY=django-insecure-secret-key

DB_NAME=tu_credito
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

### Levantar el entorno

```bash
docker compose up --build
```

La aplicación estará disponible en:

- http://localhost:8000
- http://localhost:8000/admin
- http://localhost:8000/api

---

## Decisiones técnicas relevantes

- **Validaciones en modelos**: se priorizó la consistencia del dominio sobre validaciones solo en serializers.
- **Separación API / Web**: endpoints REST y backoffice web desacoplados.
- **Docker**: entorno reproducible con un solo comando.
- **Poetry + pip**: Poetry como gestor de dependencias, pip para instalación estable en contenedores.
- **JWT**: autenticación moderna y stateless.
- **PostgreSQL**: base de datos relacional robusta para el dominio.

---

