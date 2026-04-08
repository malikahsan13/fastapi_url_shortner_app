# URL Shortener API

A high-performance URL shortening service built with FastAPI, featuring RESTful API design, SQLAlchemy ORM integration, and robust error handling. This project demonstrates expertise in building scalable microservices with modern Python web frameworks.

## 🚀 Features

- **URL Shortening**: Convert long URLs into compact, shareable short codes
- **Redirection Service**: Seamless HTTP redirects with proper status codes
- **Duplicate Detection**: Efficient handling of duplicate URLs to prevent redundancy
- **CRUD Operations**: Complete Create, Read, Update, Delete functionality
- **Database Persistence**: SQLite database with SQLAlchemy ORM for data integrity
- **CORS Support**: Cross-origin resource sharing for frontend integration
- **Unique Code Generation**: Collision-resistant short code generation algorithm

## 🛠️ Tech Stack

- **Framework**: FastAPI 0.104+ - Modern, high-performance web framework
- **Database**: SQLite with SQLAlchemy ORM - Type-safe database operations
- **Validation**: Pydantic - Data validation using Python type annotations
- **HTTP Client**: RedirectResponse with proper 3xx status codes
- **CORS Middleware**: Configurable cross-origin access control
- **Package Manager**: uv - Blazing fast Python package installer

## 📋 Prerequisites

- Python 3.8+
- uv package manager (recommended) or pip

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd fastapi_url_shortner_app
   ```

2. **Install dependencies**

   **Option A: Using uv (Recommended - Faster)**
   ```bash
   # Install uv if you haven't already (Windows)
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   
   # Install uv if you haven't already (Linux/Mac)
   curl -LsSf https://astral.sh/uv/install.sh | sh
   
   # Create virtual environment and install dependencies
   uv venv
   source .venv/bin/activate  # Linux/Mac
   # or
   .venv\Scripts\activate     # Windows
   
   uv pip install fastapi uvicorn sqlalchemy pydantic
   ```

   **Option B: Using Traditional pip**
   ```bash
   pip install fastapi uvicorn sqlalchemy pydantic
   ```

3. **Run the application**
   ```bash
   uvicorn main:app --reload
   ```

The API will be available at `http://localhost:8000`

## 📡 API Endpoints

### Create Short URL
```http
POST /shorten
Content-Type: application/json

{
  "original_url": "https://example.com/very/long/url"
}
```

**Response:**
```json
{
  "original_url": "https://example.com/very/long/url",
  "short_code": "abc123",
  "short_url": "http://localhost:8000/abc123"
}
```

### Get All URLs
```http
GET /all
```

**Response:**
```json
[
  {
    "original_url": "https://example.com",
    "short_code": "xyz789",
    "short_url": "http://localhost:8000/xyz789"
  }
]
```

### Redirect to Original URL
```http
GET /{short_code}
```

**Response:** HTTP 302 Redirect to original URL

### Delete URL
```http
DELETE /delete/{short_code}
```

**Response:**
```json
{
  "message": "URL deleted successfully"
}
```

## 🏗️ Project Structure

```
fastapi_url_shortner_app/
├── main.py                 # Application entry point
├── urls.db                 # SQLite database (auto-created)
├── README.md              # Project documentation
└── requirements.txt       # Python dependencies
```

## 💡 Technical Highlights

### Database Design
- **Schema**: Optimized table design with indexed columns for fast lookups
- **ORM**: SQLAlchemy declarative base for type-safe database operations
- **Session Management**: Dependency injection pattern for database connection handling

### API Design
- **RESTful Principles**: Proper HTTP methods and status codes
- **Request Validation**: Pydantic models for automatic request validation
- **Error Handling**: Comprehensive HTTP exception handling
- **Response Models**: Consistent response formatting with Pydantic

### Code Quality
- **Type Hints**: Full type annotation coverage for better IDE support
- **Separation of Concerns**: Clear separation between business logic and data access
- **Collision Handling**: Robust short code generation with uniqueness guarantees
- **Duplicate Prevention**: Efficient duplicate URL detection and reuse

### Performance Optimizations
- **Database Indexing**: Indexed columns on frequently queried fields
- **Connection Pooling**: SQLAlchemy engine with optimized connection management
- **Efficient Queries**: Optimized database queries to prevent N+1 problems

## 🚀 Running Tests

Access interactive API documentation at:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 🔮 Future Enhancements

- [ ] Custom alias support for memorable short codes
- [ ] URL analytics and click tracking
- [ ] QR code generation for short URLs
- [ ] Rate limiting and API throttling
- [ ] User authentication and private URLs
- [ ] Expiration dates for temporary links
- [ ] PostgreSQL/MySQL support for production deployment
- [ ] Docker containerization
- [ ] Redis caching for frequently accessed URLs
- [ ] Comprehensive unit and integration tests

## 📊 API Usage Examples

### Using cURL
```bash
# Create short URL
curl -X POST "http://localhost:8000/shorten" \
  -H "Content-Type: application/json" \
  -d '{"original_url": "https://www.example.com/long-url"}'

# Get all URLs
curl -X GET "http://localhost:8000/all"

# Delete URL
curl -X DELETE "http://localhost:8000/delete/abc123"
```

### Using Python
```python
import requests

# Create short URL
response = requests.post("http://localhost:8000/shorten", 
    json={"original_url": "https://www.example.com"})
print(response.json())
```

## 🤝 Contributing

This project is open for contributions. Please feel free to submit pull requests or open issues for bugs and feature requests.

## 📝 License

This project is available for educational and professional use.

## 👨‍💻 Developer

This project demonstrates expertise in:
- RESTful API design and development
- Modern Python web frameworks (FastAPI)
- Database design and ORM patterns
- Error handling and validation
- Microservices architecture
- API documentation and testing

---

**Built with FastAPI** - Modern Python web framework with automatic validation, serialization, and documentation.