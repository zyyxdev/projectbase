# 🚀 ProjectBase – Painel Administrativo para Lojas Virtuais

> ⚠️ **Disclaimer importante:** Este projeto é uma **base funcional** para demonstrar habilidades de desenvolvimento full-stack. Não é uma loja virtual completa e pronta para produção. Não possui banco de dados real, sistema de pagamentos ou integração com meios de pagamento. É um **protótipo** criado para servir como ponto de partida para projetos reais.

---

## 📌 Sobre o projeto

**ProjectBase** é um painel administrativo completo com funcionalidades de loja virtual, suporte e gestão de usuários. Desenvolvido com Flask no backend e HTML/CSS/JS no frontend, ele oferece uma base sólida para quem deseja criar uma loja virtual ou sistema de gerenciamento.

Ele foi pensado para ser **educacional e demonstrativo**, mostrando como integrar autenticação, carrinho de compras, sistema de suporte e painel administrativo em um único projeto.

---

## ✅ Funcionalidades implementadas

| Módulo | Funcionalidades |
|--------|-----------------|
| 🔐 **Autenticação** | Login com dois níveis de acesso (admin e usuário comum) |
| 📊 **Dashboard** | Cards com métricas e gráfico de atividades semanais |
| 👥 **Usuários** | Lista de usuários com status, assinatura e remoção (apenas admin) |
| 🛒 **Loja** | Produtos com carrinho de compras e checkout (simulado) |
| 🎫 **Suporte** | Abertura de tickets, respostas, fechamento e reabertura |
| 📰 **Notícias** | Feed de notícias e códigos promocionais |
| 🛡️ **Admin** | Painel exclusivo para administradores |
| 🎨 **Design** | Interface dark, responsiva, com partículas animadas e modais estilizados |

---

## 🔑 Credenciais de acesso

| Nível | Usuário | Senha |
|-------|---------|-------|
| Admin | `admin` | `123` |
| Usuário | `zyyx` | `123` |
| Usuário | `sniper` | `123` |

---

## 🧱 Estrutura do projeto

```

ProjectBase/
├── add.py                 # Arquivo principal (Flask)
├── static/
│   ├── css/
│   │   └── style.css      # Estilos globais
│   └── js/
│       └── script.js      # Interações e gráficos
└── templates/
├── base.html          # Layout base
├── login.html         # Tela de login
├── dashboard.html     # Painel principal
├── usuarios.html      # Lista de usuários
├── logs.html          # Registro de atividades
├── loja.html          # Página da loja
├── carrinho.html      # Carrinho de compras
├── checkout.html      # Finalização de compra
├── noticias.html      # Notícias e promoções
├── suporte.html       # Lista de tickets
├── suporte_detalhe.html # Detalhe do ticket
├── novo_ticket.html   # Abrir novo ticket
└── admin.html         # Painel administrativo

```

---

## 🚀 Como rodar o projeto localmente

### 📦 Pré-requisitos

- Python 3.8+
- Pip

### 🔧 Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/ProjectBase.git
   cd ProjectBase
```

2. Instale as dependências:
   ```bash
   pip install flask
   ```
3. Execute o servidor:
   ```bash
   python add.py
   ```
4. Acesse no navegador:
   ```
   http://localhost:5000
   ```

---

❌ O que este projeto NÃO possui (e que você pode adicionar)

· ❌ Banco de dados real (dados são armazenados em memória)

· ❌ Sistema de pagamento integrado

· ❌ Envio de e-mails

· ❌ Cadastro de novos usuários (os usuários são fixos)

· ❌ Hospedagem de imagens

· ❌ Recuperação de senha

· ❌ Logs persistentes

---

🔧 Próximos passos (sugestões de evolução)

· Adicionar banco de dados SQLite ou PostgreSQL

· Criar sistema de cadastro de usuários

· Integrar com Mercado Pago ou PagSeguro

· Adicionar upload de imagens para produtos

· Melhorar segurança com hashing de senhas

---

📄 Licença

MIT – sinta-se livre para usar, modificar e distribuir.

---

👨‍💻 Autor

Zyyx – Projeto desenvolvido como base para estudos e demonstração de habilidades.

---

⭐ Se este projeto te ajudou, considere dar uma estrela no repositório!
