#!/usr/bin/env python3
import sys
import socket
import time
import os
from tkinter import * 					#Импортируем модель  для работы с  окнами
from tkinter import ttk     			# подключаем пакет ttk
import requests
import json

root = Tk()     						# создаем корневой объект - окно
root.title("Проверка действительности токена WIALON")
root.iconbitmap(default="favicon.ico")	#Устанавливаем иконку приложения
root.geometry("420x180")    			# устанавливаем размеры окна
root.resizable(False, False)			#Запрет изменения размера окна

TOKEN = ""
HTTPS = ""

def Close():
	print("Close")
	exit()
	
def Token():
	print("TOKEN")
	global TOKEN
	global HTTPS
	TOKEN = EntryTOKEN.get()
	HTTPS = EntryHTTPS.get()
	if len(TOKEN) == 0 or len(HTTPS) == 0:
		LabelResult['text'] = "Введены не актуальные данные"
	#https://app.wialonlocal.com/wialon/ajax.html?svc=token/login&params={"token":"токен"}
	URL = "https://" + HTTPS+ "/wialon/ajax.html?svc=token/login&params={\"token\":\""+ TOKEN + "\"}"
	print(URL)
	try:
		Response = requests.get(URL)
		if Response.status_code == 200:
			JSONResponse = json.loads(Response.text)
			print(JSONResponse)
			try:
				error = JSONResponse["error"]
				err = "Ошибка токена номер: " + str(error)
				LabelResult['text'] = err
			except:
				eid = JSONResponse["eid"]
				au = JSONResponse["au"]
				data = "EID: " + eid + " LOGIN: " + au
				LabelResult['text'] = data
		else:
			LabelResult['text'] = "Ошибка запроса"
	except:
		LabelResult['text'] = "Ошибка доступа к сайту"

	
LabelHTTPS = ttk.Label(text="Ссылка на WIALON:")
LabelHTTPS.grid(row=0, column=0, ipadx=6, ipady=6, padx=4, pady=4)

LabelTOKET = ttk.Label(text="Токен для WIALON:")
LabelTOKET.grid(row=1, column=0, ipadx=6, ipady=6, padx=4, pady=4)

EntryHTTPS = ttk.Entry()
EntryHTTPS.grid(row=0, column=1, ipadx=6, ipady=6, padx=4, pady=4)

EntryTOKEN = ttk.Entry()
EntryTOKEN.grid(row=1, column=1, ipadx=6, ipady=6, padx=4, pady=4)

BtnCLOSE = ttk.Button(text="Закрыть", command = Close)
BtnCLOSE.grid(row=0, column=2, ipadx=6, ipady=6, padx=4, pady=4)

BtnTOKEN = ttk.Button(text="Проверить", command = Token)
BtnTOKEN.grid(row=1, column=2, ipadx=6, ipady=6, padx=4, pady=4)

LabelResult = ttk.Label(text="Результат проверки")
LabelResult.grid(row=2, column=0, columnspan=3, ipadx=6, ipady=6, padx=4, pady=4)

LabelAuthor = ttk.Label(text="Дмитрий © 2025 urbannova@yandex.ru")
LabelAuthor.grid(row=3, column=0, columnspan=3, ipadx=6, ipady=6, padx=4, pady=4)

def main(args):
	root.mainloop()

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
