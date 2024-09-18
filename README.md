# ShellGPT 🇬🇧
OpenAI Technology: **Chat with ChatGPT from the Terminal.**

- **🤖 ShellGPT Features**:
  - Easy to use, executable from any terminal.
  - ShellGPT can create queries for ChatGPT 3.5 Turbo.
  - Requires the **"openai"** module to be installed.

# **Installation Guide**:

  - **Install "openai":**
    ```bash
    pip install openai
    ```

  - **Navigate to the ShellGPT directory:**
    ```bash
    cd ShellGPT
    ```

  - **Start ShellGPT:**
    ```bash
    python shellgpt.py
    ```

--- 


# Guide to Obtaining an OpenAI API Key

This tutorial will guide you step-by-step through the process of obtaining an OpenAI API key, which is necessary to integrate and use the platform's services.

## Step 1: Create an OpenAI Account

1. Visit the official [OpenAI website](https://beta.openai.com/signup/).
2. Click on **Sign Up**.
3. You can register using your email, Google account, or Microsoft account.
4. Complete the verification process if required.

## Step 2: Log in to Your Account

1. Once you've created your account, go to [https://beta.openai.com/login](https://beta.openai.com/login).
2. Enter your credentials (email and password) or log in with Google or Microsoft.

## Step 3: Access the API Section

1. Once logged in, go to the top right menu (profile icon) and click on **View API Keys** or **API Keys**.
2. If this is your first time accessing this section, you won’t have any keys generated yet.

## Step 4: Generate a New API Key

1. Click the **Create new secret key** button to generate a new API key.
2. Once generated, the key will appear on the screen. **Copy it immediately**, as you won’t be able to view it again after leaving the page.

> ⚠️ **Important:** Store your API key in a secure place, such as a password manager. Do not share it publicly or upload it to unsecured code repositories.

## Step 5: Use the API Key
```python
Once you have the key, you can use it in your projects. For example, if you are using the `openai` Python library, you can set the key like this:
```
# Set your API key
```python
openai.api_key = 'your-api-key-here'
```

---

# ShellGPT 🇪🇸
Tecnología OpenAI: **Chatea con ChatGPT desde terminal.**

- **🤖 Características ShellGPT**:  
- Fácil de usar, ejecutable en cualquier terminal.
- ShellGPT es capaz de crear consultas para ChatGPT 3.5 Turbo.
- Requiere tener instalado el modulo **"openai"**.

# **Guía de Instalación**:

- **Instalar "openai"**
  ```bash
  pip install openai
  ```

- **Navegar al directorio de ShellGPT:**
  ```bash
  cd ShellGPT
  ```

- **Iniciar ShellGPT:**
  ```bash
  pyhton shellgpt.py
  ```

---


  # Guía para obtener una API Key de OpenAI

Este tutorial te guiará paso a paso en el proceso de obtener una clave de API de OpenAI, que es necesaria para integrar y utilizar los servicios de la plataforma.

## Paso 1: Crear una cuenta en OpenAI

1. Visita el sitio web oficial de [OpenAI](https://beta.openai.com/signup/).
2. Haz clic en **Sign Up**.
3. Puedes registrarte utilizando tu correo electrónico, cuenta de Google o cuenta de Microsoft.
4. Completa el proceso de verificación si es requerido.

## Paso 2: Inicia sesión en tu cuenta

1. Una vez que hayas creado tu cuenta, ve a [https://beta.openai.com/login](https://beta.openai.com/login).
2. Introduce tus credenciales (correo electrónico y contraseña) o inicia sesión con Google o Microsoft.

## Paso 3: Accede a la sección de API

1. Una vez que hayas iniciado sesión, dirígete al menú superior derecho (icono de perfil) y haz clic en **View API Keys** o **API Keys**.
2. Si es tu primera vez accediendo a esta sección, no tendrás ninguna clave generada todavía.

## Paso 4: Genera una nueva API Key

1. Haz clic en el botón **Create new secret key** para generar una nueva clave de API.
2. Una vez generada, la clave aparecerá en la pantalla. **Cópiala inmediatamente**, ya que no podrás verla de nuevo después de salir de la página.

> ⚠️ **Importante:** Guarda tu clave de API en un lugar seguro, como un gestor de contraseñas. No la compartas públicamente ni la subas a repositorios de código sin protección.

## Paso 5: Usa la API Key

Una vez que tengas la clave, puedes utilizarla en tus proyectos. Por ejemplo, si estás utilizando la librería `openai` en Python, puedes configurarla de esta manera:
```python
import openai
```

# Configura tu API key
```python
openai.api_key = 'tu-api-key-aquí'
```


