# ArtiNo

A modern, responsive e-commerce website built with **Django, Alpine.js, HTMX, and Tailwind CSS**. Designed to provide a fast, interactive, and user-friendly online shopping experience.

## Features

- **Product Catalog** – Browse products with categories and detailed product pages.
- **Product Search** – Find products quickly.
- **Shopping Cart** – Add, remove, and update products.
- **User Authentication** – Customer registration, login, and logout.
- **Order Management** – Manage customer orders.
- **Responsive Design** – Optimized for desktop, tablet, and mobile.
- **Dynamic Interactions** – Powered by HTMX and Alpine.js.
- **Modern UI** – Styled with Tailwind CSS.
- **Admin Dashboard** – Manage products, categories, and orders through Django Admin.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web framework |
| HTML5 | Website structure |
| CSS3 | Styling |
| Tailwind CSS | Utility-first CSS framework |
| Alpine.js | Lightweight frontend interactions |
| HTMX | Dynamic server-rendered interactions |
| SQLite / PostgreSQL | Database |

## Project Structure

```text
store/
├── config/
├── apps/
│   ├── products/
│   ├── cart/
│   ├── orders/
│   └── accounts/
├── templates/
│   ├── base.html
│   ├── includes/
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│   └── fonts/
├── media/
├── .env.example
├── .gitignore
├── LICENSE
├── manage.py
├── package.json
├── README.md
└── requirements.txt
```

## Requirements

Before installing, make sure you have:

- Python 3.11+
- Node.js and npm
- Git

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Artin-Nobahari/ArtiNo.git
cd ArtiNo
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Linux / macOS**
```bash
source .venv/bin/activate
```

**Windows**
```bash
.venv\Scripts\activate
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 4. Install frontend dependencies

```bash
npm install
```

### 5. Configure environment variables

Create your local `.env` file using the example:

```bash
cp .env.example .env
```

Configure the required environment variables.

### 6. Run database migrations

```bash
python manage.py migrate
```

### 7. Create a superuser

```bash
python manage.py createsuperuser
```

### 8. Build frontend assets

Run the appropriate Tailwind CSS build command configured in `package.json`.

### 9. Start the development server

```bash
python manage.py runserver
```

Open your browser:

```text
http://127.0.0.1:8000/
```

## Development

Run Django:

```bash
python manage.py runserver
```

Run your Tailwind CSS development/build process using the scripts defined in `package.json`.

## Environment Variables

Example `.env.example`:

```env
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=localhost,127.0.0.1

DATABASE_URL=
```

Never commit your actual `.env` file or production secrets.

## Screenshots

Add screenshots of your website here:

```markdown
![Store Homepage](docs/screenshots/homepage.png)
```

## Roadmap

- [ ] Product catalog
- [ ] Product categories
- [ ] Search and filtering
- [ ] Shopping cart
- [ ] Customer authentication
- [ ] Checkout system
- [ ] Payment integration
- [ ] Order tracking
- [ ] Customer reviews
- [ ] Wishlist

## Contributing

Contributions are welcome!

1. Fork this repository.
2. Create a feature branch.
3. Commit your changes.
4. Push your branch.
5. Open a Pull Request.

## License

This project is licensed under the [MIT License](LICENSE).

## Author

**Artin Nobahari**

- GitHub: [@Artin-Nobahari](https://github.com/Artin-Nobahari)

---

If you find this project useful, consider giving it a star on GitHub.
