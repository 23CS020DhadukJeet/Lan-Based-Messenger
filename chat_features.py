import json
import base64
import os
from datetime import datetime

class ChatFeatures:
    # Emoji mapping
    EMOJI_MAP = {
        ":smile:": "😊",
        ":laugh:": "😂",
        ":heart:": "❤️",
        ":thumbsup:": "👍",
        ":wave:": "👋",
        ":fire:": "🔥",
        ":star:": "⭐",
        ":check:": "✅",
        ":x:": "❌",
        ":rocket:": "🚀"
    }

    # User avatars (you can replace these with actual image paths)
    USER_AVATARS = {
        "user1": "👤",
        "user2": "👤",
        "default": "👤"
    }

    @staticmethod
    def format_message(message):
        """Format message with emojis and text styling"""
        # Replace emoji codes with actual emojis
        for code, emoji in ChatFeatures.EMOJI_MAP.items():
            message = message.replace(code, emoji)
            
        # Handle text formatting
        message = message.replace("*", "**")  # Bold
        message = message.replace("_", "__")  # Italic
        
        return message
    
    @staticmethod
    def create_message(username, content, msg_type="text"):
        """Create a structured message object"""
        return {
            "type": msg_type,
            "username": username,
            "content": content,
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "avatar": ChatFeatures.USER_AVATARS.get(username, ChatFeatures.USER_AVATARS["default"])
        }
    
    @staticmethod
    def encode_file(file_path):
        """Encode file to base64 for transmission"""
        try:
            with open(file_path, "rb") as file:
                return base64.b64encode(file.read()).decode()
        except Exception as e:
            return None
    
    @staticmethod
    def decode_file(file_data, save_path):
        """Decode base64 file data and save it"""
        try:
            with open(save_path, "wb") as file:
                file.write(base64.b64decode(file_data))
            return True
        except Exception as e:
            return False
    
    @staticmethod
    def get_file_info(file_path):
        """Get file information"""
        try:
            return {
                "name": os.path.basename(file_path),
                "size": os.path.getsize(file_path),
                "type": os.path.splitext(file_path)[1]
            }
        except:
            return None 