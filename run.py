print("run.py is running")

from app import create_app   # Kinukuha ang function mula sa package
from app.models import db    # Kinukuha ang database instance

app = create_app()           # ina-instantiate ang application gamit ang factory function

print("app created successfully")

# Create database tables
with app.app_context():
    db.create_all()
    print("Database tables created successfully!")

if __name__ == "__main__":   # sini-sure ang script ay tumatakbo nang maayus
    print("starting flask server...")
    app.run(debug=True)      # pinapa-run ang application sa debug mode

