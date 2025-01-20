class Camera:
    def __init__(self, numero: int, tipo: str, disponibile: bool):
        self.numero_di_camera = numero
        self.tipo_di_camera = tipo
        self.disponibilita = disponibile

    def prenota(self) -> bool:
        if self.disponibilita:
            self.disponibilita = False
            return True
        return False

    def libera(self) -> None:
        self.disponibilita = True

    def __str__(self) -> str:
        return f"Camera {self.numero_di_camera} ({self.tipo_di_camera}) - {'Disponibile' if self.disponibilita else 'Non disponibile'}"


class Albergo:
    def __init__(self):
        self.camere = []
        self.prenotazioni = []

    def aggiungi_camera(self, camera: Camera) -> None:
        self.camere.append(camera)

    def prenota_camera(self, numero: int) -> bool:
        for camera in self.camere:
            if camera.numero_di_camera == numero and camera.prenota():
                self.prenotazioni.append(camera)
                return True
        return False

    def visualizza_camere_disponibili(self) -> list:
        return [camera for camera in self.camere if camera.disponibilita]

    def visualizza_prenotazioni(self) -> list:
        return self.prenotazioni