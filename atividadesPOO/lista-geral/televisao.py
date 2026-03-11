class TV():
    def __init__(self, canal, volume=0):
        self.volume = volume
        self.canal = canal
    def setAumentarVolume(self):
        if self.volume == 100:
            return print(f"Volume está no máximo")
        else:
            self.volume += 1
    def setDiminuirVolume(self):
        if self.volume == 0:
            return print("Volume esta em 0")
        else: 
            self.volume -= 1
            if self.volume < 0:
                self.volume = 0
    def setTrocaCanal(self, canal_novo):
        self.canal = canal_novo
    def getDadosTv(self):
        return f"Canal: {self.canal}, volume: {self.volume}"
televisao = TV(12,50)
print(televisao.getDadosTv())
televisao.setTrocaCanal(13)
televisao.setDiminuirVolume()
print(televisao.getDadosTv())