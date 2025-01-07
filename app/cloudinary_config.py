import os
import cloudinary
import cloudinary.uploader

from dotenv import load_dotenv

load_dotenv()

cloudinary.config(
    secure=True
)