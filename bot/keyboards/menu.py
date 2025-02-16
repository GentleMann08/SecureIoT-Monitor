from .operations.keyboard_operations import KeyboardOperations

class Menu:
    @staticmethod
    async def info():
        buttons_dict = {
            "📝 Про проект": "project_info",
            "📊 Тестирование": "testing",
            "🔙 Назад": "to_start"
        }
        
        keyboard = await KeyboardOperations.create_base_keyboard(buttons=buttons_dict)
        return keyboard
    
    @staticmethod
    async def start():
        buttons_dict = {
            "ℹ️ Информация": "info",
            "👤 Поучаствовать": "join"
        }
        
        keyboard = await KeyboardOperations.create_base_keyboard(buttons=buttons_dict)
        return keyboard
    
    @staticmethod
    async def to_start():
        buttons_dict = {
            "В меню": "to_start"
        }
        
        keyboard = await KeyboardOperations.create_base_keyboard(buttons=buttons_dict)
        return keyboard
    
    @staticmethod
    async def to_info():
        buttons_dict = {
            "Назад": "info"
        }
        
        keyboard = await KeyboardOperations.create_base_keyboard(buttons=buttons_dict)
        return keyboard