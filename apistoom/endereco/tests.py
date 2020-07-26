# -*- coding: utf-8 -*-
import json

from django.test import TestCase
# Create your tests here.
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Endereco

class salvarEnderecoApi(APITestCase):
    
      def test_adidionar_dados_todos_campos(self): 
            data = {"streetName":"Rua Linda 4",
                    "number":"23",
                    "complement":"apt 123",
                    "neighbourhood":"cambui",
                    "city":"campinas",
                    "state":"sp",
                    "country":"Brazil",
                    "zipcode":"1222322",        
                    "latitude":"1119",
                    "longitude":"20"}           
            response = self.client.post("/endereco/", data)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            
       def test_pega_todos_dados(self): 
            response = self.client.get("/endereco/")
            data = response.json()
            print("JSON data: ", data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            