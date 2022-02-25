import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

tie = .5

class Funciones_Globales():

	def __init__(self,driver):
		self.driver = driver

	def tiempo(self,tie):
		t = time.sleep(tie)
		return t

	def navegar(self,url,tie):
		self.driver.get(url)
		self.driver.maximize_window()
		print("Página abierta: " + str(url))
		t = time.sleep(tie)
		return t

	def text_xpath(self,xpath,texto,tie):
		val = self.driver.find_element_by_xpath(xpath)
		val.clear()
		val.send_keys(texto)
		t = time.sleep(tie)
		return t

	def text_xpath_val(self,xpath,text,tie):
		try:
			val = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,xpath)))
			val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
			val = self.driver.find_element_by_xpath(xpath)
			val.clear()
			val.send_keys(text)
			print("Escribiendo en el campo {} el texto {} ".format(xpath,text))
			t = time.sleep(tie)
			return t
		except TimeoutException as ex:
			print(ex.msg)
			print("El Elemento no se encontro"+ xpath)

	def texto_id(self, id, texto, tie):

		val = self.driver.find_element_by_id(id)
		val.clear()
		val.send_keys(texto)
		t = time.sleep(tie)
		return t

	def text_id_val(self,id,text,tie):

		try:
			val = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID,id)))
			val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
			val = self.driver.find_element_by_id(id)
			val.clear()
			val.send_keys(text)
			print("Escribiendo en el campo {} el texto {} ".format(id, text))
			t = time.sleep(tie)
			return t
		except TimeoutException as ex:
			print((ex.msg))
			print("El Elemento no se Encontro " + id)

	def click_xpath_val(self,xpath,tie):

		try:
			val = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,xpath)))
			val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
			val = self.driver.find_element_by_xpath(xpath)

			val.click()
			print("\n Damos click en el campo {}".format(xpath))
			t = time.sleep(tie)
			return t

		except TimeoutException as ex:

			print(ex.msg)
			print("\n El Elemento no se encontro "+ xpath)

	def click_id_val(self,id,tie):
		try:
			val = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,id)))
			val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
			val = self.driver.find_element_by_id(id)
			val.click()
			print("Damos click en el campo {}".format(id))
			t = time.sleep(tie)
			return t
		except TimeoutException as ex:
			print(ex.msg)
			print("El Elemento no se encontro "+ id)

	def salida(self):
		print("Termina la prueba Exitosamente....")

	def select_xpath_text(self,xpath,text,tie):
		try:
			val = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,xpath)))
			val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
			val = self.driver.find_element_by_xpath(xpath)
			val = Select(val)
			val.select_by_visible_text(text)
			print("El campo seleccionado es {}".format(text))
			#val.send_keys(text)
			t = time.sleep(tie)
			return t
		except TimeoutException as ex:
			print(ex.msg)
			print("El Elemento no se encontro "+ xpath)

	def select_xpath_type(self,xpath,tipo,dato,tie):
		try:
			val = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,xpath)))
			val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
			val = self.driver.find_element_by_xpath(xpath)
			val = Select(val)

			if tipo == "text":
				val.select_by_visible_text(dato)
			elif tipo == "index":
				val.select_by_index(dato)
			elif tipo == "value":
				val.select_by_value(dato)

			print("El campo seleccionado es {}".format(dato))
			#val.send_keys(text)
			t = time.sleep(tie)
			return t
		except TimeoutException as ex:
			print(ex.msg)
			print("El Elemento no se encontro "+ xpath)

	def upload_xpath(self,xpath,ruta,tie):
		try:
			val = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,xpath)))
			val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
			val = self.driver.find_element_by_xpath(xpath)
			val.send_keys(ruta)

			print("Se carga la imagen {}".format(ruta))
			#val.send_keys(text)
			t = time.sleep(tie)
			return t
		except TimeoutException as ex:
			print(ex.msg)
			print("El Elemento no se encontro "+ xpath)

	def upload_id(self,id,ruta,tie):
		try:
			val = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID,id)))
			val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
			val = self.driver.find_element_by_id(id)
			val.send_keys(ruta)

			print("Se carga la imagen {}".format(ruta))
			#val.send_keys(text)
			t = time.sleep(tie)
			return t
		except TimeoutException as ex:
			print(ex.msg)
			print("El Elemento no se encontro "+ id)

	# Funcion Radio y Check por xpath
	def check_xpath(self,xpath,tie):
		try:
			val = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,xpath)))
			val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
			val = self.driver.find_element_by_xpath(xpath)
			val.click()

			print("Click en el elemento {} ".format(xpath))
			#val.send_keys(text)
			t = time.sleep(tie)
			return t
		except TimeoutException as ex:
			print(ex.msg)
			print("El Elemento no se encontro "+ xpath)

	# Funcion Radio y Check por id
	def check_id(self, id, tie):
		try:
			val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, id)))
			val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
			val = self.driver.find_element_by_id(id)
			val.click()

			print("Click en el elemento {} ".format(id))
			# val.send_keys(text)
			t = time.sleep(tie)
			return t
		except TimeoutException as ex:
			print(ex.msg)
			print("El Elemento no se encontro " + id)

	# Funcion Radio y Check por xpath multiselect mia
	def check_xpath_multiselect(self, xpath, tie):
		try:
			val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
			val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
			val = self.driver.find_element_by_xpath(xpath)
			val.click()

			print("Click en el elemento {} ".format(xpath))
			# val.send_keys(text)
			t = time.sleep(tie)
			return t
		except TimeoutException as ex:
			print(ex.msg)
			print("El Elemento no se encontro " + xpath)

	# Funcion Radio y Check por xpath multiselect mia
	def check_xpath_multiselect_1(self,tie, *args):
		try:
			for num in args:
				val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, num)))
				val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
				val = self.driver.find_element_by_xpath(num)
				val.click()

				print("Click en el elemento {} ".format(num))
				# val.send_keys(text)
				t = time.sleep(tie)
				return t
		except TimeoutException as ex:
			for num in args:
				print(ex.msg)
				print("El Elemento no se encontro " + num)

	def Existe(self, tipo, selector, tiempo):

		if tipo == "xpath":
			try:
				val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, selector)))
				val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
				val = self.driver.find_element_by_xpath(selector)
				val.click()
				print("El elemento existe ---> {} ".format(selector))
				t = time.sleep(tie)
				return "Existe"
			except TimeoutException as ex:
				print(ex.msg)
				print("El Elemento no se Existe " + selector)
				return "No Existe"
		elif tipo == "id":
			try:
				val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, selector)))
				val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
				val = self.driver.find_element_by_id(selector)
				print("Click en el elemento Existe --> {} ".format(selector))
				t = time.sleep(tie)
				return "Existe"
			except TimeoutException as ex:
				print(ex.msg)
				print("El Elemento no se Existe " + selector)
				return "No Existe"

	def Double_Click(self,tipo,selector,tie):

		if tipo == "id":
			try:
				val = self.Selector_id(selector)
				act = ActionChains(self.driver)
				act.double_click(val).perform()
				print("Doble Click en {} ".format(selector))
				t = time.sleep(tie)
				return t
			except TimeoutException as ex:
				print(ex.msg)
				print("El Elemento no se encontro"+ id)

		elif tipo == "xpath":

			try:
				val = self.Selector_xpath(selector)
				act = ActionChains(self.driver)
				act.double_click(val).perform()
				print("Doble Click en {} ".format(selector))
				t = time.sleep(tie)
				return t
			except TimeoutException as ex:
				print(ex.msg)
				print("El Elemento no se encontro" + selector)

	def click_derecho(self,tipo,selector,tie):

		if tipo == "id":
			try:
				val = self.Selector_id(selector)
				act = ActionChains(self.driver)
				act.context_click(val).perform()
				print("Click Derecho en {} ".format(selector))
				t = time.sleep(tie)
				return t
			except TimeoutException as ex:
				print(ex.msg)
				print("El Elemento no se encontro"+ id)

		elif tipo == "xpath":

			try:
				val = self.Selector_xpath(selector)
				act = ActionChains(self.driver)
				act.context_click(val).perform()
				print("Click derecho en {} ".format(selector))
				t = time.sleep(tie)
				return t
			except TimeoutException as ex:
				print(ex.msg)
				print("El Elemento no se encontro" + selector)


	def Selector_xpath(self,element):

		val = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,element)))
		val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
		val = self.driver.find_element_by_xpath(element)
		return val

	def Selector_id(self,element):

		val = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,element)))
		val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
		val = self.driver.find_element_by_id(element)
		return val

	def dragandrop(self,tipos,selector,destino,tie):

		if tipos == "id":
			try:
				val = self.Selector_id(selector)
				val2 = self.Selector_id(destino)
				act = ActionChains(self.driver)
				act.drag_and_drop(val,val2).perform()
				print("El elemento {} se movio ".format(selector))
				t = time.sleep(tie)
				return t
			except TimeoutException as ex:
				print(ex.msg)
				print("El Elemento no se encontro"+ id)

		elif tipos == "xpath":
			try:
				val = self.Selector_xpath(selector)
				val2 = self.Selector_xpath(destino)
				act = ActionChains(self.driver)
				act.drag_and_drop(val,val2).perform()
				print("El elemento {} se movio ".format(selector))
				t = time.sleep(tie)
				return t
			except TimeoutException as ex:
				print(ex.msg)
				print("El Elemento no se encontro" + selector)

	def dragandropxy(self,tipos,selector,x,y,tie):

		if tipos == "id":
			try:
				self.driver.switch_to.frame(0)
				val = self.Selector_id(selector)
				act = ActionChains(self.driver)
				act.drag_and_drop_by_offset(val,x,y).perform()
				print("El elemento {} se movio ".format(selector))
				t = time.sleep(tie)
				return t
			except TimeoutException as ex:
				print(ex.msg)
				print("El Elemento no se encontro"+ id)

		elif tipos == "xpath":
			try:
				self.driver.switch_to.frame(0)
				val = self.Selector_xpath(selector)
				act = ActionChains(self.driver)
				act.drag_and_drop_by_offset(val,x,y).perform()
				print("El elemento {} se movio ".format(selector))
				t = time.sleep(tie)
				return t
			except TimeoutException as ex:
				print(ex.msg)
				print("El Elemento no se encontro" + selector)

	def clickxy(self,tipos,selector,x,y,tie):

		if tipos == "id":
			try:
				#self.driver.switch_to.frame(0)
				val = self.Selector_id(selector)
				act = ActionChains(self.driver)
				act.move_to_element_with_offset(val,x,y).click().perform()
				print("Click al elemento {} coordenadas {}, {} ".format(selector,x,y))
				t = time.sleep(tie)
				return t
			except TimeoutException as ex:
				print(ex.msg)
				print("El Elemento no se encontro"+ id)

		elif tipos == "xpath":
			try:
				#self.driver.switch_to.frame(0)
				val = self.Selector_xpath(selector)
				act = ActionChains(self.driver)
				act.move_to_element_with_offset(val, x, y).click().perform()
				print("Click al elemento {} coordenadas {}, {} ".format(selector, x, y))
				t = time.sleep(tie)
				return t
			except TimeoutException as ex:
				print(ex.msg)
				print("El Elemento no se encontro" + selector)