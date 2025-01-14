# Nom de l'image Docker
IMAGE_NAME = health-calculator

# Port utilisé pour le conteneur Docker
PORT = 5000

# Commandes
.PHONY: help build run test clean

# Afficher les commandes disponibles
help:
	@echo "Commandes disponibles:"
	@echo "  make build   - Construire l'image Docker"
	@echo "  make run     - Lancer le conteneur Docker"
	@echo "  make test    - Lancer les tests unitaires"
	@echo "  make clean   - Supprimer les fichiers inutiles et les conteneurs Docker"

# Construire l'image Docker
build:
	docker build -t $(IMAGE_NAME) .

# Lancer le conteneur Docker
run:
	docker run -p $(PORT):5000 $(IMAGE_NAME)

# Lancer les tests unitaires
test:
	python -m unittest test.py

# Nettoyer les fichiers inutiles
clean:
	@echo "Nettoyage des fichiers inutiles..."
	@find . -type f -name "*.pyc" -delete
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@docker rm -f $$(docker ps -aq) 2>/dev/null || true
	@docker rmi -f $(IMAGE_NAME) 2>/dev/null || true
