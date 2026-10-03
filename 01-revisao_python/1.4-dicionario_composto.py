<<<<<<< HEAD
funcionarios = {
    101: {
        "nome": "Carlos",
        "Cargo": "Desenvolvedor",
        "Habilidades": ["Python", "C##", "Java"]
    },
102: {"nome": "Fabiana",
"Cargo": "Analista de transporte",
"Habilidades": ["Monitoramento de rota", "Frota", "Captação"]

}
}

print(funcionarios[102]["Habilidades"])
print(funcionarios.get(102,{}))
=======
funcionarios = {
    101: {
        "nome": "Carlos",
        "cargo": "desenvolvedor",
        "habilidades": ["Python","C##","Java"]
    },
    102: {
        "nome": "Mariana",
        "cargo": "gerente de projetos",
        "habilidades": ["Scrum","Gestão"]
    }
}

print(funcionarios[101]["cargo"])
print(funcionarios.get(103,{}).get("nome","Fucionário não encontrado"))
>>>>>>> 0f42d89 (primeiro envio pelo git)
