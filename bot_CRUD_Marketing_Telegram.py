import os
import datetime
import telebot
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Inisialisasi bot Telegram
bot_token = 'YOUR_BOT_TOKEN'
bot = telebot.TeleBot(bot_token)

# Konfigurasi Google Sheets
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(credentials)
spreadsheet_id = 'YOUR_SPREADSHEET_ID'
worksheet_name = 'Sheet1'  # Ubah sesuai nama sheet Anda

# Fungsi untuk mengisi data ke Google Sheets
def write_to_sheet(data):
        worksheet = client.open_by_key(spreadsheet_id).worksheet(worksheet_name)
            worksheet.append_row(data)

# Menangani perintah /start dari pengguna
@bot.message_handler(commands=['start'])
    def handle_start(message):
                    user_id = message.from_user.id
                    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    user_data = [user_id, current_time, '', '', '', '', '', '', '']
                    write_to_sheet(user_data)
                    bot.send_message(message.chat.id, 'Halo! Silakan masukkan data Anda.')

# Menangani pesan masuk dan mengisi data ke Google Sheets
@bot.message_handler(func=lambda message: True)
     def handle_message(message):
                        user_id = message.from_user.id
                        current_time = datetime.datetime.now().strftime('%H:%M:%S')
                        user_data = [user_id, current_time, '', '', '', '', '', '', '']
                                                        
# Menangani pengisian data secara berurutan
if len(message.text.splitlines()) >= 8:
                    lines = message.text.splitlines()
                    user_data[2] = lines[0]  # Nama Sales
                    user_data[3] = lines[1]  # Nama Calon Customer
                    user_data[4] = lines[2]  # No Telepon
                    user_data[5] = lines[3]  # Alamat
                    user_data[6] = lines[4]  # Sumber Data
                    user_data[7] = lines[5]  # Kota
                    user_data[8] = lines[6]  # Status (Leads,Hot,Prospek)
                                                                                                                                            
                            write_to_sheet(user_data)
                            bot.send_message(message.chat.id, 'Data telah berhasil disimpan!')
                                else:
                                    bot.send_message(message.chat.id, 'Silakan masukkan data dengan format yang benar.')

                                                                                                                                                                            # Menjalankan bot
                                                                                                                                                                            bot.polling()

