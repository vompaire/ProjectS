from telethon import TelegramClient, events, sync, connection
from project.config import api_id, api_hash


system_version = "4.16.30-vxCUSTOM"
device_model = "CustomDevice"
app_version = "1.0.0"

with TelegramClient('session_name', api_id, api_hash,
                    system_version=system_version,
                    device_model=device_model,
                    app_version=app_version) as client:
    channel_username = 'dtfbest'
    entity = client.get_entity(channel_username)
    message_limit = 1
    all_mes = client.get_messages(entity, limit=message_limit)

    for mes in all_mes:
        print(mes.text)

        if mes.media and mes.photo:
            # Загружаем и сохраняем фото в файл
            photo = client.download_media(mes.photo)
            photo_path = f'photo_{mes.id}.jpg'
            with open(photo_path, 'wb') as file:
                file.write(photo)
            print(f"Saved photo to {photo_path}")