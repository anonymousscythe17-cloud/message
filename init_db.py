from app import create_app, db

print("Creating app context...")
app = create_app()

with app.app_context():
    print("Dropping all tables...")
    db.drop_all()
    
    print("Creating new tables...")
    db.create_all()
    
    print("✓ Database created successfully with new schema!")
    
    # Verify tables were created
    from sqlalchemy import inspect
    inspector = inspect(db.engine)
    print("\nTables created:")
    for table in inspector.get_table_names():
        print(f"  - {table}")
    
    print("\nMessage table columns:")
    for column in inspector.get_columns('message'):
        print(f"  - {column['name']}")
