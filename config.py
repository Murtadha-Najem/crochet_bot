"""
Bot Configuration - Settings and constants

IMPORTANT: Set your bot token here before running!
"""

# Telegram Bot Token (get from @BotFather)
# TODO: Replace with your actual bot token
BOT_TOKEN = "***REMOVED***"

# File paths
DATA_DIR = "data"
TEMP_DIR = "data/temp"
DATABASE_PATH = "data/sessions.db"

# Pattern generation settings
DEFAULT_SIZE = 150
MAX_PATTERN_SIZE = 400
MIN_PATTERN_SIZE = 80
MAX_COLORS = 10

# Bot behavior
RATE_LIMIT_PATTERNS_PER_HOUR = 5
SESSION_TIMEOUT_HOURS = 24

# Error messages (Arabic)
ERROR_MESSAGES = {
    'image_too_small': "الصورة صغيره كلش جربي صوره اكبر",
    'image_invalid': "نوع الصورة غير مدعوم",
    'processing_timeout': "الصورة كبيرة جربي صورة اصغر",
    'generic_error': "صار خلل جربي من جديد",
    'no_session': "ماكو مخطط شغال دزي الصورة من جديد",
}

# Success messages (Arabic)
SUCCESS_MESSAGES = {
    'pattern_ready': "المخطط جاهز",
    'color_changed': "تم التغيير",
    'welcome': "صباحو, دزي صوره نحولها مخطط🧶",
}

# Help text
HELP_TEXT = """
🧶 **بوت محول الصور إلى كروشيه**

**كيفية الاستخدام:**
1. أرسل صورة
2. اختر الحجم المناسب
3. احصل على مخططك!

**الأوامر:**
/start - البدء
/help - المساعدة
/new - باترون جديد

"""
 
# Logging configuration
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)
