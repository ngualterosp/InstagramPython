from instabot import Bot

mi_bot = Bot()
mi_bot.login(username='ingeniero_gualteros', password='****')
lista_fotos = mi_bot.get_total_user_medias('im__nico_')
mi_bot.download_photos(lista_fotos, folder='mis_fotos')