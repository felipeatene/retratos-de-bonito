from app.database import engine
from app.models.story import Story

# Create the stories table if it doesn't exist
Story.__table__.create(bind=engine, checkfirst=True)
print('stories table created (or already existed)')
