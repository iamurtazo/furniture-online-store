# Furniture Online Store

A Django-based furniture storefront for browsing products, managing a shopping cart, and placing orders. The project includes a responsive Bootstrap interface, product categories and search, user accounts, order history, and PostgreSQL-backed persistence.

## Features

- Browse furniture by category
- Search the product catalog
- View product details, prices, discounts, and stock status
- Add, update, and remove products from a cart
- Support carts for both authenticated users and anonymous sessions
- Register, sign in, and manage a user profile
- Create orders with delivery and payment preferences
- View order details and order status
- Manage products, categories, users, carts, and orders through Django admin
- Load sample categories and products from fixtures
- Use template and view-level caching (file-based cache backend) for frequently accessed pages

## Tech stack

- Python
- Django 5.1
- PostgreSQL
- Bootstrap
- jQuery
- Django Debug Toolbar

## Project structure

```text
src/
└── app/
    ├── app/          # Django project configuration
    ├── main/         # Home, about, delivery, and contact pages
    ├── goods/        # Categories, products, catalog, and search
    ├── carts/        # Cart models, views, and cart operations
    ├── orders/       # Checkout and order management
    ├── users/        # Authentication, profiles, and user carts
    ├── common/       # Shared mixins used across apps
    ├── templates/    # Shared templates
    ├── static/       # CSS, JavaScript, icons, and product images
    ├── fixtures/     # Sample catalog data
    ├── requirements.txt
    └── manage.py
```

## Requirements

- Python 3.10 or newer
- PostgreSQL 13 or newer

The application currently uses PostgreSQL settings defined in `src/app/app/settings.py`. Before running it, create a local database and update the database connection values for your environment. Do not commit real passwords or production secrets.

## Installation

1. Clone the repository and enter the application directory:

   ```bash
   git clone https://github.com/iamurtazo/furniture-online-store.git
   cd furniture-online-store/src/app
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

   On Windows PowerShell, use:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure PostgreSQL and update `DATABASES` in `app/settings.py` with your local database name, user, password, host, and port.

5. Apply migrations:

   ```bash
   python manage.py migrate
   ```

6. Load the sample catalog:

   ```bash
   python manage.py loaddata fixtures/goods/categories.json fixtures/goods/products.json
   ```

7. Optionally create an administrator:

   ```bash
   python manage.py createsuperuser
   ```

8. Start the development server:

   ```bash
   python manage.py runserver
   ```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Useful URLs

| Page | URL |
| --- | --- |
| Storefront | `/` |
| Catalog/search | `/catalog/` |
| User login | `/user/login/` |
| Registration | `/user/registration/` |
| User profile | `/user/profile/` |
| User cart | `/user/users-cart/` |
| Checkout | `/orders/create/` |
| Django admin | `/admin/` |

## Running tests

From `src/app`, run:

```bash
python manage.py test
```

## Development notes

- The project uses a custom user model (`users.Users`), so configure `AUTH_USER_MODEL` before creating migrations in a new installation.
- Uploaded media is served from the local `media/` directory in debug mode.

## Known limitations / roadmap

This project currently targets local development only. Before deploying it or accepting external contributions, the following should be addressed:

- `DEBUG` is hardcoded to `True`; disable it and configure `ALLOWED_HOSTS` for production.
- The Django secret key and database credentials are hardcoded in `settings.py`; move them to environment variables (e.g. via `django-environ` or `python-decouple`).
- Secure cookies, HTTPS, static file collection (`collectstatic`), and production-grade media storage are not yet configured.
- No CI pipeline or automated linting is currently set up.

## Demo

https://github.com/user-attachments/assets/44c48534-c247-49d7-bc50-8875e5a92d22

[furniture-online-store-demo-video.mp4](furniture-online-store-demo-video.mp4).

## License

This project is licensed under the [MIT License](LICENSE).
