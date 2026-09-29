class NotificationService:
    @staticmethod
    async def send_booking_confirmation(user_email: str, message: str):
        print(f"[Повідомлення] Було відправлено на {user_email}: {message}")