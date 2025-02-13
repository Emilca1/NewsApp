# Utilisation d'une image Python légère
FROM python:3.10-slim

# Définition du répertoire de travail
WORKDIR /app

# Copie des fichiers nécessaires
COPY requirements.txt requirements.txt
COPY . .

# Installation des dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposition du port Flask
EXPOSE 4000

# Commande de lancement de l’application
CMD ["python", "src/main.py"]
