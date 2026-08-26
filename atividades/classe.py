class Usuario:
    def __init__(self, nome):
        self.nome = nome

    def cumprimentar(self):
        return f"Ola, meu nome é {self.nome}"
        
usuario1 = Usuario("Alice")
usuario2 = Usuario("job")

print(usuario1.cumprimentar())
print(usuario2.cumprimentar())