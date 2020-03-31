#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

    def post(self):
        kms = self.request.get("kmsInput")
        tiempo = self.request.get("tempInput")
        consumo_medio = self.request.get("consumoInput")
        velocidad=0
        consumo_total=0

        if (kms is None) or (tiempo is None) or (consumo_medio is None):
            self.response.write("No se pueden procesar numeros vacios")
        else:
            if kms.isdigit() and tiempo.isdigit() and consumo_medio.isdigit()  :
                distancia = int(kms)
                horas = int(tiempo)
                consumo = int(consumo_medio)
                if(horas == 0):
                    velocidad = 0
                else:
                    velocidad = distancia/horas
                consumo_total = (consumo * distancia) / 100

            self.response.write("Velocidad media: {} \nConsumo total: {}".format(velocidad, consumo_total))

app = webapp2.WSGIApplication([
    ('/consumo', MainHandler)
], debug=True)
