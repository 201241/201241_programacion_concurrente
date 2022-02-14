import threading
import time
import random
import cv2

#el codigo esta comentado para no generar el video

class ImagenSatelite():
    def __init__(self, conta = 0):
        self.locked = threading.Lock()
        self.conta_send = conta
        self.progreso = conta+1;
        self.limite = 9
        self.imagenes_array = []

        for x in range (1,10):
            path = 'images\img_%01d.png' %x
            print(path)
            imagen = cv2.imread(path)
            self.imagenes_array.append(imagen)
        #configuracion de video
        alto, ancho = imagen.shape[:2]
        # self.video = cv2.VideoWriter('video_completo.mp4', cv2.VideoWriter_fourcc(*'mp4v'),1,(ancho, alto))
        

    def rederizar(self):
        self.locked.acquire() #espera a que el locked termine
        try:
            #agregar imagen al video            
            #self.video.write(self.imagenes_array[self.conta_send]) 
            self.progreso += 11
            self.conta_send += 1
            print(self.progreso," %")
            print("[add image ",self.conta_send,"]")
            
        finally:
            self.locked.release()
            if(self.limite==self.conta_send):
                print(self.conta_send, " en limite")
                #self.video.release() #descomentar para que funcione el guardado del video
            print("termina alguno")
    
def fun_render_pc_1(x): #ordenador jaxa
    for y in range(3):
        time_f = random.random()
        time.sleep(time_f)        
        x.rederizar()        

def fun_render_pc_2(x): #ordenador aem
    for y in range(3):
        time_f = random.random()
        time.sleep(time_f)        
        x.rederizar()            

def fun_render_pc_3(x): #ordenador esa
    for y in range(3):
        time_f = random.random()
        time.sleep(time_f)        
        x.rederizar()            

if __name__ == "__main__":
    imagen_sat = ImagenSatelite()

    #for y in range(3):
    print("[ Renderizado imagenes satelitales ]")
    centro_jaxa_1 = threading.Thread(target=fun_render_pc_1, args=(imagen_sat,))
    centro_aem_2 = threading.Thread(target=fun_render_pc_2, args=(imagen_sat,))
    centro_esa_3 = threading.Thread(target=fun_render_pc_3, args=(imagen_sat,))

    #agencia espacial japonesa
    centro_jaxa_1.start()
    #agencia espacial mexicana
    centro_aem_2.start()
    #agencia espacial europea
    centro_esa_3.start()
