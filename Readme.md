## Prerequisites

- Python 3.8 or later

## Project structure 

food_ordering_app/
├── main.py
├── business/
│   └── food_ordering_system.py
├── presentation/
│   ├── screens.py
│   └── static/         # (contains CSS, images, etc.)
├── templates/          # Move your templates here!
│   ├── index.html
│   ├── menu.html
│   └── order.html
├── assets/
├── README.md
└── requirements.txt

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd food_ordering_app
   ```

 2. **Set up Virtual environment:**

   ```bash
   python3 -m venv myenv
   source myenv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

### Note: Application running on 
 ```bash
   Expose 5000
   ```

## **For Running the Application in development mode (with debugging enabled):**
```bash
   python3 main.py
   ```

## **For Running Flask app in the background, you can use nohup:**
```bash
   nohup python3 main.py > flask.log 2>&1 &
   ```

