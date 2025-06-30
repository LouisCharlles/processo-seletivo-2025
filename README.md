# Processo Seletivo - Sistema de DUVs

Aplicação Django para gerenciamento de DUVs (Declaração Única de Viagem), Navios, Passageiros e Tripulantes.

---

## ✨ Funcionalidades

- CRUD completo de DUVs, Passageiros e Navios
- Busca de DUVs por número
- Busca de Passageiros por nome ou nacionalidade
- Visualização detalhada de DUVs (incluindo navio, passageiros e tripulantes)
- Paginação dos resultados
- Filtros dinâmicos com JavaScript para refinar buscas
- Templates organizados e design responsivo

---

## 🚀 Como rodar o projeto localmente

### 1. Clone o repositório

```bash
git clone https://github.com/LouisCharlles/processo-seletivo-2025.git
cd processo-seletivo-2025
```

### 2. Crie e ative um ambiente virtual

No **Windows**:
```bash
python -m venv .venv
.venv\Scripts\activate
```
No **Linux/Mac**:
```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute as migrações

```bash
python manage.py migrate
```

### 5. Inicie o servidor

```bash
python manage.py runserver
```

### 6. Acesse o sistema

Abra [http://127.0.0.1:8000/](http://127.0.0.1:8000/) no navegador.

---

## 📄 Observações

- Certifique-se de estar usando Python 3.8+.
- Para dúvidas ou sugestões, abra uma